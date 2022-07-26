# cos-test-python

## Start Allure web server

* Open Terminal and navigate to the project root

  ```commandline
  bash start_allure_server.sh
  ```

* If the server is error, run the command

  ```commandline
  bash reset_allure_server.sh
  ```

## Run tests

* Run only one test case

  ```commandline: generate Allure report
  bash run.sh tests/search/test_search.py
  ```
  
  ```commandline
  pytest tests/search/test_search.py --alluredir=allure-results
  allure open allure-reports
  ```
cho # oxstreet
# oxstreet
