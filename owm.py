from pyowm import OWM


# Setting up owm object with my API key
api_key = "b3d67d6ef220e7bfe7f6e4fb688940d3"
owm_obj = OWM(api_key)

# Searching for Lund, Sweden with the registry
reg = owm_obj.city_id_registry()
cities_found = reg.ids_for('Lund', country='SE')

# Setting the observation object to Lund and collecting weather data
obs_obj = owm_obj.weather_at_id(cities_found[0][0])
weather = obs_obj.get_weather()

# Creating forecast object
fc = owm_obj.three_hours_forecast_at_id(cities_found[0][0])
print(fc.will_have_sun())

# Getting the daily forecast for Lund, Sweden
# daily_forecast = owm_obj.daily_forecast_at_id(cities_found[0][0])
# print(daily_forecast)


