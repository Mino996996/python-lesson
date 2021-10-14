p = [True]*100
p[0] = False
p[1] = False
n=2

def hyou():
  s= ""
  for i in range(100):
    if p[i] == True:
      s += "{:2d}, ".format(i)
    else:
      s +="/, "
    if i%10 == 9:
      s +="\n"
  print(s)

def furui():
  global n
  for i in range(2*n, 100, n):
    p[i] = False
  print(n, "の倍数を篩い落としました")
  hyou()
  while n<100:
    n += 1
    if p[n] == True:
      break

hyou()
while n<10:
  input("enter を押してください")
  furui()