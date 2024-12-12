from django.shortcuts import render
from .utils import get_village_info, get_top_restaurants, get_busy_times, get_weather, predict_price

def index(request):
    # Get village info
    village_info = get_village_info()
    
    # Check if we have any businesses returned
    if 'businesses' in village_info and len(village_info['businesses']) > 0:
        # Get the first business's place_id
        place_id = village_info['businesses'][0]['id']  # Assuming the ID is the place_id for Google Maps
        
        # Get top restaurants
        top_restaurants = get_top_restaurants()
        
        # Get busy times using the place_id
        busy_times = get_busy_times(place_id)
        
        # Get weather information
        weather = get_weather()
        
        # Extract necessary data for price prediction
        lowest_price = village_info['businesses'][0].get('price', 0)  # Example extraction
        temperature = weather['temperature']  # Example extraction
        is_busy = len(busy_times) > 0  # Example condition
        is_raining = weather['rain'] > 0  # Example extraction
        
        # Predict price
        predicted_price = predict_price(lowest_price, temperature, is_busy, is_raining)
        
        context = {
            'village_info': village_info,
            'top_restaurants': top_restaurants,
            'busy_times': busy_times,
            'weather': weather,
            'predicted_price': predicted_price,
        }
    else:
        # Handle case where no businesses are found
        context = {
            'error': 'No businesses found for Village.'
        }

    return render(request, 'index.html', context)