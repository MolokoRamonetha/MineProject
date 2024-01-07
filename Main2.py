import re
import openpyxl
from Tracking import session,Tracking_info

file_path = 'Bus_055_Raw_Data.txt'  # Replace with the actual path to your text file
connection_list = []

# Open the file in read mode
with open(file_path, 'r') as file:
    for line in file:
        connection_list.append(line.strip())

# Define a regular expression pattern
pattern = r'\[\[(.*?)\]\](.*)'

# Filter out rows containing "Not connected to Wi-Fi"
filtered_strings = [string for string in connection_list if "Not connected to Wi-Fi" not in string]

# Create a set to store unique MAC addresses
unique_macs = set()



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
        if mac_address and mac_address not in unique_macs:
            unique_macs.add(mac_address)

            session.add(Tracking_info(
                DateColumn = date,
                TimeColumn = time,
                Connected_mac = mac_address,
                Signal = info_dict.get("Signal Strength"),
                Raspberry = info_dict.get("Raspberry Pi MAC")
            ))
            session.commit()
            print("Done")



