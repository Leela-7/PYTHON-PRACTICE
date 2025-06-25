def dict(**keyvalue):
  for k,v in keyvalue.items():
    print(f'{k} --> {v}')
  return keyvalue


total={"naresh": 100, "suresh": 200, "rajesh": 300}
print("The dictionary is", dict(**total))