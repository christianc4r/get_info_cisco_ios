from netmiko import ConnectHandler
import os
data_import = []
sites_to_connect = []
connection = {}
ids=[]
import json

#read the file of sites and load into an array
with open("list_of_sites.txt","r") as reader:
   for line in reader.readlines():
       data_import=line.split()
       connection = {"host":data_import[1],"username":"YOUR_USERNAME","password":"YOUR_PASSWORD","device_type":"cisco_ios","secret":"YOUR_SECRET"}
       sites_to_connect.append(connection)
       ids.append(data_import[0])

export = open("export.txt", "w+")
count=0
for i in sites_to_connect:
    try:    
        connect = ConnectHandler(**i)
        connect.enable()
        cmd_send = connect.send_command("show version",use_textfsm=True)
        print(ids[count]+i["host"]+" "+cmd_send[0]["hardware"][0]+" "+cmd_send[0]["serial"][0])
        export.write(ids[count]+i["host"]+" "+cmd_send[0]["hardware"][0]+" "+cmd_send[0]["serial"][0]+os.linesep)
        count +=1
    except Exception as e:
        print(e)
        print(ids[count]+" "+i["host"]+" conection error")
        export.write(ids[count]+" "+i["host"]+" conection error"+os.linesep)
        count+=1
export.close()