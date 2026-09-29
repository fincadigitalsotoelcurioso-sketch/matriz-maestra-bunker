import numpy as np


def analizar_data(data):
    """
    Analizar los datos y devolver el resultado.

    Args:
        data (numpy.array): Los datos a analizar.

    Returns:
        numpy.array: El resultado del análisis.
    """
    if not isinstance(data, np.ndarray):
        raise ValueError("Error: La entrada no es un array NumPy.")

    return data * 2


def optimizar_rendimiento(data):
    """
    Optimizar el rendimiento del resultado.

    Args:
        data (numpy.array): El resultado del análisis.

    Returns:
        numpy.array: El resultado optimizado.
    """
    return data


def procesar_datos(data):
    """
    Procesar los datos y devolver el resultado.

    Args:
        data (numpy.array): Los datos a procesar.

    Returns:
        numpy.array: El resultado del proceso.
    """
    datos_estructurados = data.reshape((-1, 4))

    try:
        analisis = analizar_data(datos_estructurados)
        optimized_data = optimizar_rendimiento(analisis)
        return optimized_data
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    datos_prueba = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    resultado = procesar_datos(datos_prueba)
    print("Resultado exitoso:", resultado)
