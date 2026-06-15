def add_to_k(numbers, k):
    seen_numbers = set()
    for n in numbers:
        if k - n in seen_numbers:
            return True
        seen_numbers.add(n)
    return False

print(add_to_k([1,2,3,4], 3) == True)
print(add_to_k([1,2,3,4], 10) == False)  
print(add_to_k([1,3], 3) == False)  
print(add_to_k([1,1,3,4], 2) == True)  
print(add_to_k([1,1,1,4], 3) == False)  
print(add_to_k([10, 15, 3, 7], 17) == True)  
