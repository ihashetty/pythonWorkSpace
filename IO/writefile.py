"""Readfile command"""


FILE = open("data.txt", "w", encoding="utf-8")
FILE.write("Hello File")
FILE.close()
