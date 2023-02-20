import json

# Load the JSON data from the file
with open('index.json') as f:
    data = json.load(f)

# Show the table headers
headers = ["DN", "Description", "Speed", "MTU"]

# Print  out the table headers
print("{:<50} {:<20} {:<8} {}".format(headers[0], headers[1], headers[2], headers[3]))
print("=" * 80)

# Loop through the interface data and print each row
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<8} {}".format(dn, description, speed, mtu))