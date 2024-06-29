
n = 30000

def f(n, p):
    return (n**2 - n + p)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

for p in range(n):
    a=0
    for i in range(p):
        if is_prime(f(i, p)) == True:
            a+=1
        if a == (p):
            print(p) 
        




   