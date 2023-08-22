# ArchiBardo

ArchiBardo es un sistema demostrativo que utiliza ChatGPT a través del API provisto por OpenAI para coadyuvar en la clasificación automática de documentos nativos electrónicos en formato PDF, mediante la determinación de la serie documental y el año de producción del documento.

ArchiBardo se ofrece bajo la licencia MIT para libre uso y descarga.

## Prerequisitos

1. ArchiBardo funciona en la versión 3.11 de Python, en adelante.

2. Requiere de la generación de una llave de API que debe ser obtenida en el sitio de OpenAI. Más información en https://platform.openai.com/docs/guides/production-best-practices/api-keys
El sistema busca la llave en un archivo llamado APIKEY que deberá existir en la misma raíz de archivos del sistema ArchiBardo. Utiliza la llave y la cuenta asociada para generar las consultas con ChatGPT. Esto tiene un costo que debe ser configurado y asumido por el usuario.

3. Ejecutar el comando pip install -r requirements.txt sobre la raíz para instalar todos los requisitos de librerías externas.

## Configuración

1. El sistema está preconfigurado para utilizar el modelo gpt-4, que por el momento requiere una solicitud de acceso. En caso de no contar con el acceso, puede utilizar la versión de gpt-3.5-turbo, comentando la línea de código de GPT4 y descomentando la línea de GPT3.5. Esto debe hacerse en el script llamado "ArchiBardo.py"

2. Debe modificar la lista de tiposDeDocumentos.csv si desea utilizar otras series documentales.

3. En la raíz del sistema, debe existir una carpeta llamada: "DocumentosPorClasificar", y todos los documentos que desean ser clasificados deben colocarse en dicha carpeta.

4. El código del script de ArchiBardo.py puede ser modificado para establecer la perspectiva de la unidad organizacional desde donde se hace la clasificación de los documentos. Por defecto, el valor apunta a "Unidad de Archivo Central".

5. Si desea probar con otras variantes de prompts para sus procesos, puede hacer cambios en el script denominado DocumentInterpreter.py

6. Cuando el sistema falla en tres ocasiones consecutivas al tratar de determinar la serie documental o el año de producción de un documento, le asigna valores por defecto. Este valor puede ser cambiado en el script DocumentInterpreter.py

## Ejecución

Desde línea de comandos, puede invocar el script de ArchiBardo.py

## Autores
Alexander Barquero Elizondo

Ana Catalina Chacón Hernández

Sofía Irola Rojas