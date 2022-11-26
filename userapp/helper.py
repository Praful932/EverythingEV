import json
import math
from urllib.request import urlopen


def get_user_location():
    """
    Return value:
    Tuple - (latitude_user, longitude_user)
    """
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    # Get User location(lat & lng)
    lat_user = math.radians(float(data["loc"].split(",")[0]))
    lng_user = math.radians(float(data["loc"].split(",")[1]))

    return (lat_user, lng_user)
