# Logger Object
#
# Alice Seaborn (Austin Dial)
# FEB. 18 2021
#
# This object stores the configuration details for the
#    program's log functions. The format and level of
#    all logs is stored within this file and is simply
#    imported by client programs.
#

import logging as log
from pathlib import Path

# Establish path to logfile

logfile = Path(__file__).parent.parent / "logs/primary_events.log"

# create logger with 'spam_application'
logger = log.getLogger()
logger.setLevel(log.INFO)

# Suppress root logger
logger.propagate = False

# Create file handler which logs info messages
fh = log.FileHandler(logfile)
fh.setLevel(log.INFO)

# Create formatter and add it to the handler
formatter = log.Formatter("%(asctime)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
fh.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(fh)
