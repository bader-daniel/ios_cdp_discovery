def init_queue():
    """Returns all hosts to be scanned from every selected source"""
    return get_initial_hosts_csv()


def get_initial_hosts_csv():
    csv = open('hosts.csv', 'r')

    delimiter = ','
    orig_hosts = list(csv.read().split(delimiter))

    hosts = []
    for i in orig_hosts:
        hosts.append(i.strip())

    csv.close()
    return hosts
