import requests
import hmac
import hashlib
import json
import logging

# --- CONFIGURATION ---
# In production, load these from os.environ
BTCPAY_URL = "https://mainnet.demo.btcpayserver.org"
STORE_ID = "4n1WHr4nZDfrjhP76Hwbsdb6iN5hU18ZibsYJiZCohYP"
API_KEY = "88c87ff9071ac34cc343eaf1b6e97a0d3e3ef6ce"
WEBHOOK_SECRET = None # Optional: Set this if you configure a secret in BTCPay

def create_invoice(amount, currency, metadata=None):
    """
    Creates an invoice on BTCPay Server.
    metadata: dict containing custom fields (e.g. {'userId': '123', 'plan': 'commander'})
    """
    url = f"{BTCPAY_URL}/api/v1/stores/{STORE_ID}/invoices"
    headers = {
        "Authorization": f"token {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "amount": str(amount),
        "currency": currency,
        "metadata": metadata or {},
        "checkout": {
            "speedPolicy": "HighSpeed", # Recommend for digital goods
            "redirectAutomatically": True,
            # "redirectURL": "http://localhost:5173/success" # Ideally dynamic
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"BTCPay Invoice Creation Failed: {e}")
        if hasattr(e, 'response') and e.response:
            logging.error(f"Response: {e.response.text}")
        raise e

def verify_webhook_signature(payload_body, sig_header, secret):
    """
    Verifies that the webhook came from BTCPay Server.
    sig_header: The 'BTCPay-Sig' header value.
    secret: The webhook secret configured in BTCPay.
    """
    if not secret:
        return True # specific override if no secret set
        
    computed_sig = "sha256=" + hmac.new(
        key=secret.encode('utf-8'),
        msg=payload_body,
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(computed_sig, sig_header)
