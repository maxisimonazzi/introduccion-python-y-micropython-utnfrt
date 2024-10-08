import matplotlib.pyplot as plt
import numpy as np

# Generar la señal senoidal
x = np.linspace(0, 2 * np.pi, 1000)  # 1000 puntos entre 0 y 2π
signal = np.sin(25 * x)  # Señal senoidal con frecuencia 25

# Calcular la FFT de la señal
fft_signal = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(signal), d=1/1000)

# Ordenar las frecuencias y la FFT
fft_signal_shifted = np.fft.fftshift(fft_signal)
fft_freqs_shifted = np.fft.fftshift(fft_freqs)

# Crear los gráficos
plt.figure(figsize=(12, 6))

# Gráfico de la señal original
plt.subplot(2, 1, 1)
plt.plot(x, signal)
plt.title('Señal Senoidal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

# Gráfico de la FFT de la señal
plt.subplot(2, 1, 2)
plt.plot(fft_freqs_shifted, np.abs(fft_signal_shifted))
plt.title('FFT de la Señal Senoidal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.xlim(-100, 100)  # Limitar el eje x para ver mejor las frecuencias relevantes

# Mostrar los gráficos
plt.tight_layout()
plt.show()