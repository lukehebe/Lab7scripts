import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'  # Replace with your desired JSON API URL
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
