
import requests

BASE_URL = "http://127.0.0.1:5000"

def generate_id(prefix=None):
    url = f"{BASE_URL}/generate-id"

    params = {}
    if prefix:
        params["prefix"] = prefix

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Generated ID:", data["generated_id"])
    else:
        print("Error:", response.status_code)


def get_all_ids():
    url = f"{BASE_URL}/ids"

    response = requests.get(url)

    if response.status_code == 200:
        print("All IDs:")
        print(response.json())
    else:
        print("Error:", response.status_code)


# ✅ Run tests
if __name__ == "__main__":
    print("---- Generating Customer ID ----")
    generate_id("CUST")

    print("\n---- Generating Bike ID ----")
    generate_id("BIKE")

    print("\n---- Getting All IDs ----")
    get_all_ids()
