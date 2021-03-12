'''
Created on 2 nov. 2018

@author: Revnic
'''  
from datetime import datetime
from book import *
from client import *
from rental import *
from _operator import index
def findBookById(Id,ListOfBooks):
    '''
    Function that finds a book in a list of books by its Id
    input: Id,ListOfBooks
    preconditions: Id should be an integer in the list
    output: myBook
    postconditions:-
    '''
    for book in ListOfBooks:
        if int(book._Book__Id)==Id:  
            myBook=Book(Id,book._Book__title,book._Book__description,book._Book__author)
            return myBook
        
def findClientById(Id,ListOfClients):  
    '''
    Function that finds a client in a list of clients by its Id
    input: Id,ListOfClients
    preconditions: Id should be an integer in the list
    output: myClient
    postconditions:-
    '''  
    for client in ListOfClients:
        if int(client._Client__Id)==Id:
            myClient=Client(Id,client._Client__name)
            return myClient                  
        
def findRentalById(Id,ListOfRentals):
    '''
    Function that finds a rental in a list of rentals by its Id
    input: Id,ListOfRentals
    preconditions: Id should be an integer in the list
    output: myRental
    postconditions:-
    '''  
    for rental in ListOfRentals:
        if rental._Rental__rentalId==Id:
            myRental=Rental(Id,rental._Rental__bookId,rental._Rental__clientId,rental._Rental__rentedDate,rental._Rental__dueDate,rental._Rental__returnedDate)
            return myRental
  
def uniqueBookId(Id,ListOfBooks):
    '''
    Function that checks whether a given Id already exists or not in a list of books
    input: Id, ListOfBooks
    preconditions: Id should be a string
    output:  -
    postconditions: If the Id already exists, an error will appear
    '''
    for book in ListOfBooks:
        if book._Book__Id==Id:
            raise ValueError("Existing Id")
        
def uniqueClientId(Id,ListOfClients):
    '''
    Function that checks whether a given Id already exists or not in a list of clients
    input: Id, ListOfClients
    preconditions: Id should be a string
    output:-
    postconditions: If athe Id already exists, an error will appear
    '''
    for client in ListOfClients:
        if client._Client__Id==Id:
            raise ValueError("Existing Id")
                         
def uniqueRentalId(Id,ListOfRentals):   
    '''
    Function that checks whether a given Id already exists or not in a list of rentals
    input: Id, ListOfRentals
    preconditions: Id should be a string
    output:-
    postconditions: If athe Id already exists, an error will appear
    '''                     
    for rental in ListOfRentals:
        if rental._Rental__rentalId==Id:
            raise ValueError("Existing Id")
         
def searchBookById(Id,ListOfBooks):
    '''
    Function that prints the book with the given Id
    input: Id,ListOfBooks
    preconditions: Id should be an integer
    output: the book with the given Id
    postconditions:-
    '''
    for book in ListOfBooks:
        if book._Book__Id==Id:
            print("Id:",Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)
                    
def searchBooksByTitle(title,ListOfBooks):
    '''
    Function that prints all the books with the given title
    input: title, ListOfBooks
    preconditions:-
    output: All the books with the given title
    postconditions:-
    '''
    title=title.lower()
    for book  in ListOfBooks:
        bookTitle=book._Book__title
        bookTitle=bookTitle.lower()
        if title in bookTitle:
            print("Id:",book._Book__Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)
             
def searchBooksByDescription(description,ListOfBooks):
    '''
    Function that prints all the books with the given description   
    input: description, ListOfBooks
    preconditions:-
    output: All the books with the given description
    postconditions: -
    '''
    description=description.lower()
    for book in ListOfBooks:
        bookDescription=book._Book__description
        bookDescription=bookDescription.lower()
        if description in bookDescription:
            print("Id:",book._Book__Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)
            
def searchBooksByAuthor(author, ListOfBooks):
    '''
    Function that prints all the books with the given author
    input: author, ListOfBooks
    preconditions:-
    output: All the books with the given author
    postconditions:-
    '''
    author=author.lower()
    for book in ListOfBooks:
        bookAuthor=book._Book__author
        bookAuthor=bookAuthor.lower()
        if author in bookAuthor:
            print("Id:",book._Book__Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)
            
def searchClientById(Id,ListOfClients):
    '''
    Function that prints the client with the given Id
    input: Id, ListOfClients
    preconditions: Id should be an integer
    output: The client with the given Id
    postconditions:-
    '''
    for client in ListOfClients:
        if client._Client__Id==Id:
            print("Id:",client._Client__Id," Name:",client._Client__name)
            
def searchClientsByName(name,ListOfClients):
    '''
    Function that prints the clients with the given name
    input: name, ListOfClients
    preconditions:-
    output: The clients with the given name
    postconditions:-
    '''
    name=name.lower()
    for client in ListOfClients:
        clientName=client._Client__name
        clientName=clientName.lower()
        if name in clientName:
            print("Id:",client._Client__Id," Name:",client._Client__name)
            
 
def findIndexOfRentedBook(Id,listOfRentedBooks):
    '''
    Function that finds the index of a rented book with the given Id
    input: Id, listOfRentedBooks
    preconditions:-
    output:index
    postconditions:-
    '''
    index=0
    while index < len(listOfRentedBooks):
        if listOfRentedBooks[index][0]==Id:
            return index      
        index=index+1      
        
def completeList(listOfRentedBooks,ListOfBooks,ListOfRentals):
    '''
    Function that completes the listOfRentedBooks with lists of length 3, containing the Id, the number of times a book has been rented and the number of days it has been rented for
    input: listOfRentedBooks,ListOfBooks,ListOfRentals
    preconditions:-
    output:-
    postconditions: The list will be complete
    '''                        
    for book in ListOfBooks:
        rentedBook=[book._Book__Id,0,0]
        listOfRentedBooks.append(rentedBook)   
    for rental in ListOfRentals:
        index=findIndexOfRentedBook(rental._Rental__bookId,listOfRentedBooks)   
        listOfRentedBooks[index][1]+=1
        rentedDate=rental._Rental__rentedDate.split(".")
        rentedDate[0]=int(rentedDate[0])
        rentedDate[1]=int(rentedDate[1])
        rentedDate[2]=int(rentedDate[2])
        if(rental._Rental__returnedDate==""):
            rentedDateOfBook=datetime(rentedDate[2],rentedDate[1],rentedDate[0])
            numberOfDays=datetime.now()-rentedDateOfBook
            listOfRentedBooks[index][2]+=int(numberOfDays.days)
        else:
            rentedDateOfBook=datetime(int(rentedDate[2]),int(rentedDate[1]),int(rentedDate[0]))
            returnedDate=rental._Rental__returnedDate.split(".")
            returnedDate[0]=int(returnedDate[0])
            returnedDate[1]=int(returnedDate[1])
            returnedDate[2]=int(returnedDate[2])
            returnedDateOfBook=datetime(returnedDate[2],returnedDate[1],returnedDate[0])
            numberOfDays=returnedDateOfBook-rentedDateOfBook        
            listOfRentedBooks[index][2]=listOfRentedBooks[index][2]+int(numberOfDays.days)
        
def printMostRentedBooks(listOfRentedBooks,ListOfBooks):
    '''
    Function that prints the books in the order they appear in listOfRentedBooks
    input: listOfRentedBooks, ListOfBooks
    preconditions:-
    output: The list of books
    postconditions:-
    '''
    for rentedBook in listOfRentedBooks:
        book=findBookById(rentedBook[0],ListOfBooks)
        print("Id:",book._Book__Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)            

def findIndexOfActiveClient(Id,listOfMostActiveClients):
    '''
    Function that finds the index of a client with the given Id
    input: Id, listOfMostActiveClients    
    preconditions: Id should exist in the given list
    output: index
    postconditions:-
    '''
    index=0
    while index <len(listOfMostActiveClients):
        if listOfMostActiveClients[index][0]==Id:
            return index
        index+=1
            
def completeListOfActiveClients(listOfMostActiveClients,ListOfClients,ListOfRentals):
    '''
    Function that completes the list of active clients with information concerning the number of days they have rented books for
    input: listOfMostActiveClients, ListOfClients, ListOfRentals
    preconditions:-
    output:-
    postconditions: The listOfMostActiveClients will be completed with information concerning the number of days the have rented books for
    '''
    for client in ListOfClients:
        activeClient=[client._Client__Id,0]
        listOfMostActiveClients.append(activeClient)
    for rental in ListOfRentals:
        index=findIndexOfActiveClient(rental._Rental__clientId,listOfMostActiveClients)
        rentedDateAsList=rental._Rental__rentedDate.split(".")
        
        rentedDateAsList[0]=int(rentedDateAsList[0])
        rentedDateAsList[1]=int(rentedDateAsList[1])
        rentedDateAsList[2]=int(rentedDateAsList[2])
        
        if(rental._Rental__returnedDate==""):
            rentedDateAsDate=datetime(rentedDateAsList[2],rentedDateAsList[1],rentedDateAsList[0])
            numberOfDays=datetime.now()-rentedDateAsDate
            listOfMostActiveClients[index][1]+=int(numberOfDays.days)
        else:
            rentedDateAsDate=datetime(rentedDateAsList[2],rentedDateAsList[1],rentedDateAsList[0])
            returnedDateAsList=rental._Rental__returnedDate.split(".")
            returnedDateAsDate=datetime(int(returnedDateAsList[2]),int(returnedDateAsList[1]),int(returnedDateAsList[0]))
            numberOfDays=returnedDateAsDate-rentedDateAsDate
            listOfMostActiveClients[index][1]+=int(numberOfDays.days)
            
def printMostActiveClients(listOfActiveClients,ListOfClients):
    '''
    Function that prints the clients in the order they appear in listOfActiveClients
    input: listOfActiveClients, ListOfClients
    preconditions:-
    output: the list of clients
    postconditions:-
    '''
    for activeClient in listOfActiveClients:
        client=findClientById(activeClient[0],ListOfClients)
        print("Id:",client._Client__Id," Name:",client._Client__name)
        
 
def findAuthorByName(name,listOfRentedAuthors):
    '''
    Function that finds the index of an author in a listOfRentedAuthor
    input: name, listOfRentedAuthors
    preconditions: name should exist in the list
    output: index
    postconditions:-
    '''
    index=0
    while index < len(listOfRentedAuthors):
        if listOfRentedAuthors[index][0]==name:
            return index
        index+=1
                
def completeListOfRentedAuthors(listOfRentedAuthors,ListOfBooks,ListOfRentals):
    '''
    Function that completes the list of rented author with the number of rentals their books have
    input: listOfRentedAuthors, ListOfBooks, ListOfRentals
    preconditions:-
    output:-
    postconditions: The list of rented authors will be completed
    '''
    for book in ListOfBooks:
        if(book._Book__author not in listOfRentedAuthors):
            rentedAuthor=[book._Book__author,0]
            listOfRentedAuthors.append(rentedAuthor)
    for rental in ListOfRentals:
        book=findBookById(rental._Rental__bookId, ListOfBooks)
        index=findAuthorByName(book._Book__author,listOfRentedAuthors)
        listOfRentedAuthors[index][1]+=1
        
                        
def printMostRentedAuthors(listOfRentedAuthors):
    '''
    Function that prints the authors, in descending order of their rented books
    input: listOfRentedAuthors, ListOfBooks
    preconditions:-
    output: the list of authors
    postconditions:-
    '''
    for rentedAuthor in listOfRentedAuthors:
        print(rentedAuthor[0])                       
        
def completeListOfLateRentals(listOfLateRentals,ListOfRentals):
    '''
    Function that completes the list of late rentals from the list of late rentals
    input: listOfLateRentals, ListOfRentals
    preconditions:-
    output:-
    postconditions: The list of late rentals will be completed
    '''
    for rental in ListOfRentals:
        if rental._Rental__returnedDate=="":
            dueDate=rental._Rental__dueDate.split(".")
            dueDateOfBook=datetime(int(dueDate[2]),int(dueDate[1]),int(dueDate[0]))
            numberOfDays=datetime.now()-dueDateOfBook
            lateRental=[rental._Rental__bookId,int(numberOfDays.days)]   
            listOfLateRentals.append(lateRental)     
            
def printListOfLateRentals(listOfLateRentals,ListOfBooks):
    '''
    Function that prints the list of books who are rented but not returned, and for which the current date has passed the due date
    input: listOfLateRentals, ListOfBooks
    preconditions:-
    output: the list of book who should be returned
    postconditions:-
    '''
    for lateRental in listOfLateRentals:
        book=findBookById(lateRental[0],ListOfBooks)
        print("Id:",book._Book__Id," Title:",book._Book__title," Description:",book._Book__description," Author:",book._Book__author)
        
                