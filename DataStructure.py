'''
Created on 10 dec. 2018

@author: Revnic
'''
import unittest
def filterFunction(myList,condition):
    for element in myList:
        if condition(element):
            print(element)

def shellSort(myList,condition):
    gap = len(myList) // 2#we choose the initial gap to be the length of the list divided by two
    while gap > 0:
        for firstIndex in range(gap, len(myList)):#we go through every index between gap and the length of the list
            value = myList[firstIndex]#value holds the element at that index
            secondIndex = firstIndex#secondIndex holds the value of the initial index
            while secondIndex >= gap and condition(myList[secondIndex - gap],value)==0:#we compare the elements at indexes of gap difference between them, and while the condition isn't fulfilled, we rearrange them
                myList[secondIndex] = myList[secondIndex - gap]
                secondIndex = secondIndex - gap
            myList[secondIndex] = value
        gap //= 2#we divide the gap by two
         
class IterableData():
    def __init__(self):
        self._list=[]
        self._index=0
    def __iter__(self):
        self._index=0
        return self
    
    def __next__(self):
    
        
        if self._index < len(self._list)-1:
            self._index+=1
            return self._list[self._index]
        else:
            raise StopIteration()
        
    def __setItem__(self,position,value):
        self._list[position]=value
    def __delItem__(self,position):
        del self._list[position]
                
class MyTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def testIterableData(self):
        '''
        Function that tests whether the data methods implemented above are working properly
        input:-
        preconditions:-
        output:-
        postconditions: If the data methods are incorrectly implemented, an error will appear.
        '''
        iterable=IterableData()
        iterable._list=[0,2,4,6,8]
        
        iterable.__delItem__(2)   
        self.assertEqual(iterable._list,[0,2,6,8])
        
        iterable.__setItem__(3,88)
        self.assertEqual(iterable._list,[0,2,6,88])
        
        
        nextElement=iterable.__next__()
        self.assertEqual(nextElement,2)
        nextElement=iterable.__next__()
        self.assertEqual(nextElement,6)
        nextElement=iterable.__next__()
        self.assertEqual(nextElement,88)
        
        
            
    def testShellSort(self):
        '''
        Function that checks whether shellsort is working properly
        input:-
        preconditions:-
        output:-
        postconditions: If it's working incorrectly, an error will appear
        '''
        myList=[12,8,0,15,60]
        def condition(firstNumber,secondNumber):
            if firstNumber<=secondNumber:
                return 1
            return 0
        shellSort(myList,condition)
        newList=[0,8,12,15,60]
        self.assertEqual(myList,newList)
        
    
               

if __name__=="__main__":
    unittest.main()            