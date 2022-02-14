from netmiko import ConnectHandler
from datetime import datetime

def convertDate(strH,strL):
    dist=0 
    dateH=datetime.strptime(strH, "%b %d")
    dateL=datetime.strptime(strL, "%b %d")
    dateH= dateH.day + (dateH.month-1)*30
    dateL= dateL.day + (dateL.month-1)*30
    if (dateH<dateL):
        dist=dateH+(365-dateL)
    if (dateH>=dateL):
        dist=dateH-dateL
    return dist
print("Insert IP")
#ip=input()

CSR = {
    'device_type': 'cisco_ios',
    'ip': "10.210.79.225",
    'username': 'orion',
    'password': 'orionams'
}
net_connect = ConnectHandler(**CSR)
cmd="sh logg | i MACFLAP"
print("MAC FLAPP CHECKER")

f = open("output3.txt", "w")

f.writelines(net_connect.send_command(cmd))
count=0
mac=[]
day="Jan 1"
f.close()
f = open("output3.txt", "r")
aux="Jan 1"

for line in f:
    macFlapp={}
    if(count==0):
        aux=line[0:6]
    day=line[0:6]
    dist=convertDate(day,aux)
    aux=day
    macFlapp["Day"]=day
    macFlapp["Mac"]=line.partition("Host ")[2][0:14]
    macFlapp["Dist"]=dist
    mac.append(macFlapp)
    if(count>=6):
        break
    count+=1

print(mac)

#print(str(count) + " MAC FLAPS ON THIS SWITCH")
#print(mac)
#print(" START: "+ day[0]+" END: "+day[-1])
#mac=list(dict.fromkeys(mac))
#print(mac)
open('output3.txt', 'w').close()


    
#for i in range(1,10):
#   output = net_connect.send_command('ping 192.168.200.' + str(i) + " timeout 1 repeat 2")
#   print (output)
 
# Finally close the connection
net_connect.disconnect()

