import csv

# Specify the CSV file paths
plate_file_path = 'Mock_Plate_Layout.csv'
counts_file_path = 'Mock_Counts.csv'
sample_info_file_path = 'Mock_Sample_Assignment.csv'

# Create lists to store result columns
well_labels = []
number_values = []
plate_numbers = []
transformed_plate_data = []
plate_and_counts = []

# Read CSV data and create CSV writers
with open(plate_file_path, 'r') as plate_file, \
        open(counts_file_path, 'r') as counts_file, \
        open(sample_info_file_path, 'r') as sample_info_file, \
        open('Callose_Data.csv', 'w', newline='') as merged_file:

    # Create CSV readers
    plate_csv_reader = csv.reader(plate_file)
    counts_csv_list = list(csv.reader(counts_file))
    sample_info_csv_list = list(csv.reader(sample_info_file))

    # Create CSV writer
    merged_csv_writer = csv.writer(merged_file)

    # Set column labels for fully merged table
    merged_csv_writer.writerow([
        "Experiment", "Plate", "Well", "Plant_No", "Leaflet_No", "Sample_No",
        "Plasmid", "Callose_Count", "Unadjusted_Callose_Area",
        "Unadjusted_Callose_Avg_Size", "Unadjusted_Total_Area"
    ])

    # Initialize plate_number variable
    plate_number = None

    # Iterate through each row in the plate CSV data
    for row in plate_csv_reader:
        # Check if the row indicates a new plate
        if row[0].startswith("Plate"):
            # Extract the plate number from the row
            plate_number = row[0].split()[1]

        # Skip rows that do not contain well data
        if not any(row[1:]):
            continue

        # Extract the letter (row identifier)
        letter = row[0]

        # Extract the number values and corresponding plate number for each well
        for col_index, value in enumerate(row[1:], start=1):
            well_label = f"{letter}{col_index}"

            # Check if the well label includes the specified characters
            if any(char in "ABCDEFGH" for char in well_label):
                well_labels.append(well_label)
                number_values.append(value)
                plate_numbers.append(plate_number)

    # Append all plate data
    transformed_plate_data = [
        [well, number, plate] for well, number, plate in zip(well_labels, number_values, plate_numbers)
    ]

    # Iterate through each row in the transformed plate data
    for well_data in transformed_plate_data:
        # Iterate through each row in the counts data
        for row in counts_csv_list:
            well_id = well_data[0] + "_"
            # Check for matching plate and well values 
            if well_data[2] == row[1] and well_id in row[2]:
                # Append new rows with matching identifiers to plate_and_counts
                plate_and_counts.append(row[0:2] + well_data[0:2] + row[3:])

    # Iterate through each row in plates and counts
    for entry in plate_and_counts:
        # Iterate through each row in sample data
        for sample in sample_info_csv_list:
            # Check for matching sample numbers
            if entry[3] == sample[0]:
                merged_csv_writer.writerow(
                    entry[0:3] + sample[1:3] + [sample[0]] + [sample[3]] + entry[4:]
                )
