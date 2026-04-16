import os
from pathlib import Path
import configparser

APP = Path(os.path.dirname(__file__)).parent
CORE = APP / "core"

DATABASE = APP / "data/app.db"

config = configparser.ConfigParser()

config["Database"] = {
    "path": str(DATABASE)
}
