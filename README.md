# Overview
This is a Demo test framework for Automation QA course. 

# How to use this project:

## Lesson 1. Test automation framework 

Example of pytest + allure based automation test framework. Follow link for details [lesson1](https://github.com/auto-qa-course/python-framework-example/tree/lesson1). 

## Lesson 2. Service test coverage

Same framework extended with REST API test cases for [saas-template](https://github.com/swe-course/saas-template) project. Follow link for details [lesson2](https://github.com/auto-qa-course/python-framework-example/tree/lesson2). 

[Compare](https://github.com/auto-qa-course/python-framework-example/compare/lesson1...lesson2) lesson1 and lesson2. 

## lesson 3. Continuous testing

Same framework extended with Dockerfile and Jenkinsfile examples. Follow link for details [lesson3](https://github.com/auto-qa-course/python-framework-example/tree/lesson3). 

[Compare](https://github.com/auto-qa-course/python-framework-example/compare/lesson2...lesson3) lesson2 and lesson3. 

# Generic project description

## Requirements

* `pytest`
* `allure-pytest`
* `requests`

Also one need to install Alure CLI to be able generate allure reports, see https://docs.qameta.io/allure/latest/#_reporting. 

## Test configuration

One can configure test execution against specific environment using environment variables:
 
| Name                  | Required  | Default                  | Example                                               |
| --------------------  | --------- | ------------------------ |------------------------------------------------------ |
|  ENVIRONMENT          | yes       | none                     | QA, Stage   |  
|  TEST_TYPE            | yes       | none                     | ui, api     |
|  RESULTS_FOLDER       | no        | reports                  | reports     |


## API Test execution from CLI

```
ENVIRONMENT=QA
TEST_TYPE=api
RESULTS_FOLDER=reports

pytest test/api --alluredir $RESULTS_FOLDER/$TEST_TYPE

allure serve reports
```
`
## API Test execution within Docker container 

```
docker build -t automation_demo . 
mkdir out_docker_results

# Fix Linux
docker run -v $(pwd)/out_docker_results:/out:rw -e "ENVIRONMENT=QA" -e "TEST_TYPE=api" -it automation_demo pytest test/$TEST_TYPE --alluredir /out/$TEST_TYPE

# For Windows 
docker run -v /c/users/out_docker_results:/out:rw -e "ENVIRONMENT=QA" -e "TEST_TYPE=api" -it automation_demo pytest test/$TEST_TYPE --alluredir /out/$TEST_TYPE

allure serve out_docker_results
```
