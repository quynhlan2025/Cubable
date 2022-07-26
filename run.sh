#!/bin/bash

ALLURE_RESULT="_allure-results"
RUN_TIME=$(date +"%Y%m%d-%H%M%S")
REPORT_DIR="reports/${RUN_TIME}"

# Create a folder '_allure-results' if not exist
if [ ! -d ${ALLURE_RESULT} ]; then
  mkdir ${ALLURE_RESULT}
fi

# Execute tests
pytest $1 --alluredir=${ALLURE_RESULT}/${RUN_TIME}

# Generate allure report
allure generate "${ALLURE_RESULT}/${RUN_TIME}" -o ${REPORT_DIR}
allure open ${REPORT_DIR}