from github_client import *

async def fetch_repositories():
    return await get_user_repos()

async def fetch_issues(owner: str, repo: str):
    return await list_issues(owner, repo)

async def add_issue(owner: str, repo: str, title: str, body: str):
    return await create_issue(owner, repo, title, body)

async def fetch_all_commits(owner: str,repo: str):
    return await get_all_commits_from_repo(owner,repo)