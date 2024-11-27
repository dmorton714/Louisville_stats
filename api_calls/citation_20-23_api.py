# # -------------------------------------------------------- #
# # Only run the API calls if you dont have the current data #
# # -------------------------------------------------------- #

import pandas as pd
import os
import requests

urls = [
    'https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Uniform_Citation_Data_2023/FeatureServer/0/query', # noqa
    'https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Uniform_Citation_Data_2020/FeatureServer/0/query', # noqa
    'https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Uniform_Citation_Data_2021/FeatureServer/0/query', # noqa
    'https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Uniform_Citation_Data_2022/FeatureServer/0/query' # noqa
]

batch_size = 1000
data_list = []

for url in urls:
    offset = 0
    while True:
        params = {
            'where': '1=1',
            'outFields': '*',
            'returnGeometry': 'false',
            'f': 'json',
            'resultOffset': offset,
            'resultRecordCount': batch_size
        }

        response = requests.get(url, params=params)
        print(f"Requesting URL: {response.url}")

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            break

        try:
            query_result = response.json()
        except ValueError:
            print(f"Failed to parse JSON response: {response.text}")
            break

        features = query_result.get('features', [])
        if not features:
            break

        for feature in features:
            data_list.append(feature['attributes'])

        if len(features) < batch_size:
            break

        offset += batch_size

if data_list:
    df = pd.DataFrame(data_list)

    output_directory = 'test'
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, 'citations_20-23.csv')
    df.to_csv(output_path, index=False)

    print(f"Data saved to {output_path}")
else:
    print("No data retrieved.")
