# EverythingEV

Smart India Hackathon 2020 Project
Problem Statement - Electric Vehicle Ecosystem
Problem Statement Owner - VMware Software India Pvt.Ltd.

## Development
Note : Make sure you have Python version 3.8+

Environment Setup

`$ git clone https://github.com/Praful932/SIH-2020.git`

`$ cd SIH-2020/`

If virtualenv is not installed [(What is virtualenv?)](https://www.youtube.com/watch?v=N5vscPTWKOk&t=313s):

`$ pip install virtualenv`

Create a virtual environment

`$ virtualenv venv`

Activate the environment everytime you open the project

`$ source venv/Scripts/activate`

`$ git checkout dev`

Install requirements

`$ pip install -r requirements.txt`

To run alpr, Install alpr for your OS from [here](https://github.com/openalpr/openalpr) using the docs, preferrably use Ubuntu, then put this file - `alpr/main.py` where alpr is installed and make sure the videos, runtime and config paths in the script point to the path in your system. Then run the script to see the Live Feed

`python3 main.py`

Add Google Map API Keys in these pages:

templates/userapp/add_charging_station.html
templates/userapp/complaint_dashboard.html
templates/userapp/consumer_charging_stations.html
templates/userapp/routeyourway.html

All Set!

`$ python manage.py runserver`

Before you do a git add/commit make sure to check the code base for coding style/programming errors

`$ flake8`

Fix it then stage changes!

To exit the environment

`$ deactivate `

