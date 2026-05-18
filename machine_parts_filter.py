# Python program to filter machine parts
# using "in" and "not in" operators

# List of machine parts
parts = [
    ["Bolt", 50, 10],
    ["Nut", 20, 5],
    ["Gear", 150, 25],
    ["Bearing", 80, 15],
    ["Shaft", 200, 30]
]

print("Machine Parts:")
for part in parts:
    print(part)

# Selecting parts with cost below 100
selected_parts = []

for part in parts:
    if part not in selected_parts and part[1] < 100:
        selected_parts.append(part)

print("\nParts with cost below 100:")
for part in selected_parts:
    print(part)

# Removing parts with dimensions greater than 20
filtered_parts = []

for part in parts:
    if part not in filtered_parts and part[2] <= 20:
        filtered_parts.append(part)

print("\nParts with dimensions within range (<=20):")
for part in filtered_parts:
    print(part)
