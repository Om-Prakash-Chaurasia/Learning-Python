count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            if int(num) % 2 == 0:
                count += 1
            num = ""
        else:
            num += data[i]

    # Check the last number
    if num:
        if int(num) % 2 == 0:
            count += 1

print(count)
