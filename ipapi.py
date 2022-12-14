import requests

def get_ip(): # Retrieve IP Address of the user
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(): # Retrieve information from the IP of user
    ip_address = get_ip()
    response = requests.get("https://ipapi.co/{}/json/".format(ip_address)).json()
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

if __name__ == "__main__":
    res = get_location() # Save the information to a variable (dictionary datatype)

    for x, y in res.items(): # loop the information to be display cleanly
        print("{}: {}".fosrmat(x, y))