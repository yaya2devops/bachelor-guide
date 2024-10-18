import requests
import csv
from datetime import datetime

GITHUB_USER = 'yaya2devops'
GITHUB_REPO = 'bachelor-guide'
TOKEN = 'pat' 

url = f'https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/commits'

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

params = {
    'per_page': 100,  # Max number of items per page
}

commits = []

while True:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # Parse JSON response
        current_page_commits = response.json()
        commits.extend(current_page_commits)
        if 'next' in response.links.keys():
            url = response.links['next']['url']  # URL for the next page
        else:
            break  # Exit loop if there are no more pages
    else:
        print('Failed to fetch commits:', response.status_code)
        break

# Writing to that CSV 
with open('got-it.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'date', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for commit in commits:
        commit_message = commit['commit']['message'].split('\n')[0]  # Get the first line of the commit message
        commit_url = commit['html_url']
        commit_date = datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow({'title': commit_message, 'date': commit_date, 'url': commit_url})

print('CSV file has been created successfully. Total commits:', len(commits))