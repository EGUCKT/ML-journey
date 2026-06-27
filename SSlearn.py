
# user_name = 'Atharv'
# incidents_reported = 5
# initial_score = 100
# score_deduction_per_incident = 5
# final_score = initial_score - (incidents_reported * score_deduction_per_incident)
# print(f" Hello {user_name}, your area has had {incidents_reported} incidents. The safety score is now {final_score}.")





# city_names = ['CityA', 'CityB', 'CityC', 'CityD', 'CityE']
# safety_score = [85, 42, 60, 95, 30]

# city_safety = dict(zip(city_names, safety_score))

# for city, score in city_safety.items():
#     if score >= 80:
#         print(f"{city} is considered very safe with a score of {score}.")
#     elif score >= 50:
#         print(f"{city} is considered moderately safe with a score of {score}.")
#     else:
#         print(f"{city} is considered unsafe with a score of {score}.")





# base_score = 100

# penalties = {
#         'dark_streets': 15,
#         'potholes': 10,
#         'rainy_weather': 5
#     }

# def compute_safety_score(base_score, **penalties):
#         new_score = base_score - sum(penalties.values())
#         print(f"The base score was {base_score} but after calculating the penalties, the new score is {new_score}")

# compute_safety_score(base_score, **penalties)






# route_data = {
#     'route_id': "R-101",
#     'waypoints':[
#         [18.288, 77.456],
#         [19.123, 78.789],
#         [20.456, 79.012]
#     ]
# }

# route_data['waypoints'].append([21.789, 80.345])

# print(route_data.get('driver_name', 'No nodes found for this route'))





# gps_coordinates = [[19.07, 72.87], [0.0, 0.0], [18.52, 73.85], [0.0, 0.0], [28.70, 77.10]]
# valid_coordinates = [coordinate for coordinate in gps_coordinates if coordinate != [0.0, 0.0]]
# print(valid_coordinates)






# class Report:
#     def __init__(self, category, severity):
#         self.category = category
#         self.severity = severity

#     def is_high_risk(self):
#         if self.severity >= 4:
#            return True
#         else :
#            return False


# calc = Report(category="dark street", severity=5)
# result = calc.is_high_risk()
# print(result)



# class BaseModel:
#     def __init__(self, model_name):
#         self.model_name = model_name

# class RouteModel(BaseModel):
#     def __init__(self, model_name, accuracy_score, latency_ms):
#         super().__init__(model_name)
#         self.accuracy_score = accuracy_score
#         self.latency_ms = latency_ms

#     @property
#     def is_production_ready(self):
#         if self.accuracy_score > 0.8 and self.latency_ms < 50:
#             return True
#         else:
#             return False
        
# route_model = RouteModel(model_name="SafeRouteV1", accuracy_score=0.85, latency_ms=45)
# result = route_model.is_production_ready
# print(f"Is the model production ready? {result}")





# from typing import List

# route_points = [
#     [19.22, 82.44],
#     [37.33, 74.65]
# ]

# max_distance = 100.00

# def validate_route(route_points : List[List[float]], max_distance : float) -> bool:
#     if len(route_points) > 0:
#         return True
#     else:
#         return False

# result = validate_route(route_points, max_distance)
# print(f"Is the route valid? {result}")






# def fetch_routing_api(url: str) -> str :
#     if url == "" :
#         raise ValueError("URL cannot be empty")
#     else:
#         return "Route Data Fetched!"

# url = ""

# try:
#     run = fetch_routing_api(url)
#     print(run)
# except ValueError as e:
#     print(f"Caught an error: {e}")
# finally:
#     print("API request process finished.")





# from scratch_math import add_scores
# print(add_scores(10.5, 20.5))





# import pandas as pd
# import numpy as np

# data = {
#     'road_id': [1, 2, 3, 4],
#     'lighting_lux': [120, 10, 5, 95],          # Raw light level (0-150)
#     'dist_to_police_meters': [1200, 200, 3500, 800], # Distance in meters
#     'crime_reports': [0, 4, 12, 1]              # Incidents reported
# }
# df = pd.DataFrame(data)



"""WORKING ON REAL WORLD DATA FROM MY COLLEGE"""
import pandas as pd
import matplotlib as mpl
import numpy as np

df = pd.read_csv("atsres.csv")

sf = df

"""dealing with str, and symbols like '/', '-', '%' and convertign them to NaN and then filling with median while converting to float"""
sf['ATS Resume Score'] = sf['ATS Resume Score'].replace(r"[^\d.-]", np.nan, regex=True) 

sf['ATS Resume Score'] = pd.to_numeric(sf['ATS Resume Score'], errors= "coerce")

sf['ATS Resume Score'] = sf['ATS Resume Score'].fillna(sf['ATS Resume Score'].median())

# print('The mean is:')
# print(sf['ATS Resume Score'].mean())

# print('The lowest score is:')
# print(sf['ATS Resume Score'].min())
# print("Whose index is:", sf['ATS Resume Score'].idxmin())
# print(sf.loc[202])

# print('The highest score is:')
# print(sf['ATS Resume Score'].max())
# print("Whose index is:", sf['ATS Resume Score'].idxmax())
# print(sf.loc[72])

# print(sf.groupby('Section')['ATS Resume Score'].mean())

# print(sf.groupby('Section')['Name'].count())

# print(sf.groupby('Section')['Name'].count().idxmax())

# print(sf.groupby('Section')['Name'].count().idxmin())

# print(sf['ATS Resume Score'].sort_values(ascending = False))

# print(sf.nlargest(10, 'ATS Resume Score'))

# print(sf.groupby('Section')['ATS Resume Score'].idxmax())

# print(sf.groupby('Section')['ATS Resume Score'].max(), sf.groupby('Section')['ATS Resume Score'].min())

