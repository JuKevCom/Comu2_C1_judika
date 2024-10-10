import numpy as np              # Importa la biblioteca NumPy para operaciones numéricas
from gnuradio import gr         # Importa la clase base de GNU Radio para crear bloques
import math                     # Importa la biblioteca matemática para funciones como coseno

class blk(gr.sync_block):       # Define la clase 'blk' que hereda de 'gr.sync_block'
    """This block is a RF VCO and works as following: It acts as a continuous wave (CW) voltage-controlled oscillator (VCO) at baseband, generating a complex output signal based on an amplitude and a phase. This is commonly used in modulation and signal processing applications."""

    def __init__(self, fc=128000, samp_rate=320000):  
        # Constructor que inicializa el bloque con frecuencia de portadora y tasa de muestreo
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   # Nombre del bloque
            in_sig=[np.float32, np.float32],  # Define las señales de entrada (amplitud y fase)
            out_sig=[np.float32]  # Define la señal de salida
        )
        self.fc = fc              # Almacena la frecuencia de portadora
        self.samp_rate = samp_rate  # Almacena la tasa de muestreo
        self.n_m = 0              # Inicializa el contador de muestras procesadas

    def work(self, input_items, output_items):
        # Método que realiza el procesamiento de datos
        A = input_items[0]        # Obtiene la señal de amplitud de la entrada
        Q = input_items[1]        # Obtiene la señal de fase de la entrada
        y = output_items[0]       # Prepara el buffer de salida
        N = len(A)                # Obtiene el número de muestras en A
        n = np.linspace(self.n_m, self.n_m + N - 1, N)  
        # Crea un arreglo de índices de muestras desde n_m hasta n_m + N - 1
        self.n_m += N             # Actualiza el contador de muestras procesadas
        y[:] = A * np.cos(2 * math.pi * self.fc * n / self.samp_rate + Q)
        # Calcula la señal de salida multiplicando A por el coseno con la frecuencia y fase
        return len(output_items[0])  # Retorna el número de muestras procesadas



