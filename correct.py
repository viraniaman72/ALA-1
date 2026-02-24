print("Countdown Simulator")

start = int(input("Enter start number: "))

total = 0
count = 0   

current = start   

while current >= 0:
    print("Count:", current)
    total = total + current
    count = count + 1

    if current % 5 == 0:
        print("Multiple of 5")

    current = current - 1

print("Total sum:", total)

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("Cannot calculate average")

print("Finished")