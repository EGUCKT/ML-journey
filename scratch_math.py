# def add_scores(a: float, b: float) -> float:
#     return a + b


"""bad pratice"""

# import pandas as pd
# import numpy as np
# from SSlearn import data
# from SSlearn import df

# df = pd.DataFrame(data)

# norm = df['lighting_lux'] / df['lighting_lux'].max()
# np.clip(norm, 0.0, 1.0)

# def near_police():
#     return df['dist_to_police_meters'] < 1000

# police = near_police()

# base_score = 100

# def safety_label(crime_reports):
#     for reports in crime_reports:
#         if reports != [0]:
#             new_score = base_score - 10 * reports
#         elif police.any():
#             new_score = base_score + 10
#         else:             new_score = base_score
#     return np.clip(new_score, 0, 100)

# score = safety_label(df['crime_reports'])

# print(f"Safety Score:\n{score}")



"""Instead I could have done this"""

import pandas as pd
import numpy as np
from SSlearn import df  # Just import the DataFrame directly

# 1. Feature 1: Normalize light and assign to a new column
# The raw max light level is 120 in this dataset
df['normalized_light'] = df['lighting_lux'] / 120

# 2. Feature 2: Proximity flag (checks the whole column at once)
df['near_police'] = df['dist_to_police_meters'] < 1000

# 3. Weak Supervision Label: Calculate for all rows simultaneously
# True booleans act as 1, False acts as 0 in math equations!
df['safety_label'] = 100 - (df['crime_reports'] * 10) + (df['near_police'] * 10)

# Clip the entire column to keep values between 0 and 100
df['safety_label'] = df['safety_label'].clip(0, 100)

print(df)
