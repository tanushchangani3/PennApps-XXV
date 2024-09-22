import json

# File paths
file1 = 'formatted_output.json'
file2 = 'formatted_output_tanush.json'
output_file = 'combined_output.json'

# Read the first JSON file
with open(file1, 'r') as f:
    data1 = json.load(f)

# Read the second JSON file
with open(file2, 'r') as f:
    data2 = json.load(f)

# Combine the data
combined_data = data1 + data2

# Write the combined data to a new JSON file
with open(output_file, 'w') as f:
    json.dump(combined_data, f, indent=4)

print(f"Combined JSON data has been written to {output_file}")