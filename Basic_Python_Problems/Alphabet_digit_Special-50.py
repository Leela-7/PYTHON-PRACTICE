ch=input("Single Character ")
if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
   print("Alphabet")
elif ch.isdigit():  #ch>=0 and ch<=9
   print("Digit")
else:
   print("Special Character")