import csv

# Path to the uploaded file
file_path = '/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv'

# Initialize variables to track the previous water level
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
        
        # Check if the water level is missing (no reading received)
        if water_level == '-':
            print(f"WARNING: No reading received at {date} {time}")
            continue
        
        # Convert the water level to a float
        try:
            water_level = float(water_level)
        except ValueError:
            print(f"WARNING: Invalid water level at {date} {time}")
            continue
        
        # Check if the water level exceeds 5.0 ft
        if water_level > 5.0:
            print(f"WARNING: Water level exceeds 5.0 ft at {date} {time} (Water level: {water_level} ft)")

        # If this is not the first reading, compare with the previous water level
        if previous_water_level is not None:
            # Calculate the rise in water level
            water_level_rise = water_level - previous_water_level
            
            # Check if the water level rises more than 0.25 ft since the previous reading
            if water_level_rise > 0.25:
                print(f"WARNING: Water level increased by more than 0.25 ft at {date} {time} (Rise: {water_level_rise} ft)")

        # Update the previous water level and date/time for the next iteration
        previous_water_level = water_level
        previous_date_time = f"{date} {time}"
