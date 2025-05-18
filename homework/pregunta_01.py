"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re 
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            sequence.append(line.strip())

    columns = sequence[0:2]
    content = sequence[4:]

    columns = '\t'.join([(a + ' ' + b).strip() for a,b in zip(re.split(r"\s\s+", columns[0].strip()),re.split(r"\s\s+", '  '+columns[1].strip()+'  '))]).lower().replace(' ', '_')

    processed_content = []
    nums = None
    for line in content:
        if '%' in line:
            line = line.split('%')
            nums = re.sub(r"\s+", "\t", line[0].strip().replace(',','.'))
            base = re.sub(r"\s+", " ", line[1].strip().replace('.',''))
        else:
            if line != '':
                complement = re.sub(r"\s+", " ", line.strip().replace('.',''))
                base = base + ' ' + complement
            else:
                processed_content.append(nums + '\t' + base + '\n')
    
    with open('files/input/clusters_report_processed.tsv','w') as f:
        f.write(columns + '\n') 
        for line in processed_content:
            f.write(line)

    df = pd.read_csv('files/input/clusters_report_processed.tsv', sep='\t')

    return df

print(pregunta_01())