import requests

url = 'https://example.com'  # Replace with your desired website URL
headers = {'User-Agent': 'My Custom User Agent'}
params = {'param1': 'value1', 'param2': 'value2'}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
