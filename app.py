
import urllib
import json
import time

api_url = "http://52.90.208.174:6003/baseball/current/game-state"

def main():
    while True:
        try:
            response = urllib.urlopen(api_url)
            data = json.loads(response.read())
            for key, value in data.iteritems():
                print "key: {0} value: {1}".format(key, value)
        except:
            print "error fetching game state"
        time.sleep(3)

main()
