import csv

class CSVDocumentReader:

    # Constructor
    def __init__(self, filename):
        self.filename = filename

    # Leer un archivo CSV que solo tiene la columna de tipos, y retornar un string con todos los valores separados por coma
    def readCSV(self):
        text = ""
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                text += row[0] + ", "
            
            # Remove the last comma
            text = text[:-1]

        return text
    
    
