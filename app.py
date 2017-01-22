#!.env/bin/python
import config
import urllib
import json
import time
import display

def main():
    while True:
        response = urllib.urlopen(config.API_URL)
        data = json.loads(response.read())
        display.main(data)
        time.sleep(3)

main()
