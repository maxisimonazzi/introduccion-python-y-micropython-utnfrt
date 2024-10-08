import matplotlib.pyplot as plt
import numpy as np

# Parámetros
fs = 1000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs)  # Vector de tiempo de 1 segundo

# Señal portadora
fc = 100  # Frecuencia de la portadora
carrier = np.cos(2 * np.pi * fc * t)

# Señal moduladora
fm = 5  # Frecuencia de la moduladora
modulator = np.sin(2 * np.pi * fm * t)

# Señal modulada en amplitud (AM)
modulation_index = 1.0  # Índice de modulación
am_signal = (1 + modulation_index * modulator) * carrier

# Calcular la FFT de la señal modulada
fft_am_signal = np.fft.fft(am_signal)
fft_freqs = np.fft.fftfreq(len(am_signal), d=1/fs)

# Crear los gráficos
plt.figure(figsize=(10, 8))

# Gráfico de la señal portadora
plt.subplot(2, 2, 1)
plt.plot(t, carrier)
plt.title('Señal Portadora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Gráfico de la señal moduladora
plt.subplot(2, 2, 2)
plt.plot(t, modulator)
plt.title('Señal Moduladora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Gráfico de la señal modulada en amplitud (AM)
plt.subplot(2, 2, 3)
plt.plot(t, am_signal)
plt.title('Señal Modulada en Amplitud (AM)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Gráfico de la FFT de la señal modulada
plt.subplot(2, 2, 4)
plt.plot(fft_freqs, np.abs(fft_am_signal))
plt.title('FFT de la Señal Modulada en Amplitud (AM)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.xlim(0, fs/2)  # Mostrar solo la mitad positiva del espectro

# Ajustar el layout para que no se solapen los subplots
plt.tight_layout()

# Mostrar los gráficos
plt.show()