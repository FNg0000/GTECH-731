############################################################################################################################
##
## Code by Fred Ng
## Assignment 4
## 732
## 2014/12/12
##
## Object-Oriented Programming: The file nys_cities_towns.txt has the locations and populations of cities and
## towns in New York State.  Write an object-oriented Python program to represent this data.  It should include
## a class that holds the id, name, location, and population of each city.  Your program should read in the
## text file and create a collection of objects based on this class.  Use the collection to execute a spatial
## query on the data:  for example, have the program take in a city name and a distance, and return the names
## and populations of cities within the distance. Or, see if you can find evidence of the rank-size-distribution
## typically found in cities (see, for example http://en.wikipedia.org/wiki/Rank-size_distribution for an explanation).
## This should be possible using only Python (assuming you will implement your own distance function).
## The data is in UTM 18 N projection, with units in meters.
##
##
##
############################################################################################################################


# Importing moduels

import sys
from math import sqrt

class Town(object):
    def __init__ (self, ID, name, population, xcoord, ycoord):
        self.ID = ID
        self.name = name
        self.population = population
        self.xcoord = float(xcoord)
        self.ycoord = float(ycoord)

    def distance(self, town_2):
        distance = sqrt((town_2.xcoord - self.xcoord)**2 + (town_2.ycoord - self.ycoord)**2)
        return distance

    def displayTown(self):
        return "Name: " + self.name + "| Pop: " + self.population +  "| XY Coordinates: " + str(self.xcoord) + ", " + str(self.ycoord)

# Create lists to for holding the values

list_city = []
citydict = {}

# Importing the file with the list of towns and their information.

infile = open("E:/nys_cities_towns.txt", 'r')
infile.readline() #Skips the header line
for row in infile:  #parses the first line
    rowEle = row.strip().split("\t")
    ID = rowEle[0]
    name = rowEle[1]
    pop = rowEle[2]
    x = rowEle[3]
    y = rowEle[4]
    town = Town(ID = ID, name = name, population = pop, xcoord = x, ycoord = y)
    citydict[name] = town  
infile.close()

infile = open("E:/nys_cities_towns.txt", 'r')
infile.readline()
for line in infile:
    lineEle = line.strip().split("\t")
    list_city.append(lineEle[1])
infile.close()

sort_list = sorted(list_city)
list_fc = [f[0] for f in sort_list]


def mainmenu():
    print("\n")
    print("+------------------------------------------------------------------------------------------+")
    print("|                                                                                          |")
    print("|                                                                                          |")
    print("| Welcome. This program can find information about New York State cities and towns. Such   |")
    print("| information include the city/town's ID, population size, and their XY coordinate.        |")
    print("| Another function of the program is it can find city/towns within a designated distance   |")
    print("| of a town you select.                                                                    |")
    print("|                                                                                          |")
    print("|  1. Display information about a citytown.                                                |")
    print("|  2. Find all cities within desired distance for selected city/town.                      |")
    print("|  3. Find the distance to all towns from selected city/town.                              |")
    print("|  4. Exit program.                                                                        |")
    print("|                                                                                          |")
    print("|                                                                                          |")
    print("+------------------------------------------------------------------------------------------+")
    print("\n")
    menuchoice = (str(raw_input("Enter choice: ")))
    print

    if menuchoice == '1':
        while True:

            target_letter = (str(raw_input("Choose a letter for a list of towns that begins with that letter: ").capitalize()))
            print 

            if target_letter in list_fc:
                                
                display_list = []
                
                for line in sort_list:
                    cls_line = line.strip()
                    
                    if target_letter == cls_line[0]:
                        display_list.append(str(cls_line))
                        
                    elif target_letter != cls_line[0]:
                        continue

                while len(display_list) > 0:
                    
                    print display_list
                    print 

                    target_name = (str(raw_input("Enter the name of the town: ").capitalize()))
                    print 
                    
                    if target_name in citydict:

                        target_town = citydict[target_name]
                        
                        print "City name is", target_town.name, ", the population size is", target_town.ID, ", and the XY coordinates are (", target_town.xcoord, ", ", target_town.ycoord, ")."
                        print
                        mainmenu()
                                        
                    else:
                        print "Inncorrect spelling or name of the city does not exist. Please try again!"
                        print

                else:
                    print "There are no cities that begin with that letter. Please try again!"
                    print

            elif target_letter not in list_fc:
                print "There are no cities that begin with that letter. Please try again!"
                print


    elif menuchoice == '2':
        while True:

            target_letter = (str(raw_input("Choose a letter for a list of towns that begins with that letter: ").capitalize()))
            print

            if target_letter in list_fc:
                                
                display_list = []
                
                for line in sort_list:
                    cls_line = line.strip()
                    
                    if target_letter == cls_line[0]:
                        display_list.append(str(cls_line))
                        
                    elif target_letter != cls_line[0]:
                        continue

                while len(display_list) > 0:

                    
                    print display_list
                    print

                    target_name = (str(raw_input("Enter the name of the town: ").capitalize()))
                    print

                    if target_name in citydict:

                        target_town = citydict[target_name]

                        distance_input = (float(raw_input("Please enter a distance, from the selected town, to find towns that are within that distance: ")))
                        print

                        list_nearby = []
                                                
                        print "The following is a list of towns within the distance of: ", distance_input
                        print
                        
                        for name in citydict.keys():
                            
                            town_other = citydict[name]
                            
                            dist_method = target_town.distance(town_2 = town_other)
                            
                            if dist_method <= distance_input and town_other != target_town:
                                
                                list_nearby.append(town_other.displayTown() + str(" | Distance from town: ") + str(round(dist_method)))

                        for place in list_nearby:

                            print place
                            print

                        mainmenu()
                            
                                        
                    else:
                        print "Inncorrect spelling or name of the city does not exist. Please try again! \n"
                        print

                else:
                    print "There are no cities that begin with that letter. Please try again!"
                    print

            elif target_letter not in list_fc:
                print "There are no cities that begin with that letter. Please try again!"
                print

    elif menuchoice == '3':
         while True:

            target_letter = (str(raw_input("Choose a letter for a list of towns that begins with that letter: ").capitalize()))
            print

            if target_letter in list_fc:
                                
                display_list = []
                
                for line in sort_list:
                    cls_line = line.strip()
                    
                    if target_letter == cls_line[0]:
                        display_list.append(str(cls_line))
                        
                    elif target_letter != cls_line[0]:
                        continue

                while len(display_list) > 0:

                    
                    print display_list
                    print

                    target_name = (str(raw_input("Enter the name of the town: ").capitalize()))
                    print

                    if target_name in citydict:

                        target_town = citydict[target_name]

                        list_nearby = []                   
                                                
                        print "The following is a list of towns from ", target_name, " distance of: "
                        print
                        
                        for name in citydict.keys():
                            
                            town_other = citydict[name]
                            
                            dist_method = target_town.distance(town_2 = town_other)
                            
                            if town_other != target_town:
                                
                                list_nearby.append(town_other.displayTown() + str(" | Distance from town: ") + str(round(dist_method)))

                        for place in list_nearby:

                            print place
                            print

                        mainmenu()
                            
                                        
                    else:
                        print "Inncorrect spelling or name of the city does not exist. Please try again! \n"
                        print

                else:
                    print "There are no cities that begin with that letter. Please try again!"
                    print

            elif target_letter not in list_fc:
                print "There are no cities that begin with that letter. Please try again!"
                print
        

    elif menuchoice == '4':
        sys.exit("Melting down. Good Bye =)")        

    else:
        print "Unknown option Selected! Please try again! \n"
        print

mainmenu()
