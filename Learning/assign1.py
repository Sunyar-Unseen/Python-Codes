#Comparing 2 list

l1 = [1,2,3,4,5,6]
l2 = [6,5,4,3,2,1]

for i in l1:
    for j in l2:
        if i > j:
            print(i)
        else:
            print(j)


z = (10,20,30,40,50)

#Adding 10 to the value

def add_10(abc):
    return 10 + abc


print(add_10(60))

# Checkeing odd Even for given number
def check_odd_even(x):
    if x%2:
        print("Odd")
    else:
        print("Even")

check_odd_even(55)
