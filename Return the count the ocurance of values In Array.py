# Given Array a=[a,b,c,t,a,c,d,b] return the count the ocurance of values In Array:
def Fun(a):
  result = {}
  for i in a:
    if i not in result:
      result[i] = a.append(i)
  for key, value in result.items():
    print(f"{key}, {value}")

b = int(input(":"))
a = []
for i in range(b):
  c = input(":")
  a.append(c)

Fun(a)
  
  
