import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv()
ZONE_ID = os.environ.get("ZONE_ID")
ZONE_API_KEY = os.environ.get("ZONE_API_KEY")
ZONE_DNS_NAME = os.environ.get("ZONE_DNS_NAME")
PROD = True if os.environ.get("PROD") == "true" else False
ZONE = "https://api.zone.eu/v2/dns/"+ZONE_DNS_NAME+"/a/"
AUTH_HEADER = headers={'Authorization' : (b"Basic "+base64.b64encode(f"{ZONE_ID}:{ZONE_API_KEY}".encode())).decode()}

def main():
    r = requests.get(ZONE, headers=AUTH_HEADER)
    if r.status_code != 200:
        print("error occurred: ", r.json())
        return
    cur_ip = requests.get("https://api.myip.com/").json()["ip"]

    if cur_ip == r.json()[0]['destination']:
        return
    
    if not PROD:
        print("dry run")
        return
    
    for record in r.json():
        id = record["id"]
        name = record["name"]
        rs = requests.put(ZONE+id, json={"destination":cur_ip, "name":name}, headers=AUTH_HEADER)
        if rs.status_code != 200:
            print(f"status code: {rs.status_code}\nerror: {r.json()}")

main()