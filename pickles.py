'''
Created on 1 dec. 2018

@author: Revnic
'''

import pickle 
from myRepository import Repository
class PickleRepository():
    def __init__(self,fileName):
        Repository.__init__(self)
        self.__fileName=fileName
        self.__loadFromFile()
     
          
    def __removeItem(self,index):
        del self.__list[index]
                  
    def __loadFromFile(self):
        file=open(self.__fileName,"rb")
        try:
            self.__data=pickle.load(file)
        except EOFError:
            self.__data=[]
        except Exception as exception:
            raise exception
        finally:
            file.close()
            
    def __storeToFile(self):
        file=open(self.__fileName,"wb")
        pickle.dump(self.__data,file)
        file.close()                    
    