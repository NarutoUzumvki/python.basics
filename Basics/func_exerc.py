def arr_Check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


nums=[0,1,2,4,1,2,3]


result=arr_Check(nums)
print(result)

st2=[1,2,3,6,40]
result=arr_Check(st2)
print(result)

st3=[2,5,4,1,2,3,6,50]
result=arr_Check(st3)
print(result)

st4=[1,5,3,4,2,6,8]
result=arr_Check(st4)
print(result)



# FOR EX :
# string_bits("Hello") -->'Hlo'
# string_bits("Hi") -->'H'


def string_Bits(myString):

    result = ""

    for i in range(len(myString)):
        if i % 2==0:
            result = result + myString[i]
    return result

myString="Hello"
ans=string_Bits(myString)
print(ans)

myString=" Hover on application names and click on favorite icon. "
ans=string_Bits(myString)
print(ans)

# We can also do it using Slicing by   " myString[::2] "


# ** Double Char **
# doubleChar('The') --> 'TThhee'
# doubleChar('AAbb') --> 'AAAAbbbb'
# doubleChar(' Hi-There') --> 'HHii--TThheerree'

def doubleChar(myStr):
    result=''
    for char in myStr:
        result=result + char*2
    return result

myStr='How-You-Doinn!'
ans=doubleChar(myStr)
print(ans)


