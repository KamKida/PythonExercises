import requests
import json
import pprint
import webbrowser

from datetime import datetime, timedelta

timeBefore = timedelta(days=30)

searchedDate =datetime.today() - timeBefore

params= {
"site":"stackoverflow",
"sort":"votes",
"order":"desc",
"fromdate":int(searchedDate.timestamp()) ,
"tagged": "python",
"min": 15


}

r = requests.get("https://api.stackexchange.com/2.3/questions/",params)

try:
    questions = r.json()
except json.decoder.JsonDecodeError:
    print("Nie poprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])