import os
import socket
from importlib.metadata import PackageNotFoundError, version

from dotenv import load_dotenv

load_dotenv()

try:
    VERSION = version("llamacpp-deploy")
except PackageNotFoundError:
    VERSION = "unknown"

MODELNAME = os.getenv("MODELNAME", "unknown")
HOSTNAME = socket.gethostname()
LLAMACPP_URL = os.getenv("LLAMACPP_URL", "http://localhost:8080/v1")
