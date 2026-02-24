print("Countdown Simulator")

start = int(input("Enter start number: "))

total = 0

while start >= 0:
    print("Count:", start)
    total = total + start

    if start % 5 == 0:
        print("Multiple of 5")

    start = start - 1

print("Total sum:", total)

average = total / start   # ❌ ERROR: start becomes -1 after loop

print("Average:", average   # ❌ ERROR: Missing closing bracket )

if total < 0:              # ❌ Logical error (never negative)
    print("Unexpected negative total")