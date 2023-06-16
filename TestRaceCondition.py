import requests
from concurrent.futures import ThreadPoolExecutor

def make_request(url):
    try:
        payload = {
            # add payload here.
        }
        headers = {
            # add request Header here.
        }
        response = requests.post(url, json=payload, headers=headers)
        print(f"Response from {url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request to {url} failed: {e}")

cookies = {
    # add cookies here.
}

urls = [
    # add urls here.
]

executor = ThreadPoolExecutor()
for url in urls:
    executor.submit(make_request, url)

executor.shutdown(wait=True)
