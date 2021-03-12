'''
Created on 30 nov. 2018

@author: Revnic
'''

from book import Book
class BookRepository():
    def __init__(self,fileName):
        self.__list=[]
        self.__fileName=fileName
        self.__loadBooksFromFile()
          
              
    def __loadBooksFromFile(self):
        file=open(self.__fileName,"r")
        oneLine=file.readline().strip()
        while oneLine!="":
            attributes=oneLine.split(" ; ")
            book=Book(attributes[0],attributes[1],attributes[2],attributes[3])
            book._Book__addBook(self.__list)
            oneLine=file.readline().strip()
        file.close()
        
    def __uploadBooksToFile(self):
        file=open(self.__fileName,"w")
        for book in self.__list:
            stringToFile=str(str(book._Book__Id)+" ; "+book._Book__title+" ; "+book._Book__description+" ; "+book._Book__author+"\n")
            file.write(stringToFile)
            