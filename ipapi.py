import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
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
        "ASN": response.get("asn")
    }
    return location_data

res = get_location()

for x, y in res.items():
    print(f"{x}: {y}")