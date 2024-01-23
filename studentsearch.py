import json
import csv
import pandas as pd
import requests

#response = requests.post('https://ap-south-1.aws.data.mongodb-api.com/app/data-yubip/endpoint/data/v1/action/find', {"dataSource":"Cluster0","database":"student_data","collection":"student_data","filter":{},"limit":30000})
#print(response.status_code)


#preparing the data to a csv file
def prepare():
    file = open("data.json");
    data = json.load(file)
    #making a new file for y23
    COLUMN_NAMES = ["name", "rollnumber", "roomnumber", "wing", "hall"]
    with open("data.csv", 'w') as file:  
        # creating a csv writer object  
        csvwriter = csv.writer(file)   
        # writing the fields  
        csvwriter.writerow(COLUMN_NAMES)
        for student in data:
            if student["i"][:2] == "23" and len(student["i"]) == 6:
                # writing the data rows  
                csvwriter.writerow([student["n"], student["i"], student["r"],  student["r"][0:3:1], student["h"]])    
#wing sorting 
def wingsort(file, wing, hall):
    df = pd.read_csv(file)
    wingdic = []
    for index, line in df.iterrows():
        if(line["wing"] == wing and line["hall"][4:] == hall):
            wingdic.append({"name": line["name"], "rollnumber": line["rollnumber"]})
    #print(wingdic)
    with open( wing + "hall" + hall + ".csv", 'w') as f: 
        csvwriter = csv.DictWriter(f, fieldnames=["name", "rollnumber"])
        csvwriter.writerows(wingdic)          

def roomisort(file, r1, r2):
    df = pd.read_csv(file)
    if r1 == r2:
        print("same roll number!")
        return
    sorted_data = df.sort_values(by="rollnumber", ascending=True)
    if sorted_data.iloc[r1-1-230000]["roomnumber"] == sorted_data.iloc[r2-1-230000]["roomnumber"]:
        print("They are roomies")
    else:
        print("They are NOT roomies")
    

def main():
    print("Enter the wing you wnat sorted out! ")
    wing = input("Wing: ").strip().upper()
    hall = input("Hall: ").strip()
    prepare()       
    wingsort("data.csv", wing, hall)
    print("Enter the two roll numbers to check if they are roomies ")
    r1 = int(input("Roll Number1: ").strip())
    r2 = int(input("Roll Number2: ").strip())
    roomisort("data.csv", r1, r2)

main()
