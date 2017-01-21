#!.env/bin/python
import config
import urllib
import json
import time

def main():
    while True:
        try:
            response = urllib.urlopen(config.API_URL)
            data = json.loads(response.read())
            for key, value in data.iteritems():
                print "key: {0} value: {1}".format(key, value)
        except:
            print "error fetching game state"
        time.sleep(3)

main()
