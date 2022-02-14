from netmiko import ConnectHandler

print("Insert IP")
ip=input()

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
day=[]
f.close()
f = open("output3.txt", "r")
for line in f:
    mac.append(line[52:66])
    day.append(line[0:6])
    count+=1
print(str(count) + " MAC FLAPS ON THIS SWITCH")
print(" START: "+ day[0]+" END: "+day[-1])
mac=list(dict.fromkeys(mac))
print(mac)
open('output3.txt', 'w').close()


    
#for i in range(1,10):
#   output = net_connect.send_command('ping 192.168.200.' + str(i) + " timeout 1 repeat 2")
#   print (output)
 
# Finally close the connection
net_connect.disconnect()

