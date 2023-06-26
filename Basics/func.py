def addNum(num1,num2):
    return (num1+num2)


result = addNum(2,3)
print(result)

def subNum(num1,num2):
    return num1-num2
result = subNum(1,5)
print(result)
 


# FILTER FUNC.

mylist= [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0
even=filter(even_bool,mylist)
print(list(even))



# LAMBDA EXP.

mylist= [1,2,3,4,5,6,7,8]

# ( lambda num:num%2==0 ) --> {This is Lambda Expression Which
# is used inside a function majorly ...however we can define it too
# by writing it outside any function }
     
even=filter(lambda num:num%2==0 ,mylist)
print(list(even))

# This how we can use filter Func. and lambda Exp.










