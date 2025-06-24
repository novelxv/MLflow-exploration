import requests
import json

test_data = {
    "average_temperature": [25.5, 30.2, 22.1],
    "rainfall": [2.1, 0.5, 3.2],
    "weekend": [1, 0, 1],
    "holiday": [0, 0, 0],
    "price_per_kg": [1.5, 2.0, 1.8],
    "promo": [1, 0, 1],
    "previous_days_demand": [1200, 1100, 1300]
}

response = requests.post(
    "http://localhost:5000/predict",
    json=test_data,
    headers={"Content-Type": "application/json"}
)

print("Status Code:", response.status_code)
print("Response:", response.json())