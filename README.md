# ios_cdp_discovery
CDP Discovery tool for Cisco IOS devices

add hosts you want to include in the search in hosts.csv. It will then go through all of them and find their neighbors through CDP. Then it will do the same
with the discovered neighbors. 

Current state:

GUI not implemented, sparse information is give during and after discovery but the plan is to do present a map

Will also find trunks with no CDP information.
Optionally, it will find access-ports with too many mac addresses, and look for text-strings on trunks or access ports(in running-config), or the absens of
those strings. 

Only works on active ports!

Mac search works with both Cisco and Microsoft type mac addresses, or any delimeter at all. But donät use more than one delimiter per mac address. That won't work. 



TODO/Not working yet:

Implement more support for different IOS version, it also finds version and has the ability to change the show mac-address command accordingly. But it itsn't
properly implemented. 

if you choose to use additional checks while scanning the network, you have to say yes when asked if you want to search for specific commands. 


GUI

Password is collected with input(), not ideal

ability to specify initial hosts to odd to search using a range (low to high address), instead of csv file. 

Different IOS-versions should be different classes, so that more types of devices can be used with better methods for collecting data for those that support it. 
