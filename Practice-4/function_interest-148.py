def interest():
  principal = int(input("Enter the principal amount: "))
  rate = float(input("Enter the rate of interest: "))
  time = int(input("Enter the time in years: "))
  interest = (principal * rate * time) / 100
  return interest

print("Simple Interest:" ,interest())