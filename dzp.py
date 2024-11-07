import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Molde para zeros e polos complexos:
zero_complex_1 = 0.5 * np.exp(1j * np.pi / 3)  # 0.5 * e^(j*pi/3)
pole_complex_1 = (-0.9 * np.exp(1j * np.pi / 4) -0.9* np.exp(-1j * np.pi / 4)) # 0.2 * e^(j*pi/2)

# Defina os coeficientes da função de transferência
num = [1,0,0]    # Numerador da Transformada Z
den = [1,pole_complex_1,0.81] # Denominador da Transformada Z



def plot_pole_zero(num, den):
    """Função para plotar o diagrama de polos e zeros no plano complexo."""
    zeros, poles, _ = signal.tf2zpk(num, den)

    # Criação do diagrama
    fig, ax = plt.subplots(figsize=(6, 6))

    # Adiciona o círculo unitário
    unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    ax.add_artist(unit_circle)

    # Plota os polos e zeros
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='b', label="Zeros")
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label="Polos")

    # Configurações do gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Diagrama de Polos e Zeros')
    plt.grid()
    plt.legend()

    # Limite dos eixos para visualizar o círculo unitário
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    
    plt.show()

def plot_frequency_response(num, den):
    """Função para plotar a resposta em frequência (magnitude e fase)."""
    # Calcule a resposta em frequência
    w, h = signal.freqz(num, den, worN=8000)

    # Plote a magnitude da resposta em frequência
    plt.figure(figsize=(10, 6))
    plt.plot(w / np.pi, 20 * np.log10(abs(h)))
    plt.title('Resposta em Frequência - Magnitude')
    plt.xlabel('Frequência Normalizada [×π rad/amostra]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()

    # Plote a fase da resposta em frequência
    plt.figure(figsize=(10, 6))
    plt.plot(w / np.pi, np.angle(h))
    plt.title('Resposta em Frequência - Fase')
    plt.xlabel('Frequência Normalizada [×π rad/amostra]')
    plt.ylabel('Fase [radianos]')
    plt.grid()

    plt.show()
    
plot_frequency_response(num, den)
plot_pole_zero(num, den)