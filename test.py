'''
Created on 1 nov. 2018    

@author: Revnic
'''
import unittest
from datetime import datetime
from book import Book
from client import Client
from rental import Rental
from helpers import uniqueBookId,uniqueClientId, findBookById, findRentalById, findClientById, findIndexOfRentedBook, findIndexOfActiveClient, completeList, completeListOfActiveClients, completeListOfRentedAuthors, findAuthorByName, completeListOfLateRentals,\
    uniqueRentalId
from validator import validateBookUpdate,validateClientUpdate,validateBookId,validateClientId,validateRentalId,validateDateValue
from repository import findBookIndex, findClientIndex, findRentalIndex, checkBookAvailability
from errors import ClientError,BookError
class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def testCreateBook(self):
        '''
        Function that checks whether a book object is created correctly or not
        input:-
        preconditions:-
        output:-
        postconditions: If a book object is incorrectly created, an error will appera
        '''
        book=Book(3,"Fancy name","Fancy description","Fancy author name")
        self.assertEqual(book._Book__getId(),3)
        self.assertEqual(book._Book__getTitle(),"Fancy name")
        self.assertEqual(book._Book__getDescription(),"Fancy description")
        self.assertEqual(book._Book__getAuthor(),"Fancy author name")
        
    
        book._Book__setId(5)
        self.assertEqual(book._Book__getId(),5)
        book._Book__setTitle("New title")
        self.assertEqual(book._Book__getTitle(),"New title")
        book._Book__setDescription("New description")
        self.assertEqual(book._Book__getDescription(),"New description")
        book._Book__setAuthor("New author")
        self.assertEqual(book._Book__getAuthor(),"New author")
    
    def testAddBook(self):
        '''
        Function that checks whether a book is added correctly to a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If the addition of a book is incorrectly implemented, an error will appear
        '''
        bookList=[]
        firstBook=Book(1,"Poezii","Volum ce cuprinde capodoperele poeziei eminesciene","Mihai Eminescu")
        secondBook=Book(2,"Poezii","Volum ce cuprinde capodoperele poeziei bacoviene","George Bacovia")
        thirdBook=Book(3,"Amintiri din copilarie","Povestiri inspirate din copilaria autorului","Ion Creanga")
        bookList.append(firstBook)
        bookList.append(secondBook)
        bookList.append(thirdBook)
        newBook=Book(4,"Cartof","Agricultura","Who knows")
        newBook._Book__addBook(bookList)
    
        anotherBookList=[]
        anotherBookList.append(firstBook)
        anotherBookList.append(secondBook)
        anotherBookList.append(thirdBook)
        anotherBookList.append(newBook)
        self.assertEqual(bookList,anotherBookList)            
                
    def testRemoveBook(self):
        '''
        Function that tests whether a book is removed correctly from a list or not(considering the case of an already empty list, or of a non-existent book).
        input:-
        preconditions:-
        output:-
        postconditions: If a book is not removed correctly, an error will appear.   
        '''
        book=Book(3,"jdk","shsjk","d")
        mylist=[book]
        book._Book__removeBook(mylist)
        self.assertEqual(mylist,[])             

    def testUpdateBook(self):
        '''
        Function that checks whether a book is updated correctly or not, without risking to create duplicates
        input:- 
        preconditions:-
        output:-
        postconditions: If the update of a book is incorrectly implemented, an error will appear
        '''
        mylist=[]
        book1=Book(3,"Love","Amazing","Doctor Love")
        book2=Book(2,"Curtains","A complete guide to curtains","Senor Draperie")
        book1._Book__addBook(mylist)
        book2._Book__addBook(mylist)
        book1._Book__updateBook(3,1,"A","B","C",mylist)
        
        self.assertEqual(book1._Book__getId(),1)
        self.assertEqual(book1._Book__getTitle(),"A")
        self.assertEqual(book1._Book__getDescription(),"B")
        self.assertEqual(book1._Book__getAuthor(),"C")    

    def testCreateClient(self):
        '''
        Function that checks whether a client is properly added to a list or not.
        input:-
        preconditions:-
        output:-
        postconditions: If the client is not added correctly, an error will appear.
        '''    
        client=Client(4,"Hagrid Fluffy")
        self.assertEqual(client._Client__getId(),4)
        self.assertEqual(client._Client__getName(),"Hagrid Fluffy")
    
        client._Client__setId(7)
        self.assertEqual(client._Client__getId(),7)
        client._Client__setName("Tinkerbell Fairydust")
        self.assertEqual(client._Client__getName(),"Tinkerbell Fairydust")
    def testAddClient(self):
        '''
        Function that checks whether a client is added correctly to the list or not
        input:-
        preconditions:-
        output:-
        postcondition: If a client is not added correctly, an error will appear.
        '''
        mylist=[]
        client=Client(3,"Luna Lovegood")
        client._Client__addClient(mylist) 
        self.assertEqual(mylist,[client])        
    
    def testRemoveClient(self):
        '''
        Function that checks whether a client is correctly removed from the list of clients or not
        input:-
        preconditions:-
        output:-
        postconditions: If the client is not removed correctly from the list, or the list is already empty, or the client isn't in the list, an error will appear.
        '''
        mylist=[]
        client=Client(4,"George Weasley")
        client._Client__addClient(mylist)
        client._Client__removeClient(mylist)
        self.assertEqual(mylist,[])   
    
    def testUpdateClient(self):                                        
        '''
        Function that checks whether a client is correctly updated or not.
        input:-
        preconditions:-
        output:-
        postconditions: If the client is not correctly updated, an error will appear.
        '''
        mylist=[]
        client=Client(5,"Cho Chang")
        client._Client__addClient(mylist)
        client._Client__updateClient(5,3,"Hermione Granger",mylist)
        self.assertEqual(client._Client__getId(),3)
        self.assertEqual(client._Client__getName(),"Hermione Granger")

    def testCreateRental(self):
        '''
        Function that checks whether a rental is correctly created or not
        input:-
        preconditions:-
        output:-
        postconditions: If the rental is incorrectly created, an error will appear
        '''
        rental=Rental(4,7,10,"12.09.2018","28.09.2018","19.10.2018")
        self.assertEqual(rental._Rental__getRentalId(),4)
        self.assertEqual(rental._Rental__getBookId(),7)
        self.assertEqual(rental._Rental__getClientId(),10)
        self.assertEqual(rental._Rental__getRentedDate(),"12.09.2018")
        self.assertEqual(rental._Rental__getDueDate(),"28.09.2018")
        self.assertEqual(rental._Rental__getReturnedDate(),"19.10.2018")
    
        rental._Rental__setRentalId(3)
        self.assertEqual(rental._Rental__getRentalId(),3)
        rental._Rental__setBookId(18)
        self.assertEqual(rental._Rental__getBookId(),18)
        rental._Rental__setClientId(22)
        self.assertEqual(rental._Rental__getClientId(),22)
        rental._Rental__setRentedDate("17.10.2018")
        self.assertEqual(rental._Rental__getRentedDate(),"17.10.2018")
        rental._Rental__setDueDate("24.10.2018")
        self.assertEqual(rental._Rental__getDueDate(),"24.10.2018")
        rental._Rental__setReturnedDate("28.10.2018")
        self.assertEqual(rental._Rental__getReturnedDate(),"28.10.2018")        
        
    def testUniqueBookId(self):
        '''
        Function that checks whether a book Id is correctly validated for its unicity or not
        input:-
        preconditions:-
        output:-
        postconditions: If the Id is not correctly validated, an error will appear
        '''
        myListOfBooks=[Book(1,"Title1","Cool","Walter"),Book(2,"Title2","Greatness in a book","Scott")]
        try:
            uniqueBookId(3,myListOfBooks)
            assert True
        except ValueError:
            assert False        
            
    def testUniqueClientId(self):
        '''
        Function that checks whether a client Id is correctly validated for its unicity or not
        input:-
        preconditions:-
        output:-
        postconditions: If the Id is not correctly validated, an error will appear
        '''
        myListOfClients=[Client(1,"Marcel"),Client(2,"Dan Petrescu"),Client(3,"Pele")]
        try:
            uniqueClientId(3,myListOfClients)
            assert False
        except ValueError:
            assert True           
            
    def testFindBookById(self):
        '''
        Function that checks whether a book Id is correctly found in a list
        input:-
        preconditions:-
        output:-
        postconditions: If the Id is not correctly found, an error will appear
        '''
        myListOfBooks=[Book(1,"Bonzai","Copacei","Autorul misterios"),Book(2,"Gardening 101","A book for those who can afford a garden, but not a gardener","Poor fellow")]
        thisBook=findBookById(2,myListOfBooks)
        myBook=Book(2,"Gardening 101","A book for those who can afford a garden, but not a gardener","Poor fellow")
        self.assertEqual(thisBook._Book__Id,myBook._Book__Id)
        self.assertEqual(thisBook._Book__title,myBook._Book__title)
        self.assertEqual(thisBook._Book__description,myBook._Book__description)
        self.assertEqual(thisBook._Book__author,myBook._Book__author)
        
    def testFindClientById(self):
        '''
        Function that checks whether a client Id is correctly found is a list
        input:-
        preconditions:-
        output:-
        postconditions: If the Id is not correctly found, an error will appear
        '''
        myListOfClients=[Client(1,"Pi Patel"),Client(2,"Tania Wundermann")]
        thisClient=findClientById(2,myListOfClients)
        myClient=Client(2,"Tania Wundermann")
        self.assertEqual(myClient._Client__Id,thisClient._Client__Id)
        self.assertEqual(myClient._Client__name,thisClient._Client__name)    
        
    def testFindRentalById(self):
        '''
        Function that checks whether a rental Id is correctly found in a list
        input:-
        preconditions:-
        output:-
        postconditions: If the Id is not correctly found, an error will appear
        '''
        myListOfRentals=[Rental(1,2,3,"10.11.2018","20.11.2018",""),Rental(2,5,4,"9.11.2018","19.11.2018","14.11.2018")]
        thisRental=findRentalById(1,myListOfRentals)
        myRental=Rental(1,2,3,"10.11.2018","20.11.2018","")
        self.assertEqual(thisRental._Rental__rentalId,myRental._Rental__rentalId)
        self.assertEqual(thisRental._Rental__bookId,myRental._Rental__bookId)
        self.assertEqual(thisRental._Rental__clientId,myRental._Rental__clientId)
        self.assertEqual(thisRental._Rental__rentedDate,myRental._Rental__rentedDate)
        self.assertEqual(thisRental._Rental__dueDate,myRental._Rental__dueDate)
        self.assertEqual(thisRental._Rental__returnedDate,myRental._Rental__returnedDate)   
        
    def testValidateBookUpdate(self):
        '''
        Function that checks whether a book duplicate is allowed to be added to a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If a book duplicate is allowed to be added to the list, an error will appear
        '''
        myListOfBooks=[Book(1,"gg","ff","ee"),Book(2,"dd","bb","ss")]
        try:
            validateBookUpdate(1,3,"gg","ff","ee",myListOfBooks)
            assert False
        except BookError:
            assert True          
            
        try:
            validateBookUpdate(2,4,"dd","bb","sse",myListOfBooks)
            assert True
        except ValueError:
            assert False            
            
    def testValidateClientUpdate(self):
        '''
        Function that checks whether a client duplicate is allowed to be added to a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If a client duplicate is allowed to be added to the list, an error will appear
        '''
        myListOfClients=[Client(1,"cartof pai"),Client(2,"barcuta mica")]
        try:
            validateClientUpdate(1,1,"strugure verde",myListOfClients)
            assert True
        except ClientError:
            assert False
         
    def testValidateBookId(self):
        '''
        Function that checks whether an Id is already in a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If the Id doesn't exist, an error will appear
        '''
        myListOfBooks=[Book(1,"d","a","s"),Book(2,"q","w","t")]
        try:
            validateBookId(2,myListOfBooks)
            assert True
        except ValueError:
            assert False
            
    def testValidateClientId(self):
        '''
        Function that checks whether a client Id is already in a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If the Id doesn't exist, an error will appear
        '''
        myListOfClients=[Client(1,"cartofior piure"),Client(2,"rosioara coapta")]
        try:
            validateClientId(3,myListOfClients)
            assert False
        except ClientError:
            assert True
            
    def testValidateRentalId(self):
        '''
        Function that checks whether a rental Id already exists in a list or not
        input:-
        preconditions:-
        output:-
        postconditions: If the id doesn't exist, an error will appear
        '''
        myListOfRentals=[Rental(1,3,2,"23.8.2018","28.8.2018",""),Rental(2,4,5,"12.9.2018","22.9.2018","")]
        try:
            validateRentalId(2,myListOfRentals)
            assert True
        except ValueError:
            assert False
            
    def testValidateDateValue(self):
        '''
        Function that checks whether a date is correctly validated or not
        input:-
        preconditions:-
        output:-
        postconditions: If the date is incorrectly validated, an error will appear
        '''
        date=[4,10]
        try:
            validateDateValue(date)
            assert True
        except ValueError:
            assert False
    
    def testFindBookIndex(self):
        '''
        Function that checks whether the index of a book with the given Id is correctly found in a list
        input:-
        preconditions:-
        output:-
        postconditions: If the index isn't correctly found, an error will appear
        '''
        myListOfBooks=[Book(1,"a","b","c"),Book(2,"d","e","f")]
        index=findBookIndex(2,myListOfBooks)
        self.assertEqual(index,1)
        
    def testFindClientIndex(self):
        '''
        Function that checks whether the index of a client with the given Id is correctly found in a list
        input:-
        preconditions:-
        output:-
        postconditions: If the index isn't correctly found, an error will appear
        '''
        myListOfClients=[Client(1,"test"),Client(2,"driven"),Client(3,"development")]
        index=findClientIndex(3,myListOfClients)
        self.assertEqual(index,2)
        
    def testFindRentalIndex(self):
        '''
        Function that checks whether the index of a rental with the given Id is correctly found in a list        
        input:-
        preconditions:-
        output:-
        postconditions: If the index isn't correctly found, an error will appear
        '''
        myListOfRentals=[Rental(1,2,4,"12.12.2017","12.1.2018","")]
        index=findRentalIndex(1,myListOfRentals)
        self.assertEqual(index,0)
        
    def testCheckBookAvailability(self):
        '''
        Function that checks whether the availability of a book is correctly found
        input:-
        preconditions:-
        output:-
        postconditions: If the availabilty is incorrectly interpreted, an error will appear
        '''
        myListOfRentals=[Rental(1,2,3,"1.1.2018","2.2.2018",""),Rental(2,4,3,"1.2.2018","2.3.2018","3.3.2018")]
        IdBook1=2
        IdBook2=4
        try:
            checkBookAvailability(IdBook1,myListOfRentals)
            assert False
        except ValueError:
            assert True
            
        try:
            checkBookAvailability(IdBook2,myListOfRentals)
            assert True
        except ValueError:
            assert False
               
    def testRentBook(self):
        '''
        Function that checks whether a book is correctly rented or not
        input:-
        preconditions:-
        output:-
        postconditions: If the book is rented incorrectly, an error will appear
        '''
        myListOfRentals=[Rental(1,3,2,"1.1.2018","2.2.2018",""),Rental(2,5,3,"2.3.2018","4.3.2018","5.3.2018")]
        myRental=Rental(3,2,4,"2.3.2018","4.4.2018","")
        myRental._Rental__rentBook(myListOfRentals)
        newList=[Rental(1,3,2,"1.1.2018","2.2.2018",""),Rental(2,5,3,"2.3.2018","4.3.2018","5.3.2018"),Rental(3,2,4,"2.3.2018","4.4.2018","")]
        self.assertEqual(myListOfRentals[2]._Rental__rentalId,newList[2]._Rental__rentalId)
        self.assertEqual(myListOfRentals[2]._Rental__bookId,newList[2]._Rental__bookId)
        self.assertEqual(myListOfRentals[2]._Rental__clientId,newList[2]._Rental__clientId)
        self.assertEqual(myListOfRentals[2]._Rental__rentedDate,newList[2]._Rental__rentedDate)
        self.assertEqual(myListOfRentals[2]._Rental__dueDate,newList[2]._Rental__dueDate)
        self.assertEqual(myListOfRentals[2]._Rental__returnedDate,newList[2]._Rental__returnedDate) 
        
    def testReturnBook(self):
        '''
        Function that checks whether a book is correctly returned or not
        input:-
        preconditions:-
        output:-
        postconditions: If the book is incorrectly returned, an error will appear
        '''
        myListOfRentals=[Rental(1,3,2,"1.1.2018","2.2.2018",""),Rental(2,5,3,"2.3.2018","4.3.2018","5.3.2018")]
        myRental=Rental(1,3,2,"1.1.2018","2.2.2018","")
        myRental._Rental__returnBook("3.2.2018",0,myListOfRentals)
        self.assertEqual(myListOfRentals[0]._Rental__returnedDate,"3.2.2018")    
        
    def testFindIndexOfRentedBook(self):
        '''
        Function that checks whether the index of a book with a given Id is correctly found in a list of rented books or not
        input:-
        preconditions:-
        output:-
        postconditions: If the index is incorrectly found, an error will appear
        '''
        myListOfRentedBooks=[[1,4,23],[2,2,60],[4,10,129]]
        index=findIndexOfRentedBook(2,myListOfRentedBooks)
        self.assertEqual(index,1)   
        
    def testCompleteList(self):
        '''
        Function that checks whether a list of rented books is correctly completed from the list of books and the list of rentals
        input:-
        preconditions:-
        output:-
        postconditions: If the list is incorrectly completed, an error will appear
        '''
        myListOfRentedBooks=[]
        myListOfBooks=[Book(1,"Enciclopedia tuturor","Multe informatii","Smart guy"),Book(2,"Romance at its finest","For the soft-hearted","Sensitive guy")]
        myListOfRentals=[Rental(1,2,3,"1.4.2018","5.4.2018",""),Rental(2,1,5,"2.3.2018","9.3.2018","15.3.2018"),Rental(3,2,1,"2.1.2018","5.1.2018","4.1.2018")]
        completeList(myListOfRentedBooks,myListOfBooks,myListOfRentals)
        self.assertEqual(myListOfRentedBooks[0][0],1)
        self.assertEqual(myListOfRentedBooks[0][1],1)
        self.assertEqual(myListOfRentedBooks[0][2],13)
        self.assertEqual(myListOfRentedBooks[1][0],2)
        self.assertEqual(myListOfRentedBooks[1][1],2)
        date=datetime.now()  
        numberOfDays=date-datetime(2018,4,1)
        self.assertEqual(myListOfRentedBooks[1][2],int(numberOfDays.days) + 2)
        
    def testFindIndexOfActiveClient(self):
        '''
        Function that checks whether the index of a client with the given Id is correctly found or not
        input:-
        preconditions:-
        output:-
        postconditions: If the index isn't correctly found, an error will appear
        '''
        myListOfActiveClients=[[1,24],[2,78],[4,89]]
        index=findIndexOfActiveClient(2,myListOfActiveClients)
        self.assertEqual(index,1)
        
    def testCompleteListOfActiveClients(self):
        '''
        Function that checks whether a list of active clients is correctly completed, relying on the list of clients and the list of rentals    
        input:-
        preconditions:-
        output:-
        postconditions: If the list is incorrectly completed, an error will appear
        '''
        myListOfActiveClients=[] 
        myListOfClients=[Client(1,"ABC"),Client(2,"def")]
        myListOfRentals=[Rental(1,4,2,"1.4.2018","3.4.2018","5.4.2018"),Rental(2,3,1,"2.1.2018","10.1.2018","14.1.2018")]
        completeListOfActiveClients(myListOfActiveClients,myListOfClients,myListOfRentals)
        self.assertEqual(myListOfActiveClients[0][0],1)
        self.assertEqual(myListOfActiveClients[0][1],12)
        self.assertEqual(myListOfActiveClients[1][0],2)
        self.assertEqual(myListOfActiveClients[1][1],4)
        
    def testFindAuthorByName(self):
        '''
        Function that checks whether the index of an author is correctly found in a list
        input:-
        preconditions:-
        output:-
        postconditions: If the index isn't correctly found, an error will appear
        '''
        myListOfRentedAuthors=[["O persoana misterioasa",5],["A mysterious person",9]]
        name="O persoana misterioasa"
        index=findAuthorByName(name,myListOfRentedAuthors)
        self.assertEqual(index,0)
        
    def testCompleteListOfRentedAuthors(self):
        '''
        Function that checks whether a list of rented authors is correctly completed, based on the list of books and the list of rentals
        input:-
        preconditions:-
        output:-
        postconditions: If the list is not completed correctly, an error will appear
        '''
        myListOfRentedAuthors=[]
        myListOfBooks=[Book(1,"a","b","c"),Book(2,"d","e","f")]
        myListOfRentals=[Rental(1,2,4,"2.3.2018","16.3.2018",""),Rental(2,1,3,"1.2.2018","19.2.2018","21.2.2018")]
        completeListOfRentedAuthors(myListOfRentedAuthors,myListOfBooks,myListOfRentals)
        self.assertEqual(myListOfRentedAuthors[0][0],"c")
        self.assertEqual(myListOfRentedAuthors[0][1],1)
        self.assertEqual(myListOfRentedAuthors[1][0],"f")
        self.assertEqual(myListOfRentedAuthors[1][1],1)         
        
    def testCompleteListOfLateRentals(self):
        '''
        Function that checks whether a list of late rentals is correctly completed or not
        input:-
        preconditions:-
        output:-
        postconditions: If the list isn't correctly completed, an error will appear
        '''
        myListOfLateRentals=[]
        myListOfRentals=[Rental(1,2,3,"2.1.2018","8.1.2018",""),Rental(2,5,4,"2.5.2018","4.5.2018","5.5.2018")]
        completeListOfLateRentals(myListOfLateRentals,myListOfRentals)
        self.assertEqual(myListOfLateRentals[0][0],2)
        numberOfDays=datetime.now()-datetime(2018,1,8)
        self.assertEqual(myListOfLateRentals[0][1],int(numberOfDays.days))
        
    def testUniqueRentalId(self):
        '''
        Function that checks whether a function correctly validates a new Id, in order to avoid duplicates
        input:-
        preconditions:-
        output:-
        postconditions: If the Id isn't validated correctly, an error will appear
        '''
        myListOfRentals=[Rental(1,2,3,"1.1.1","2.2.2","")]
        try:
            uniqueRentalId(2,myListOfRentals)
            assert True
        except ValueError:
            assert False        
    def testAddBookToIndex(self):
        '''
        Function that checks whether a book is correctly inserted in a list or nah
        input:-
        preconditions:-
        output:-
        postconditions: If the book isn't correctly inserted, an error will appear
        '''
        myListOfBooks=[Book(1,"a","b","c"),Book(3,"g","h","i")]
        myBook=Book(2,"d","e","f")
        index=[1]
        myBook._Book__addBookToIndex(index,myListOfBooks)
        self.assertEqual(myListOfBooks[1]._Book__Id,2)
        self.assertEqual(myListOfBooks[1]._Book__title,"d")
        self.assertEqual(myListOfBooks[1]._Book__description,"e")
        self.assertEqual(myListOfBooks[1]._Book__author,"f")    
        
    def testAddClientToIndex(self):
        '''
        Function that checks whether a client is correctly inserted in a list or nah
        input:-
        preconditions:-
        output:-
        postconditions: If the client isn't correctly inserted, an error will appear
        '''
        myListOfClients=[Client(1,"Uno"),Client(3,"Tres")]
        myClient=Client(2,"Dos")
        index=[1]
        myClient._Client__addClientToIndex(index,myListOfClients)
        self.assertEqual(myListOfClients[1]._Client__Id,2)
        self.assertEqual(myListOfClients[1]._Client__name,"Dos")
        
    def testAddRentalToIndex(self):
        '''
        Function that checks whether a rental is correctly inserted in a list or nott
        input:-
        preconditions:-
        output:-
        postconditions: If the rental isn't correctly inserted, an error will appear
        '''
        myListOfRentals=[Rental(1,2,1,"1.1.1","2.2.2",""),Rental(3,2,1,"2.2.2","3.3.3","")]
        myRental=Rental(2,3,2,"1.1.1","3.3.3","")
        index=[1]
        myRental._Rental__addRentalToIndex(index,myListOfRentals)
        self.assertEqual(myListOfRentals[1]._Rental__rentalId,2)
        self.assertEqual(myListOfRentals[1]._Rental__bookId,3)
        self.assertEqual(myListOfRentals[1]._Rental__clientId,2)
        self.assertEqual(myListOfRentals[1]._Rental__rentedDate,"1.1.1")
        self.assertEqual(myListOfRentals[1]._Rental__dueDate,"3.3.3")
        self.assertEqual(myListOfRentals[1]._Rental__returnedDate,"")       
        
        
if __name__=="__main__":
    unittest.main()        