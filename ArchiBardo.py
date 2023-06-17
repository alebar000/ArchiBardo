import os
import csv
import time
import shutil

from PDFDocumentReader import *
from DocumentInterpreter import *
from CSVDocumentReader import *


chosenModel = "gpt-4" #8,192 tokens | $0.03 / 1K tokens | 0.03 * 8.192 = $0.24576
#chosenModel = "gpt-3.5-turbo" #4,096 tokens | $0.002 / 1K tokens | 0.002 * 4.096 = $0.008192    
#chosenModel = "gpt-4-32k" #32,768 tokens | $0.06 / 1K tokens | 0.06 * 32.768 = $1.96608

tokenLimit = 3000
documentosPorClasificar = "DocumentosPorClasificar"
documentosClasificados = "DocumentosClasificados"
unidadAnalizada = "Unidad de Archivo Central"
tiposDeDocumentos = "tiposDeDocumentos.csv"

def procesarDocumento(rutaDocumento):
    # Obtener el nombre del documento de la ruta dada, conla extension
    nombreDocumento = os.path.basename(rutaDocumento)
    print ("Procesando documento: ", nombreDocumento)

    reader = PDFDocumentReader(rutaDocumento)
    text = reader.readAllPages()
    #print ("Texto del documento: ", text)

    interpreter = DocumentInterpreter()
    tokens = interpreter.tokenCounter(text, chosenModel)
    print ("Costo en tokens: ", tokens)

    if tokens > tokenLimit:
        factor = tokens / tokenLimit
        text = reader.splitDocument(factor)
        #print ("Nuevo texto: ", text)
        tokens = interpreter.tokenCounter(text, chosenModel)
        print ("Nuevo costo en tokens: ", tokens)

    textObjects = interpreter.interpret(text, nombreDocumento, chosenModel, unidadAnalizada, obtenerTiposDeDocumentos())
    print ("Resultado clasificador: ", textObjects)

    # Separar en lista de strings separadas por coma
    textObjects = textObjects.split(",")

    # Remover los espacios al principio y final de cada string de la lista
    textObjects = [x.strip() for x in textObjects]
    
    # Si el archivo "resultados.csv" no existe, se crea
    if not os.path.isfile("resultados.csv"):
        with open("resultados.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Documento", "Año", "Tipo de Documento"])

    # Si el archivo "resultados.csv" existe, se actualiza
    with open("resultados.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nombreDocumento, textObjects[0], textObjects[1]])

    print ("*****************\n\n")


def obtenerTiposDeDocumentos():
    csvReader = CSVDocumentReader(tiposDeDocumentos)
    tipos = csvReader.readCSV()
    #print ("Lista de tipos de documentos: ", tipos)
    return tipos

def main():        
    # Guardar el tiempo de inicio
    start_time = time.time()
    print ("Inicio del programa: ", time.ctime(start_time))

    # Obtener el directorio actual
    cwd = os.getcwd()
    # Obtener la ruta del directorio documentosPorClasificar
    path = os.path.join(cwd, documentosPorClasificar)
    # Obtener la lista de arcivos en el directorio "DocumentosPorClasificar" y sus subdirectorios
    files = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                for name in files
                if name.endswith((".pdf", ".PDF"))]
    
    # Contar el numero de documentos por procesar
    print ("Número de documentos por procesar: ", len(files))
    contadorArchivos = 1
    
    # Por cada archivo en la lista de archivos
    for file in files:
        # Process the file
        print ("Archivo ", contadorArchivos, " de ", len(files))
        print ("Archivo a procesar: ", file)
        procesarDocumento(file)
        print ("Archivo procesado: ", file)
        contadorArchivos += 1

    # Guardar el tiempo de finalizacion
    end_time = time.time()
    print ("Fin del programa: ", time.ctime(end_time))
    # Calcular el tiempo total transcurrido
    elapsed_time = end_time - start_time
    print ("Tiempo transcurrido: ", elapsed_time, " segundos")


    # Si el folder "DocumentosClasificados" no existe, se crea
    if not os.path.exists(documentosClasificados):
        print ("Creando carpeta: ", documentosClasificados)
        os.makedirs(documentosClasificados)

    # Dentro del folder "DocumentosPorClasificar", por cada valor de la columna "Tipo de Documento" en "resultados.csv", se crea un folder con el nombre del valor
    with open("resultados.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if not os.path.exists(os.path.join(documentosClasificados, row[2])):
                print ("Creando carpeta: ", row[2])
                os.makedirs(os.path.join(documentosClasificados, row[2]))

    # Dentro del folder "DocumentosPorClasificar", por cada archivo en la lista de archivos, mover el archivo al folder con el nombre del valor de la columna "Tipo de Documento" del archivo "resultados.csv"
    for file in files:
        with open("resultados.csv", "r") as file2:
            reader = csv.reader(file2)
            next(reader)
            for row in reader:
                if file.endswith(row[0]):
                    print ("Moviendo archivo: ", file)
                    shutil.move(file, os.path.join(documentosClasificados, row[2]))

    # Eliminar todos los folder y archivos dentro de "DocumentosPorClasificar"
    shutil.rmtree(documentosPorClasificar)
    

if __name__ == "__main__":
    main()
                        
    