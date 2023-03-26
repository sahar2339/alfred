import os
from typing import get_type_hints, Union
from dotenv import load_dotenv
import logging
import inspect
import json

load_dotenv()


class AppConfig:
    pass


Config = AppConfig(os.environ)