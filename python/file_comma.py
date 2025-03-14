with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            num = ""
        else:
            num += data[i]



count = 0
with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt", "r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")

    for val in nums:
        try:
            if int(val) % 2 == 0:
                count += 1
        except ValueError:
            # Handle the case where val is not an integer
            print(f"Skipping non-integer value: {val}")

    print(count)  # Print the count after the loop finishes
