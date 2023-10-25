#!/usr/bin/env python3
import csv
import sys

# Define a function to process the CSV file
def process_csv(input_file):
    # Create a dictionary to hold file writers for each unique UF
    uf_files = {}

    # Open the input CSV file
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            cnpj, razao_social, uf = row

            # Construct the output filename based on UF
            output_filename = f"empresas_{uf.lower()}.csv"

            # Open the output file for writing
            if output_filename not in uf_files:
                uf_files[output_filename] = open(output_filename, 'w', newline='')

            # Write the CNPJ and Razão Social to the output file
            writer = csv.writer(uf_files[output_filename])
            writer.writerow([cnpj, razao_social])

    # Close all output files
    for file in uf_files.values():
        file.close()

# Call the function to process the CSV file
process_csv(sys.argv[1])
