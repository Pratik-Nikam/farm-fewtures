import os

import pynetlogo
from flask import current_app

from config import base_dir


def initialize_netlogo():
    # Retrieve configuration values from the Flask app's context
    jvm_path = current_app.config['JVM_PATH']
    path = current_app.config["NETLOGO_FEW_CALC_PATH"]
    net_logo_home = current_app.config["NET_LOGO_HOME"]

    # Initialize the NetLogoLink object
    netlogo = pynetlogo.NetLogoLink(
        gui=True,
        netlogo_home=net_logo_home,
        jvm_path=jvm_path,
    )

    # Define the path to the NetLogo model
    nlogo_path = os.path.join(base_dir, "netlogo/FEWCalc_Export_Test.nlogo")

    # Load the NetLogo model
    netlogo.load_model(nlogo_path)

    return netlogo, path