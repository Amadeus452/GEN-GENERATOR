
import re
import os
from socket import socket, SOL_SOCKET, SO_REUSEADDR

# IP address regex
ipRegex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
# MAC address regex
macRegex = re.compile("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")

""" Get router ip address """
def GetDefaultGateway():
    cmd = "chcp 65001 && ipconfig | findstr /i \"Default Gateway\""
    res = os.popen(cmd).read()

    for word in res.split(' '):
        if word and ipRegex.match(word):
            return word.replace("\n", '')

    
""" Scan network """
def ScanNetwork(gateway=GetDefaultGateway(), start=1, stop=256):
    result = []
    # If not ip
    if not ipRegex.match(gateway):
        return result
    # Ping all
    ip = '.'.join(gateway.split('.')[:-1])
    for target in range(start, stop):
        target = f"{ip}.{target}"
        code = os.system(f"ping -w 10 -n 1 {target} 1> nul")
        if code == 0:
            result.append(target)

    return result

""" Check if port is open """
def PortIsOpen(ip, port, timeout = 0.5):
    sock = socket()
    sock.settimeout(timeout)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

""" Get mac by local ip """
def GetMacByIP(ip):
    _ = os.popen(f"arp -a {ip}").read()
    f = _.find("Physical Address")
    o = _[f:].split(' ')
    for _ in o:
        if macRegex.match(_):
            return _.replace('-', ':')
