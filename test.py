from tkinter import *

fenetre = Tk()


alphabet = [chr(n) for n in range(65,65+26)]
print(alphabet)





for i in range(26):
    print("\tdef lettreTappee{}():\n\t\tprint('{}')\n\t\treturn '{}'".format(chr(65+i),chr(65+i),chr(65+i)))