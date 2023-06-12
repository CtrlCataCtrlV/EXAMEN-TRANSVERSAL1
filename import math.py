import math
import matplotlib.pyplot as plt

def calcular_circunferencia(radio):
    circunferencia = 2 * math.pi * radio
    return circunferencia

def graficar_circunferencia(radio):
    angulos = [math.radians(grado) for grado in range(0, 361)]
    x = [radio * math.cos(angulo) for angulo in angulos]
    y = [radio * math.sin(angulo) for angulo in angulos]

    plt.plot(x, y)
    plt.axis('equal')
    plt.title('Circunferencia de radio {} (C = {:.2f})'.format(radio, calcular_circunferencia(radio)))
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid(True)
    plt.show()

radio = float(input("Ingrese el radio de la circunferencia: "))

circunferencia = calcular_circunferencia(radio)

print("El cálculo de la circunferencia con radio {:.1f} es: {:.2f}".format(radio, circunferencia))

graficar_circunferencia(radio)

print("¡Cálculo de circunferencia completado!")

