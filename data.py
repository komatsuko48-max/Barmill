import json
import os

def load_offers():
    try:
        if not os.path.exists("data.json"):
            print("data.json file not found")
            return []
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception as e:
        print(f"Error loading data.json: {e}")
        return []

offers = load_offers()
