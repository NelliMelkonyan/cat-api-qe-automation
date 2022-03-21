# Cat Fact API AUtomation project

## Description
The project contains automated test cases for CAT Fact API.
Doc for the API - https://catfact.ninja/ 

## Frameworks
The API automation is done with python/pytest framework

## Requirements & Build project
You need to have installed
- python3.* (Please follow the [documentation](https://www.python.org/downloads/))
- Install/Activate python virtual env (Follow the steps in the [doc](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))
- Install required modules
  - ```pip install -r requirements.txt```
 
## Run Tests
For running tests please use the following command
``` pytest tests/ -v```

## Analyze results
Open `pytest_html_report.html` file in your browser.

## Project structure
Project has the following structure
```
├── constants // for storing constants
│   ├── const.py
│   └── status_codes.py
├── README.md // project readme file
├── requirements.txt //dependencies
├── schemas // json schema files
│   ├── get_facts.json
├── tests //tests
│   ├── get_cats_api_positive_test.py
└── utils // utility fuctions
    ├── request_builder
    │   ├── builder.py
    └── response_validator
        └── validator.py
```