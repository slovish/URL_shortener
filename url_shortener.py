import requests

def shorten_url(long_url):
    bitly_api_key = "1e1b064f72260afcacf886e7bfd0ef76e14c409c"
    headers = {
        "Authorization": f"Bearer {bitly_api_key}"
    }
    data = {
        "long_url": long_url
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten",
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        return response.json()["link"]
    else:
        raise Exception("Failed to shorten URL")

print(shorten_url("https://www.w3schools.com/python/module_requests.asp"))