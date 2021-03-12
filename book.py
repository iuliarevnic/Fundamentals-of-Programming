'''
Created on 1 nov. 2018

@author: Revnic
'''
from repository import findBookIndex
class Book:
    def __init__(self,Id,title,description,author):
        self.__Id=Id
        self.__title=title
        self.__description=description
        self.__author=author
    
    def __getId(self):
        return self.__Id
    def __getTitle(self):
        return self.__title
    def __getDescription(self):
        return self.__description
    def __getAuthor(self):
        return self.__author
    
    def __setId(self,Id):
        self.__Id=Id
    def __setTitle(self,title):
        self.__title=title
    def __setDescription(self,description):
        self.__description=description
    def __setAuthor(self,author):
        self.__author=author
      
    def __eq__(self,other):
        return self.__Id==other.__Id    
                   
    def __addBook(self,ListOfBooks):
        '''
        Function that adds a new book to the list
        input: self,ListOfBooks
        preconditions:-
        output:-
        postconditions:If the book isn't already in the list, it will be added to the list ListOfBooks
        '''
        for book in ListOfBooks:
            if int(book.__Id)==self.__Id:
                print("This Id already exists.")
                return
            elif (book.__title==self.__title and book.__description==self.__description and book.__author==self.__author):
                print("This book is already in the list!")
                return
        ListOfBooks.append(self)
        
    def __removeBook(self,ListOfBooks):    
        '''  
        Function that deletes a book from a list
        input: self, ListOfBooks
        preconditions:-
        output:-
        postconditions: If the given book is in the list, it will be deleted from the list ListOfBooks.
        '''
        if(len(ListOfBooks)==0):
            print("The list is already empty!")
            return
         
        ok=0
        for book in ListOfBooks:
            if int(book.__Id)==int(self.__Id) and book.__title==self.__title and book.__description==self.__description and book.__author==self.__author:
                ok=1
                ListOfBooks.remove(book)           
        if ok==0:
            print("Inexistent book!")
            return
             
           
                       
            
             
    def __updateBook(self,oldId,Id,title,description,author,ListOfBooks):    
        '''
        Function that updates a book in a list
        input: self,Id,title,description,author      
        preconditions: Id should be an integer, while title,description and author should be strings
        output:-
        postconditions: The book will be updated with the given values
        ''' 
        index=findBookIndex(oldId,ListOfBooks)
        self.__setId(Id)       
        self.__setTitle(title)
        self.__setDescription(description)
        self.__setAuthor(author)
        ListOfBooks[index]=self
         
           
    def __listBook(self,ListOfBooks): 
        '''         
        Function that prints a list of books
        input: self, ListOfBooks
        preconditions:-
    
        output: The list of books is printed
        postconditions:-
        '''
        if(len(ListOfBooks)==0):
            print("The list is empty!")
            return
        for book in ListOfBooks:
            print("Id:",book.__Id," Title:",book.__title," Description:",book.__description," Author",book.__author,"\n")
    
    def __addBookToIndex(self,index,ListOfBooks):
        '''
        Function that adds a book in a list at the specified index
        input: self,index, ListOfBooks
        preconditions: index should be an existing index in the list
        output:-
        postconditions:-
        '''             
        ListOfBooks.insert(index[len(index)-1],self)    