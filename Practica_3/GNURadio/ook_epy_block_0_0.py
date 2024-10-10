import numpy as np              # Importa la biblioteca NumPy para operaciones numéricas
from gnuradio import gr         # Importa la clase base de GNU Radio para crear bloques
import math                     # Importa la biblioteca matemática (no se utiliza en este bloque)

class blk(gr.sync_block):       # Define la clase 'blk' que hereda de 'gr.sync_block'
    """This block is a CE VCO or baseband VCO and works as following: ….."""

    def __init__(self,):  
        # Constructor que inicializa el bloque sin parámetros adicionales
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   # Nombre del bloque
            in_sig=[np.float32, np.float32],  # Define las señales de entrada (amplitud y fase)
            out_sig=[np.complex64]  # Define la señal de salida como compleja
        )
        
    def work(self, input_items, output_items):
        # Método que realiza el procesamiento de datos
        A = input_items[0]        # Obtiene la señal de amplitud de la entrada
        Q = input_items[1]        # Obtiene la señal de fase de la entrada
        y = output_items[0]       # Prepara el buffer de salida
        N = len(A)                # Obtiene el número de muestras en A
        y[:] = A * np.exp(1j * Q) # Calcula la señal de salida como el producto de A y el exponencial complejo de Q
        return len(output_items[0])  # Retorna el número de muestras procesadas

