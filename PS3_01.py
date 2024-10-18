import csv

# Path to the uploaded file
file_path = '/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv'

# Initialize variables to track the highest water level and corresponding date/time
max_water_level = None
max_water_level_date_time = None

# Open the file and read it line by line
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Read the header row
    header = next(csv_reader)
    
    # Find the index for 'Date', 'Time (GMT)', and 'Preliminary (ft)'
    date_idx = header.index('Date')
    time_idx = header.index('Time (GMT)')
    water_level_idx = header.index('Preliminary (ft)')

    # Iterate over each row
    for row in csv_reader:
        date = row[date_idx]
        time = row[time_idx]
        water_level = row[water_level_idx]
        
        # Skip rows where the preliminary water level is missing or not valid ('-')
        if water_level == '-':
            continue
        
        # Convert the preliminary water level to a float
        try:
            water_level = float(water_level)
        except ValueError:
            continue
        
        # Update the maximum water level and corresponding date/time
        if max_water_level is None or water_level > max_water_level:
            max_water_level = water_level
            max_water_level_date_time = f"{date} {time}"

# Report the results
if max_water_level_date_time:
    print(f"Highest preliminary water level: {max_water_level} ft observed on {max_water_level_date_time}")
else:
    print("No valid preliminary water level data available.")
