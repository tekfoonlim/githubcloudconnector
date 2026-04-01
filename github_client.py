import httpx
from config import GITHUB_TOKEN

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# FETCH REPOS
async def get_user_repos():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/user/repos",
            headers=headers
        )
        response.raise_for_status()
        return response.json()

#Fetch all commits from a Repo
async def get_all_commits_from_repo(owner: str, repo: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            headers=headers
        )
        response.raise_for_status()
        return response.json()


#LIST ISSUES
async def list_issues(owner: str, repo: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/issues",
            headers=headers
        )
        response.raise_for_status()
        return response.json()


#CREATE ISSUE
async def create_issue(owner: str, repo: str, title: str, body: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://api.github.com/repos/{owner}/{repo}/issues",
            headers=headers,
            json={
                "title": title,
                "body": body
            }
        )
        response.raise_for_status()
        return response.json()