'''
Created on 3 nov. 2018

@author: Revnic
'''
def findBookIndex(Id,ListOfBooks):
    '''
    Function that finds the index of a book in list
    input: Id, ListOfBooks
    preconditions: Id should be an existing integer in the list
    output: index
    postconditions:-
    '''
    for index in range(len(ListOfBooks)):
        if int(ListOfBooks[index]._Book__Id)==Id:
            return index        
        
def findClientIndex(Id,ListOfClients):
    '''
    Function that finds the index of a client in list
    input: Id, ListOfClients
    preconditions: Id should be an existing integer in the list
    output: index
    postconditions:-
    '''
    for index in range(len(ListOfClients)):
        if int(ListOfClients[index]._Client__Id)==Id:
            return index              
        
def checkBookAvailability(Id,ListOfRentals):
    '''
    Function that checks whether a book is available for rental or not
    input: Id,ListOfRentals
    preconditions: Id should be an integer that exists in the list of books
    output: 0 or 1
    postconditions: If the book is available, ok will be 1,otherwise it will be 0
    '''
    validator=1
    for rental in ListOfRentals:
        if int(rental._Rental__bookId)==Id and rental._Rental__returnedDate=="":
            validator=0
    if validator == 0:
        raise ValueError("Unavailable book.")            

def findRentalIndex(Id,ListOfRentals):
    '''
    Function that finds the index of a rental in list
    input: Id, ListOfRentals
    preconditions: Id should be an existing integer in the list
    output: index
    postconditions:-
    '''
    for index in range(len(ListOfRentals)):
        if ListOfRentals[index]._Rental__rentalId==Id:
            return index     