import requests,json

YELP_API_KEY = 'YOUR_YELP_API_KEY'
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
OPENWEATHER_API_KEY = 'YOUR_OPENWEATHER_API_KEY'

def get_village_info():
    # Get Village info from Yelp
    url = f'https://api.yelp.com/v3/businesses/search?term=Village&location=Hicksville'
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_top_restaurants(location='Hicksville', radius=2000):
    # Get top-rated restaurants within 2 km
    url = f'https://api.yelp.com/v3/businesses/search?location={location}&radius={radius}&sort_by=rating'
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    response = requests.get(url, headers=headers)
    if response:
        return response.json()
    

def get_busy_times(place_id):
    # Get busy times from Google Maps API
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={GOOGLE_MAPS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    # Extract busy times if available
    busy_times = data.get('result', {}).get('opening_hours', {}).get('periods', [])
    return busy_times

def get_weather(location='Hicksville'):
    # Get temperature and rain from OpenWeather API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=imperial'  # Use 'imperial' for Fahrenheit
    response = requests.get(url)
    weather_data = response.json()
    
    # Extract temperature and rain information
    temperature = weather_data.get('main', {}).get('temp')
    rain = weather_data.get('rain', {}).get('1h', 0)  # Rain volume in the last hour
    return {
        'temperature': temperature,
        'rain': rain
    }

def predict_price(lowest_price, temperature, is_busy, is_raining):
    if temperature < 45 and is_raining and is_busy:
        return lowest_price + 5  # Increase price
    else:
        return lowest_price  # Keep lowest price