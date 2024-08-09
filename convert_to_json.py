import json

# Reading in the simulated VSAM data file 
with open('vsam_simulated.txt', 'r') as file:
    vsam_records = file.readlines()[1:]  # Skip the header line

json_records = []

# Convert each record to a JSON object
# Then converting each record to a JSON object (could change depending on how many different categories exist)
for record in vsam_records:
    record_fields = record.strip().split('|')
    json_record = {
        "id": record_fields[0],
        "name": record_fields[1],
        "salary": record_fields[2],
        "department": record_fields[3],
        "date_of_joining": record_fields[4],
        "city": record_fields[5],
        "email": record_fields[6]
    }
    json_records.append(json_record)

# Now writing all of the JSON objects to a new file which should be created after executing scripts
with open('vsam_data.json', 'w') as json_file:
    json.dump(json_records, json_file, indent=4)

print("VSAM data successfully converted to JSON.")
