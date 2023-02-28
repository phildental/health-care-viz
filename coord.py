import pandas as pd
import requests
from pandasgui import show
import requests_cache 

# Define the URL and API key
url = 'https://api.opencagedata.com/geocode/v1/json'
api_key = 'dd1b9d97b6a048bb8faacb7e736ffaac'
requests_cache.install_cache('http_cache')

def get_countries_coordinates(metrics_df):
    # Get the dictionary of countries
    countries = metrics_df['CountryName'].to_dict()

    # Create an empty DataFrame to store the results
    results_df = pd.DataFrame()

    # Loop through the countries and make the API call
    for country in list(countries.values()):
        params = {'q': country, 'key': api_key}
        with requests.get(url, params=params) as response:
            data = response.json()
        country_df = pd.json_normalize(data['results'][0])
        results_df = pd.concat([results_df, country_df], ignore_index=True)
        results_df = results_df.iloc[:, :4]
