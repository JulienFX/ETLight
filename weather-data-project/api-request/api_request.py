import requests 
api_key = "0ecbe5635ccf962f4076fc7224b05726"
# fstring pour inclure des variables 
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York" 

# Récupération données API 
def fetch_data() : 
    print("Fetching weather data from Weatherstack API")
    try : 
        response = requests.get(api_url)
        response.raise_for_status() # pour gérer erreur 400 ou http
        print("API response received successfully.")
        print(response.json())
        return response.json()
    except requests.exception.RequestException as e : 
        print(f"An error occured : {e}")

# Simulation d'appel d'API
def mock_fetch_data() : 
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-11-16 14:26', 'localtime_epoch': 1763303160, 'utc_offset': '-5.0'}, 'current': {'observation_time': '07:26 PM', 'temperature': 12, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:44 AM', 'sunset': '04:37 PM', 'moonrise': '03:15 AM', 'moonset': '02:38 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 16}, 'air_quality': {'co': '200.85', 'no2': '14.25', 'o3': '61', 'so2': '3.15', 'pm2_5': '3.45', 'pm10': '3.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 33, 'wind_degree': 288, 'wind_dir': 'WNW', 'pressure': 993, 'precip': 0, 'humidity': 32, 'cloudcover': 75, 'feelslike': 9, 'uv_index': 1, 'visibility': 16, 'is_day': 'yes'}}

mock_fetch_data()