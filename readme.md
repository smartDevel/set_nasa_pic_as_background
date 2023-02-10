# NASA Picture of the Day Background Changer

This script downloads the NASA Picture of the Day and sets it as the background image in Windows.

## Requirements

- Python 3
- `requests` library

## Usage

1. Clone the repository or download the script file.
2. Replace `YOUR_API_KEY` in the script with your own NASA API key, which you can obtain from the NASA API website (https://api.nasa.gov/).
3. Run the script by executing the following command in your terminal or command prompt:

python nasa_picture_of_the_day_background.py

## Code Explanation

The script uses the following libraries:
- `requests` to make a request to the NASA API and download the image
- `ctypes` to change the Windows desktop background

The script first makes a request to the NASA API to retrieve the data for the Picture of the Day. It then parses the data and extracts the URL of the image. The image is then downloaded and saved as background.jpg. Finally, the script sets the image as the Windows desktop background using the ctypes library.

