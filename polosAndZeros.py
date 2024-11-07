
def plot_pole_zero_and_frequency_response(num, den):
    """Função para plotar o diagrama de polos e zeros e a resposta em frequência (magnitude e fase) juntos."""
    
    # Criação do diagrama de polos e zeros
    zeros, poles, _ = signal.tf2zpk(num, den)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

    # Diagrama de Polos e Zeros
    unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    ax1.add_artist(unit_circle)
    ax1.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='b', label="Zeros")
    ax1.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label="Polos")
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    ax1.set_xlabel('Parte Real')
    ax1.set_ylabel('Parte Imaginária')
    ax1.set_title('Diagrama de Polos e Zeros')
    ax1.grid()
    ax1.legend()
    ax1.set_xlim([-1.5, 1.5])
    ax1.set_ylim([-1.5, 1.5])

    # Calcule a resposta em frequência
    w, h = signal.freqz(num, den, worN=8000)

    # Magnitude da Resposta em Frequência
    ax2.plot(w / np.pi, 20 * np.log10(abs(h)))
    ax2.set_title('Resposta em Frequência - Magnitude')
    ax2.set_xlabel('Frequência Normalizada [×π rad/amostra]')
    ax2.set_ylabel('Magnitude [dB]')
    ax2.grid()

    # Fase da Resposta em Frequência
    ax3.plot(w / np.pi, np.angle(h))
    ax3.set_title('Resposta em Frequência - Fase')
    ax3.set_xlabel('Frequência Normalizada [×π rad/amostra]')
    ax3.set_ylabel('Fase [radianos]')
    ax3.grid()

    # Exibir todos os gráficos
    plt.tight_layout()
    plt.show()
