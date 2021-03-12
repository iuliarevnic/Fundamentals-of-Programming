'''
Created on 30 nov. 2018

@author: Revnic
'''

from client import Client
class ClientRepository():
    def __init__(self,fileName):
        self.__list=[]
        self.__fileName=fileName
        self.__loadClientsFromFile()
          

                  
    def __loadClientsFromFile(self):
        file=open(self.__fileName,"r")
        oneLine=file.readline().strip()
        while oneLine!="":
            attributes=oneLine.split(" ; ")
            client=Client(attributes[0],attributes[1])
            client._Client__addClient(self.__list)
            oneLine=file.readline().strip()
        file.close()
        
    def __uploadClientsToFile(self):
        file=open(self.__fileName,"w")
        for client in self.__list:
            stringToFile=str(str(client._Client__Id)+" ; "+client._Client__name+"\n")
            file.write(stringToFile)
            