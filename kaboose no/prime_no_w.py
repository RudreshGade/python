import math

n = 100000000

A = []

# define func. to check if a no. is prime
def is_prime(number):
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# append all prime to list 
with open('prime', 'w') as fp:
    for i in range(2,n):
        if is_prime(i) == True:
            A.append(i)
            fp.write(str(i)+ '\n')
        print('Done writing list into a binary file',i)



# # write list to binary file
# def write_list(a_list):
#     # store list in binary file so 'wb' mode
#     with open('prime', 'w') as fp:
#         for i in A:
#             fp.write(str(i)+ '\n')
#         print('Done writing list into a binary file')





   




   