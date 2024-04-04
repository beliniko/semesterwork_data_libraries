from datetime import datetime
from github import Github

# Setzen des Access Token aus GitHub
g = Github("xxx")

# Angabe der GitHub Repository
repo = g.get_repo("matplotlib/matplotlib")

# Abruf der Commits der Repository
commits = repo.get_commits(since=datetime(2023, 1, 1))
commit_count = commits.totalCount

print(f"Anzahl der Commits seit 2023-01-01: {commit_count}")

distinct_users = {}
total_followers = 0
countries = set()
companies = set()

total_additions = 0
total_deletions = 0

# Durchlaufen der Commits und Sammeln der Autoren
for commit in commits:
    if commit.author is None:
        continue  # Ignoriere Commits ohne zugeordneten GitHub-Autor
    author = commit.author
    total_additions += commit.stats.additions
    total_deletions += commit.stats.deletions
    if author.login not in distinct_users:
        distinct_users[author.login] = author
        total_followers += author.followers  # Addiere Follower zum Gesamtwert
        if author.location: countries.add(author.location)
        if author.company: companies.add(author.company)


# Ausgabe der einzigartigen Beitragenden und ihrer Follower
for user_login, user in distinct_users.items():
    print(f"Contributor: {user_login}, Anzahl der Follower: {user.followers}")
# Ausgabe der Contributorzahl und Berechnung der durchschnittlichen Followeranzahl
num_contributors = len(distinct_users)
avg_followers = total_followers / num_contributors if num_contributors > 0 else 0
print(f"Anzahl der einzigartigen Contributors: {num_contributors}")
print(f"Anzahl der Gesamtanzahl der Follower: {total_followers}")
print(f"Durchschnittliche Anzahl der Follower pro Contributor: {avg_followers:.2f}")

# Abrufen der Issues / offen, geschlossen, inesgesamt

all_issues = repo.get_issues(state='all')
all_issues_count = all_issues.totalCount
open_issues = repo.get_issues(state='open')
open_issues_count = open_issues.totalCount
closed_issues = repo.get_issues(state='closed')
closed_issues_count = closed_issues.totalCount

print(f"Anzahl der offenen Issues: {open_issues_count}")
print(f"Anzahl der geschlossenen Issues: {closed_issues_count}")
print(f"Anzahl aller Issues: {all_issues_count}")

print(len(countries))
print(len(companies))
print(countries)
totalLOC = total_additions + total_deletions
print(f"Anzahl LOC: {totalLOC}")
print(f"monatliche Anzahl von LOC: {totalLOC / 12}")




