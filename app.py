#!.env/bin/python
import config
import urllib
import json
import time
import display

current_data = []

def main():
    global current_data
    while True:
        try:
            response = urllib.urlopen(config.API_URL)
            data = json.loads(response.read())
            if data != current_data:
                display.main(data)
            current_data = data
        except Exception as e:
            print "Error fetching game state"
            print e
        time.sleep(2)

main()
