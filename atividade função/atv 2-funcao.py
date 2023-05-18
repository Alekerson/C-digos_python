while True:
  a = int(input("Informe um valor: "))
  b = int(input("Informe outro valor: "))
  if a != b:
    break

def somarImpares(a, b):
  soma = 0 
  while a < b:
    if a % 2 == 1:
      soma += a
    a += 1
  print(f"A soma de todos os números ímpares é {soma}")

def mediaMultiplos3(c, d):
  soma = 0 
  contador = 0
  while d < c: 
    if d % 3 == 0:
      soma += d
      contador += 1
    d += 1
  print(f"A média dos números ímpares é {soma/contador}")


if a < b:
  somarImpares(a ,b)
else:
  mediaMultiplos3(a, b)