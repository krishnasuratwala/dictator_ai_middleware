import requests
import json

# CREDENTIALS FROM btcpay_utils.py
BTCPAY_URL = "https://mainnet.demo.btcpayserver.org"
STORE_ID = "DaNg7NwJmsqvNj1XNso5baREmGc1qy96g66BezRyB364"
API_KEY = "88c87ff9071ac34cc343eaf1b6e97a0d3e3ef6ce"

def test_connection():
    url = f"{BTCPAY_URL}/api/v1/stores/{STORE_ID}/invoices"
    headers = {
        "Authorization": f"token {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "amount": "10.0",
        "currency": "USD",
        "metadata": {"test": "true"},
        "checkout": {
            "speedPolicy": "HighSpeed", 
            "redirectAutomatically": True
        }
    }
    
    print(f"--- CONNECTING TO {BTCPAY_URL} ---")
    print(f"STORE: {STORE_ID}")
    print(f"Heades: Authorization: token {API_KEY[:4]}...")
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"STATUS CODE: {response.status_code}")
        print(f"RESPONSE TEXT: {response.text}")
        
        if response.ok:
            print("\n✅ SUCCESS! Invoice Created.")
            print(json.dumps(response.json(), indent=2))
        else:
            print("\n❌ FAILED.")
            
    except Exception as e:
        print(f"\n❌ EXCEPTION: {e}")

if __name__ == "__main__":
    test_connection()
