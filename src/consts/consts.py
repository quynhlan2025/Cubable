from pathlib import Path

PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
PROJECT_NAME = PROJECT_ROOT.split("/")[-1]
ENV_CONFIG_FILE = PROJECT_ROOT + "/config/%s.properties"
LOG_DIR = PROJECT_ROOT + "/logs/"
LOG_FILE = LOG_DIR + "%s.log"
SCREENSHOT_DIR = PROJECT_ROOT + "/screenshots/{}/"
SCREENSHOT_TC_DIR = PROJECT_ROOT + "/screenshots/{}/{}/"
SCREENSHOT_FILE = "{}.png"
DOWNLOAD_DIR = PROJECT_ROOT + "/data/download/"

