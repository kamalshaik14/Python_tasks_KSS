#2. Missing City Data (NaN Handling)
#A dataset contains city populations:
#cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
#Scenario:
#You want data for:["Delhi", "Chennai", "Bangalore"]
#Task:
#● Create a Series with the above index
#● Identify which cities have missing values (NaN)



import pandas as pd

populations = {
    "Delhi": 2_000_000,
    "Mumbai": 3_000_000,
    "Chennai": 1_500_000
}

requested_cities = ["Delhi", "Chennai", "Bangalore"]
city_data = pd.Series(populations).reindex(requested_cities)

missing_cities = city_data[city_data.isna()].index.tolist()

print(city_data)
print("Cities with missing values:", missing_cities)
