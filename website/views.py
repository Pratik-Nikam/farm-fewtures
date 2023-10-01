import seaborn as sns
from flask import Blueprint, flash, jsonify, redirect, render_template, request

from website.services.agriculture import (agriculture_calc,
                                          net_income_calculation)


sns.set_style("white")
sns.set_context("talk")

import pynetlogo

# import the flask_login module
views = Blueprint('views', __name__)

# this is the home page
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

# Flag to check if route1 has been executed
setup_executed = False

@views.before_request
def check_setup_execution():
    global setup_executed
    if request.endpoint == 'run' and not setup_executed:
        flash('Run Setup first!', category='Error')
        return redirect('/')

# this is the setup button
@views.route('/setup', methods=['POST'])
def setup():
    # This is the code to run the NetLogo model  
    netlogo = pynetlogo.NetLogoLink(gui=True, jvm_path="/usr/libexec/java_home")
    netlogo.load_model(r"C:\Users\godia\OneDrive\Desktop\Siva\Professional\Software Engineer\Jobs\Inst of Policy and Pub Res KU\Website\FEWCalc\NetLogo\FEWtures\FEWCalc.nlogo")
    netlogo.command("setup")
    
    return jsonify({})

# # this is the run button
# @views.route('/run', methods=['POST'])
# def run(num_runs):
#     netlogo.command("repeat " + str(num_runs) + " [ go ]")
#     report = netlogo.report("report")
#     return report


@views.route("/agriculture")
def agriculture():
    crop_production, net_income = agriculture_calc()
    return render_template('index.html', crop_production=crop_production, net_income=net_income)


# @views.route("/ag-net-income")
# def agriculture_net():
#     plot = calculate_net_income()
#     return render_template('index.html', plot=f'data:image/png;base64,{plot}')