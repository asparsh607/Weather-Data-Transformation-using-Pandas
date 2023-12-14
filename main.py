from extract_data import saveRawWeatherDataFrameAsCsv, getRawWeatherDataFrame
from transform_data import readRawWeatherDataAsCsv, transformWeatherData

# Uncomment and use this code if you decide to save the raw data as a CSV file locally, then perform the transformations.
# saveRawWeatherDataFrameAsCsv('raw-weather-data.csv')
# rawDataframe = readRawWeatherDataAsCsv('raw-weather-data.csv')

# Alternatively, use this code to directly collect the raw data and apply transformations
rawData = getRawWeatherDataFrame()
aggregatedWeeklyData = transformWeatherData(rawData)

# Save the transformed data to a CSV file
aggregatedWeeklyData.to_csv('transform-data.csv')
