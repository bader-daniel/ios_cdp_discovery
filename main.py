from functions import *
from netmiko import ConnectHandler
import netmiko


ne_list = []
link_list = []
bad_link_list = []
link_id_list = []
unknown_ne_list = []
# mac search does not need to be specified with Cisco formatting, any delimiter, anywhere, is fine. Just don't add more than one delimiter per mac address.
mac_search = ['00:06:8e:30:68:38','00:06:8e:30:da:e4','00:06:8e:30:da:e5','00:06:8e:30:da:ac','00:06:8e:30:da:ab','00:06:8e:30:da:e8','00:06:8e:30:da:64','00:06:8e:30:da:ca','00:06:8e:30:da:9a','00:06:8e:30:ca:8f','00:06:8e:30:da:69','00:06:8e:31:09:5d','00:06:8e:30:b4:42','00:06:8e:30:da:ad','00:06:8e:30:da:af','00:06:8e:30:da:b5','00:06:8e:31:57:ef','00:06:8e:30:68:6b','00:06:8e:30:da:b0','00:06:8e:30:b2:82','00:06:8e:30:11:c6','00:06:8e:30:32:f6','00:06:8e:30:11:c2']
mac_search_results = []
skip_list = []
not_work = []


def get_initial_hosts_csv():
    csv = open('hosts.csv', 'r')

    delimiter = ','
    orig_hosts = list(csv.read().split(delimiter))

    hosts = []
    for i in orig_hosts:
        hosts.append(i.strip())

    csv.close()
    return hosts


ne_queue = get_initial_hosts_csv()


class Engine:

    def __init__(self, user, password):
        self.username = user
        self.password = password


    def main_loop(self):

        # additional checks
        # find macs on access-ports
        # find command in interfaces
        global b
        print('Do you want to do additional checks on interface while discovering the network?')
        additional_checks = input('> ')

        if additional_checks == 'yes':
            verification_functions = []

            print('Do you want to verify a certain command?')
            verify_command = input('> ')

            if verify_command == 'yes':
                verification_functions.append(True)
            else:
                verification_functions.append(False)

            print('Find a certain MAC address?')
            mac_find = input('> ')

            if mac_find == 'yes':
                verification_functions.append(True)
            else:
                verification_functions.append(False)

            print('Check for too many mac addresses on access-ports?')
            mac_count_find = input('> ')

            if mac_count_find == 'yes':
                verification_functions.append(True)
            else:
                verification_functions.append(False)

            if verification_functions[0]:
                print('enter to string to search for')
                command = input('> ')

                print('trunk or access-ports?')
                while True:
                    interface_type = input('> ')
                    if interface_type == 'trunk' or interface_type == 'access':
                        break
                    else:
                        print('You must enter "trunk" or "access"')

                print('Do you want to check if the command is present or missing?')
                while True:
                    command_present = input('> ')
                    if command_present == 'present':
                        break
                    elif command_present == 'missing':
                        command_present = ''
                        break
                    else:
                        print('You must enter either "present" or "missing"')

            if verification_functions[1]:
                pass
                # TODO: MAC SEARCH

            if verification_functions[2]:
                # TODO: specify number if macs and vlans to ignore
                pass
                # Get the trunk list from one function and send it to the next:

            b = VerifyCommands(interface_type, command, [], verification_functions, command_present)
            # TODO: Instantiation doesn't work if verification_functions[0] = False because the variables are never set
            # but I still need to instantiate if I want to use mac verification

        elif additional_checks == 'no':
            b = ''

        for main_index, ip in enumerate(ne_queue):

            if ip in skip_list:
                ne_list.append('')
                continue
            iosv_l2 = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': self.username,
                'password': self.password,
            }
            print(f"Currently working on {ip}\n")
            skip_list.append(ip)
            try:
                net_connect = ConnectHandler(**iosv_l2) # TODO: more specific error handling if the connection doesn't work
            except netmiko.ssh_exception.NetmikoTimeoutException:
                ne_list.append('')
                not_work.append(ip)
                continue
            except netmiko.ssh_exception.NetmikoAuthenticationException:
                ne_list.append('')
                skip_list.append(ip)
                not_work.append(ip)
                continue
            # Below are the commands that get the IOS output that will be used by the various methods, if
            # that is needed for instantiation
            swlocal_link_id_list = []
            temphost = net_connect.send_command('show run | inc hostname')
            tempinv = net_connect.send_command('show inventory')
            ne_list.append(NetworkElement(main_index, ip, temphost, tempinv))

            # More commands needed by functions, after instantiation of NE
            temptrunks = net_connect.send_command('show interface trunk | begin pruned')
            temp_access_ports = net_connect.send_command('sh int status | inc connected')
            ne_list[main_index].trunks_clean = ne_list[main_index].trunkinterfacesclean(temptrunks)
            ne_list[main_index].trunks_dollar = ne_list[main_index].trunkinterfaces(temptrunks)
            ne_list[main_index].access_ports = ne_list[main_index].get_access_ports(temp_access_ports, ne_list[main_index].trunks_clean)

            for trunks_clean_i, trunks_clean_item in enumerate(ne_list[main_index].trunks_clean):
                link_list.append(TrunkLink(str(main_index) + '-' + str(trunks_clean_i), ne_list[main_index].index, ne_list[main_index].hostname,
                                           ne_list[main_index].ip, trunks_clean_item))
                swlocal_link_id_list.append(str(main_index) + '-' + str(trunks_clean_i))

            for swlocal_index, swlocal_value in enumerate(swlocal_link_id_list):
                cdp_check = net_connect.send_command("sh cdp nei " + str(ne_list[main_index].trunks_clean[swlocal_index]) + " detail")
                try:
                    link_list[swlocal_index].remote_swhostname, link_list[swlocal_index].remote_swip = link_list[swlocal_index].cdp_neighbors(cdp_check)
                    if link_list[swlocal_index].remote_swip not in skip_list:
                        ne_queue.append(link_list[swlocal_index].remote_swip)
                except ValueError:
                    print('No CDP information!')
                    bad_link_list.append(TrunkLink(main_index, ne_list[main_index].index, ne_list[main_index].hostname, ne_list[main_index].ip, str(ne_list[main_index].trunks_clean[swlocal_index])))
                    print(bad_link_list[len(bad_link_list) - 1].local_swip) # TODO: DON'T USE LENGTH AS AN INDEX
                    print(bad_link_list[len(bad_link_list) - 1].local_swif)
                except:
                    print('CDP FUNCTION NOT WORKING')
                    print(link_list[swlocal_index].cdp_neighbors(cdp_check))
                    bad_link_list.append('')
            link_id_list.append(swlocal_link_id_list)

            if b:
                # TODO: a lot of verification commands use the same functions. Run a loop before executing the verifications
                # themselves that generates all the necessary show commands and their output
                #  or example: finding certain mac addresses on interfaces and checking for too many macs on access-
                #  ports require the same information.

                if b.verification_functions[0]:
                    command_list = list(b.generate_netmiko_command())
                    if command_list[1] == 'trunk':
                        for trunk in ne_list[main_index].trunks_clean:
                            command_check = net_connect.send_command('show run interface ' + trunk +
                                                                     ' | inc ' + command_list[0])
                            result = command_check
                            b.verify_command(ne_list[main_index].ip, trunk, result)
                    elif command_list[1] == 'access':
                        for access in ne_list[main_index].access_ports:
                            command_check = net_connect.send_command('show run interface ' + access +
                                                                     ' | inc ' + command_list[0])
                            result = command_check
                            b.verify_command(ne_list[main_index].ip, access, result)

                # Find specific Mac addresses in the network:
                if b.verification_functions[1] and mac_search:
                    temp_mac_find_list = []
                    try:
                        get_macs = net_connect.send_command(b.sh_mac_command(b.show_mac_hyphen(ne_list[main_index].model),
                                                                             ne_list[main_index].trunks_dollar))
                        mac_list = b.clean_mac_table(get_macs)

                        # take mac addresses we want to find and compare them to the access-port CAM table
                        found_macs = b.sh_mac_command_host(b.convert_to_cisco_mac(mac_search), mac_list)

                        # Add found mac addresses and relating information to list called mac_search_results:
                    except:  #  .NetmikoTimeoutException:
                        print('Timed out')

                    for macs in found_macs:
                        # temp_mac_find_list.clear()
                        # temp_mac_find_list.extend(macs)
                        # temp_mac_find_list.append(ne_list[main_index].ip)
                        # temp_mac_find_list.append(ne_list[main_index].hostname)

                        temp_mac_find_list = [macs[0], macs[1], macs[2], ne_list[main_index].ip, ne_list[main_index].hostname]
                        mac_search_results.append(temp_mac_find_list)
                        print(temp_mac_find_list)
                elif b.verification_functions[1] and not mac_search:
                    print("You haven't specified any MAC-Addresses")

                # Verify if there are too many mac addresses on the access ports
                if b.verification_functions[2]:
                    # Get the command that we send to the switch using a number of methods in the VerifyCommands Class
                    # Also send command to get the show mac output
                    if not b.verification_functions[1]:
                        get_macs = net_connect.send_command(b.sh_mac_command(b.show_mac_hyphen(ne_list[main_index].model),
                                                                             ne_list[main_index].trunks_dollar))
                        #  clean it by removing unwanted lines and return the data is nestled lists:
                        mac_list = b.clean_mac_table(get_macs)
                    mac_threshold = 3


                    # find all interfaces
                    if_count = []
                    skip_if = []
                    for line in mac_list:
                        if_count.append(line[3])

                    for ints, int in enumerate(if_count):
                        if int in skip_if:
                            continue
                        if if_count.count(int) > mac_threshold:
                            print(f"Too many macs ({if_count.count(int)}) found on {int}")
                            skip_if.append(int)
                            unknown_ne_list.append(UnknownNetworkElement(str(main_index) + str(ints), ne_list[main_index].index, ne_list[main_index].hostname, ne_list[main_index].ip, int))

                net_connect.disconnect()
print('Enter SSH Credentials: Username')
user_name = input('> ')


print('Enter SSH Credentials: Password')
password = input('> ')
# Getpass() doesn't work very well in my IDE and alternatives requires installation from sources I haven't verified.
# TODO: Find a better password solution.

#
a = Engine(user_name, password)
a.main_loop()

# Code that runs after discovery process, outputs findings
if not_work:
    print("switches that are offline or where login doesn't work: ", not_work)
    print("")
    print("*" * 10)
    print("\n")
for val, item in enumerate(unknown_ne_list):
    print("Access-ports with too many mac-addresses:")
    print("Index of element:", unknown_ne_list[val].index)
    print("Index of local switch:", unknown_ne_list[val].local_swindex)
    print("Hostname of local switch:", unknown_ne_list[val].local_swhostname)
    print("IP of local switch:", unknown_ne_list[val].local_swip)
    print("Local interface:", unknown_ne_list[val].local_swif)
    print("*" * 10)
    print("\n")
for i, value in enumerate(ne_queue):
    print("Switches found:")
    print("Index of element:", ne_list[i].index)
    print("Hostname of switch:", ne_list[i].hostname)
    print("IP of switch:", ne_list[i].ip)
    print("Model:", ne_list[i].model)
    print("*" * 10)
    print("\n")


print("MAC Addresses found: ")
try:
    for mac in mac_search_results:
        print(f'Mac: {mac}')
except:
    print('no macs found or search not done')


# command was found/missing on:
# the following trunk interfaces cannot find neighbor interfaces with CDP
#
