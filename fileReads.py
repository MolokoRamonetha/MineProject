import pandas as pd
from TrackingDto import TrackingInfoDTO
import re
df = pd.read_excel("info.xlsx")



def matchAPAndBus(connected_mac,date,time,signal,Raspberry,df=df):
    
    for index, row in df.iterrows():
        if mac_split(row["Unnamed: 2"]) == connected_mac:
             return TrackingInfoDTO(date,time,connected_mac,signal,Raspberry,row["Unnamed: 3"],row["Unnamed: 8"])


def mac_split(input_string):
    mac_address_pattern = re.compile(r'MAC: (\S+)')

    # Search for the MAC address in the input string
    match = mac_address_pattern.search(input_string)

    # Check if a match is found
    if match:
        mac_address = match.group(1)
        print(f"Extracted MAC address: {mac_address}")
        return mac_address
    else:
        print("No MAC address found in the input string.")
        return None

for index, row in df.head(5).iterrows():
        print(row)
    