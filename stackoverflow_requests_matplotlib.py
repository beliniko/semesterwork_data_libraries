import requests
import json
import time
from stackapi import stackapi
from datetime import datetime


stackoverflow = stackapi.StackAPI('stackoverflow')


def readOrFetchData():
    try:
        with open('matplotlib_questions.json', 'r') as file:
            # Lesen des gesamten Inhalts der Datei
            data = file.read()
            # Konvertieren des JSON-Strings in ein Python-Datenobjekt
            matplotlib_questions = json.loads(data)
            return matplotlib_questions
    except Exception as e:
        # Wenn die Datei nicht gefunden wird, rufen Sie die Daten von der API ab
        return fetchBokehQuestions()


def fetchBokehQuestions():
    # Abrufen von Fragen zu Bokeh von Stack Overflow
    matplotlib_questions = stackoverflow.fetch('questions', fromdate=datetime(2023, 1, 1), todate=datetime(2023, 12, 31),
                                          tagged='matplotlib')
    # Konvertieren des Python-Datenobjekts in einen JSON-String
    json_data = json.dumps(matplotlib_questions, indent=4)
    # Schreiben des JSON-Strings in eine Datei
    with open('matplotlib_questions.json', 'w') as file:
        file.write(json_data)
    return matplotlib_questions


matplotlib_questions = readOrFetchData()

items = matplotlib_questions['items']
count_true = 0
for item in items:
    created_at = datetime.fromtimestamp(item['creation_date'])
    answered = item['is_answered']
    print(f"{created_at} {answered} {item['title']}" )
    if answered == True:
        count_true += 1
print(count_true)
print (len(items))
# print(map(items, lambda x: x['title']))

# def fetch_bokeh_questions(api_key):
#     # Konvertieren von Datumsangaben in Unix-Zeitstempel
#     start_date = int(datetime(2023, 1, 1, 0, 0).timestamp())
#     end_date = int(datetime(2023, 12, 31, 23, 59).timestamp())
#
#     # Basis-URL für Stack Exchange API
#     base_url = "https://api.stackexchange.com/2.3/questions"
#     # Parameter für die Anfrage
#     params = {
#         'fromdate': start_date,
#         'todate': end_date,
#         'order': 'desc',
#         'sort': 'creation',
#         'tagged': 'bokeh',  # Tag für die Bokeh-Bibliothek
#         'site': 'stackoverflow',
#         'key': api_key,  # Ihr API-Schlüssel
#     }
#
#     # API-Anfrage
#     response = requests.get(base_url, params=params)
#     # Prüfen, ob die Anfrage erfolgreich war
#     if response.status_code == 200:
#         data = response.json()
#         # Convert the Python dictionary to a pretty-printed JSON string
#         pretty_json = json.dumps(data, indent=4)
#
#         # Print the pretty-printed JSON
#         print(pretty_json)
#         # Verwenden Sie get() um einen Standardwert zurückzugeben, falls 'total' nicht vorhanden ist
#         total_questions = data.get('total', 0)
#         answered_questions = sum(1 for item in data['items'] if item.get('is_answered', False))
#         unanswered_questions = total_questions - answered_questions
#
#         print(f"Gesamtanzahl der Fragen zu Bokeh für das Jahr 2023: {total_questions}")
#         print(f"Davon beantwortet: {answered_questions}")
#         print(f"Davon unbeantwortet: {unanswered_questions}")
#     else:
#         print("Fehler bei der API-Anfrage")

# Ersetzen Sie 'Ihr_API_Schlüssel' mit Ihrem tatsächlichen API-Schlüssel
api_key = 'xxx(('
# fetch_bokeh_questions(api_key)
