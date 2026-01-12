import requests

BASE_URL = "http://10.3.10.104:3000/api"

def get_token():
    try:
        req = requests.post(f"{BASE_URL}/token")
        req.raise_for_status()
        token = req.json()["token"]
        print(f"Token is: {token}")
        return token
    except Exception as e:
        print("Fel vid hämtning av token")
        raise e


def verify_token(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Custom-header": "secret"
    }

    try:
        req = requests.post(f"{BASE_URL}/verify", headers=headers, params={"token": token})
        req.raise_for_status()
        secret = req.json()["secret"]
        print(f"Token is verified and secret is: {secret}")
        return secret
    except Exception as e:
        print("Fel vid verifiering av token")
        raise e


def get_flag(token, secret):
    headers = {
        "Authorization": f"Bearer {token}",
        "Custom-header": "secret"
    }

    body = {"secret": secret}

    try:
        req = requests.post(f"{BASE_URL}/flag", headers=headers, json=body, params={"token": token})
        req.raise_for_status()
        flag = req.json()["flag"]
        print(f"Flaggan är: {flag}")
        return flag
    except Exception as e:
        print("Fel vid hämtning av flagga")
        raise e


def main():
    token = get_token()
    secret = verify_token(token)
    get_flag(token, secret)


if __name__ == "__main__":
    main()