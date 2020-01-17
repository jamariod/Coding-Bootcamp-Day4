#Sum the Numbers
my_numbers = [1,3,4,6,7]
print(sum(my_numbers))

#Largest Number
my_numbers = [4,1,5,8,3,9,6,7]
my_numbers.sort()
print(my_numbers[-1])

#Smallest Number
my_numbers = [4,1,5,8,3,9,6,7] 
my_numbers.sort()
print(my_numbers[0])

#Even Numbers
my_numbers = [4,1,5,8,3,9,6,7]

for x in my_numbers:  
    if x % 2 == 0:
        print(x)

#Positive Number
my_numbers = [-1,-5,-9,4,1,5,8,3,9,6,7]
for x in my_numbers:
    if x >= 0:
        print(x)

#Positve Numbers II
my_numbers = [-1,-5,-9,4,1,5,8,3,9,6,7]
positive_numbers = []
for x in my_numbers:
    if x >= 0:
        my_numbers.append(x)
        print(my_numbers)
       
        
        




    



    
    
