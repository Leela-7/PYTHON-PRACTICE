def count_special(*,string):
  c=0
  for ch in string:
    if not ch.isalnum():
      c+=1
  print(f"Number of special characters in '{string}' is {c}")
count_special(string="Hello, World! @2023")