# Settings used by weather.py
""" Constants used in weather.py """
# This is your Dark Sky API key
DS_API_KEY = 'f19b71c4aa4b100daa107ee5a1360f07'

# Seconds between API calls.
# Note: the free Dark Sky access only allows for 1,000 calls / day
#       aka a check ~ every 1.44 minutes
DS_CHECK_INTERVAL = 300 # 5 minutes

# The location you want to check
LAT = 49.878708
LON = 8.646927

# Full screen is for when this is running on a TV or
# similar device with a much higher resolution.
FULLSCREEN = False

# If the weather icons are overlapping the text try adjusting
# this value. Negative values raise the icon.
LARGE_ICON_OFFSET = -23.5
