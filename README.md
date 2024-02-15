# Callose-Experiment-Data-Consolidation

    Reading CSV Files:
        Three CSV files are specified: Mock_Plate_Layout.csv, Mock_Counts.csv, and Mock_Sample_Assignment.csv.
        CSV readers are created for each file (plate_csv_reader, counts_csv_list, sample_info_csv_list).

    Creating CSV Writer for Merged Data:
        A new CSV file named Callose_Data.csv is created for storing the merged data.
        A CSV writer (merged_csv_writer) is initialized to write data into the new file.

    Writing Column Labels to Merged File:
        Column labels for the fully merged table are written to the Callose_Data.csv file.

    Iterating Through Plate CSV Data:
        Iterate through each row in the plate CSV data.
        Extract the plate number when a new plate is encountered.

    Extracting Well Data:
        Extract letter (row identifier) and number values along with the corresponding plate number for each well.
        Store the well labels, number values, and plate numbers in separate lists.

    Transforming Plate Data:
        Create a list transformed_plate_data containing lists of well label, number, and plate for each well.

    Matching Plate Data with Counts Data:
        Iterate through each row in the transformed plate data and counts data.
        Check for matching plate and well values, then append new rows with matching identifiers to plate_and_counts list.

    Merging Data with Sample Information:
        Iterate through each row in the plate_and_counts list and sample information data.
        Check for matching sample numbers and write merged rows to the Callose_Data.csv file.
