import os
import json
import datetime
from util.path_definition import ROOT_DIR

# CONFIG_PATH = os.path.join(ROOT_DIR, 'Config/Global.json')
CONFIG_PATH = os.path.join(ROOT_DIR, 'Config/Global_local.json')
# CONFIG_PATH = os.path.join(ROOT_DIR, 'Config/Global_usb.json')

with open(CONFIG_PATH, 'r', encoding = "utf-8") as in_file:
    GLOBAL_CONFIG = json.load(in_file)

DATA_PATH = os.path.join(ROOT_DIR, 'data')

CostRatio = 0.0008

