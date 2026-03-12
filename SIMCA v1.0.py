# --- FUNCIONES DE CLASIFICACIÓN ---

def obtener_clasificacion(temp):
    """Determina la categoría climática."""
    if temp < 0:
        return "Congelación"
    elif 0 <= temp <= 10:
        return "Frío"
    elif 11 <= temp <= 25:
        return "Templado"
    elif 26 <= temp <= 35:
        return "Caliente"
    else:
        return "Ola de calor"

# --- FUNCIONES DE ALERTAS ---

def alerta_sequia(temp, lluvia):
    """Verifica si hay riesgo de sequía."""
    if temp > 30 and lluvia < 20:
        print("- Riesgo de sequía.")
        return True
    return False

def alerta_hielo(temp):
    """Verifica si hay riesgo de hielo."""
    if temp < 5:
        print("- Posible formación de hielo.")
        return True
    return False

def alerta_lluvia(lluvia):
    """Verifica si hay alta probabilidad de lluvia."""
    if lluvia > 70:
        print("- Alta probabilidad de lluvia.")
        return True
    return False

def procesar_avisos(temp, lluvia):
    """Orquesta la impresión de todas las alertas."""
    print("--- ALERTAS Y AVISOS ---")
    
    # Ejecutamos cada alerta y guardamos si alguna fue verdadera
    s = alerta_sequia(temp, lluvia)
    h = alerta_hielo(temp)
    ll = alerta_lluvia(lluvia)
    
    if not s and not h and not ll:
        print("- No hay alertas climáticas activas.")

# --- FUNCIONES DE SALIDA DE DATOS ---

def mostrar_informe(ciudad, temp, lluvia, estado):
    """Muestra el reporte final sin usar + ni str()."""
    print("\n--- INFORME METEOROLÓGICO ---")
    print("CIUDAD:", ciudad.upper())
    print("ESTADO:", estado)
    print("TEMPERATURA REGISTRADA:", temp, "°C")
    print("PROBABILIDAD DE LLUVIA:", lluvia, "%")
    print("-----------------------------")

# --- FUNCIÓN DE ENTRADA DE DATOS ---

def realizar_consulta():
    """Gestiona la captura de datos y coordina las funciones."""
    ciudad = input("Ingrese el nombre de la ciudad: ")
    
    try:
        # Nota: print con coma para evitar usar +
        print("Configurando datos para", ciudad)
        t_entrada = input("Temperatura actual (°C): ")
        temp = float(t_entrada)

        l_entrada = input("Probabilidad de lluvia (0-100): ")
        lluvia = float(l_entrada)

        # 1. Obtener la etiqueta del clima
        estado = obtener_clasificacion(temp)
        
        # 2. Mostrar los datos generales
        mostrar_informe(ciudad, temp, lluvia, estado)
        
        # 3. Procesar las alertas
        procesar_avisos(temp, lluvia)
        
    except ValueError:
        print("Error: El sistema solo acepta números para temperatura y lluvia.")

# --- MENÚ ---

def mostrar_guia():
    """Imprime la tabla de rangos."""
    print("\n--- TABLA DE REFERENCIA ---")
    print("Menor a 0°C  : Congelación")
    print("0 a 10°C     : Frío")
    print("11 a 25°C    : Templado")
    print("26 a 35°C    : Caliente")
    print("Mayor a 35°C : Ola de calor")

def menu_principal():
    """Controlador principal del programa."""
    while True:
        print("\n===============================")
        print("   SISTEMA METEOROLÓGICO PRO")
        print("===============================")
        print("1. Analizar ciudad")
        print("2. Ver guía de rangos")
        print("3. Salir")
        
        opcion = input("Seleccione: ")

        if opcion == "1":
            realizar_consulta()
        elif opcion == "2":
            mostrar_guia()
        elif opcion == "3":
            print("Cerrando programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()