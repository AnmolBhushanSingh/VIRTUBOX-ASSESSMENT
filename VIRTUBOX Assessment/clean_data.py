import numpy as np
import pandas as pd


df = pd.read_csv("test.csv")  


if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)


df["Customer Type"] = df["Customer Type"].str.title() 


df["Arrival Delay in Minutes"] = df["Arrival Delay in Minutes"].fillna(df["Departure Delay in Minutes"])


df["Total Delay Minutes"] = df["Departure Delay in Minutes"] + df["Arrival Delay in Minutes"]


delay_bins = [-np.inf, 0, 15, 60, np.inf]
delay_labels = ["On-Time / Early", "Minor Delay (1-15m)", "Moderate Delay (16-60m)", "Major Delay (>60m)"]
df["Delay Category"] = pd.cut(df["Arrival Delay in Minutes"], bins=delay_bins, labels=delay_labels)

age_bins = [0, 19, 35, 50, 65, 120]
age_labels = ["Under 20", "20-35", "36-50", "51-65", "65+"]
df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

service_cols = [
    "Inflight wifi service", "Departure/Arrival time convenient", "Ease of Online booking",
    "Gate location", "Food and drink", "Online boarding", "Seat comfort",
    "Inflight entertainment", "On-board service", "Leg room service",
    "Baggage handling", "Checkin service", "Inflight service", "Cleanliness"
]
df["Average Service Rating"] = df[service_cols].mean(axis=1).round(2)


df["Is_Satisfied"] = (df["satisfaction"] == "satisfied").astype(int)


df.to_csv("Processed_Data.csv", index=False)
print(f"Processed dataset saved! Shape: {df.shape}")