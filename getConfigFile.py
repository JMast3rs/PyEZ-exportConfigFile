from jnpr.junos import Device
from lxml import etree

address = str(input("Hostname or IP: "))
username = str(input("Username: "))
password = str(input("Password: "))
fileName = str(input("File Name: "))

if ".txt" not in fileName:
    fileName += ".txt"

with Device(host=address, user=username, passwd=password) as dev:
	data = dev.rpc.get_config()
	f = open(fileName, "w")
	f.write(etree.tostring(data, encoding='unicode', pretty_print=True))
	f.close()
	print (etree.tostring(data, encoding='unicode', pretty_print=True))
