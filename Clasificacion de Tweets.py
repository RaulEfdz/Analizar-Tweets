import csv
import re
import string
import time
from textblob import TextBlob

RES = []
Url_csv = input('Coloque ella direccion del archivo .csv: ')
resultado = ""
F = ''
with open(Url_csv, newline='') as File:  
    print('Procesando a 0.5s por elemento...')
    documento = csv.reader(File)
    for elemento in documento:
        if len(elemento) == 2 :
            if len(elemento[1]) > 2 :
                F = elemento[1].replace("'","")
                F = F.replace("[", "")
                F = F.replace("]", "")
                F = F.replace(",", "")
                # a = TextBlob(F).translate(from_lang='es', to='en').sentiment
                analysis = TextBlob(F)
                if F != '':
                    if analysis.detect_language() == 'es':
                        resultado = analysis.translate(from_lang = 'es', to = 'en').sentiment.polarity
                        time.sleep(2)
                        if len(str(resultado)) >2:
                            if resultado >= -1 and resultado < 0.5:
                                RES.append('\n'+'N,'+elemento[1]) 
                            elif resultado >= 0.5 and resultado < 2:
                                RES.append('\n'+'P,'+elemento[1])        
print(RES)
E_Document = open(Url_csv, 'w')
with E_Document:
    writer = csv.writer(E_Document)
    writer.writerow(['POLARIDAD','TEXT'])
    writer.writerows([RES])
print("Completado")
