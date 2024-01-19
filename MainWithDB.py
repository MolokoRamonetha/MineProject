import re
import openpyxl
from Tracking import session,Tracking_info
from TrackingDto import TrackingInfoDTO
from fileReads import *
import os
import glob
from sqlalchemy import create_engine, select
import schedule
directory_path = 'logs/*.txt'
def schedule_job():
    # Use glob to get a list of all files with .txt extension in the specified directory
    txt_files = glob.glob(directory_path)

    connection_list = []
    # Iterate through each text file and read its content
    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            for line in file:
                connection_list.append(line.strip())


    txt_files = glob.glob(directory_path)

    # Iterate through each text file and delete it
    for txt_file in txt_files:
        try:
            os.remove(txt_file)
            print(f"File {txt_file} deleted successfully.")
        except OSError as e:
            print(f"Error deleting file {txt_file}: {e}")
    # Define a regular expression pattern
    pattern = r'\[\[(.*?)\]\](.*)'

    # Filter out rows containing "Not connected to Wi-Fi"
    filtered_strings = [string for string in connection_list if "Not connected to Wi-Fi" not in string]

    # Create a set to store unique MAC addresses
    unique_macs = set()

    def compare(info,result):
        for val in result:
            if ((val.DateColumn==info.DateColumn) and val.TimeColumn == info.TimeColumn and val.Connected_mac==info.Connected_mac and val.Signal == info.Signal and val.Raspberry==info.Raspberry and val.APName == info.APName and val.BussName == info.BussName ):
                return True
            else:
                return False
    stmt = select(Tracking_info.DateColumn,Tracking_info.TimeColumn,Tracking_info.Connected_mac,Tracking_info.Signal,Tracking_info.Raspberry,Tracking_info.APName,Tracking_info.BussName,Tracking_info.APlocation)
    result = session.execute(stmt)

    # Loop through filtered strings
    for filtered_string in filtered_strings:
        match = re.match(pattern, filtered_string)

        if match:
            datetime_part = match.group(1)
            text_part = match.group(2)

            date, time = datetime_part.split(' ')

            text_parts_list = [part.strip() for part in text_part.split(',')]
            info_dict = {}

            for part in text_parts_list:
                key, value = map(str.strip, part.split(':', 1))
                info_dict[key] = value

            # Get the MAC address
            mac_address = info_dict.get('Connected to Wi-Fi AP with MAC')

            # Check if this MAC address is unique
            
            unique_macs.add(mac_address)

            # TrackingInfoDTO(date,time,mac_address,info_dict.get("Signal Strength"),info_dict.get("Raspberry Pi MAC"))

            info = matchAPAndBus(mac_address,date,time,info_dict.get("Signal Strength"),info_dict.get("Raspberry Pi MAC"))
            
            if compare(info,result):

                session.add(Tracking_info(
                    DateColumn=info.DateColumn,
                    TimeColumn=info.TimeColumn,
                    Connected_mac=info.Connected_mac,
                    Signal=info.Signal,
                    Raspberry=info.Raspberry,
                    APName = info.APName,
                    BussName = info.BussName,
                    APlocation = info.APlocation
                ))
            else:
                print("Duplicates")
            session.commit()
            print("Done")

                # Delete the processed entry from the text file
            connection_list.remove(filtered_string)

    # Write the updated content back to the file

import time
schedule.every(0.1).minutes.do(schedule_job)

while True:
    schedule.run_pending()
    time.sleep(1)
