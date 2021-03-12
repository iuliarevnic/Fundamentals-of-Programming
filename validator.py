'''
Created on 2 nov. 2018  

@author: Revnic
'''
from book import *
from client import *
from errors import *
def validateBookId(Id,ListOfBooks):
    '''
    Function that checks whether a given book Id exists in a list
    input: Id, ListOfBooks
    preconditions: Id should be an integer
    output:-
    postconditions: If the Id doesn't exist in the list, an error will appear.
    '''
    ok=0
    for book in ListOfBooks:
        if int(book._Book__Id)==Id:
            ok=1
    if ok==0:
        raise BookError("Invalid Id.")
        
def validateClientId(Id,ListOfClients):
    '''
    Function that checks whether a given client Id exists in a list
    input: Id, ListOfBooks
    preconditions: Id should be an integer
    output:-
    postconditions: If the Id doesn't exist in the list, an error will appear.
    '''
    ok=0
    for client in ListOfClients:
        if int(client._Client__Id)==Id:
            ok=1
    if ok==0:
        raise ClientError("Invalid Id.")       
    
def validateBookUpdate(oldId,Id,title,description,author,ListOfBooks):
    '''
    Function that checks whether the given updated values already exist in a list, in order to avoid duplicates
    input: Id,title,description,author,ListOfBooks
    preconditions: Id should be an integer, title,description and author should be strings
    output:-
    postconditions: If the values exist, an error will appear
    '''
    for book in ListOfBooks:
            if book._Book__Id==Id and book._Book__Id!=oldId:
                raise BookError("Existing Id!")
            if book._Book__title==title and book._Book__description==description and book._Book__author==author:
                raise BookError("There already exists a book with the given updated values!")

def validateClientUpdate(oldId,Id,name,ListOfClients):
    '''
    Function that checks whether the given updated values already exist in a list, in order to avoid duplicates
    input: Id,name,ListOfClients
    preconditions: Id should be an integer,name should be a string
    output:-
    postconditions: If the values exist, an error will appear
    '''
    for  client in ListOfClients:                  
            if client._Client__Id==Id and oldId!=client._Client__Id:
                raise ClientError("Existing Id!")
            if client._Client__name==name:
                raise ClientError("There already exists a client with the same name!")     
            
    
def validateDateValue(date):
    '''
    Function that checks the correctness of the values given for the day, month and the year of a date
    input: date
    preconditions: date should be a list of integers, representing the day, month and the year of the date
    output:-
    postconditions: If at least one of the values isn't correct, an error will appear
    '''
    errors=""
    if date[0]<1 or date[0]>31:
        errors+="Wrong day.\n"
    if date[1]<1 or date[1]>12:
        errors+="Wrong month.\n"
    if len(errors)!=0:
        raise DateError(errors)                                                   
    
def validateRentalId(rentalId,ListOfRentals):
    '''
    Function that checks if there exists a rental with the given Id in a list
    input: rentalId,ListOfRentals
    preconditions: rentalId should be an integer
    output:-
    postconditions: If the Id isn't in the list, an error will appear
    '''
    ok=0
    for rental in ListOfRentals:
        if rental._Rental__rentalId==rentalId:
            ok=1
    if ok==0:
        raise RentalError("Inexistent Id.")        