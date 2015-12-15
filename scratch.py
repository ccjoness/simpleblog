def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

lst = list(range(2, 78))

filterit = [num for num in lst if is_even(num) == False]
print(filterit)
