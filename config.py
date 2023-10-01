import os

class Config(object):
    DEBUG = False
    TESTING = False
    JVM_PATH="/Library/Java/JavaVirtualMachines/jdk-19.jdk/Contents/MacOS/libjli.dylib"
    NETLOGO_FEW_CALC_PATH = "/Users/pratiknikam/Documents/FEWCalc/FEWCalc-master/"
    NET_LOGO_HOME = r"/Applications/NetLogo 6.3.0"
    DATABASE_URI = "sqlite:///my_database.db"
    SECRET_KEY = "my_secret_key"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    DEBUG = True

base_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(base_dir, 'static')
template_folder = os.path.join(base_dir, 'templates')