import pandas as pd

# Create datetime objects
dates = pd.to_datetime([
    '2026-01-01',
    '2026-01-02',
    '2026-01-03',
    '2026-01-04',
    '2026-01-05'
])

# Create data
temperature = [28, 30, 29, 31, 32]

# Create time series with timestamps as index
time_series = pd.Series(
    temperature,
    index=dates
)

# Display the time series
print("Time Series:")
print(time_series)
