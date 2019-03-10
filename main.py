# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:03:36 2019

@Project Name: Lasp Interview Homework
@author: Maureen Aubrey
"""

import csv
import json
from pprint import pprint

def main():
    #Alright the first thing one must do is to read in the data in the csv file.
    #Well we have 9 items in which the csv file holds. 
    csvfile = open('kerbals.csv', 'r')
    csv_headings = next(csvfile)
    jsonfile = open('kerbalsTemp.json', 'w')
    #What we are doing here is taking all the items from the csv file and then dumps the contants of the csv file
    #into a json file which we will user later. 
    i = 0;
    fieldnames = ("Id","FirstName","LastName","Job","Level", "IsFemale", "Courage", "Stupidity", "BadS")
    reader = csv.DictReader(csvfile, fieldnames)
    jsonfile.write("[")
    for row in reader:
        json.dump(row, jsonfile)
        if(i < 3):
            jsonfile.write(",\n")
            i = i+1;
    jsonfile.write("]")
    csvfile.close()
    jsonfile.close()
    
    #For this step I read in the json file I created and then printed it out so it can work with teh jsoninit
    #how it does that is by opening the json file we created and then taking the data from that and formating it
    #such taht the jsoninit will accept it as json array. 
    with open('kerbalsTemp.json', 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    tempString = "["
    for i in range(4): 
        if(i < 3):
            tempString1 = tempString + '{"Id": "'+ str(obj[i]['Id']) + '", "FirstName": "' 
            tempString2 = tempString1 + str(obj[i]['FirstName']) + '", "LastName": "' + str(obj[i]['LastName'])
            tempString3 = tempString2 + '", "Job": "' + str(obj[i]['LastName']) + '", "Level": "'
            tempString4 = tempString3 + str(obj[i]['Level']) + '", "IsFemale": "'
            tempString5 = tempString4 + str(obj[i]['IsFemale']) + '", "Courage": "'
            tempString6 = tempString5 + str(obj[i]['Courage']) + '", "Stupidity": "'
            tempString7 = tempString6 + str(obj[i]['Stupidity']) + '", "BadS": "'
            tempString8 = tempString7 + str(obj[i]['BadS']) + '"},'
            tempString = tempString8
        else: 
            tempString1 = tempString + '{"Id": "'+ str(obj[i]['Id']) + '", "FirstName": "' 
            tempString2 = tempString1 + str(obj[i]['FirstName']) + '", "LastName": "' + str(obj[i]['LastName'])
            tempString3 = tempString2 + '", "Job": "' + str(obj[i]['LastName']) + '", "Level": "'
            tempString4 = tempString3 + str(obj[i]['Level']) + '", "IsFemale": "'
            tempString5 = tempString4 + str(obj[i]['IsFemale']) + '", "Courage": "'
            tempString6 = tempString5 + str(obj[i]['Courage']) + '", "Stupidity": "'
            tempString7 = tempString6 + str(obj[i]['Stupidity']) + '", "BadS": "'
            tempString8 = tempString7 + str(obj[i]['BadS']) + '"}]'
            tempString =tempString8
    #Now that we have made the string that will hold the text of a json and close the file. 
    myfile.close()
    print(tempString)
 
if __name__ == "__main__":
    main()
