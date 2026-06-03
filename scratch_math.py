# def add_scores(a: float, b: float) -> float:
#     return a + b




import pandas as pd
import numpy as np
from SSlearn import data
from SSlearn import df

df = pd.DataFrame(data)

norm = df['lighting_lux'] / df['lighting_lux'].max()
np.clip(norm, 0.0, 1.0)

def near_police():
    return df['dist_to_police_meters'] < 1000

police = near_police()

base_score = 100

def safety_label(crime_reports):
    for reports in crime_reports:
        if reports != [0]:
            new_score = base_score - 10 * reports
        elif police.any():
            new_score = base_score + 10
        else:             new_score = base_score
    return np.clip(new_score, 0, 100)

score = safety_label(df['crime_reports'])

print(f"Safety Score:\n{score}")