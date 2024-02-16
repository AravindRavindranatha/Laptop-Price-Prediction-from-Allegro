import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")


graphic_card_type=st.selectbox("Graphic Card Type",df["graphic card type"].unique())
cpu_cores=st.selectbox("Cpu Cores",df["CPU cores"].unique())
ram_size=st.selectbox("Ram Size",df["RAM size"].unique())
ram_type=st.selectbox("Ram Type",df["RAM type"].unique())
cpu_clock_speed=st.selectbox("Cpu Clock Speed (Ghz)",df["CPU clock speed (GHz)"].unique())
cpu_model=st.selectbox("Cpu Model",df["CPU model"].unique())
drive_memory_size=st.selectbox("Drive Memory Size (Gb)",df["drive memory size (GB)"].unique())
warranty=st.selectbox("Warranty",df["warranty"].unique())
screen_size=st.selectbox("Screen Size",df["screen size"].unique())
resolution = st.selectbox('Screen Resolution',["1280x800","1366x768","1600x900","1920x1080","1920x1200","1920x1280","2160x1440","2560x1440","2560x1600","2880x1620","3200x1800","3840x2160"])
bluetooth=st.selectbox("Bluetooth",["No","Yes"])
wifi=st.selectbox("Wifi",["No","Yes"])
lan=st.selectbox("Lan",["No","Yes"])
windows=st.selectbox("Windows",["No","Yes"])
linux=st.selectbox("Linux",["No","Yes"])
other=st.selectbox("Other",["No","Yes"])
no_system=st.selectbox("No System",["No","Yes"])
hdd=st.selectbox("Hdd",["No","Yes"])
ssd=st.selectbox("Ssd",["No","Yes"])
emmc=st.selectbox("Emmc",["No","Yes"])
hybrid=st.selectbox("Hybrid",["No","Yes"])
keyboard=st.selectbox("Keyboard",["No","Yes"])
touchpad=st.selectbox("Touchpad",["No","Yes"])
numeric_keyboard=st.selectbox("Numeric Keyboard",["No","Yes"])
illuminated_keyboard=st.selectbox("Illuminated Keyboard",["No","Yes"])

if st.button('Predict Price'):
    # query
    ppi = None
    if bluetooth == 'Yes':
        bluetooth = 1
    else:
        bluetooth = 0

    if wifi == 'Yes':
        wifi = 1
    else:
        wifi = 0

    if lan == 'Yes':
        lan = 1
    else:
        lan = 0

    if windows == 'Yes':
        windows = 1
    else:
        windows = 0

    if linux == 'Yes':
        linux = 1
    else:
        linux = 0

    if other == 'Yes':
        other = 1
    else:
        other = 0

    if no_system == 'Yes':
        no_system = 1
    else:
        no_system = 0

    if hdd == 'Yes':
        hdd = 1
    else:
        hdd = 0
    
    if ssd == 'Yes':
        ssd = 1
    else:
        ssd = 0

    if emmc == 'Yes':
        emmc = 1
    else:
        emmc = 0

    if hybrid == 'Yes':
        hybrid = 1
    else:
        hybrid = 0

    if keyboard == 'Yes':
        keyboard = 1
    else:
        keyboard = 0

    if touchpad == 'Yes':
        touchpad = 1
    else:
        touchpad = 0

    if numeric_keyboard == 'Yes':
        numeric_keyboard = 1
    else:
        numeric_keyboard = 0

    if illuminated_keyboard == 'Yes':
        illuminated_keyboard = 1
    else:
        illuminated_keyboard = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

    query = np.array([graphic_card_type,cpu_cores,ram_size,ram_type,cpu_clock_speed,cpu_model,drive_memory_size,warranty,screen_size,ppi,bluetooth,wifi,lan,windows,linux,other,no_system,hdd,ssd,emmc,hybrid,keyboard,touchpad,numeric_keyboard,illuminated_keyboard])

    query = query.reshape(1,25)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))