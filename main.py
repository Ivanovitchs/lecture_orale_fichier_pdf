import pyttsx3
from PyPDF2 import PdfFileReader

fichier=open("RapportFinales.pdf","rb")
fichiers=PdfFileReader(fichier)
nbr_pages=fichiers.numPages

print(nbr_pages)
for i in range(nbr_pages):
   rec_fichier=fichiers.getPage(i)
   extract_fichier=rec_fichier.extractText()
   droid=pyttsx3.init()
   droid.say(extract_fichier)
fichier.close()


#droid.say(fichier)
droid.runAndWait()