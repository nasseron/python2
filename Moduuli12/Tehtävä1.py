import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
if response.status_code == 200:
    joke = response.json()
    print(joke['value'])


else:
    print("Vietsin haku epäonnestui! ",responses.status_code)


                                                                                            

