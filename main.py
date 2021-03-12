'''
Created on 1 nov. 2018
 
@author: Revnic           
'''                    
from console import *
from BookRepository import *
from ClientRepository import *
from RentalRepository import *
from pickles import PickleRepository

settings_file="settings.properties"
def readSettingsFile():

    file = open(settings_file, "r")
    lines = file.read().split("\n")
    settings = {}
    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    file.close()
    return settings
 
      
def run():               
       
    start=command()
    setup=readSettingsFile()
    if 'text' == setup['repository']:
        ListOfBooks=BookRepository(setup['books'])
        ListOfClients=ClientRepository(setup['clients'])
        ListOfRentals=RentalRepository(setup['rentals'])
        storage=1  
          
    if 'binary' == setup['repository']:  
        ListOfBooks=PickleRepository(setup['books'])
        ListOfClients=PickleRepository(setup['clients']) 
        ListOfRentals=PickleRepository(setup['rentals'])   
        ListOfBooks._PickleRepository__data=[Book(1,"The picture of Dorian Grey","Beautiful novel","Oscar Wilde"),Book(2,"The Night Circus","Fantasy","Erin Morgenstern"),Book(3,"Old man and the Sea","Book","Ernest Hemingway"),Book(4,"How the Marquis got his coat back","Adventure","Neil Gaiman"),Book(5,"Desire","Story","Haruki Murakami"),Book(6,"Out of ideas","Really?","Lame"),Book(7,"This is a book","Because why not","I know right"),Book(8,"Why so many items tho?","20 were enough","Too many actually"),Book(9,"Pretty cover","Judge me","Sassy elevator"),Book(10,"One","Two","Three"),Book(11,"This","is","extremely"),Book(12,"Luke,I am your father","Parenting 101","Darth Vader"),Book(13,"The art of disappearing","What to do when Thanos strikes","Marvel characters"),Book(14,"Harley Queen","Toys and trivia","Joker"),Book(15,"Batman","Hero Tales","Superman"),Book(16,"Sony","Vaio","Lenovo"),Book(17,"Samsung","Apple","Pineapple"),Book(18,"Jail","Prison","Break"),Book(19,"Vampire","Werewolf","Witch"),Book(20,"Club Penguin","Rules","the penguin world as we know it"),Book(21,"Harry Potter","An actual book","J.K.Rowling"),Book(22,"OOO","Carol","whatchadoin"),Book(23,"Bling bling","Boss","Dowery"),Book(24,"In the morning","Early bird","Hedwig"),Book(25,"Love triangle","Juicy story","Cheesy author"),Book(26,"Almost there","Refrigerator","Pastry"),Book(27,"Pizza","Italy","Pasta"),Book(28,"Stonehenge","Gizah","Machu Pichu"),Book(29,"Vegetarian","Vegan","Raw-vegan"),Book(30,"Fantastic beasts","and amazing pets","AnimalLover")]
        ListOfClients._PickleRepository__data=[Client(1,"Hiroyuki Takei"),Client(2,"Masashi Kishimoto"),Client(3,"Hayao Miyazaki"),Client(4,"Makoto Shinkai"),Client(5,"Naruto Uzumaki"),Client(6,"Sakura Haruno"),Client(7,"Uchiha Sasuke"),Client(8,"Hatake Kakashi"),Client(9,"Hayato Date"),Client(10,"Yuhi Kurenai"),Client(11,"Sarutobi Asuma"),Client(12,"Sarutobi Konohamaru"),Client(13,"Sarutobi Mirai"),Client(14,"Sarutobi Hiruzen"),Client(15,"Uchiha Shisui"),Client(16,"Uchiha Madara"),Client(17,"Uchiha Fugaku"),Client(18,"Menma"),Client(19,"Hyuga Hinata"),Client(20,"Hyuga Hanabi"),Client(21,"Hyuga Neji"),Client(22,"Tenten"),Client(23,"Rock Lee"),Client(24,"Senju Tsunade"),Client(25,"Senju Hashirama"),Client(26,"Senju Tobirama"),Client(27,"Uzumaki Kushina"),Client(28,"Namikaze Minato"),Client(29,"Jiraiya"),Client(30,"Orochimaru"),Client(31,"Kabuto Yakushi"),Client(32,"Gaara"),Client(33,"Temari"),Client(34,"Kankuro"),Client(35,"Uchiha Obito"),Client(36,"Nohara Rin"),Client(37,"Kaguya"),Client(38,"Tenji"),Client(39,"Ebisu"),Client(40,"Iruka"),Client(41,"Yona"),Client(42,"Hak"),Client(43,"Uzumaki Boruto"),Client(44,"Uchiha Sarada"),Client(45,"Mitsuki"),Client(46,"Chocho Akimichi"),Client(47,"Inojin Yamanaka"),Client(48,"Shikadai Nara"),Client(49,"Kawaki"),Client(50,"Chitanda Eru")]
        ListOfRentals._PickleRepository__data=[Rental(1,1,2,"3.11.2018","4.12.2018","17.11.2018"),Rental(2,3,4,"1.1.2017","2.1.2017","3.1.2017"),Rental(3,5,5,"3.2.2018","10.3.2018","17.2.2018"),Rental(4,5,3,"3.3.2018","5.3.2018","20.3.2018"),Rental(5,3,2,"15.11.2018","16.11.2018","17.11.2018"),Rental(6,1,2,"2.5.2018","11.5.2018",""),Rental(7,2,4,"23.8.2018","30.8.2018",""),Rental(8,3,2,"10.1.2017","11.1.2017","12.1.2017"),Rental(9,27,30,"1.4.2018","5.5.2018","10.5.2018"),Rental(10,13,20,"1.1.2018","2.2.2018","3.3.2018"),Rental(11,12,10,"1.7.2017","4.7.2017","10.7.2017"),Rental(12,8,26,"12.7.2017","12.1.2018","10.1.2018"),Rental(13,19,2,"1.9.2016","5.9.2016","3.9.2016"),Rental(14,18,22,"20.4.2015","12.5.2015","16.5.2915"),Rental(15,7,14,"10.2.2010","1.3.2010","1.4.2010"),Rental(16,20,35,"2.10.2009","20.10.2009","23.11.2009"),Rental(17,30,15,"12.7.2012","20.8.2012","27.7.2018"),Rental(18,16,20,"1.1.2001","2.2.2001","3.3.2001"),Rental(19,20,19,"1.1.2002","2.2.2002","17.1.2002"),Rental(20,21,50,"1.1.2003","2.2.2003","3.3.2003")]
        ListOfBooks._PickleRepository__storeToFile()  
        ListOfClients._PickleRepository__storeToFile()
        ListOfRentals._PickleRepository__storeToFile()
        storage=2   
    
    if 'inmemory' == setup['repository']:  
        ListOfBooks=Repository()
        ListOfClients=Repository() 
        ListOfRentals=Repository()   
        ListOfBooks._Repository__list=[Book(1,"The picture of Dorian Grey","Beautiful novel","Oscar Wilde"),Book(2,"The Night Circus","Fantasy","Erin Morgenstern"),Book(3,"Old man and the Sea","Book","Ernest Hemingway"),Book(4,"How the Marquis got his coat back","Adventure","Neil Gaiman"),Book(5,"Desire","Story","Haruki Murakami"),Book(6,"Out of ideas","Really?","Lame"),Book(7,"This is a book","Because why not","I know right"),Book(8,"Why so many items tho?","20 were enough","Too many actually"),Book(9,"Pretty cover","Judge me","Sassy elevator"),Book(10,"One","Two","Three"),Book(11,"This","is","extremely"),Book(12,"Luke,I am your father","Parenting 101","Darth Vader"),Book(13,"The art of disappearing","What to do when Thanos strikes","Marvel characters"),Book(14,"Harley Queen","Toys and trivia","Joker"),Book(15,"Batman","Hero Tales","Superman"),Book(16,"Sony","Vaio","Lenovo"),Book(17,"Samsung","Apple","Pineapple"),Book(18,"Jail","Prison","Break"),Book(19,"Vampire","Werewolf","Witch"),Book(20,"Club Penguin","Rules","the penguin world as we know it"),Book(21,"Harry Potter","An actual book","J.K.Rowling"),Book(22,"OOO","Carol","whatchadoin"),Book(23,"Bling bling","Boss","Dowery"),Book(24,"In the morning","Early bird","Hedwig"),Book(25,"Love triangle","Juicy story","Cheesy author"),Book(26,"Almost there","Refrigerator","Pastry"),Book(27,"Pizza","Italy","Pasta"),Book(28,"Stonehenge","Gizah","Machu Pichu"),Book(29,"Vegetarian","Vegan","Raw-vegan"),Book(30,"Fantastic beasts","and amazing pets","AnimalLover")]
        ListOfClients._Repository__list=[Client(1,"Hiroyuki Takei"),Client(2,"Masashi Kishimoto"),Client(3,"Hayao Miyazaki"),Client(4,"Makoto Shinkai"),Client(5,"Naruto Uzumaki"),Client(6,"Sakura Haruno"),Client(7,"Uchiha Sasuke"),Client(8,"Hatake Kakashi"),Client(9,"Hayato Date"),Client(10,"Yuhi Kurenai"),Client(11,"Sarutobi Asuma"),Client(12,"Sarutobi Konohamaru"),Client(13,"Sarutobi Mirai"),Client(14,"Sarutobi Hiruzen"),Client(15,"Uchiha Shisui"),Client(16,"Uchiha Madara"),Client(17,"Uchiha Fugaku"),Client(18,"Menma"),Client(19,"Hyuga Hinata"),Client(20,"Hyuga Hanabi"),Client(21,"Hyuga Neji"),Client(22,"Tenten"),Client(23,"Rock Lee"),Client(24,"Senju Tsunade"),Client(25,"Senju Hashirama"),Client(26,"Senju Tobirama"),Client(27,"Uzumaki Kushina"),Client(28,"Namikaze Minato"),Client(29,"Jiraiya"),Client(30,"Orochimaru"),Client(31,"Kabuto Yakushi"),Client(32,"Gaara"),Client(33,"Temari"),Client(34,"Kankuro"),Client(35,"Uchiha Obito"),Client(36,"Nohara Rin"),Client(37,"Kaguya"),Client(38,"Tenji"),Client(39,"Ebisu"),Client(40,"Iruka"),Client(41,"Yona"),Client(42,"Hak"),Client(43,"Uzumaki Boruto"),Client(44,"Uchiha Sarada"),Client(45,"Mitsuki"),Client(46,"Chocho Akimichi"),Client(47,"Inojin Yamanaka"),Client(48,"Shikadai Nara"),Client(49,"Kawaki"),Client(50,"Chitanda Eru")]
        ListOfRentals._Repository__list=[Rental(1,1,2,"3.11.2018","4.12.2018","17.11.2018"),Rental(2,3,4,"1.1.2017","2.1.2017","3.1.2017"),Rental(3,5,5,"3.2.2018","10.3.2018","17.2.2018"),Rental(4,5,3,"3.3.2018","5.3.2018","20.3.2018"),Rental(5,3,2,"15.11.2018","16.11.2018","17.11.2018"),Rental(6,1,2,"2.5.2018","11.5.2018",""),Rental(7,2,4,"23.8.2018","30.8.2018",""),Rental(8,3,2,"10.1.2017","11.1.2017","12.1.2017"),Rental(9,27,30,"1.4.2018","5.5.2018","10.5.2018"),Rental(10,13,20,"1.1.2018","2.2.2018","3.3.2018"),Rental(11,12,10,"1.7.2017","4.7.2017","10.7.2017"),Rental(12,8,26,"12.7.2017","12.1.2018","10.1.2018"),Rental(13,19,2,"1.9.2016","5.9.2016","3.9.2016"),Rental(14,18,22,"20.4.2015","12.5.2015","16.5.2915"),Rental(15,7,14,"10.2.2010","1.3.2010","1.4.2010"),Rental(16,20,35,"2.10.2009","20.10.2009","23.11.2009"),Rental(17,30,15,"12.7.2012","20.8.2012","27.7.2018"),Rental(18,16,20,"1.1.2001","2.2.2001","3.3.2001"),Rental(19,20,19,"1.1.2002","2.2.2002","17.1.2002"),Rental(20,21,50,"1.1.2003","2.2.2003","3.3.2003")]
        storage=0 
    
             
    start._command__run(ListOfBooks,ListOfClients,ListOfRentals,storage)                         
          
run()          

#repository=binary
#books=C:\\Users\\Revnic\\eclipse-workspace\\L5\\book.pickle
#clients=C:\\Users\\Revnic\\eclipse-workspace\\L5\\client.pickle
#rentals=C:\\Users\\Revnic\\eclipse-workspace\\L5\\rental.pickle


#repository=text
#books=C:\\Users\\Revnic\\eclipse-workspace\\L5\\book.txt
#clients=C:\\Users\\Revnic\\eclipse-workspace\\L5\\client.txt
#rentals=C:\\Users\\Revnic\\eclipse-workspace\\L5\\rental.txt