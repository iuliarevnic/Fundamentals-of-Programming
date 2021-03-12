'''
Created on 1 nov. 2018

@author: Revnic
'''
from myRepository import Repository
from copy import copy
from operator import itemgetter
from book import *
from client import *
from errors import *
from helpers import *
from validator import *
from rental import *
from repository import findRentalIndex
from copy import deepcopy
from DataStructure import shellSort
class command():
    def __init__(self):
        self.__commands=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    def __displayMenu(self):
        
        print("1.Add book.")  
        print("2.Remove book.")
        print("3.Update book.")
        print("4.List books.")
        print("5.Add client.")
        print("6.Remove client.")
        print("7.Update client.")
        print("8.List clients.")
        print("9.Rent book.")
        print("10.Return book.")
        print("11.Search book")
        print("12.Search client")
        print("13.Most rented books")
        print("14.Most active clients")
        print("15.Most rented authors")
        print("16.Late rentals")
        print("17.List rentals")
        print("18.Undo")
        print("19.Redo")
        print("20.Exit")
        
    def __addBook(self,Books,ListOfBooks,listOfBookAttributes,undoOption,countBook,listOfBookAttributesRedo,bookIndexRedo,redoOption,storage):
        
        try:    
            Id=int(input("Please give Id:"))
            title=input("Please give title:")
            description=input("Please give description:")
            author=input("Please give author:")
            book=Book(Id,title,description,author)
            try:
                
                uniqueBookId(Id,ListOfBooks)
                try:
                    book._Book__addBook(ListOfBooks)
                    listOfBookAttributes.append(Id)
                    listOfBookAttributes.append(title)
                    listOfBookAttributes.append(description)
                    listOfBookAttributes.append(author)
                    listOfBookAttributesRedo.append(Id)
                    listOfBookAttributesRedo.append(title)
                    listOfBookAttributesRedo.append(description)
                    listOfBookAttributesRedo.append(author)
                    undoOption.append(1)
                    countBook[0]+=1
                    redoOption.append(1)
                    bookIndexRedo.append(len(ListOfBooks)-1)
                    if storage==1:
                        Books._BookRepository__list=ListOfBooks.copy()
                        Books._BookRepository__uploadBooksToFile()
                    if storage==2:
                        Books._PickleRepository__data=ListOfBooks.copy()
                        Books._PickleRepository__storeToFile()
                except BookError as bookError:
                    print(bookError)
            except ValueError as valueError:
                print(valueError)        
        except ValueError:
            print("Please give integer.")        
    
           
    def __removeBook(self,Books,ListOfBooks,listOfBookAttributes,index,undoOption,countBook,listOfBookAttributesRedo,redoOption,storage):
        
        
        try:    
            Id=int(input("Please give Id:"))      
            try:
                validateBookId(Id,ListOfBooks)
                book=findBookById(Id,ListOfBooks)
                myIndex=findBookIndex(Id,ListOfBooks)
                index.append(myIndex)
                try: 
                    book._Book__removeBook(ListOfBooks)
                    listOfBookAttributes.append(Id)
                    listOfBookAttributes.append(book._Book__title)
                    listOfBookAttributes.append(book._Book__description)
                    listOfBookAttributes.append(book._Book__author)
                    listOfBookAttributesRedo.append(book._Book__Id)
                    listOfBookAttributesRedo.append(book._Book__title)
                    listOfBookAttributesRedo.append(book._Book__description)
                    listOfBookAttributesRedo.append(book._Book__author)
                    undoOption.append(2)
                    countBook[0]+=1
                    redoOption.append(2)
                    if storage==1:
                        Books._BookRepository__list=ListOfBooks.copy()
                        Books._BookRepository__uploadBooksToFile()

                    if storage==2:
                        Books._PickleRepository__data=ListOfBooks.copy()
                        Books._PickleRepository__storeToFile()
                except BookError as bookError:
                    print(bookError)             
            except BookError as bookError:
                print(bookError)  
        except ValueError:
            print("Please give integer.")
                   
    def __updateBook(self,Books,ListOfBooks,listOfBookAttributes,oldBookId,undoOption,countBook,listOfBookAttributesRedo,redoOption,newBookId,storage):
        
        
        try:    
            Id=int(input("Please give current Id:"))
            try:
                validateBookId(Id,ListOfBooks)
                book=findBookById(Id,ListOfBooks)
                oldId=Id
                try:    
                    Id=int(input("Please give updated Id:"))
                    title=input("Please give updated title:")
                    description=input("Please give updated description:")
                    author=input("Please give updated author:")
                    try:
                        validateBookUpdate(oldId,Id, title, description, author, ListOfBooks)
                        listOfBookAttributes.append(book._Book__Id)
                        listOfBookAttributes.append(book._Book__title)
                        listOfBookAttributes.append(book._Book__description)
                        listOfBookAttributes.append(book._Book__author)
                        book._Book__updateBook(oldId,Id,title,description,author,ListOfBooks)
                        listOfBookAttributesRedo.append(Id)
                        listOfBookAttributesRedo.append(title)
                        listOfBookAttributesRedo.append(description)
                        listOfBookAttributesRedo.append(author)
                        oldBookId.append(Id)
                        undoOption.append(3)
                        countBook[0]+=1
                        redoOption.append(3)
                        newBookId.append(oldId)
                        if storage==1:
                            Books._BookRepository__list=ListOfBooks.copy()
                            Books._BookRepository__uploadBooksToFile()
                        if storage==2:
                            Books._PickleRepository__data=ListOfBooks.copy()
                            Books._PickleRepository__storeToFile()
                    except BookError as bookError:
                            print(bookError)    
                except ValueError:
                    print("Please give integer.")              
            except BookError as bookError:
                print(bookError)
        except ValueError:
            print("Please give integer.")
                                
                            
                
    def __listBook(self,ListOfBooks):
        '''
        Function that raises an error if the list to be printed is empty, otherwise it calls a book class method to print the list of books
        input: self, ListOfBooks
        preconditions:-
        output: The list of books
        postconditions: If the list of books is empty, the function raises an error
        '''
        book=Book(0,"","","") 
        try:
            book._Book__listBook(ListOfBooks)
        except BookError as bookError:
            print(bookError)
            
    def __addClient(self,Clients,ListOfClients,listOfClientAttributes,undoOption,countClient,listOfClientAttributesRedo,clientIndexRedo,redoOption,storage):
        
      
        try:    
            Id=int(input("Please give Id:"))
            name=input("Please give name")
            client=Client(Id,name)
            try:
                uniqueClientId(Id,ListOfClients)
                try:    
                    client._Client__addClient(ListOfClients)
                    listOfClientAttributes.append(Id)
                    listOfClientAttributes.append(name)
                    listOfClientAttributesRedo.append(Id)
                    listOfClientAttributesRedo.append(name)
                    undoOption.append(4)
                    countClient[0]+=1
                    redoOption.append(4)
                    clientIndexRedo.append(len(ListOfClients)-1)
                    if storage==1:
                        Clients._ClientRepository__list=ListOfClients.copy()
                        Clients._ClientRepository__uploadClientsToFile()
                    if storage==2:
                        Clients._PickleRepository__data=ListOfClients.copy()
                        Clients._PickleRepository__storeToFile()
                except ClientError as clientError:
                    print(clientError)
            except ValueError as valueError:
                print(valueError)        
        except ValueError:
            print("Please give integer.")  
            
    def __removeClient(self,Clients,ListOfClients,listOfClientAttributes,index,undoOption,countClient,listOfClientAttributesRedo,redoOption,storage):
        
       
        try:    
            Id=int(input("Please give Id:"))
            try:
                validateClientId(Id,ListOfClients)
                client=findClientById(Id,ListOfClients)
                myIndex=findClientIndex(Id,ListOfClients)
                index.append(myIndex)
                try:
                    client._Client__removeClient(ListOfClients)
                    listOfClientAttributes.append(client._Client__Id)
                    listOfClientAttributes.append(client._Client__name)
                    listOfClientAttributesRedo.append(client._Client__Id)
                    listOfClientAttributesRedo.append(client._Client__name)
                    undoOption.append(5)
                    countClient[0]+=1
                    redoOption.append(5)
                    if storage==1:
                        Clients._ClientRepository__list=ListOfClients.copy()
                        Clients._ClientRepository__uploadClientsToFile()
                    if storage==2:
                        Clients._PickleRepository__data=ListOfClients.copy()
                        Clients._PickleRepository__storeToFile()
                except ClientError as clientError:
                    print(clientError)
            except ClientError as clientError:
                print(clientError)
        except ValueError:
            print("Please give integer.")                  
                              
    def __updateClient(self,Clients,ListOfClients,listOfClientAttributes,oldClientId,undoOption,countClient,listOfClientAttributesRedo,redoOption,newClientId,storage):

     
        try:
            Id=int(input("Please give current Id:"))
            try:
                validateClientId(Id,ListOfClients)
                client=findClientById(Id,ListOfClients)
                oldId=Id
                try:    
                    Id=int(input("Please give updated Id:"))
                    name=input("Please give updated name:")
                    try:
                        validateClientUpdate(oldId,Id, name, ListOfClients)
                        listOfClientAttributes.append(client._Client__Id)
                        listOfClientAttributes.append(client._Client__name)
                        client._Client__updateClient(oldId,Id,name,ListOfClients)
                        listOfClientAttributesRedo.append(Id)
                        listOfClientAttributesRedo.append(name)
                        oldClientId.append(Id)
                        undoOption.append(6)
                        countClient[0]+=1
                        redoOption.append(6)
                        newClientId.append(oldId)
                        if storage==1:
                            Clients._ClientRepository__list=ListOfClients.copy()
                            Clients._ClientRepository__uploadClientsToFile()
                        if storage==2:
                            Clients._PickleRepository__data=ListOfClients.copy()
                            Clients._PickleRepository__storeToFile()
                    except ClientError as clientError:    
                        print (clientError)
                except ValueError:
                    print("Please give integer.")  
            except ClientError as clientError:
                print(clientError)
        except ValueError:
            print("Please give integer.")                    
        
    def __listClient(self,ListOfClients):  
        
        '''
        Function that raises an error if the list to be printed is empty, otherwise it calls a client class method to print the list of books
        input: self, ListOfClients
        preconditions:-
        output: The list of clients
        postconditions: If the list of clients is empty, the function raises an error
        '''
        client=Client(0,"")
        try:
            client._Client__listClient(ListOfClients)
        except ClientError as clientError:
            print(clientError)
    
    def __rentBook(self,Rentals,ListOfRentals,listOfRentalAttributes,undoOption,countRental,listOfRentalAttributesRedo,rentalIndexRedo,redoOption,storage):
        
        try:
            rentalId=int(input("Please give rental Id:"))
            try:
                bookId=int(input("Please give book Id:"))
                try:
                    checkBookAvailability(bookId, ListOfRentals)
                    try:
                        clientId=int(input("Please give client Id:"))
                        command=input("Please give rented date:")
                        rentedDate=command.split(".")
                        try:
                            rentedDate[0]=int(rentedDate[0])
                            try:
                                rentedDate[1]=int(rentedDate[1])
                                try:
                                    rentedDate[2]=int(rentedDate[2])
                                    myRentedDate=command
                                    try:
                                        validateDateValue(rentedDate)
                                        command=input("Please give due date:")
                                        dueDate=command.split(".")
                                        try:
                                            dueDate[0]=int(dueDate[0])
                                            try:
                                                dueDate[1]=int(dueDate[1])
                                                try:
                                                    dueDate[2]=int(dueDate[2])
                                                    myDueDate=command
                                                    try:
                                                        validateDateValue(dueDate)
                                                        rental=Rental(rentalId,bookId,clientId,myRentedDate,myDueDate,"")
                                                        try: 
                                                            uniqueRentalId(rentalId,ListOfRentals)
                                                            try:
                                                                rental._Rental__rentBook(ListOfRentals)    
                                                                listOfRentalAttributes.append(rentalId)
                                                                listOfRentalAttributes.append(bookId)
                                                                listOfRentalAttributes.append(clientId)
                                                                listOfRentalAttributes.append(myRentedDate)
                                                                listOfRentalAttributes.append(myDueDate)
                                                                listOfRentalAttributes.append("")
                                                                listOfRentalAttributesRedo.append(rentalId)
                                                                listOfRentalAttributesRedo.append(bookId)
                                                                listOfRentalAttributesRedo.append(clientId)
                                                                listOfRentalAttributesRedo.append(myRentedDate)
                                                                listOfRentalAttributesRedo.append(myDueDate)
                                                                listOfRentalAttributesRedo.append("")
                                                                indexRedo=findRentalIndex(rentalId, ListOfRentals)
                                                                rentalIndexRedo.append(indexRedo)
                                                                undoOption.append(7)
                                                                countRental[0]+=1
                                                                redoOption.append(7)
                                                                if storage==1:
                                                                    Rentals._RentalRepository__list=ListOfRentals.copy()
                                                                    Rentals._RentalRepository__uploadRentalsToFile()
                                                                if storage==2:
                                                                    Rentals._PickleRepository__data=ListOfRentals.copy()
                                                                    Rentals._PickleRepository__storeToFile()
                                                            except ValueError as valueError:
                                                                print(valueError)    
                                                        except ValueError as valueError:
                                                            print(valueError)
                                                    except DateError as dateError:
                                                        print(dateError)
                                                except ValueError:
                                                    print("Please give integer value for year.")        
                                            except ValueError:
                                                print("Please give integer value for month.")            
                                        except ValueError:
                                            print("Please give integer value for day.")  
                                    except DateError as dateError:
                                        print(dateError)
                                except ValueError:
                                    print("Please give integer value for year.")        
                            except ValueError:
                                print("Please give integer value for month.")            
                        except ValueError:
                            print("Please give integer value for day.")    
                    except ValueError:
                        print("Please give integer.")    
                except ValueError as valueError:
                    print(valueError)       
            except ValueError:
                print("Please give integer.")    
        except ValueError:
            print("Please give integer.")     
    
    def __returnBook(self,Rentals,ListOfRentals,myRentalId,undoOption,countReturnedDate,returnedDateRedo,rentalIdRedo,redoOption,storage):
        
        try:
            rentalId=int(input("Give rental Id."))
            try:
                validateRentalId(rentalId, ListOfRentals)
                rental=findRentalById(rentalId,ListOfRentals)
                command=input("Please give returned date.")
                returnedDate=command.split(".")
                try:
                    returnedDate[0]=int(returnedDate[0])
                    try:
                        returnedDate[1]=int(returnedDate[1])
                        try:
                            returnedDate[2]=int(returnedDate[2])
                            myReturnedDate=command
                            index=findRentalIndex(rentalId,ListOfRentals)
                            rental._Rental__returnBook(myReturnedDate,index,ListOfRentals)
                            myRentalId.append(rentalId)
                            returnedDateRedo.append(myReturnedDate)
                            rentalIdRedo.append(rentalId)
                            undoOption.append(8)
                            countReturnedDate[0]+=1
                            redoOption.append(8)
                            if storage==1:
                                Rentals._RentalRepository__list=ListOfRentals.copy()
                                Rentals._RentalRepository__uploadRentalsToFile()
                            if storage==2:
                                Rentals._PickleRepository__data=ListOfRentals.copy()
                                Rentals._PickleRepository__storeToFile()
                        except ValueError:
                            print("Please give integer value for year.")    
                    except ValueError:
                        print("Please give integer value for month.")    
                except ValueError:
                    print("Please give integer value for day.")
            except RentalError as rentalError:
                print(rentalError)            
        except ValueError:
            print("Please give integer value for Id.")     
    def __printRentals(self,ListOfRentals):
        
        for rental in ListOfRentals:
            print("Rental Id:",rental._Rental__rentalId," Book Id:",rental._Rental__bookId," Client Id:",rental._Rental__clientId," Rented Date:",rental._Rental__rentedDate," Due date:",rental._Rental__dueDate," Returned date:",rental._Rental__returnedDate)                                          
    def __printBookMenu(self):
        print("a)search by Id")
        print("b)search by title")
        print("c)search by description")
        print("d)search by author")
        
    def __searchBookById(self,ListOfBooks):
        
        try:
            Id=int(input("Please give Id"))
            try:
                validateBookId(Id, ListOfBooks)
                searchBookById(Id,ListOfBooks)
            except BookError as bookError:
                print(bookError)
        except ValueError:
            print("Please give integer for Id.")   
                 
    def __searchBookByTitle(self,ListOfBooks):
        
        title=input("Please give title")
        searchBooksByTitle(title,ListOfBooks)
        
    def __searchBookByDescription(self,ListOfBooks):
        
        description=input("Please give description")
        searchBooksByDescription(description,ListOfBooks)
        
    def __searchBookByAuthor(self,ListOfBooks):
        
        author=input("Please give author")
        searchBooksByAuthor(author,ListOfBooks) 
                            
    def __searchBook(self,ListOfBooks):
        
        self.__printBookMenu()
        choice=input("Please choose a searching method.")
        if(choice=="a"):
            self.__searchBookById(ListOfBooks)
        elif(choice=="b"):
            self.__searchBookByTitle(ListOfBooks)
        elif(choice=="c"):
            self.__searchBookByDescription(ListOfBooks)
        elif(choice=="d"):
            self.__searchBookByAuthor(ListOfBooks)
        else:
            print("Please choose correctly.")
        
    def __printClientMenu(self):
        
        print("a)search by Id")
        print("b)search by name")
        
    def __searchClientById(self,ListOfClients):
        
        try:
            Id=int(input("Please give Id"))
            try:
                validateClientId(Id,ListOfClients)
                searchClientById(Id,ListOfClients)
            except ClientError as clientError:
                print(clientError) 
        except ValueError:
            print("Please give integer")            
    
    def __searchClientByName(self,ListOfClients):
        
        name=input("Please give name")
        searchClientsByName(name,ListOfClients)
                               
    def __searchClient(self,ListOfClients):
        
        self.__printClientMenu()
        choice=input("Please choose a searching method")
        if(choice=="a"):
            self.__searchClientById(ListOfClients)
        elif (choice=="b"):
            self.__searchClientByName(ListOfClients)
        else:
            print("Please choose correctly")
     
    def __mostRentedBooks(self,ListOfBooks,ListOfRentals):
        '''
        Function that sorts and prints books in the order of most rented to least rented
        input: self,ListOfBooks, ListOfRentals
        preconditions:-
        output: The list of books
        postconditions:-
        '''
        listOfRentedBooks=[]
        completeList(listOfRentedBooks,ListOfBooks,ListOfRentals)
        #listOfRentedBooks.sort(key=itemgetter(1,2),reverse=True)
        def condition(firstList,secondList):
            if(firstList[1]>secondList[1]):
                return 1
            elif (firstList[1]==secondList[1]):
                if(firstList[2]>=secondList[2]):
                    return 1
                else:
                    return 0
            else:
                return 0
        shellSort(listOfRentedBooks,condition)        
        printMostRentedBooks(listOfRentedBooks,ListOfBooks)
                          
    def __mostActiveClients(self,ListOfClients,ListOfRentals):
        '''
        Function that sorts and prints the clients in the order of most active to least active
        input: self,ListOfClients, ListOfRentals
        preconditions:-
        output: the list of clients
        postconditions:-
        '''
        listOfActiveClients=[]
        completeListOfActiveClients(listOfActiveClients,ListOfClients,ListOfRentals)
        listOfActiveClients.sort(key=itemgetter(1),reverse=True)
        def condition(firstList,secondList):
            if firstList[1]>=secondList[1]:
                return 1
            else:
                return 0
        shellSort(listOfActiveClients,condition)    
        printMostActiveClients(listOfActiveClients,ListOfClients)
       
    def __mostRentedAuthors(self,ListOfBooks,ListOfRentals):
        '''
        Function that sorts and prints the list of authors, in the order of most rented to least rented
        input: self,ListOfBooks, ListOfRentals
        preconditions:-
        output: The list of authors
        postconditions:-
        '''
        listOfRentedAuthors=[]
        completeListOfRentedAuthors(listOfRentedAuthors,ListOfBooks,ListOfRentals)
        #listOfRentedAuthors.sort(key=itemgetter(1),reverse=True)
        def condition(firstList,secondList):
            if(firstList[1]>=secondList[1]):
                return 1
            else:
                return 0
        shellSort(listOfRentedAuthors,condition)    
        printMostRentedAuthors(listOfRentedAuthors)
                           
    def __lateRentals(self,ListOfBooks,ListOfRentals):
        '''
        Function that sorts and prints the list of books, starting from the most late rental
        input: self,ListOfBooks, ListOfRentals
        preconditions:-
        output: List of books that have late rentals
        postconditions:-
        '''
        listOfLateRentals=[]
        completeListOfLateRentals(listOfLateRentals,ListOfRentals)
        #listOfLateRentals.sort(key=itemgetter(1), reverse=True)
        def condition(firstList,secondList):
            if firstList[1]>=secondList[1]:
                return 1
            else:
                return 0
        shellSort(listOfLateRentals,condition)    
        printListOfLateRentals(listOfLateRentals,ListOfBooks)
        
    def __undoBook(self,Books,undoOption,book,ListOfBooks,index,oldBookId,storage):
        '''
        Function that performs undo for the addition, removal and update of a book
        input: self,undoOption, book, ListOfBooks, index
        preconditions: undoOption, book, ListOfBooks, index
        output:-
        postconditions:-
        '''
        if undoOption==1:
            book._Book__removeBook(ListOfBooks)
        elif undoOption==2:
            book._Book__addBookToIndex(index,ListOfBooks)
            del index[-1]
        elif undoOption==3:
            book._Book__updateBook(oldBookId[len(oldBookId)-1],book._Book__Id,book._Book__title,book._Book__description,book._Book__author,ListOfBooks)            
            del oldBookId[-1]
        if storage==1:
                Books._BookRepository__list=ListOfBooks.copy()
                Books._BookRepository__uploadBooksToFile()
        if storage==2:
                Books._PickleRepository__data=ListOfBooks.copy()
                Books._PickleRepository__storeToFile()    
             
    def __undoClient(self,Clients,undoOption,client,ListOfClients,index,oldClientId,storage):
        '''
        Function that performs undo for the addition, removal and update of a client in a list
        input: self, undoOption, client, ListOfClients, index
        preconditions:-
        output:-
        postconditions:-
        '''
        if (undoOption==4):
            client._Client__removeClient(ListOfClients)
        elif(undoOption==5):
            client._Client__addClientToIndex(index,ListOfClients)
            del index[-1]
        elif(undoOption==6):
            client._Client__updateClient(oldClientId[len(oldClientId)-1],client._Client__Id,client._Client__name,ListOfClients)        
            del oldClientId[-1]
        if storage==1:
                Clients._ClientRepository__list=ListOfClients.copy()
                Clients._ClientRepository__uploadClientsToFile()
        if storage==2:
                Clients._PickleRepository__data=ListOfClients.copy()
                Clients._PickleRepository__storeToFile()    
    def __undoRental(self,Rentals,rental,ListOfRentals,storage):
        '''
        Function that remove a rental from a list when the user wants to undo a rental's addition to the list
        input: self, rental, ListOfRentals
        preconditions:-
        output:-
        postconditions:-
        '''
        ListOfRentals.remove(rental)
        if storage==1:
                Rentals._RentalRepository__list=ListOfRentals.copy()
                Rentals._RentalRepository__uploadRentalsToFile()
        if storage==2:
                Rentals._PickleRepository__data=ListOfRentals.copy()
                Rentals._PickleRepository__storeToFile()   
    def __undoReturnedDate(self,Rentals,rentalId,ListOfRentals,storage):
        '''
        Function that undo the change of the returned date of a book in a list of rentals
        input: self, rental, ListOfRentals
        preconditions:-
        output:-
        postconditions:-
        '''
        index=0
        while index <len(ListOfRentals):
            if(ListOfRentals[index]._Rental__rentalId==rentalId[0]):
                ListOfRentals[index]._Rental__returnedDate=""   
            index=index+1    
        if storage==1:
                Rentals._RentalRepository__list=ListOfRentals.copy()
                Rentals._RentalRepository__uploadRentalsToFile()
        if storage==2:
                Rentals._PickleRepository__data=ListOfRentals.copy()
                Rentals._PickleRepository__storeToFile()      
    def __redoBook(self,Books,undoOption,book,ListOfBooks,index,oldBookId,storage):
        '''
        Function that redoes the last operation performed on a book
        input: self,undoOption,book,ListOfBooks,index,oldBookId
        preconditions:-
        output:-
        postconditions:-
        '''
        if undoOption==1:
            book._Book__addBookToIndex(index,ListOfBooks)
            del index[-1]
        elif undoOption==2:
            book._Book__removeBook(ListOfBooks)
        elif undoOption==3:
            book._Book__updateBook(oldBookId[len(oldBookId)-1],book._Book__Id,book._Book__title,book._Book__description,book._Book__author,ListOfBooks)                
            del oldBookId[-1]
        if storage==1:
                Books._BookRepository__list=ListOfBooks.copy()
                Books._BookRepository__uploadBooksToFile()
        if storage==2:
                Books._PickleRepository__data=ListOfBooks.copy()
                Books._PickleRepository__storeToFile()    
    def __redoClient(self,Clients,undoOption,client,ListOfClients,index,oldClientId,storage):
        '''
        Function that redoes the last operation performed on a client
        input: self,undoOption,client,ListOfClients,index,oldClientId
        preconditions:-
        output:-
        postconditions:-
        '''
        if undoOption==4:
            client._Client__addClientToIndex(index,ListOfClients)
            del index[-1]
        elif undoOption==5:
            client._Client__removeClient(ListOfClients)
        elif undoOption==6:
            client._Client__updateClient(oldClientId[len(oldClientId)-1],client._Client__Id,client._Client__name,ListOfClients) 
            del oldClientId[-1]  
        if storage==1:
                Clients._ClientRepository__list=ListOfClients.copy()
                Clients._ClientRepository__uploadClientsToFile()
        if storage==2:
                Clients._PickleRepository__data=ListOfClients.copy()
                Clients._PickleRepository__storeToFile()       
    def __redoRental(self,Rentals,rental,ListOfRentals,index,storage):
        '''
        Function that redoes the last operation performed on a rental
        input: self,rental,ListOfRentals,index
        preconditions:-
        output:-
        postconditions:-
        '''
        rental._Rental__addRentalToIndex(index,ListOfRentals)
        del index[-1]
        if storage==1:
                Rentals._RentalRepository__list=ListOfRentals.copy()
                Rentals._RentalRepository__uploadRentalsToFile()
        if storage==2:
                Rentals._PickleRepository__data=ListOfRentals.copy()
                Rentals._PickleRepository__storeToFile()  
    def __redoReturnedDate(self,Rentals,returnedDate,rentalId,ListOfRentals,storage):
        '''
        Function that adds a returned date attributed to a rental
        input: self,returnedDate,rentalId
        preconditions:-
        output:-
        postconditions:-
        '''
        
        rental=findRentalById(rentalId[len(rentalId)-1], ListOfRentals)
        rental._Rental__setReturnedDate(returnedDate[len(returnedDate)-1])
        index=findRentalIndex(rental._Rental__rentalId, ListOfRentals)
        ListOfRentals[index]=rental
        del rentalId[-1]
        del returnedDate[-1]
        if storage==1:
                Rentals._RentalRepository__list=ListOfRentals.copy()
                Rentals._RentalRepository__uploadRentalsToFile()
        if storage==2:
                Rentals._PickleRepository__data=ListOfRentals.copy()
                Rentals._PickleRepository__storeToFile()                                 
    def __run(self,Books,Clients,Rentals,storage): 
        
        self.__displayMenu()
        
        if storage==0:
            ListOfBooks=Books._Repository__list
            ListOfClients=Clients._Repository__list
            ListOfRentals=Rentals._Repository__list
        elif storage==1:
            ListOfBooks=Books._BookRepository__list
            ListOfClients=Clients._ClientRepository__list
            ListOfRentals=Rentals._RentalRepository__list
        elif storage==2:
            ListOfBooks=Books._PickleRepository__data
            ListOfClients=Clients._PickleRepository__data
            ListOfRentals=Rentals._PickleRepository__data
            
                    
                  
        
        undoOption=[]
        myBook=Book(0,"","","")
        myClient=Client(0,"")
        myRental=Rental(0,0,0,"","","")
        myRentalId=[]
        listOfBookAttributes=[]
        listOfClientAttributes=[]
        listOfRentalAttributes=[]
        indexBook=[]
        indexClient=[]
        countBook=[0]
        countClient=[0]
        countRental=[0]
        countReturnedDate=[0]
        oldBookId=[]
        oldClientId=[]
        
        newBookId=[]
        newClientId=[]
        listOfBookAttributesRedo=[]
        listOfClientAttributesRedo=[]
        listOfRentalAttributesRedo=[]
        returnedDateRedo=[]
        rentalIdRedo=[]
        bookIndexRedo=[]
        clientIndexRedo=[]
        rentalIndexRedo=[]
        redoOption=[]
        countRedo=0
        while True:
            try:
                optionNumber=int(input("Please choose option."))  
                if optionNumber in self.__commands:
                    if optionNumber==1:
                        
                        self.__addBook(Books,ListOfBooks,listOfBookAttributes,undoOption,countBook,listOfBookAttributesRedo,bookIndexRedo,redoOption,storage)
                          
                
                    elif optionNumber==2:
                        
                        self.__removeBook(Books,ListOfBooks,listOfBookAttributes,indexBook,undoOption,countBook,listOfBookAttributesRedo,redoOption,storage)
                       
                    elif optionNumber==3:
                        self.__updateBook(Books,ListOfBooks,listOfBookAttributes,oldBookId,undoOption,countBook,listOfBookAttributesRedo,redoOption,newBookId,storage)
                         
                    elif optionNumber==4:
                        self.__listBook(ListOfBooks)
                    elif optionNumber==5:
                
                        self.__addClient(Clients,ListOfClients,listOfClientAttributes,undoOption,countClient,listOfClientAttributesRedo,clientIndexRedo,redoOption,storage)
                            
                    elif optionNumber==6:
                    
                        self.__removeClient(Clients,ListOfClients,listOfClientAttributes,indexClient,undoOption,countClient,listOfClientAttributesRedo,redoOption,storage)
                           
                    elif optionNumber==7:
                    
                        self.__updateClient(Clients,ListOfClients,listOfClientAttributes,oldClientId,undoOption,countClient,listOfClientAttributesRedo,redoOption,newClientId,storage)
                            
                    elif optionNumber==8:
                        self.__listClient(ListOfClients) 
                    elif optionNumber==9:
                        
                        self.__rentBook(Rentals,ListOfRentals,listOfRentalAttributes,undoOption,countRental,listOfRentalAttributesRedo,rentalIndexRedo,redoOption,storage)
                         
                    elif optionNumber==10:
                        
                        self.__returnBook(Rentals,ListOfRentals,myRentalId,undoOption,countReturnedDate,returnedDateRedo,rentalIdRedo,redoOption,storage)
                   
                           
                    elif optionNumber==11:
                        self.__searchBook(ListOfBooks)
                    elif optionNumber==12:
                        self.__searchClient(ListOfClients)
                    elif optionNumber==13:
                        self.__mostRentedBooks(ListOfBooks,ListOfRentals)  
                    elif optionNumber==14:
                        self.__mostActiveClients(ListOfClients, ListOfRentals)
                    elif optionNumber==15:
                        self.__mostRentedAuthors(ListOfBooks,ListOfRentals)  
                    elif optionNumber==16:
                        self.__lateRentals(ListOfBooks,ListOfRentals)
                    elif optionNumber==17:
                        self.__printRentals(ListOfRentals) 
                    elif optionNumber==18:
                        if len(undoOption)==0:
                            print("No operation to undo.")
                        elif undoOption[len(undoOption)-1]>=1 and undoOption[len(undoOption)-1] <=3:
                            if len(countBook)>0:
                                myBook._Book__setId(int(listOfBookAttributes[len(listOfBookAttributes)-4]))
                                myBook._Book__setTitle(listOfBookAttributes[len(listOfBookAttributes)-3])
                                myBook._Book__setDescription(listOfBookAttributes[len(listOfBookAttributes)-2])
                                myBook._Book__setAuthor(listOfBookAttributes[len(listOfBookAttributes)-1])
                                myCopiedBook=copy(myBook)
                                self.__undoBook(Books,undoOption[len(undoOption)-1],myCopiedBook,ListOfBooks,indexBook,oldBookId,storage)
                                del listOfBookAttributes[-1]
                                del listOfBookAttributes[-1]
                                del listOfBookAttributes[-1]
                                del listOfBookAttributes[-1]
                                countBook[0]=countBook[0]-1
                                del undoOption[-1]
                                countRedo+=1
                            else:
                                print("No more commands to undo.")    
                        elif undoOption[len(undoOption)-1]>=4 and undoOption[len(undoOption)-1]<=6:
                            if len(countClient)>0:
                                myClient._Client__setId(int(listOfClientAttributes[len(listOfClientAttributes)-2]))
                                myClient._Client__setName(listOfClientAttributes[len(listOfClientAttributes)-1])
                                myCopiedClient=copy(myClient)
                                self.__undoClient(Clients,undoOption[len(undoOption)-1],myCopiedClient,ListOfClients,indexClient,oldClientId,storage)
                                del listOfClientAttributes[-1]
                                del listOfClientAttributes[-1]
                                countClient[0]=countClient[0]-1
                                del undoOption[-1]
                                countRedo+=1
                            else:
                                print("No more comands to undo.")
                        elif undoOption[len(undoOption)-1]==7:
                            if len(countRental)>0:
                                myRental._Rental__setRentalId(listOfRentalAttributes[len(listOfRentalAttributes)-6])
                                myRental._Rental__setBookId(listOfRentalAttributes[len(listOfRentalAttributes)-5])
                                myRental._Rental__setClientId(listOfRentalAttributes[len(listOfRentalAttributes)-4])
                                myRental._Rental__setRentedDate(listOfRentalAttributes[len(listOfRentalAttributes)-3])
                                myRental._Rental__setDueDate(listOfRentalAttributes[len(listOfRentalAttributes)-2])
                                myRental._Rental__setReturnedDate(listOfRentalAttributes[len(listOfRentalAttributes)-1])
                                myCopiedRental=copy(myRental)
                                self.__undoRental(Rentals,myCopiedRental,ListOfRentals,storage)
                                del listOfRentalAttributes[-1]
                                del listOfRentalAttributes[-1]
                                del listOfRentalAttributes[-1]
                                del listOfRentalAttributes[-1]
                                del listOfRentalAttributes[-1]
                                del listOfRentalAttributes[-1]
                                countRental[0]=countRental[0]-1
                                del undoOption[-1]
                                countRedo+=1
                            else:
                                print("No more commands to undo.")    
                        elif undoOption[len(undoOption)-1]==8:
                            if len(countReturnedDate)>0:
                                self.__undoReturnedDate(Rentals,myRentalId,ListOfRentals,storage)
                                countReturnedDate[0]=countReturnedDate[0]-1
                                del undoOption[-1]
                                countRedo+=1
                            else:
                                print("No more commands to undo.")
                     
                    elif optionNumber==19:
                        if countRedo>0:
                            if redoOption[len(redoOption)-1]>=1 and redoOption[len(redoOption)-1]<=3:
                                myBook._Book__setId(int(listOfBookAttributesRedo[len(listOfBookAttributesRedo)-4]))
                                myBook._Book__setTitle(listOfBookAttributesRedo[len(listOfBookAttributesRedo)-3])
                                myBook._Book__setDescription(listOfBookAttributesRedo[len(listOfBookAttributesRedo)-2])
                                myBook._Book__setAuthor(listOfBookAttributesRedo[len(listOfBookAttributesRedo)-1])
                                myRedoBook=copy(myBook)
                                self.__redoBook(Books,redoOption[len(redoOption)-1],myRedoBook,ListOfBooks,bookIndexRedo,newBookId,storage)
                                del listOfBookAttributesRedo[-1]
                                del listOfBookAttributesRedo[-1]
                                del listOfBookAttributesRedo[-1]
                                del listOfBookAttributesRedo[-1]
                                countRedo-=1
                                del redoOption[-1]
                            elif redoOption[len(redoOption)-1]>=4 and redoOption[len(redoOption)-1]<=6:
                                myClient._Client__setId(int(listOfClientAttributesRedo[len(listOfClientAttributesRedo)-2]))
                                myClient._Client__setName(listOfClientAttributesRedo[len(listOfClientAttributesRedo)-1])
                                myRedoClient=copy(myClient)
                                self.__redoClient(Clients,redoOption[len(redoOption)-1],myRedoClient,ListOfClients,clientIndexRedo,newClientId,storage)
                                del listOfClientAttributesRedo[-1]
                                del listOfClientAttributesRedo[-1]
                                countRedo-=1
                                del redoOption[-1]
                            elif redoOption[len(redoOption)-1]==7:
                                myRental._Rental__setRentalId(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-6])
                                myRental._Rental__setBookId(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-5])
                                myRental._Rental__setClientId(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-4])
                                myRental._Rental__setRentedDate(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-3])
                                myRental._Rental__setDueDate(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-2])
                                myRental._Rental__setReturnedDate(listOfRentalAttributesRedo[len(listOfRentalAttributesRedo)-1])
                                myRedoRental=copy(myRental)
                                self.__redoRental(Rentals,myRedoRental,ListOfRentals,rentalIndexRedo,storage)
                                del listOfRentalAttributesRedo[-1]
                                del listOfRentalAttributesRedo[-1]
                                del listOfRentalAttributesRedo[-1]
                                del listOfRentalAttributesRedo[-1]
                                del listOfRentalAttributesRedo[-1]
                                del listOfRentalAttributesRedo[-1]
                                countRedo-=1
                                del redoOption[-1]
                            elif redoOption[len(redoOption)-1]==8:
                                self.__redoReturnedDate(Rentals,returnedDateRedo,rentalIdRedo,ListOfRentals,storage)
                                countRedo-=1      
                                del redoOption[-1]  
                        else:
                            print("No more commands to redo.")   
                    elif optionNumber==20:
                        return                                                                           
                    else:
                        print("Invalid option!")
                    #self.__print(ListOfRentals)     
                    #print (myBook._Book__Id,myBook._Book__title,myBook._Book__description,myBook._Book__author)
                    #print("book",listOfBookAttributes)
                    #print("client",listOfClientAttributes)
                    #print("rental",listOfRentalAttributes)
                    #print(myRentalId)
                    #print(undoOption)
                else:
                    return
            except ValueError:
                print("Please give integer.")    
           
                