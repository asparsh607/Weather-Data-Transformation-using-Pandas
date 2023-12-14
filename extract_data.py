import pandas as pd
from getdata import getLocation, getWeatherData

def saveRawWeatherDataFrameAsCsv(csvfilename: str):
    """
    Saves hourly weather data as a CSV file.

    Parameters:
    - name_of_csv (str): The name of the CSV file to be saved.

    Returns:
    None
    """
    # Get the current location coordinates
    location_coordinates = getLocation()
    latitude = location_coordinates[0]['lat']
    longitude = location_coordinates[0]['lon']

    # Retrieve hourly weather data based on the location
    weather_data = getWeatherData(latitude=latitude, longitude=longitude)

    # Create a DataFrame using the hourly weather data
    df = pd.DataFrame(weather_data['hourly'])

    # Save the DataFrame to a CSV file
    df.to_csv(csvfilename, index=False)

def getRawWeatherDataFrame() -> pd.DataFrame:
    """
    Retrieves hourly weather data as a Pandas DataFrame.

    Returns:
    pd.DataFrame: DataFrame containing hourly weather data.
    """
    # Get the current location coordinates
    location_coordinates = getLocation()
    latitude = location_coordinates[0]['lat']
    longitude = location_coordinates[0]['lon']

    # Retrieve hourly weather data based on the location
    weather_data = getWeatherData(latitude=latitude, longitude=longitude)

    # Create a DataFrame using the hourly weather data
    df = pd.DataFrame(weather_data['hourly'])

    return df
