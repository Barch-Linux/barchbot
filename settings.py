#!/usr/bin/env python3
"""
settings.py

Load settings for BarchBot
"""

import logging
from dotenv import load_dotenv
import os


logger = logging.getLogger(__name__)

logger.info("==> Load .env")
load_dotenv(verbose=True)

logger.debug("Get TOKEN")
TOKEN = os.getenv("TOKEN")
