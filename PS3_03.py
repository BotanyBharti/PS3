import csv

# Path to the uploaded file
file_path = '/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv'

# Initialize variables to track the fastest rise in water level
max_rise = None
max_rise_date_time = None
previous_water_level = None
previous_date_time = None

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
        
        # Check if this is the first valid reading
        if previous_water_level is not None:
            # Calculate the rise in water level
            water_level_rise = water_level - previous_water_level
            
            # If this rise is the largest observed, update the max rise and time
            if max_rise is None or water_level_rise > max_rise:
                max_rise = water_level_rise
                max_rise_date_time = f"{date} {time}"

        # Update the previous water level and date/time for the next iteration
        previous_water_level = water_level
        previous_date_time = f"{date} {time}"

# Report the results
if max_rise_date_time:
    print(f"Fastest rise in water level: {max_rise} ft in 6 minutes observed on {max_rise_date_time}")
else:
    print("No valid water level data available to calculate the rise.")
