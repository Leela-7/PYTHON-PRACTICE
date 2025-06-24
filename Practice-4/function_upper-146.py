
def uppercase():
  string=input("Enter a string: ")
  output=""
  for ch in string:
    if ch>='a' and ch<='z':
      output=output+chr(ord(ch)-32)
    else:
      output=output+ch
  return output

output=uppercase()
print("Uppercase string:", output)