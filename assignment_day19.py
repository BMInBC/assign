# Step 1: Create and write readings to a new file
readings = ["120.5", "130.0", "128.4", "125.6", "132.9"]  # Example smart meter readings

# open(fn, 'w') - Create a file and write to it
fh = open("smart_meter.txt", 'w')
fh.writelines([r + "\n" for r in readings])  # fh.writelines(S)
fh.close()  # fh.close()

# Step 2: Read the file line-by-line
fh = open("smart_meter.txt", 'r')  # open(fn, 'r')
print("Reading lines using readline():")
print(fh.readline().strip())  # fh.readline()
print(fh.readline().strip())  # Read another line
fh.close()

# Step 3: Read the whole file content
fh = open("smart_meter.txt", 'r')
print("\nReading full content using read():")
print(fh.read())  # fh.read()
fh.close()

# Step 4: Read all lines into a list
fh = open("smart_meter.txt", 'r')
print("Reading all lines using readlines():")
lines = fh.readlines()  # fh.readlines()
print(lines)
fh.close()

# Step 5: Append a new reading
fh = open("smart_meter.txt", 'a')  # open(fn, 'a')
fh.write("135.2\n")  # fh.write(s)
fh.close()

# Step 6: Confirm appended content
fh = open("smart_meter.txt", 'r')
print("Final file content after appending:")
print(fh.read())
fh.close()
