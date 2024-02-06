import requests

# dinopass_url

dinopass_url = "https://dinopass.com/password/simple"

# Fetch the password from dinopass.com
response = requests.get(dinopass_url)

# validate reponse with http 200 code
if response.status_code == 200:
    # pull password from reponse and strip beginning and end of text
    password = response.text.strip()
    print(password)
else:
    print("failed to fetch, check dinopass_url")
