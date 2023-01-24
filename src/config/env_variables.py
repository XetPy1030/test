import os

DATA_FOLDER = os.environ.get("data_folder")
if not DATA_FOLDER:
    PICTURES_FOLDER = "./pictures"
    MODE = 'local'
    DATABASE_PASSWORD = None
else:
    PICTURES_FOLDER = DATA_FOLDER + "pictures"
    DATABASE_PASSWORD = os.environ.get("database_passwd")
    MODE = os.environ.get("mode")
    print("MODE: ", MODE)
