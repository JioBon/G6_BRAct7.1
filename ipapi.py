import requests

def get_ip(): # Retrieve IP Address of the user
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(): # Retrieve information from the IP of user
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IP Address": ip_address,
        "Version": response.get("version"),
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
        "Country Code": response.get("country_code"),
        "ISP": response.get("org"),
        "ASN": response.get("asn"),
        "Currency": response.get("currency")
    } 
    # more data from
    # https://www.freecodecamp.org/news/how-to-get-location-information-of-ip-address-using-python/
    
    return location_data

res = get_location() # Save the information to a variable (dictionary datatype)
assert len(res) == 9, "Data Should have 9 output"

for x, y in res.items(): # loop the information to be display cleanly
    print(f"{x}: {y}")