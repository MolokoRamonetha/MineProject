import pandas as pd
from TrackingDto import TrackingInfoDTO
import re
d_ap = pd.read_csv("ap.csv")
d_bus = pd.read_csv("bus.csv")

# def matchAPAndBus(connected_mac,date,time,signal,Raspberry,df=df):
    
#     for index, row in df.iterrows():
#         if mac_split(row["Unnamed: 2"]) == connected_mac:
#              return TrackingInfoDTO(date,time,connected_mac,signal,Raspberry,row["Unnamed: 3"],row["Unnamed: 8"])
#         else:
#              return TrackingInfoDTO(date,time,connected_mac,signal,Raspberry,"No Ap Name","No Bus Name")
def matchAPAndBus(connected_mac,date,time,signal,Raspberry,df=d_ap,d_bus=d_bus):
    for index, row in df.iterrows():
        if row['mac_address'][:14] == connected_mac[:14]: 
            ap_name = row['apName']
            ap_location = row['location']
            break
        else:
            ap_name = "Null"
            ap_location ="Null"
    for index_bus, row_bus in d_bus.iterrows():
        if row_bus["mac_address"] == Raspberry: 
            bus_name = row_bus["bus_name"]
            break
        else : bus_name = "Null"
    return TrackingInfoDTO(date,time,connected_mac,signal,Raspberry,ap_name,bus_name,ap_location)
            # Access the values in each row
            

# Unit Testing
# matchAPAndBus("70:0F:6A:0F:9B:04","2024-01-12","18:56:21",'-78 dBm', 'b8:27:eb:9b:3b:db')