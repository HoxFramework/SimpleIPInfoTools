import json
import requests
import webbrowser

userentry = str(input("Enter the IP you want to locate:"))
link = "http://ip-api.com/json/%s"% userentry
getter = requests.get(link)
#print(link)
textversion = getter.content
reader = json.loads(textversion)
# ZNACI .LOADS radi a LOAD NE RADI !!!
#JER VALJDA LINK NEAM POJMA LMFAO



print("Country: ",reader["countryCode"])
print("")
print("ISP :",reader["isp"])
print("With org. info:{}".format(reader["org"]))
print("")
print("Longitude :",reader["lon"])
print("Latitude :",reader["lat"])
print("Timezone :",reader["timezone"])
print("\nCalculating the city...")
print("City :",reader["regionName"])
print("ZIP code :",reader["zip"])

latitude = reader["lat"]
longitude = reader["lon"]

location = ("https://www.google.com/maps/place/{0},{1}".format(latitude,longitude))
print("Using link:",location)

webbrowser.open_new_tab(location)

#NAPRAVIT DA pinga sam kuzis da moze dohvatit IP preko linka adrese
    
