import json

FILE = "data/leads.json"

def save_lead(lead):
    try:
        data = json.load(open(FILE))
    except:
        data = []

    data.append(lead)
    json.dump(data, open(FILE, "w"), indent=2)
