import os

DATA_FOLDER = os.environ.get("data_folder")
MODE = os.environ.get("mode", "local")
if MODE == "local":
    PICTURES_FOLDER = "./pictures"
    DATABASE_PASSWORD = None
else:
    PICTURES_FOLDER = DATA_FOLDER + "pictures"
    DATABASE_PASSWORD = os.environ.get("database_passwd")
    print("MODE: ", MODE)
