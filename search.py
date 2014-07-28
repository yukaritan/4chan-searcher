import re
import json
import requests

data = requests.get("http://boards.4chan.org/g/catalog").text
match = re.match(".*var catalog = (?P<catalog>\{.*\});.*", data)

if not match:
    print("Couldn't scrape catalog")
    exit(1)

catalog = json.loads(match.group('catalog'))

running = True
while running:
    try:
        filtertext = input("filter: ")
        for number, thread in catalog['threads'].items():
            sub, teaser = thread['sub'], thread['teaser']
            if filtertext in sub.lower() or filtertext in teaser.lower():
                print(teaser)

    except KeyboardInterrupt:
        running = False