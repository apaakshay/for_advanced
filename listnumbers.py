list=[1,2,3,4,5,6,7,8,9,10]
def sum(list):
    sum=0
    for i in list:
     sum=sum+i
    return sum

def mul(list):
 product=1
 for i in list:
     product=product*i
 return product

def square(list):
    square=[]
    for i in list:
        square.append(i*i)
    return square
print(sum(list))
print(mul(list))
print(square(list))



