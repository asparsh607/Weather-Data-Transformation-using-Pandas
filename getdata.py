import requests

def getLocation():
    """
    Retrieves location coordinates based on user-provided address.

    Returns:
    dict or str: Dictionary containing location coordinates if successful,
                otherwise, an error message as a string.
    """
    # Get user input for the address
    address = input('Enter Address: ')

    # Check if address is provided
    if not address:
        return 'error: Address is required'

    # Make a request to the geocoding API
    api_url = f"https://geocode.maps.co/search?q={address}"  
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'error: Failed to fetch data from the geocoding API'


def getWeatherData(latitude, longitude):
    """
    Retrieves weather data based on provided latitude and longitude.

    Parameters:
    - latitude (float): The latitude coordinate.
    - longitude (float): The longitude coordinate.

    Returns:
    dict or str: Dictionary containing weather data if successful,
                otherwise, an error message as a string.
    """
    # Check if latitude and longitude are provided
    if not longitude and latitude:
        return 'error: Latitude and longitude are required'

    # Make a request to the weather API
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation_probability,precipitation,pressure_msl,cloudcover,visibility,windspeed_10m,winddirection_10m"
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'error: Failed to fetch data from the weather API'
