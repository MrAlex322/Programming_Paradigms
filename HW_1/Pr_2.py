# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_desclarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_desclarative(numbers)
print(sorted_numbers) 
