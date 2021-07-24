


# importing geopy library

# importing geopy library
from geopy.geocoders import Nominatim
  
# calling the Nominatim tool
loc = Nominatim(user_agent="GeoHack")
  
# entering the location name
location = loc.geocode({"country": "Brazil", "state": "MT"})
# printing address
print(location.address)
  
# printing latitude and longitude
print("Latitude = ", location.latitude)
print("Longitude = ", location.longitude)
print("point = ", location.point)
print("row = ", location.raw)
