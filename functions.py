class NetworkElement:

    ###############################################################
    # Function that returns the switches' hostname name
    def swhostname(self, temphost):
        hostname = ''
        for row in temphost.split('\n'):
            hostname = row[9:]
            break
        return hostname
    ###############################################################

    ###############################################################
    # Function that returns the switches' model name
    def swmodel(self, tempinv):
        sw_model = ''
        sw_line = ''
        for row in tempinv.split('\n'):
            if 'PID: ' in row:
                sw_line = row
            elif row == '':
                break

        sw_line = sw_line[5:]

        for char in sw_line:
            if char == ' ':
                break
            sw_model = sw_model + char

        return sw_model
    ###############################################################

    def __init__(self, index, ip, temphost, tempinv):
        self.swindex = index
        self.hostname = self.swhostname(temphost)
        self.ip = ip
        self.model = self.swmodel(tempinv)

    trunks_clean = []
    trunks_dollar = []
    access_ports = []

    ###############################################################
    # Function that returns a list of trunks, with just the abbreviated trunk interface names and a dollar sign
    def trunkinterfaces(self, temptrunks):
        trunks = []
        for row in temptrunks.split('\n'):
            temp = ''
            if '0/' not in row:
                continue
            for i in row:
                if i == ' ':
                    break
                temp = temp + i
            trunks.append(temp + '$')

        return trunks
    ###############################################################

    ###############################################################
    # Function that returns a list of trunks, with just the abbreviated trunk interface names no dollar sign
    def trunkinterfacesclean(self, temptrunks):
        trunks = []
        for row in temptrunks.split('\n'):
            temp = ''
            if '0/' not in row:
                continue
            for i in row:
                if i == ' ':
                    break
                temp = temp + i
            trunks.append(temp)

        return trunks

    ###############################################################
    # Function that returns a list of trunks, with just the abbreviated trunk interface names and a dollar sign
    def get_access_ports(self, temp_access_ports, trunks):
        access_ports = []
        for row in temp_access_ports.split('\n'):
            temp = ''
            if not row:
                continue
            for i in row:
                if i == ' ':
                    break
                temp += i
            if temp in trunks or temp in access_ports:
                continue
            access_ports.append(temp)

        return access_ports
    ###############################################################


class UnknownNetworkElement:

    def __init__(self, index, local_swindex, local_swhostname, local_swip, local_swif):
        self.index = index
        self.local_swindex = local_swindex
        self.local_swhostname = local_swhostname
        self.local_swip = local_swip
        self.local_swif = local_swif


class TrunkLink:

    #HAS-A NetworkElement and a local port x2
    # Function that looks at trunk interfaces and returns the neighbors ip
    def __init__(self, index, local_swindex, local_swhostname, local_swip, local_swif):
        self.index = index
        self.local_swindex = local_swindex
        self.local_swhostname = local_swhostname
        self.local_swip = local_swip
        self.local_swif = local_swif

    def cdp_neighbors(self, cdpif):
        neighbor_details = []
        ip_address = ''
        for output in cdpif.split('\n'):
            if 'Device ID:' in output:
                neighbor_details.append(output[11:])
                continue
            if 'IP address:' in output and not ip_address:
                ip_address = output[14:]
                neighbor_details.append(ip_address)
                continue
            if 'IP Address:' in output and output[14:] == '':
                return 'ERROR'
            if 'Total cdp entries displayed : 0' in output:
                return 'ERROR'
        if not neighbor_details:
            return 'ERROR'
        return neighbor_details
    #  TODO FIXA SNYGGARE

    def compile_links(self):
        pass
    #  take all the link-objects and compile them into true p2p-link objects, that contain's the object of both sides.

    remote_swhostname = ''
    remote_swip = ''

class SanityChecks:
    pass


class VerifyCommands:
    # instantiate with skip_switch, command, port_type

    def __init__(self, port_type, command, skip_switch, verification_functions, command_present):
        self.port_type = port_type
        self.command = command
        self.skip_switch = skip_switch
        self.verification_functions = verification_functions
        self.command_present = command_present

    found_commands = []

    def generate_netmiko_command(self):
        return self.command, self.port_type

    def verify_command(self, network_element, interface, result):
        if self.command_present:
            if result:
                self.found_commands.append([network_element, interface])
                print('command found on: ' + network_element + ': ' + interface)
        else:
            if not result:
                self.found_commands.append([network_element, interface])
                print('command missing on: ' + network_element + ': ' + interface)

    # in: make sure it's a list of filterered mac addreses
    # out: nestled list (inside vlan, mac, type, port, outside lines)
    def getitems(self, macreturn):
        mac_lines = []
        for mac in macreturn:
            elements = list(mac.split(' '))

            elements2 = list(filter(None, elements))

            mac_lines.append(elements2)

        return mac_lines

    def show_mac_hyphen(self, swmodel):
        sw = swmodel
        if sw == 'WS-C2960CX-8PC-L' or sw == 'WS-C2960CX-8PC-L':
            return 'show mac address-table'
        else:
            return 'show mac address-table'

    def sh_mac_command(self, mac_command, trunkinterfaces):
        showmaccommand = '{} | exclude CPU'.format(mac_command)

        for i in trunkinterfaces:
            showmaccommand = '{0}| {1}'.format(showmaccommand, i)

        return showmaccommand

    # in show mac output, out: show mac address table without cpu trunks, and with added $ at the end
    def clean_mac_table(self, macinput):
        mac_list = []
        for line in macinput.split('\n'):
            elements = line.split(' ')
            elements_list = list(filter(None, elements))
            try:
                if elements_list[2] == 'STATIC' or elements_list[2] == 'DYNAMIC':
                    mac_list.append(elements_list)
            except IndexError:
                continue
        return mac_list

    # take a mac address in any format and return on in Cisco format: xxxx.xxxx.xxxx
    def convert_to_cisco_mac(self, macs):
        delimiters = []
        assembled_macs = []
        stripped_macs = []
        # get a list of delimiters in the mac
        for mac_address in macs:
            for char in mac_address:
                if char in '0123456789abcdef':
                    continue
                else:
                    delimiters.append(char)

        for mac in macs:
            fixed_mac = ''
            for char in delimiters:
                if char in mac:
                    fixed_mac = ''.join(mac.split(char))
            stripped_macs.append(fixed_mac)

        for mac in stripped_macs:
            assembled_macs.append(mac[0:4] + '.' + mac[4:8] + '.' + mac[8:])

        return assembled_macs

    #  mac_list is the mac addresses you want to find, show_mac_output is show mac address output from the local
    #  switch without the trunk or CPE CAM-entries
    def sh_mac_command_host(self, mac_list, macs_clean):
        build_output = []
        for mac in mac_list:
            for i, line in enumerate(macs_clean):
                if mac == line[1]:
                    looped_list = [macs_clean[i][1], macs_clean[i][3], macs_clean[i][0]]
                    build_output.append(looped_list)
        return build_output

