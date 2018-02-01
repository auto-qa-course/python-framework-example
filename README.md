# Overview
This is a Demo test framework for Automation QA course. 

# Requirements

* `pytest`
* `allure-pytest`
* `requests`

Also one need to install Alure CLI to be able generate allure reports, see https://docs.qameta.io/allure/latest/#_reporting. 

# Test configuration

One can configure test execution against specific environment using environment variables:
 
| Name                  | Required  | Default                  | Example                                               |
| --------------------  | --------- | ------------------------ |------------------------------------------------------ |
|  ENVIRONMENT          | yes       | none                     | QA, Stage   |  
|  TEST_TYPE            | yes       | none                     | ui, api     |
|  RESULTS_FOLDER       | no        | reports                  | reports     |


# API Test execution from CLI

```
ENVIRONMENT=QA
TEST_TYPE=api
RESULTS_FOLDER=reports

pytest test/api --alluredir $RESULTS_FOLDER/$TEST_TYPE

allure serve reports
```



