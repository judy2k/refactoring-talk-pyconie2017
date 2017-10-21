import requests

def stupid_request(*args, **kwargs):
    print("Don't be stupid!")

requests.get = stupid_request

import requests
requests.get("https://www.reallycoolsite.com/")
# Don't be stupid!