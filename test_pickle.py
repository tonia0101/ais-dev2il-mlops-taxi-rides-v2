import pickle
import pandas as pd

with open("models/random_forest.pkl", "rb") as f:
    model = pickle.load(f)

rides = pd.DataFrame([
    {"ride_time": 2, "trip_distance": 100},    # 2-second, 100 km trip
    {"ride_time": 1800, "trip_distance": 5},   # 30-minute, 5 km trip
    {"ride_time": 0, "trip_distance": 50},     # Instant 50 km trip
])

predictions = model.predict(rides)
print(predictions)

for i, prediction in enumerate(predictions):
    status = "Outlier" if prediction else "Normal"
    print(f"Ride {i+1}: {status}")