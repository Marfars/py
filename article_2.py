import requests


def request_target_url(url):
    try:
        response = requests.get(url)
        if response:
            return response.content
        else:
            print(f"Response failed, status code is {response.status_code}")
    except Exception as e:
        print(e)


def main():
    request_target_url("https://api.github.com")
