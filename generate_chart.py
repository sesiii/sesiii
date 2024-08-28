import matplotlib.pyplot as plt
import requests
import json

# Replace with your WakaTime API key
api_key = 'waka_0777981b-a060-4e18-9cbb-9d10f2ec39ba'
url = 'https://wakatime.com/api/v1/users/current/stats/last_7_days'

headers = {
    'Authorization': f'Token {api_key}',
}

response = requests.get(url, headers=headers)
data = response.json()

# Extract data for pie chart
languages = data['data']['languages']
labels = [lang['name'] for lang in languages]
sizes = [lang['percent'] for lang in languages]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(range(len(labels))))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Programming Languages Breakdown')
plt.savefig('chart.png')
