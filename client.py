from datetime import datetime

from github import Github

# Ersetzen Sie "your_access_token" durch Ihren persönlichen Zugriffstoken
g = Github("xxx")

# Ersetzen Sie "owner/repo" durch den Repository-Namen
repo = g.get_repo("bokeh/bokeh")

# Abrufen der Commits
commits = repo.get_commits(since=datetime(2023, 1, 1))
commit_count = commits.totalCount

print(f"Anzahl der Commits: {commit_count}")
distinct_users = dict()

for commit in commits:
    if commit.author is None:
        continue
    author = commit.author
    distinct_users[author.name] = author
    print(f"Commit von {author.name}")

user_profiles = set()
for user_name in distinct_users.keys():
    print(user_name)
    user_profile = g.get_user(user_name)
    follower_count = user_profile.followers
    print(f"Anzahl der Follower: {follower_count}")
    user_profiles.add(user_profile)

