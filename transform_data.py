import pandas as pd
import numpy as np
from functools import reduce

def readRawWeatherDataAsCsv(csvfilename: str) -> pd.DataFrame:
    """
    Reads raw weather data from a CSV file into a Pandas DataFrame.

    Parameters:
    - csvfilename (str): The name of the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the raw weather data.
    """
    df = pd.read_csv(csvfilename)
    return df

def transformWeatherData(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw weather data into aggregated and processed DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): Raw weather data DataFrame.

    Returns:
    pd.DataFrame: Aggregated and processed weather data DataFrame.
    """
    # Extract date from the 'time' column
    dataframe['time'] = [time[0:10] for time in dataframe['time']]

    # Aggregating temperature data
    tempAgg_df = dataframe.groupby('time')['temperature_2m'].agg(tempAvg='mean', tempMax='max', tempMin='min')

    # Aggregating humidity data
    humidAgg_df = dataframe.groupby('time')['relativehumidity_2m'].agg(relHumidityAvg='mean', relHumidityMax='max', relHumidityMin='min')

    # Aggregating apparent temperature data
    appTempAgg_df = dataframe.groupby('time')['apparent_temperature'].agg(appTemperatureAvg='mean', appTemperatureMax='max', appTemperatureMin='min')

    # Aggregating precipitation probability data
    precProbAgg_df = dataframe.groupby('time')['precipitation_probability'].agg(precProbAvg='mean', precProMax='max', precProMin='min')

    # Aggregating precipitation data
    precAgg_df = dataframe.groupby('time')['precipitation'].agg(precAvg='mean', precMax='max', precMin='min')

    # Aggregating pressure data
    pressureAgg_df = dataframe.groupby('time')['pressure_msl'].agg(pressureAvg='mean', pressureMax='max', pressureMin='min')

    # Aggregating cloud cover data
    cloudCoverAgg_df = dataframe.groupby('time')['cloudcover'].agg(cloudCoverAvg='mean', cloudCoverMax='max', cloudCoverMin='min')

    # Aggregating visibility data
    visiilityAgg_df = dataframe.groupby('time')['visibility'].agg(visibilityAvg='mean', visibilityMax='max', visibilityMin='min')

    # Aggregating wind speed data
    windSpeedAgg_df = dataframe.groupby('time')['windspeed_10m'].agg(windSpeedAvg='mean', windSpeedMax='max', windSpeedMin='min')

    # Aggregating wind direction data
    winddirectionAgg_df = dataframe.groupby('time')['winddirection_10m'].agg(prominantWindDirection='mean')

    # Combine all aggregated DataFrames into one
    dataFramesList = [tempAgg_df, humidAgg_df, appTempAgg_df, precProbAgg_df, precAgg_df, pressureAgg_df, cloudCoverAgg_df, visiilityAgg_df, windSpeedAgg_df, winddirectionAgg_df]
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['time'], how='inner'), dataFramesList)

    # Map wind directions to cardinal directions
    df_merged['prominantWindDirection'] = np.where(
        df_merged['prominantWindDirection'].between(0, 22.5, inclusive='left'), 
        'North', 
        np.where(
        df_merged['prominantWindDirection'].between(22.5, 67.5, inclusive='left'),
        'North-East',
        np.where(
        df_merged['prominantWindDirection'].between(67.5, 112.5, inclusive='left'),
        'East',
        np.where(
        df_merged['prominantWindDirection'].between(112.5, 157.5, inclusive='left'),
        'South-East',
        np.where(
        df_merged['prominantWindDirection'].between(157.5, 202.5, inclusive='left'),
        'South',
        np.where(
        df_merged['prominantWindDirection'].between(202.5, 247.5, inclusive='left'),
        'South-West',
        np.where(
        df_merged['prominantWindDirection'].between(247.5, 292.5, inclusive='left'),
        'West',
        np.where(
        df_merged['prominantWindDirection'].between(292.5, 337.5, inclusive='left'),
        'North-West',
        np.where(
        df_merged['prominantWindDirection'].between(337.5, 360, inclusive='both'),
        'North',
        df_merged['prominantWindDirection']))))))))
    )

    return df_merged