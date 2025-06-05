age=int(input("Enter your age: "))
passed_test=input("Have you passed the driving test? (yes/no): ").lower()

if age >= 18:
  if passed_test == "yes":
    print("Congratulations! You can get a license.")
  else:
    print("You need to pass the test to get a license.")
else:
  print("You must be at least 18 years old to get a license.")