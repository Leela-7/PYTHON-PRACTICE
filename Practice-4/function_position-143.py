# by using / slash we can use only positional ,we can not use keyword

def count_vowels(string,/):
  c=0
  for ch in string:
    if ch in "aeiouAEIOU":
      c+=1
  print(f"Number of vowels in '{string}' is {c}")
count_vowels("Hello World")
count_vowels("Python Programming")