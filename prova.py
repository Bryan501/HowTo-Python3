
guardar = []

cont = 5
while cont > 0:  
  num1 = int(input())
  num2 = int(input())

  res = num1 + num2
  print("resultado:",res)
  print("-------")
  cont -= 1
  guardar.append(res)

for i in guardar[2: ]:
    print(i)
