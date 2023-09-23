
with open('data.txt', 'r') as file:
    raw_data = file.readlines()

# Initialize an empty list to store the cleaned data
cleaned_data = []
collect_data = False

# Process each line of raw data
for line in raw_data:
    # Remove leading and trailing whitespace
    line = line.strip()

    # If a line starts with "Year," it's the header, so start collecting data
    if line.startswith("Year"):
        collect_data = True
        header = line  # Store the header for later use
        continue

    # If we're collecting data, append the line to cleaned_data
    if collect_data and line:
        values = line.split()
        # Check if the first box contains numeric data
        if values[0].isdigit():
            cleaned_data.append(values)
        else:
            collect_data = False  # Stop collecting data

# Define the CSV filename
csv_filename = "clean_data.csv"

# Open the CSV file for writing
with open(csv_filename, "w") as csv_file:
    # Write the header row with separate cells
    csv_file.write(header.replace("\t", ",").strip() + "\n")

    # Write the cleaned data rows with separate cells
    for row in cleaned_data:
        csv_file.write(",".join(row) + "\n")





def anomalies_to_fahr(celsius):
    if celsius % 1 == 1:
        fahr = (celsius / 100) * 1.8 + 32
        return fahr
        











