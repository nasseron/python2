import requests
def hae_saa(paikkakunta, api_key):
    url = f'https://api.openweather.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric'
    response = reguests.get(url)
    if response.status_code == 200:
        data = response.json()
        paikkakunnan_saa = data['weather'][0]['description']
        lampotila = data['main'][0]['temp']

        return paikkakunnan_saa, lampotila
    else:
        return None, None, None

if __name__ == '__main__':
    paikkakunta = input("Anna paikkakunnan nimi: ")
    api_key = input("Syötä OpenWeatherMap api_key:")
    saa = lampotila = hae_saa(paikkakunta, api_key)
    if saa:
        print(f'Sää paikassa {paikkakunta}: {saa}')
        print(f"Lämpötila: {lampotila} ºC")
    else:
        print("Säätiedot eivät löytyneet. Tarkista paikkakunta tai API-avain.")