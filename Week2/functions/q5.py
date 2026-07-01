def even_odd(num):
    if num % 2 == 0  :
        return "EVEN"
    else:
        return "ODD"

user=int(input("enter a number:"))


print(even_odd(user))

