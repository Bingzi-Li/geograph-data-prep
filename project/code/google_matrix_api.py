# api key: AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI
# example parameter: parameters = 'origins=41.43206,-81.38992|-33.86748,151.20699'
# example request: https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=41.43206,-81.38992&destinations=-33.86748,151.20699&key=AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI

from urllib.request import urlopen
import json
outputFormat = 'json'
API_KEY = 'AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI'
# don't ever dream of using my api key :) I restricted it to my IP

def get_distance(s, d):
    parameters = 'origins=' + s + '&destinations=' + d
    url = 'https://maps.googleapis.com/maps/api/distancematrix/' + outputFormat + '?'  + parameters + '&mode=walking' + '&key=' + API_KEY
    print(url)
    with urlopen(url) as response:
        response_content = response.read()
    json_response = json.loads(response_content.decode('utf-8'))
    return json_response
    
print(get_distance('-77.18457758276422,38.93989291394156','-77.07489935925479,38.743491801018926'))


#https://maps.googleapis.com/maps/api/distancematrix/json?origins=-77.18457758276422,38.93989291394156&destinations=-77.07489935925479,38.743491801018926&mode=walking&key=AIzaSyBzNUBMRf8VYahpGY9HF76b42e08ZpDPCI