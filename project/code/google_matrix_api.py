# api key: AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI
# example parameter: parameters = 'origins=41.43206,-81.38992|-33.86748,151.20699'
# example request: https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=41.43206,-81.38992&destinations=-33.86748,151.20699&key=AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI

import requests
outputFormat = 'json'
API_KEY = 'AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI'
# don't ever dream of using my api key :) I restricted it to my IP

def get_distance(s, d):
    parameters = 'origins=' + s + '&destinations=' + d
    url = 'https://maps.googleapis.com/maps/api/distancematrix/' + outputFormat + '?' + 'units=imperial&' + parameters + '&key=' + API_KEY
    r = requests.get(url)
    return r.json()
    
print(get_distance('41.43206,-81.38992','-33.86748,151.20699'))