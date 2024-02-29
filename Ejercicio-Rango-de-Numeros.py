#Elaborar un programa en python que permita capturar una cantidad N de números y permita determinar cuántos de estos números se encuentran en el rango de 10 a 20

N = int(input("Ingrese la cantidad de números->"))

count_in_range = 0

for i in range(N):
    num = float(input("Ingrese un número:")) 
    if 10 <= num <= 20:
        count_in_range += 1

print("La cantidad de numeros en el rango de 10 a 20 es:", count_in_range)