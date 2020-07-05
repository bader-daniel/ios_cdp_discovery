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



TODO:

Implement more support for different IOS version, it also finds version and has the ability to change the show mac-address command accordingly. But it itsn't
properly implemented. 

Functionality to locate specific mac addresses in the topology isn't working yet. When prompted, you have to select no. 

GUI

Password is collected with input(), not ideal

ability to specify initial hosts to odd to search using a range (low to high address), instead of csv file. 
