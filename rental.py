'''
Created on 3 nov. 2018

@author: Revnic
'''
from repository import checkBookAvailability
class Rental():
    def __init__(self,rentalId,bookId,clientId,rentedDate,dueDate,returnedDate):
        self.__rentalId=rentalId
        self.__bookId=bookId
        self.__clientId=clientId
        self.__rentedDate=rentedDate
        self.__dueDate=dueDate
        self.__returnedDate=returnedDate
        
    def __getRentalId(self):
        return self.__rentalId
    def __getBookId(self):
        return self.__bookId 
    def __getClientId(self):
        return self.__clientId
    def __getRentedDate(self):
        return self.__rentedDate
    def __getDueDate(self):
        return self.__dueDate
    def __getReturnedDate(self):
        return self.__returnedDate
    
    def __setRentalId(self,rentalId):
        self.__rentalId=rentalId
    def __setBookId(self,bookId):
        self.__bookId=bookId
    def __setClientId(self,clientId):
        self.__clientId=clientId
    def __setRentedDate(self,rentedDate):
        self.__rentedDate=rentedDate            
    def __setDueDate(self,dueDate):   
        self.__dueDate=dueDate
    def __setReturnedDate(self,returnedDate):
        self.__returnedDate=returnedDate
        
    def __eq__(self,other):
        return self.__rentalId==other.__rentalId    
    def __rentBook(self,ListOfRentals):
        '''
        Function that rents a book, if available
        input: self, ListOfRentals
        preconditions:-
        output:-
        postconditions: If the book isn't available, an error will appear
        '''
        try:
            checkBookAvailability(self.__bookId,ListOfRentals)
            ListOfRentals.append(self)       
        except ValueError:
            print("The book isn't available.")
                            
            
    def __returnBook(self,returnedDate,index,ListOfRentals):
        '''
        Function that adds a return date to a rental
        input: self,returnedDate,ListOfRentals
        preconditions: rentedDate should be  string of the form "dd.mm.yyyy"
        output:-
        postconditions: The rental will have an updated returnedDate attribute
        '''
        self.__setReturnedDate(returnedDate)
        ListOfRentals[index]=self        
        
    def __addRentalToIndex(self,index,ListOfRentals):
        '''
        Function that adds a rental to a list at the specified index
        input: self,index,ListOfRentals
        preconditions:-
        output:-
        postconditions:-
        '''
        ListOfRentals.insert(index[len(index)-1],self)
        