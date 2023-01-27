import os

DATA_FOLDER = os.environ.get("data_folder", "./data/")
MODE = os.environ.get("mode", "local")
if DATA_FOLDER != "./data/":
    PICTURES_FOLDER = DATA_FOLDER + "pictures"
else:
    PICTURES_FOLDER = "./pictures"
DATABASE_PASSWORD = os.environ.get("database_passwd")
