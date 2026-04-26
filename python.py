import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data():
    data = []
    for i in range(15):
        zone = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone)
    return data

def personalize_data(data):
    return list(reversed(data))

def replicate_data(original):
    assigned = original
    shallow = list(original)
    deep = copy.deepcopy(original)
    return assigned, shallow, deep

def custom_risk_score(t, p, e):
    return math.log(t + p + e)

def modify_data(data):
    for item in data:
        item["metrics"]["traffic"] += 10
        item["metrics"]["pollution"] += 5
        item["metrics"]["energy"] += 8
        item["history"].append(random.randint(10, 100))
        item["risk"] = custom_risk_score(
            item["metrics"]["traffic"],
            item["metrics"]["pollution"],
            item["metrics"]["energy"]
        )

def to_dataframe(data):
    rows = []
    for item in data:
        row = {
            "zone": item["zone"],
            "traffic": item["metrics"]["traffic"],
            "pollution": item["metrics"]["pollution"],
            "energy": item["metrics"]["energy"],
            "risk": item.get("risk", 0)
        }
        rows.append(row)
    return pd.DataFrame(rows)

def manual_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    num = np.sum((x - x_mean) * (y - y_mean))
    den = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    return num / den

def analyze(df):
    traffic = df["traffic"].values
    pollution = df["pollution"].values

    mean = np.mean(df["risk"])
    std = np.std(df["risk"])

    anomalies = df[df["risk"] > mean + std]["zone"].tolist()

    corr = manual_correlation(traffic, pollution)

    stability_index = 1 / np.var(df["risk"])

    return anomalies, corr, stability_index

def detect_corruption(original, shallow):
    count = 0
    for i in range(len(original)):
        if original[i]["metrics"] == shallow[i]["metrics"]:
            count += 1
    return count

def final_decision(stability, corruption):
    if corruption > 10:
        return "Critical Failure"
    elif stability < 0.01:
        return "High Corruption Risk"
    elif stability < 0.05:
        return "Moderate Risk"
    else:
        return "System Stable"


data = generate_data()
data = personalize_data(data)

print("BEFORE")
print(data)

assigned, shallow, deep = replicate_data(data)

modify_data(shallow)
modify_data(deep)

df = to_dataframe(deep)

print("\nAFTER")
print("Original:", data)
print("Shallow:", shallow)
print("Deep:", deep)

print("\nDataFrame")
print(df)

anomalies, corr, stability = analyze(df)
corruption = detect_corruption(data, shallow)

max_risk = df["risk"].max()
min_risk = df["risk"].min()

print("\nAnomaly Zones:", anomalies)
print("Correlation:", corr)
print("Tuple:", (max_risk, min_risk, stability))

decision = final_decision(stability, corruption)
print("\nFinal Decision:", decision)
