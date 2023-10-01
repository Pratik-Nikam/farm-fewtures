import base64

import matplotlib
import pandas as pd
import seaborn as sns

matplotlib.use('Agg')
from io import BytesIO

import matplotlib.pyplot as plt

from .load_netlogo import initialize_netlogo

def agriculture_calc():
    # Set the style and context for the plots
    sns.set_style("white")
    sns.set_context("talk")

    # Retrieve configuration values from the Flask app's context
    # jvm_path = current_app.config['JVM_PATH']
    # path = current_app.config["NETLOGO_FEW_CALC_PATH"]
    # net_logo_home = current_app.config["NET_LOGO_HOME"]

    # # Initialize the NetLogoLink object
    # netlogo = pynetlogo.NetLogoLink(
    #     gui=True,
    #     netlogo_home=net_logo_home,
    #     jvm_path=jvm_path,
    # )

    # # Define the path to the NetLogo model
    # nlogo_path = os.path.join(base_dir, "netlogo/FEWCalc_Export_Test.nlogo")

    # # Load the NetLogo model
    # netlogo.load_model(nlogo_path)
    netlogo, path = initialize_netlogo()

    # Set input values for the variables
    corn_area = 200  # Replace with your desired value
    wheat_area = 125  # Replace with your desired value
    soybeans_area = 0  # Replace with your desired value
    sg_area = 125  # Replace with your desired value

    # Set NetLogo variables
    netlogo.command(f"set corn_area {corn_area}")
    netlogo.command(f"set wheat_area {wheat_area}")
    netlogo.command(f"set soybeans_area {soybeans_area}")
    netlogo.command(f"set sg_area {sg_area}")

    # Setup and run the NetLogo model
    netlogo.command("setup")
    netlogo.command('repeat 60 [go]')
    netlogo.command("go")

    # Close the NetLogo workspace
    netlogo.kill_workspace()

    # Open the CSV file and read the data into a Pandas DataFrame
    crop_production_img = crop_production_calculation(path)

    net_calc_img= net_income_calculation(path)

    
    return crop_production_img, net_calc_img

def net_income_calculation(path):
    crop_production_data = pd.read_csv(f"{path}ag-net-income.csv", delimiter="\t", header=None)

    df = crop_production_data

    df = df.drop(df.index[0:16])


    df = df[0].str.split(',', expand=True)

    df.columns = df.iloc[0]
    df = df.iloc[1:]

    df.columns = ['year', "Corn", "color_0", "pen_down_0", 
                "year_1","Wheat", "color_1", "pen_down_1",
                "year_2","Soybean", "color_2", "pen_down_2",
                "year_3","SG", "color_3", "pen_down_3",
                "year_4", "US$0", "color_4", "pen_down_4"]

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    df['Corn'] = df['Corn'].str.replace('"', '')



    df['Corn'] = df['Corn'].str.replace('"', '').astype(float)

    df['Wheat'] = df['Wheat'].str.replace('"', '').astype(float)
    df['Soybean'] = df['Soybean'].str.replace('"', '').astype(float)
    df['SG'] = df['SG'].str.replace('"', '').astype(float)

    df['US$0'] = df['US$0'].str.replace('"', '').astype(float)



    plt.figure(figsize=(10, 6))

    plt.plot(df["year"], df["Corn"], label="Corn", color="blue")
    plt.plot(df["year"], df["Wheat"], label="Wheat", color="green")
    plt.plot(df["year"], df["Soybean"], label="Soybeans", color="red")
    plt.plot(df["year"], df["SG"], label="SG", color="orange")
    plt.plot(df["year"], df["US$0"], label="US$0", color="brown")

    plt.xlabel("Year")
    plt.ylabel("Bu/ac")
    plt.legend()
    plt.title("Ag Net Income")

    # Show only a few years on the x-axis
    years_to_show = df["year"].iloc[::5]  # Show every 5th year
    plt.xticks(years_to_show)

    plt.grid(True)
    # plt.show()
    # return plt

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image as base64
    encoded_img = base64.b64encode(img.read()).decode()
    return encoded_img

def crop_production_calculation(path):
    crop_production_data = pd.read_csv(f"{path}crop-production.csv", delimiter="\t", header=None)

    # Preprocess the DataFrame
    df = crop_production_data
    df = df.drop(df.index[0:15])
    df = df[0].str.split(',', expand=True)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.columns = ['year', "Corn", "color_0", "pen_down_0", 
                  "year_1","Wheat", "color_1", "pen_down_1",
                  "year_2","Soybean", "color_2", "pen_down_2",
                  "year_3","SG", "color_3", "pen_down_3"]

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    # Convert columns to integers
    df['Corn'] = df['Corn'].str.replace('"', '').astype(int)
    df['Wheat'] = df['Wheat'].str.replace('"', '').astype(int)
    df['Soybean'] = df['Soybean'].str.replace('"', '').astype(int)
    df['SG'] = df['SG'].str.replace('"', '').astype(int)

    # Plot the data using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df["year"], df["Corn"], label="Corn", color="blue")
    plt.plot(df["year"], df["Wheat"], label="Wheat", color="green")
    plt.plot(df["year"], df["Soybean"], label="Soybeans", color="red")
    plt.plot(df["year"], df["SG"], label="SG", color="orange")

    # Add labels and legend
    plt.xlabel("Year")
    plt.ylabel("Bu/ac")
    plt.legend()
    plt.title("Crop Production")

    # Show only a few years on the x-axis
    years_to_show = df["year"].iloc[::5]  # Show every 5th year
    plt.xticks(years_to_show)

    # Save the plot as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image as base64
    encoded_img = base64.b64encode(img.read()).decode()
    return encoded_img



