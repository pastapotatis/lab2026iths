import requests

baseU = "http://10.3.10.104:3000/api"

def send_post(endpoint, key, text, headers=None, params=None, json=None):
    try:
        req = requests.post(f"{baseU}/{endpoint}", headers=headers, params=params, json=json)
        req.raise_for_status()
        value = req.json()[key]
        print(f"{text}: {value}")
        return value
    except Exception as e: # Returnerar eventuella fel
        print(f"Fel vid hämtning av {text}")
        raise e


def main():
    # Steg 1 – hämtar token. endpoint_url / token:"value" / Text
    token = send_post("token", "token", "Token")


    # Headers som används i steg 2 och 3
    headers = {
        "Authorization": f"Bearer {token}",
        "Custom-header": "secret"
    }

    # Steg 2 – verifiera token. endpoint_url / returnerad secret / Text
    secret = send_post("verify", "secret", "Secret", headers=headers, params={"token": token})


    # Steg 3 – hämtar flagga. endpoint_url / returnerad flagga / Text
    flag = send_post("flag", "flag", "Flagga", headers=headers, params={"token": token}, json={"secret": secret})


if __name__ == "__main__":
    main()