'''
Created on 30 nov. 2018

@author: Revnic
'''

from rental import Rental
class RentalRepository():
    def __init__(self,fileName):
        self.__list=[]
        self.__fileName=fileName
        self.__loadRentalsFromFile()
    
                  
    def __loadRentalsFromFile(self):
        file=open(self.__fileName,"r")
        oneLine=file.readline().strip()
        while oneLine!="":
            attributes=oneLine.split(" ; ")
            rental=Rental(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5])
            self.__list.append(rental)
            oneLine=file.readline().strip()
        file.close()
        
    def __uploadRentalsToFile(self):
        file=open(self.__fileName,"w")
        for rental in self.__list:
            stringToFile=str(str(rental._Rental__rentalId)+" ; "+str(rental._Rental__bookId)+" ; "+str(rental._Rental__clientId)+" ; "+rental._Rental__rentedDate+" ; "+rental._Rental__dueDate+" ; "+rental._Rental__returnedDate+"\n")
            file.write(stringToFile)
            