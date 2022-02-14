from netmiko import ConnectHandler


print("Insert IP")
ip=input()
 
#First create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': 'orion',
    'password': 'orionams'
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
cmd=""
# Then send the command and print the output
while(cmd != "end"):
    print("Insert Command, write end to finish: ")
    cmd=input()
    if(cmd == "end"):
        break
    output = net_connect.send_command(cmd)
    print(output)


    
#for i in range(1,10):
#   output = net_connect.send_command('ping 192.168.200.' + str(i) + " timeout 1 repeat 2")
#   print (output)
 
# Finally close the connection
net_connect.disconnect()
