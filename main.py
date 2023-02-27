import pandas as pd
from pandasgui import show
import requests
import requests_cache
from coord import get_countries_coordinates

# URLs
dimension_url = 'https://ghoapi.azureedge.net/api/Dimension/'
indicator_url = 'https://ghoapi.azureedge.net/api/Indicator'
telehealth_url = 'https://ghoapi.azureedge.net/api/GOE_Q069'
country_url = 'https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues'
requests_cache.install_cache('http_cache')

# Use context managers to handle the HTTP requests
with requests.get(dimension_url) as response:
    dimension_data = response.json()

with requests.get(indicator_url) as response:
    indicator_data = response.json()

with requests.get(telehealth_url) as response:
    telehealth_data = response.json()

with requests.get(country_url) as response:
    country_data = response.json()

# Convert the response JSON to DataFrames
dimensions_df = pd.json_normalize(dimension_data['value'])
indicators_df = pd.json_normalize(indicator_data['value'])
telehealth_df = pd.json_normalize(telehealth_data['value'])
countries_df = pd.json_normalize(country_data['value'])

# Extract relevant columns and rename them
dimensions_df = dimensions_df[['Code', 'Title']]
dimensions_df.columns = ['DimensionCode', 'DimensionTitle']

indicators_df = indicators_df[['IndicatorCode', 'IndicatorName', 'Language']]

telehealth_df = telehealth_df[['Id', 'IndicatorCode', 'SpatialDim', 'TimeDim', 'Value']]
telehealth_df.columns = ['TelehealthId', 'IndicatorCode', 'CountryCode', 'Year', 'Value']

countries_df = countries_df[['Code', 'Title']]
countries_df.columns = ['CountryCode', 'CountryName']

# Merge the DataFrames
metrics_df = countries_df.merge(telehealth_df, left_on='CountryCode', right_on='CountryCode')
