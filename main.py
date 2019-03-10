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
    #We know that all itesm are 
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
    #our next goal since we have file that holds the json list now we must print that out....how do we do that. 
    #Alright we open the file and read everything on each line and print it out. 
    
    #The next step is to take the new file and print it out so it can be itnerpited correctly. 
    #we do this by opeing the file and then grabbing the data. Then we print it out. 
    with open('kerbalsTemp.json', 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    print("[");
    tempString = "["
    for i in range(4): 
        if(i < 3):
            print("\t {'Id': " + '"' + str(obj[i]['Id']) + "'")
            print("\t 'FirstName': " + '"' + str(obj[i]['FirstName']) + '"')
            print("\t 'LastName': " + '"' + str(obj[i]['LastName']) + '"')
            print("\t 'Job': " + '"' + str(obj[i]['Job']) + '"')
            print("\t 'Level': " + '"' + str(obj[3]['Level']) + '"')
            print("\t 'IsFemale': " + '"' + str(obj[3]['IsFemale']) + '"')
            print("\t 'Courage': " + '"' + str(obj[3]['Courage']) + '"')
            print("\t 'Stupidity': " + '"' + str(obj[3]['Stupidity']) + '"')
            print("\t 'BadS': " + '"' + str(obj[3]['BadS']) + '"},')
            
            tempString1 = tempString + '{"Id": "'+ str(obj[i]['Id']) + '", "FirstName": "' 
            tempString2 = tempString1 + str(obj[i]['FirstName']) + '", "LastName": "' + str(obj[i]['LastName'])
            tempString3 = tempString2 + '", "Job": "' + str(obj[i]['LastName']) + '", "Level": "'
            tempString4 = tempString3 
        else: 
            print("\t {'Id': " + '"' + str(obj[i]['Id']) + "'")
            print("\t 'FirstName': " + '"' + str(obj[i]['FirstName']) + '"')
            print("\t 'LastName': " + '"' + str(obj[i]['LastName']) + '"')
            print("\t 'Job': " + '"' + str(obj[i]['Job']) + '"')
            print("\t 'Level': " + '"' + str(obj[3]['Level']) + '"')
            print("\t 'IsFemale': " + '"' + str(obj[3]['IsFemale']) + '"')
            print("\t 'Courage': " + '"' + str(obj[3]['Courage']) + '"')
            print("\t 'Stupidity': " + '"' + str(obj[3]['Stupidity']) + '"')
            print("\t 'BadS': " + '"' + str(obj[3]['BadS']) + '"}')
    
            '''tempString = tempString + '{"Id": "'+ str(obj[i]['Id']) + '", "FirstName": "' + str(obj[i]['FirstName'] + '",' 
                                        + '"LastName": "' + str(obj[i]['LastName']) 
                                        + '",' + '"Job": "' + str(obj[i]['Job']) + '",'
                                        + '"Level": "' + str(obj[3]['Level']) + '",' 
                                        + '"IsFemale": "' + str(obj[3]['IsFemale']) + '",'
                                        + '"Courage": "' + str(obj[3]['Courage']) + '",' 
                                        + '"Stupidity": "' + str(obj[3]['Stupidity']) + '",'
                                        + '"BadS": "' + str(obj[3]['BadS']) + '"}]' '''
    print("]")
    myfile.close()
 
if __name__ == "__main__":
    main()
