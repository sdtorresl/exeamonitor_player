import netifaces


def get_ipaddress():

    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        ip = addrs.get(netifaces.AF_INET)

        if interface.startswith("eth"):
            return "IP: " + ip[0]['addr']

    return None


