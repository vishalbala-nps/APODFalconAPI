# APODFalconAPI
A Python program built using Falcon which gets today's NASA Astronomy Picture of the day
# Introduction
This is a Python program which is built using Falcon and gets today's NASA Astronomy Picture of the Day.
# Installation

 1. Create a Virtual environment by running: `virtualenv -p python3 env`
 2. Clone this repo by running: `git clone https://github.com/vishalbala-nps/APODFalconAPI`
 3. Then, inside the Cloned Repo, activate it by running: `source env/bin/activate`
 4. Download all the required modules by running: `pip3 install -r requirements.txt`
 5. Run the app by running: `gunicorn look.app` You can get the image and description by typing: `127.0.0.1:8000/get_img` The info will be displayed in JSON Format

