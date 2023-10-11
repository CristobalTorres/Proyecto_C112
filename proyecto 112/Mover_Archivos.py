import os
import shutil

#os.mkdir("Documentos_Archivos")

from_dir='/Users/migue/Desktop/Python/proyecto 112'
to_dir='/Users/migue/Desktop/Python/proyecto 112/Documentos_Archivos/'

list_of_files= os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    root,extencion= os.path.splitext(i)
    print(f"Nombre: {root}, Extensión: {extencion}")
  

    if extencion == '':
     continue
    if extencion in [".txt",".png",".doc",".py"]:
     ruta1 = from_dir+"/"+ i
     ruta2 = to_dir+'/'+ "Documentos_Archivos"
     ruta3 = to_dir+'/'+ "Documentos_Archivos"+"/"+ i

     if os.path.exists(ruta2):
       print("el archivo "+i+" se esta moviendo . . .")
       shutil.move(ruta1,ruta3)
     else:
       os.mkdir(ruta2)
       print("Moviendo " + i)
       shutil.move(ruta1,ruta3) 
