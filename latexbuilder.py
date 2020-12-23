#! /usr/bin/python3

import os
import sys

def help():
    print("---------------------------------------------------")
    print("Compilateur LATEX")
    print("---------------------------------------------------")
    print(" ")
    print("Usage : latexbuild <source>")
    print(" ")
    print("---------------------------------------------------")
    print("Bug : leosamuel64@gmail.com")

def bonFichier(fichier):
    if fichier[-4]=='.' and fichier[-3]=='t' and fichier[-2]=='e' and fichier[-1]=='x':
        return True
    else:
        return False 

def verif():
    try:
        if sys.argv[1]=="-help" or sys.argv[1]=="--help":
            help()
            return False
        elif not bonFichier(sys.argv[1]):
            help()
            print("Erreur : Fichier incompatible")
            return False
        else:
            return True
    except:
        return False

def LitSource():
    source = open(sys.argv[1], 'r')
    content=[]
    ligne = source.readline()
    content.append(ligne)
    while ligne!="":
        ligne = source.readline()
        content.append(ligne)   
    source.close()
    return content

def ecritTemp(titre,Nom,contenu):
    os.system('touch temp.tex')
    dest = open("temp.tex", 'w')
    for ligne in init:
        dest.write(ligne)
    dest.write("\\title{"+titre+"}\n")
    dest.write("\\author{"+Nom+"}\n")
    for ligne in content:
        dest.write(ligne)
    dest.close()

def titrePDF_of_titre(titre):
    titrepdf = ""
    for i in range (len(titre)):
        if titre[i]==" ":
            titrepdf+="\\ "
        else:
            titrepdf+=titre[i]
    return titrepdf

def nettoie(titrepdf):
    os.system('cp temp.pdf '+titrepdf+".pdf")
    os.system('rm -r _minted-temp')
    os.system('rm temp.aux')
    os.system('rm temp.log')
    os.system('rm temp.pdf')
    os.system('rm temp.tex')


# ------------------------  CODE PRINCIPAL  ------------------------

if verif():
    init=['\\documentclass[10pt]{article}\n', '\t\n', '    \\usepackage[utf8x]{inputenc}\n', '    \\usepackage{stmaryrd}\n', '\t\\usepackage[T1]{fontenc}\n', '    \\usepackage[french]{babel}\n', '    \\usepackage{minted}\n', '\n', '\t\\setlength{\\hoffset}{-18pt}        \n', '\\setlength{\\oddsidemargin}{0pt} % Marge gauche sur pages impaires\n', '\\setlength{\\evensidemargin}{9pt} % Marge gauche sur pages paires\n', '\\setlength{\\marginparwidth}{54pt} % Largeur de note dans la marge\n', '\\setlength{\\textwidth}{481pt} % Largeur de la zone de texte (17cm)\n', '\\setlength{\\voffset}{-18pt} % Bon pour DOS\n', '\\setlength{\\marginparsep}{7pt} % Séparation de la marge\n', '\\setlength{\\topmargin}{0pt} % Pas de marge en haut\n', '\\setlength{\\headheight}{10pt} % Haut de page\n', '\\setlength{\\headsep}{10pt} % Entre le haut de page et le texte\n', '\\setlength{\\footskip}{27pt} % Bas de page + séparation\n', '\\setlength{\\textheight}{680pt} % Hauteur de la zone de texte (25cm)\n', '\n', '\t\\newtheorem{ex}{Exemple}\n', '\t\\newtheorem{prop}{Propriété}\n', '\t\\newtheorem{dem}{Démonstration}\n', '\t\\newtheorem{rq}{Remarque}\n', '    \\newtheorem{lem}{Lemme}\n', '    \\newtheorem{th}{Théorème}\n', '\t\\newtheorem{cor}{Corolaire}\n']
    Nom = input("Auteur : ")
    titre = input("Titre : ")

    content = LitSource()
    ecritTemp(titre,Nom,content)

    os.system("pdflatex -interaction=nonstopmode -shell-escape temp.tex")

    titre = titrePDF_of_titre(titre)

    nettoie(titre)