salary=int(input("Enter your salary: "))
hra = salary * 0.10          # HRA(10%)
da_tax = salary * 0.05    # DA (5%)
pf = salary * 0.03   # PF(3%)

taxable_salary = (salary+ hra + da_tax) - pf  # Taxable salary calculation
print(f"your HRA is {hra}, DA is {da_tax}, PF is {pf}")
print(f"Your taxable salary is {taxable_salary}")

if salary>500000 and salary<=1000000:
  tax=salary*0.1
  inhand_salary=taxable_salary-tax
  print(f"Your in-hand salary is {inhand_salary:.2f}")
elif salary>1000000 and salary<=2000000:
  tax=salary*0.2
  inhand_salary=taxable_salary-tax
  print(f"Your in-hand salary is {inhand_salary}")
elif salary>2000000:
  tax=salary*0.3
  inhand_salary=taxable_salary-tax
  print(f"Your in-hand salary is {inhand_salary}")
else:
  print(f"Your in-hand salary is {taxable_salary}")