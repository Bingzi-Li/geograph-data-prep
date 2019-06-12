# api key: AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI
# example parameter: parameters = 'origins=41.43206,-81.38992|-33.86748,151.20699'

import requests
outputFormat = 'json'
API_KEY = 'AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI'

def get_distance(s, d):
    parameters = 'origins=' + s + '|' + d
    url = 'https://maps.googleapis.com/maps/api/distancematrix/' + outputFormat + '?' + parameters + '&key=' + API_KEY
    r = requests.get(url)
    return r.json()
    
get_distance('41.43206,-81.38992','-33.86748,151.20699')