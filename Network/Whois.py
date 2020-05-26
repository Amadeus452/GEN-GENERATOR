
# Import modules
import json
import urllib.request
import requests 

""" Get info about ip """
def Info(ip=''):
    try:
        result = urllib.request.urlopen(f"http://ip-api.com/json/{ip}").read().decode('utf8')
    except urllib.error.URLError:
        return None
    else:
        result = json.loads(result)
        return result

""" Get geo info about ip """
def Geoplugin(ip=''):
    try:
        result = urllib.request.urlopen(f"http://www.geoplugin.net/json.gp?ip={ip}").read().decode('utf8')
    except urllib.error.URLError:
        return None
    else:
        result = json.loads(result)
        return result
        
""" Locate by BSSID """
def GetLocationByBSSID(bssid):
    try:
        result = urllib.request.urlopen(f"http://api.mylnikov.org/geolocation/wifi?bssid={bssid}").read().decode('utf8')
    except urllib.error.URLError:
        return None
    else:
        result = json.loads(result)
        return result["data"]

def MyIp():
    r = requests.get('http://ip.42.pl/raw')
    ip = r.text
    return ip