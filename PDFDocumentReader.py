from pypdf import PdfReader
# https://github.com/py-pdf/pypdf


# Clase que lee un documento PDF y retorna un string con el texto
class PDFDocumentReader:

    def __init__(self, path):
        self.path = path
 
    def readPDF(self):
        reader = PdfReader(self.path)
        return reader
    
    def readPage(self, pageId):
        reader = PdfReader(self.path)
        page = reader.pages[pageId]
        result = page.extract_text()
        result = result.replace("\n", "")
        result = result.replace("\t", " ")
        result = result.replace("\r", "")
        result = result.replace("  ", " ")
        text = result
        return text
    
    def readPages(self, initPageId, finalPageId):
        reader = PdfReader(self.path)
        text = ""
        for i in range(initPageId, finalPageId):
            page = reader.pages[i]
            result = page.extract_text()
            result = result.replace("\n", "")
            result = result.replace("\t", " ")
            result = result.replace("\r", "")
            result = result.replace("  ", " ")
            text = text + result
        return text
    
    def readAllPages(self):
        reader = PdfReader(self.path)
        text = ""
        for page in reader.pages:
            result = page.extract_text()
            result = result.replace("\n", "")
            result = result.replace("\t", " ")
            result = result.replace("\r", "")
            result = result.replace("  ", " ")
            text = text + result
        return text
    
    def splitDocument(self, factor):
        reader = PdfReader(self.path)
        text = ""
        factorCounter = 0
        pageCount = len(reader.pages)
        i = 0
        for page in reader.pages:
            if (factorCounter > factor) or (i in [0,1,pageCount-1,pageCount]):
                result = page.extract_text()
                result = result.replace("\n", "")
                result = result.replace("\t", " ")
                result = result.replace("\r", "")
                result = result.replace("  ", " ")
                text = text + result
                factorCounter = 0
            else:
                factorCounter = factorCounter + 1
            i = i + 1
            
        return text
 
    