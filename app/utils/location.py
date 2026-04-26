import requests

def get_user_location():
    try:
        data = requests.get("https://ipapi.co/json/").json()
        return data["latitude"], data["longitude"]
    except:
        return 0, 0