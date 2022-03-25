Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 9 Issue 3###
# Revision number BEGIN/ 03/23/22
## Begin Hussein El Sibai
##Read a value from the user
import csv
import json

SyntaxError: multiple statements found while compiling a single statement
import csv
import json
with open('C:\\Users\\Huss\\Desktop\\SalesJan2009.csv',"r") as f:
    reader = csv.reader(f)
    sales_data=[]
    for row in reader:
        sales_data.append({'Transaction_date':row[0].strip('"'),'Product':row[1].strip('"'),'Price':row[2].strip('"')
                           ,'Payment_Type':row[3].strip('"'),'Name':row[4].strip('"'), 'City':row[5].strip('"'),'State':row[6].strip('"'),'Country':row[7].strip('"')})

        
with open('SalesJan2009.json','w') as jsonf:
    json.dump(sales_data,jsonf, indent=4)

    
with open('SalesJan2009.json','r') as jsonf:
    data = json.load(jsonf)
    print(type(data))
    print(type(data[0]))

    
<class 'list'>
<class 'dict'>
## The print statement should go in the sphere_volume function ##
# Revision number 1/ 03/23/22
## End Hussein El Sibai
# HALF-LIFE/ Ron Bass/ John Richards Sr./ project # After-Burner Elite
