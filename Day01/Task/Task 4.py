
temps = []

for day in range(1, 6):
    temp = float(input(f"Enter temperature for Day {day}: "))
    temps.append(temp)

average = sum(temps) / len(temps)

print(f"\nAverage Temperature over 5 days: {average:.2f}°C")
