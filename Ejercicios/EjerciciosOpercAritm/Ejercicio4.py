'''
Hacer un programa que ingresando el radio de una circunferencia, muestre por consola
su área y perímetro.
área = π * r²
perímetro = 2 * π * r
'''
import math

radio = float(input("Digite el radio-> "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El area de la circunferencia es: {area}") #salen todos los decimales
print(f"El perímetro de la circunferencia es: {perimetro}")

print(f"El area de la circunferencia es: {area:.2f}")
print(f"El perímetro de la circunferencia es: {perimetro:.3f}")
'''
con : después de la variable entre corchetes {} con un .2f indicamos que solo queremos ver en consola
2 decimales. Si ponemos .3f indicamos que solo queremos ver 3 decimales.
'''




