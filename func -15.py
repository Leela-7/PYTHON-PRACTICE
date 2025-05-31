def fun1(val):
    print(val*val)
    print("Hello")

fun1(1)
fun1(5)
fun1(7)
fun1(9)
print("Function 2")
def fun2(first,last):
    print("Hi, "+first+""+last)
    return first +" "+last

fun2("mahesh","rakesh")
fun2("dhanush","rajesh")
fun2("mukesh","manoj")
myname=fun2("Lawrence","Rakesh")
print(myname)

def fun3(val1, val2):
    total = val1 + val2
    print(f"The sum of {val1} and {val2} is {total}")
    return total

result = fun3(6, 7)
print(f"Result from fun3: {result}")
    