import re
import openpyxl


file_path = 'log151.txt'  # Replace with the actual path to your text file
connection_list = []
# Open the file in read mode
with open(file_path, 'r') as file:
    for line in file:
        # print(line.strip())  # .strip() removes the newline character at the end of each line
        connection_list.append(line.strip())

# Define a regular expression pattern
pattern = r'\[\[(.*?)\]\]'

# Filter out rows containing "Not connected to Wi-Fi"
filtered_strings = [string for string in connection_list if "Not connected to Wi-Fi" not in string]
headers=['Date','Time','Wi-fi AP with Mac','Signal','PI Mac']
excel_file = "Problem.xlsx"
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active
sheet.append(headers)
pattern = r'\[\[(.*?)\]\](.*)'

for filtered_string in filtered_strings:
# Use re.match to extract datetime and text
    match = re.match(pattern, filtered_string)

    if match:
        datetime_part = match.group(1)  # Extract datetime part
        text_part = match.group(2)  # Extract text part
        
        # Split the datetime part into date and time
        date, time = datetime_part.split(' ')

        # Split the text part by commas
        text_parts_list = [part.strip() for part in text_part.split(',')]

        # Create a dictionary from text_parts_list
        info_dict = {}
        for part in text_parts_list:
            key, value = map(str.strip, part.split(':', 1))
            info_dict[key] = value
        
       
        
        # Append data to the next available row
        next_row = sheet.max_row + 1
        sheet.cell(row=next_row, column=1, value=date)
        sheet.cell(row=next_row, column=2, value=time)
        for idx, (key, value) in enumerate(info_dict.items(), start=3):
            sheet.cell(row=next_row, column=idx, value=value)
        
        workbook.save(excel_file)
        workbook.close()
    else:
        print("No match found.")






