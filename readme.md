# NASA Picture of the Day Background Changer

This script downloads the NASA Picture of the Day and sets it as the background image in Windows.

## Requirements

- Python 3
- `requests` library

## Usage

1. Clone the repository or download the script file.
2. Replace `YOUR_API_KEY` in the script with your own NASA API key, which you can obtain from the NASA API website (https://api.nasa.gov/).
3. Run the script by executing the following command in your terminal or command prompt:

## Run
You can use the Windows Task Scheduler to run the script at a specific time. Here are the steps to do that:

    Open the Windows Task Scheduler by typing "Task Scheduler" in the Start menu search bar and clicking on the "Task Scheduler" app.
    In the Task Scheduler, click on "Create Basic Task..." in the Actions panel on the right.
    In the "Create Basic Task Wizard", give a name to the task and a description (optional), then click on "Next".
    Choose when you want the task to run (e.g., daily, weekly, etc.), then click on "Next".
    In the next step, choose the start time and date for the task, then click on "Next".
    In the "Action" step, choose "Start a program", then click on "Next".
    In the "Program/script" field, enter the path to the Python executable (e.g., C:\Python3x\python.exe).
    In the "Add arguments (optional)" field, enter the path to your script (e.g., C:\scripts\nasa_picture_of_the_day_background.py).
    Click on "Finish" to create the task.

Now, the script will run automatically at the specified time using the Windows Task Scheduler. Note that you may need to configure the task scheduler to run with administrative privileges to allow it to change the desktop background. 


## Code Explanation

python nasa_picture_of_the_day_background.py

The script uses the following libraries:
- `requests` to make a request to the NASA API and download the image
- `ctypes` to change the Windows desktop background

The script first makes a request to the NASA API to retrieve the data for the Picture of the Day. It then parses the data and extracts the URL of the image. The image is then downloaded and saved as background.jpg. Finally, the script sets the image as the Windows desktop background using the ctypes library.

