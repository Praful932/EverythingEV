# EverythingEV

For Contributing Refer [here](https://github.com/Praful932/EverythingEV/blob/master/Contributing.md).

Smart India Hackathon 2020 Project

Problem Statement - Electric Vehicle Ecosystem

Problem Statement Owner - VMware Software India Pvt.Ltd.

## Development
Note : Make sure you have Python version 3.8+

Environment Setup

`$ git clone https://github.com/Praful932/SIH-2020.git`

`$ cd SIH-2020/`

Install requirements from [poetry](https://python-poetry.org/docs/#installation) - `poetry install`
    - OR If you prefer the vanilla route using virtual env `poetry export -f requirements.txt --output requirements.txt --without-hashes`


Activate the environment -  `poetry shell`

(Optional)To run alpr, Install alpr for your OS from [here](https://github.com/openalpr/openalpr) using the docs, preferrably use Ubuntu, then put this file - `alpr/main.py` where alpr is installed and make sure the videos, runtime and config paths in the script point to the path in your system. Then run the script to see the Live Feed

All Set!

`$ python manage.py runserver`

Before you do a git add/commit make sure to check the code base for coding style/programming errors

`pre-commit run --all-files`

