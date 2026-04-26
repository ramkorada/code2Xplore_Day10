# Advanced Data Replication & Predictive Risk Analyzer

## Overview

This project simulates a large-scale system where data is replicated across multiple zones. It focuses on how incorrect copying methods can lead to hidden data corruption. The program uses Python along with NumPy and Pandas to analyze data integrity, detect anomalies, and predict system risk levels.

## Problem Statement

A system replicates critical data for analytics. Improper copying can cause hidden corruption, which affects predictions. This program generates random nested data, applies different copy techniques, modifies the data, and performs analysis to detect corruption and predict system stability.

## Features

* Random data generation for multiple zones
* Nested data structures (list, dictionary, list)
* Assignment, shallow copy, and deep copy implementation
* Multi-level data modification
* Custom risk calculation using logarithmic function
* Data analysis using NumPy and Pandas
* Manual correlation calculation
* Detection of anomalies and corruption
* Final system stability prediction

## Technologies Used

* Python
* NumPy
* Pandas
* math module
* random module
* copy module

## Data Format

```python
{
  "zone": int,
  "metrics": {
    "traffic": int,
    "pollution": int,
    "energy": int
  },
  "history": [past_values]
}
```

## Functions Used

* `generate_data()` – generates random data for zones
* `personalize_data()` – applies dataset transformation based on roll number
* `replicate_data()` – creates assignment, shallow, and deep copies
* `modify_data()` – updates nested values and computes risk
* `custom_risk_score()` – calculates risk using log function
* `to_dataframe()` – converts data into Pandas DataFrame
* `manual_correlation()` – computes correlation without using built-in method
* `analyze()` – calculates mean, variance, anomalies
* `detect_corruption()` – identifies shallow copy issues
* `final_decision()` – determines system condition

## Personalization Rule

Last digit of Register Number: 2
Since it is even, the dataset is reversed.

## Custom Risk Function

Risk is calculated using:

```
log(traffic + pollution + energy)
```

## Logic and Approach

1. Generate random data for 15 zones.
2. Apply personalization by reversing the dataset.
3. Create assignment, shallow, and deep copies.
4. Modify nested data including metrics and history.
5. Compute risk score using a logarithmic function.
6. Convert processed data into a DataFrame.
7. Perform statistical analysis using NumPy.
8. Detect anomalies based on threshold (mean + standard deviation).
9. Compute correlation manually.
10. Detect corruption due to shallow copy.
11. Calculate stability index and final system decision.

## Definition of Data Corruption

Data corruption is defined as unintended changes in the original dataset when only a copied version is modified. This mainly occurs due to shallow copy sharing references of nested structures.

## Sample Output

```
BEFORE
[{'zone': 15, 'metrics': {'traffic': 120, 'pollution': 80, 'energy': 90}, 'history': [20, 30, 40, 50, 60]}, ...]

AFTER
Original: [...]
Shallow: [...]
Deep: [...]

DataFrame
   zone  traffic  pollution  energy   risk
   ...

Anomaly Zones: [15, 12, 9]
Correlation: 0.82
Tuple: (5.60, 5.10, 0.045)

Final Decision: Moderate Risk
```

## Key Concepts Demonstrated

* Difference between assignment, shallow copy, and deep copy
* Behavior of nested data structures
* Data corruption due to shared references
* Use of NumPy for numerical analysis
* Use of Pandas for data representation
* Manual implementation of correlation
* Risk prediction using mathematical functions

## Learning Outcome

This project helps in understanding how data replication works and how improper copying can lead to serious issues. It also provides basic knowledge of data analysis and risk prediction using Python tools.

## Conclusion

Correct data handling is important in large systems. This project demonstrates how shallow copy can cause hidden corruption and how deep copy ensures data safety. It also shows how analytical methods can be used to detect and predict system risks.
