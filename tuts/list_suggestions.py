numbers = list(range(100))

# squared = []

# for number in numbers:
#     if number % 5 == 0:
#         squared.append(number)

squared = [number ** 2 for number in numbers if number % 5 == 0]


filtered_by_five = [number for number in numbers if number % 5 == 0]
# or
filter_by_fifteen = list(filter(lambda x: x % 5 == 0 and x % 3 == 0, numbers))

filter_by_fifteen_doubles = list(map(lambda x: x*2, filter_by_fifteen))


print(filter_by_fifteen_doubles)