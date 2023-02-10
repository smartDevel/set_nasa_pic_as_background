import requests
import ctypes
import json

# URL for NASA's Picture of the Day API
# for test purpose use DEMO_KEY as api_key
# url = "https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY"
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# windows full file path 
WIN_FILEPATH = "D:\\scripts\\win\\setBackgroundPicNASA\\bg_wallpaper.jpg"

# Request the data from the API
response = requests.get(url)
data = json.loads(response.text)

# Get the URL of the image
img_url = data["hdurl"]

# Download the image
response = requests.get(img_url)
#open("background.jpg", "wb").write(response.content)
open(WIN_FILEPATH, "wb").write(response.content)

# Set the image as the background
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WIN_FILEPATH, 0)

