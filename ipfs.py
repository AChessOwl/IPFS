import requests
import json

PINATA_API_KEY = "71c61439e484bdba55c1"
PINATA_SECRET_KEY = "d23479748af3f25931de6017be6a5712d4910b89a5e8c42dc3cf703d705914cb"

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_KEY
    }
    
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    
    result = response.json()
    cid = result["IpfsHash"]  
    
    return cid


def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    
    url = f"https://gateway.moralisipfs.com/ipfs/{cid}"
    
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json() 
    
    assert isinstance(data, dict), "get_from_ipfs should return a dict"
    
    return data
