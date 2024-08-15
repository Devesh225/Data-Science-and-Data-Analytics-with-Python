ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

ages.append(min_age)
ages.append(max_age)
print(f"Updated ages: {ages}")

n = len(ages)
if n % 2 == 1:
    median_age = ages[n // 2]
else:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
print(f"Median age: {median_age}")

average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

age_range = max_age - min_age
print(f"Range of ages: {age_range}")

min_minus_avg = abs(min_age - average_age)
max_minus_avg = abs(max_age - average_age)
print(f"Absolute value of (min - average): {min_minus_avg}")
print(f"Absolute value of (max - average): {max_minus_avg}")
