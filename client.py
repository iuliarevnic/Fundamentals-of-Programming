'''
Created on 1 nov. 2018

@author: Revnic 
'''  
from repository import findClientIndex
class Client():
    def __init__(self,Id,name):
        self.__Id=Id
        self.__name=name
        
    def __getId(self):
        return self.__Id
    def __getName(self):
        return self.__name
    
    def __setId(self,Id):
        self.__Id=Id
    def __setName(self,name):
        self.__name=name    
    
    def __eq__(self,other):
        return self.__Id==other.__Id
    def __addClient(self,ListOfClients):
        '''
        Function that adds a client to the list of clients
        input: self,Id,name,ListOfClients
        preconditions: Id should be an integer, name should be a string
        output:-
        postconditions: A new client will be added to the list ListOfClients
        ''' 
        for client in ListOfClients:
            if int(client.__Id)==self.__Id:
                print("Existing Id!")
                return
            if client.__name==self.__name:
                print("Existing client!")
                return
        ListOfClients.append(self)    
        
                
    def __removeClient(self,ListOfClients):
        '''
        Function that removes a client from a list of clients.
        input: self,ListOfClients
        preconditions:-
        output:-
        postconditions: The client will be removed from the list.
        '''
        if(len(ListOfClients)==0):
            print("The list is already empty!")
            return
        ok=0
        for client in ListOfClients:
            if int(client.__Id)==self.__Id and client.__name==self.__name:
                ok=1  
                ListOfClients.remove(client) 
        if ok==0:
            print("Inexistent client!")
            return
            
        
                
    def __updateClient(self,oldId,Id,name,ListOfClients):   
        '''
        Function that updates a client from a list, with the given values
        input: self,Id,name
        preconditions: Id should be an integer, name should be a string
        output:-
        postconditions: The client will be updated with the new values.
        '''
        index=findClientIndex(oldId,ListOfClients)    
        self.__setId(Id)
        self.__setName(name)
        ListOfClients[index]=self
                   
            
    def __listClient(self,ListOfClients):
        '''
        Function that prints the list of clients
        input: self, ListOfClients
        preconditions:-
        output: The list of clients will be printed
        postconditions:-
        '''
        if(len(ListOfClients)==0):
            print("The list is empty!")
            return
        for client in ListOfClients:
            print("Id:",client.__Id," Name:",client.__name,"\n")
    
    def __addClientToIndex(self,index, ListOfClients):
        ''' 
        Function that adds a client in a list at the index index
        input: self,index,ListOfClients
        preconditions:-
        output:-
        postconditions:-
        '''
        ListOfClients.insert(index[len(index)-1],self)                 
           