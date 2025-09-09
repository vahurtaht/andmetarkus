# Elektri hind rest teenusest

import requests
import json

# elering url = "https://dashboard.elering.ee/api/nps/price?start=2025-05-31T20%3A59%3A59.999Z&end=2025-06-30T20%3A59%3A59.999Z"

# url ilma parameetrita
elering_url = "https://dashboard.elering.ee/api/nps/price"

def get_price(start: str, end: str):
    url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"
    response = requests.get(url)
    return response.json()

def save_json(data: dict, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=24)

# Kontrollime kas fail olemas, siis lae failist, muul juhul tee päring ja salvesta faili
def load_or_fetch_data(start: str, end: str, filename: str) -> dict:
    try:
        with open(filename, "r", encoding='utf-8') as f:
            return json.load(f)
        

start = "2025-05-31T20:59:59.999Z"
end = "2025-06-30T20:59:59.999Z"

data = get_price(start, end)
save_json(data, "elering_price_june_2025.json")

print(data)

