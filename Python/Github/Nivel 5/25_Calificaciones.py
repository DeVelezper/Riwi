
estudiantes = {}
estudianteActual = None

def registrarEstudiante():
    while True:
        nombre = input("Ingrese un estudiante: ").strip().lower()
        if nombre not in estudiantes:
            estudiantes[nombre] = []
            print("Estuduante registrado.")
            return(nombre)

        else:
            print("Ese estudiante ya esta.\n ")
            continuar = input("Quieres intentar con otro estuduante? (s/n): ").lower()
            if continuar == "s":
                nombre = None
                continue
            else:
                return

def ingresarNotas(nombre=None):
    global estudianteActual
    while True:

        if nombre is None:
            if estudianteActual is None:
                nombre = input(f"A que estuduante le quieres ingresar una nota? ")
            else:
                nombre = estudianteActual
        
        if nombre in estudiantes:
            try:
                nota = float(input("Ingresa la nota: "))
                estudiantes[nombre].append(nota)
                print("Nota agregada correctamente.")
                estudianteActual = nombre
                return
            except ValueError:
                print("Dato no valido. Ingresa un numero:  \n")
        else:
            print("Ese estudiante no existe.\n")
            continuar = input("Quieres intentar con otro estuduante? (s/n): ").lower()
            if continuar == "s":
                nombre = None  
                continue
            else:
                return  

def mostrarNotas(nombre=None):
    global estudianteActual
    while True:
        if nombre is None:
            if estudianteActual is None:
                nombre = input("A que estuduante quiere mostar las notas? ")
            else:
                estudianteActual = nombre
        if nombre in estudiantes:
            try:
                print(f"Notas de {nombre}: {estudiantes[nombre]} ")
                return
            except ValueError:
                print("Dato no valido. Ingresa un estudiante correcto")
                
        else:
            print("Ese estudiante no existe.")
            continuar = input("¿Quieres intentar con otro estudiante? (s/n): ").lower()
            if continuar == "s":
                nombre = None
                continue
            else:
                return

def verCalculos(nombre=None):
    global estudianteActual

    while True:

        if nombre is None:
            nombre = input("A que estuduante le quieres ver los calculos? ")
        else:
            nombre = estudianteActual

        if nombre in estudiantes:
            notas = estudiantes[nombre]

            if len(notas) == 0:
                print("Este estuduante no tiene notas aun.\n")
                return
            
            # Calculos
            suma = sum(notas) 
            promedio  = suma / len(notas)
            notaMax = max(notas)
            notaMin = min(notas)
            cantida = len(notas)    

            print(f"""
Calculos para {nombre}: 
Promedio: {promedio:.2f}
Nota mas alta: {notaMax}
Nota mas baja: {notaMin}
Suma de notas: {suma}
Cantida de notas: {cantida}""")      
            return promedio

        else:
            print("Ese estudiante no existe, intenta de nuevo.\n")

def clasificarDesempeno():
    promedio = verCalculos()

acciones = {
    1: registrarEstudiante,
    2: ingresarNotas,
    3: mostrarNotas,
    4: verCalculos,
    5: clasificaDesempeno,
    6: informeCompleto,
    7: listarEstudiantes,
    8: eliminarNotas
}
def Menu():
    try:
        return(int(input("""
==============================================
        SISTEMA DE CALIFICACIONES
==============================================

1. Registrar estudiante
2. Ingresar notas a un estudiante
3. Mostrar notas de un estudiante
4. Ver cálculos de un estudiante
    - Promedio
    - Nota más alta
    - Nota más baja
    - Cantidad de notas
    - Suma total
5. Clasificar el desempeño de un estudiante
    - Aprobado / Reprobado
    - Excelente / Bueno / Regular / Malo
6. Mostrar informe completo de un estudiante
7. Mostrar lista de estudiantes registrados
8. Eliminar notas de un estudiante
9. Salir

==============================================
Seleccione una opción: """)))

    except:
        return -1
    
