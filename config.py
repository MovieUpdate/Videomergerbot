import os


class Config(object):
    API_HASH = os.environ.get("7f23ff440eb6b551998c6c02f769071c")
    BOT_TOKEN = os.environ.get("6109861562:AAH6hHOvUtRTcISTcuKAERPnL71dGwsizqM")
    TELEGRAM_API = os.environ["26283171"]
    OWNER = os.environ.get("1229483828")
    OWNER_USERNAME = os.environ.get("RequesterMUBot")
    PASSWORD = os.environ.get("hey.iamkapil")
    DATABASE_URL = os.environ.get("mongodb+srv://MovieUpdate:movieupdate8270@cluster0.itptmrb.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001912598096")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
