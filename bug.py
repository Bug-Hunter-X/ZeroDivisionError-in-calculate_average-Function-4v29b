def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list) 
print(average) #Output:0

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(average) #Output:3.0