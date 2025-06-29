#Syntax5: from module-name import identifier-name as alias-name



from module1 import fun1 as f1, fun2 as f2

f1()
f2()
#fun3()# fun3() is not imported, so it will raise an error if called