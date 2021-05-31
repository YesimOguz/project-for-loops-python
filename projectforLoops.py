#a program that prints out the first number in the list that is greater than 10
num = [4,5,9,19,2,7,8]

for number in num:
    if number > 10:
        print(number)
        break
     

#theese are two programs that print out whether or not you have found a number greater than 10
num =[4,5,9,19,2,7,8,11]

for number in num:
    if number>10:
        print(number)
    else:
        continue



lst = [1,2,5,6,7]

for number in lst:
    if number>10:
        print(number)
    else:
        continue


#this is how can we make a list with new result with 19 and 11

num =[4,5,9,19,2,7,8,11]
lst=[]
for number in num:
    if number>10:
        #print(number)
        lst.append(number)
    else:
        continue

print(lst)
        



  


   
        
        