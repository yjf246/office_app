# from scapy.all import ARP, Ether, srp

# # utils.py

# def get_client_ip_and_mac(request):
#     client_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
#     if client_ip:
#         client_ip = client_ip.split(',')[0]
#     else:
#         client_ip = request.META.get('REMOTE_ADDR', '')

#     mac_address = get_mac(client_ip)

#     return client_ip, mac_address


# def get_mac(ip):
#     arp = ARP(pdst=ip)
#     ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#     packet = ether/arp
#     result = srp(packet, timeout=3, verbose=False)[0]

#     return result[0][1].hwsrc if result else None

import getmac
import subprocess
import socket

def get_mac(ip):
    try:
        result = subprocess.check_output(["arp", "-n", ip])
        result = result.decode("utf-8")
        mac_address = result.split()[3]
        return mac_address
    except:
        return None

def get_client_ip_and_mac(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if client_ip:
        client_ip = client_ip.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR', '')
    # mac_address = get_mac(client_ip)
    mac_address1 = getmac.get_mac_address(ip=client_ip)
    return client_ip,mac_address1


def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"

# ip_address = "8.8.8.8" # Google DNS server
# domain_name = get_domain_name(ip_address)
# print(f"The domain name for {ip_address} is {domain_name}")