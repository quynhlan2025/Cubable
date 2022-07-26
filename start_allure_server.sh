#!/bin/bash

# Create a folder 'reports' if not exist
if [ ! -d "reports" ]; then
  mkdir "reports"
fi

# Check if the port 3000 is in use or not, if not then start Allure web server
if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null; then
  echo "Allure web server is running"
else
  python3 -m http.server --cgi 3000 & disown
  echo "Started Allure web server"
fi

# Open the default browser with localhost
open http://localhost:3000/reports/
