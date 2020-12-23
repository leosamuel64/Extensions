#! /usr/bin/python3

import os
import sys

def help():
    print("---------------------------------------------------")
    print("Utilitaire de convertion jupyter Notebook vers PDF")
    print("---------------------------------------------------")
    print(" ")
    print("Usage : jupconvert originFile final_Name")
    print(" ")
    print("---------------------------------------------------")
    print("Bug : leosamuel64@gmail.com")

try:
    arg1 = sys.argv[1]
    
    if arg1 == "-help" or arg1 == "--help":
        help()
    
    else:
        if len(sys.argv)>=2:
            res = ""
            for i in range(2,len(sys.argv)):
                if i < len(sys.argv)-1:
                    res+= sys.argv[i]+"\ "
                else:
                    res+=sys.argv[i]
        nomInit = arg1
        try :
            final_name = res
        except:
            final_name = arg1
        del arg1
        del res

        print(nomInit)
        print(final_name)
        v = os.path.exists(nomInit)	## Vérifie si le fichier existe
        if not v:
            print("Erreur : Le fichier n'existe pas")
        else:
            os.system('cp '+str(nomInit)+" "+str(final_name)+".ipynb")
            os.system('jupyter nbconvert --to PDF '+str(final_name)+".ipynb")
            os.system('rm '+str(final_name)+".ipynb")
            print("-----  FIN  -----")
except:
    help()



