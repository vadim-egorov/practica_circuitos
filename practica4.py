import numpy as np
import matplotlib.pyplot as plt

# TAREA 1
inductancia = 330E-6  # sustituir por el valor experimental de la inductancia
capasitancia = 82E-6  # sustituir por el valor experimental de la capasitancia
resistencia_g = 50

omega_resonancia = np.sqrt(1/inductancia/capasitancia)
f_resonancia = omega_resonancia / 2 / np.pi

print(f"|{"w_0, Hz":^10}|{"f_0, Hz":^10}|")
print('—'*25)
print(f"|{omega_resonancia:^10.1f}|{f_resonancia:^10.1f}|")
print('—'*25)

v_g = 5  # sustituir por el valor de la amplitude medido en los terminales del generador
# que no esta conectado al circuito

# TABLA 4.2
frecuencias = np.logspace(-2, 2, 12) * f_resonancia


def z_L(f): return 2 * np.pi * f * inductancia
def z_C(f): return - 1 / (2 * np.pi * f * capasitancia)


def v_s_teorico(f): return np.abs(v_g * (z_L(f) + z_C(f)) /
                                  np.sqrt(resistencia_g ** 2 + (z_L(f) + z_C(f)) ** 2))


def v_c_teorico(f): return np.abs(v_g * np.abs(z_C(f)) /
                                  np.sqrt(resistencia_g ** 2 + (z_L(f) + z_C(f)) ** 2))


"""
frecuencias - es un array de numeros entre 0.01*f0 y 100*f0 equiespaciado en la escala logaritmica
z_L = wL
z_C = - 1/wC
"""

# El nombre del fichero con los datos experimentales
filename = "Table 4.2 Experimental.txt"
# RECUERDA CAMBIAR LOS DATOS EXPERIMENTALES A LOS TUYOS!!!!!
v_s_exp, v_c_exp = np.genfromtxt(filename, skip_header=3, unpack=True)

print('\n'*3)
print(f"|{" ":^20}|{"Experimental":^20} ||{"Teorico":^20} |")
print('—'*80)
print(f"|{"Frecuencia, Hz":^20}|{"V_s, V":^10}|{"V_c, V":^10}||{"V_s, V":^10}|{"V_c, V":^10}|")

for f, a, b, c, d in zip(frecuencias, v_s_exp, v_c_exp, v_s_teorico(frecuencias), v_c_teorico(frecuencias)):
    print(f"|{f:^20.1f}|{a:^10.3f}|{b:^10.3f}||{c:^10.3f}|{d:^10.3f}|")
print('—'*80)

# Se puede cambiar True → False si no necesitas el grafico
if True:
    funcion_transferencia_exp = v_s_exp / v_g

    fig, ax1 = plt.subplots(figsize=(10, 6))
    x = np.logspace(-2, 2, 1000) * f_resonancia
    # y = np.abs(v_c_teorico(x) / v_s_teorico(x))
    y = np.abs(v_s_teorico(x) / v_g)
    ax1.semilogx(x, y, 'b-', label=r"$T(f)_{teor}$")
    ax1.set_ylim(0, 1)
    ax1.axvline(f_resonancia, color='g', label="$f_0$")
    ax1.scatter(frecuencias, funcion_transferencia_exp,
                color="r", label=r"$T(f)_{exp}$")
    ax1.grid(True, which='both')
    ax1.set_xlabel('$f$, Hz')
    ax1.set_ylabel(r"$|V_s|/|V_g|$", )
    ax1.legend()
    plt.title(
        'Representacion de la funcion de transferencia para el circuito de la tarea 1')
    plt.savefig("Diagrama de la funcion de transferencia.pdf", format="pdf")
    plt.show()
# TAREA 2
