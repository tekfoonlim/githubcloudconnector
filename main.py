from fastapi import FastAPI, HTTPException, Query
from services import *
from models import IssueCreate
import httpx
import logging

app = FastAPI(title="GitHub Cloud Connector")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GET REPOS
@app.get("/repos")
async def get_repos(visibility: str = Query(default="all")):
    """
    Fetch repositories for authenticated user.
    Optional: visibility = all | public | private
    """
    try:
        repos = await fetch_repositories()

        # filtering
        if visibility != "all":
            repos = [r for r in repos if (
                (visibility == "public" and not r["private"]) or
                (visibility == "private" and r["private"])
            )]

        return {"count": len(repos), "data": repos}

    except httpx.HTTPStatusError as e:
        logger.error(f"GitHub API error: {e.response.text}")

        if e.response.status_code == 401:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired GitHub token"
            )

        raise HTTPException(
            status_code=e.response.status_code,
            detail="Failed to fetch repositories from GitHub"
        )


#GET ISSUES
@app.get("/repos/{owner}/{repo}/issues")
async def get_issues(owner: str, repo: str):
    try:
        issues = await fetch_issues(owner, repo)
        return {"count": len(issues), "data": issues}

    except httpx.HTTPStatusError as e:
        logger.error(f"Issues fetch error: {e.response.text}")

        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Repository not found")

        raise HTTPException(
            status_code=e.response.status_code,
            detail="Failed to fetch issues"
        )


#CREATE ISSUE
@app.post("/repos/{owner}/{repo}/issues")
async def create_issue(owner: str, repo: str, issue: IssueCreate):
    try:
        result = await add_issue(owner, repo, issue.title, issue.body)
        

        return {
            "message": "Issue created successfully",
            "issue_url": result.get("html_url"),
            "issue_number": result.get("number")
        }

    except httpx.HTTPStatusError as e:
        logger.error(f"Issue creation error: {e.response.text}")

        if e.response.status_code == 401:
            raise HTTPException(
                status_code=401,
                detail="Invalid GitHub token"
            )

        if e.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Repository not found or no access"
            )

        raise HTTPException(
            status_code=e.response.status_code,
            detail="Failed to create issue"
        )
    
#GET ALL COMMITS FROM A REPO
@app.get("/repos/{owner}/{repo}/commits")
async def get_all_commits_from_repo(owner: str, repo: str):
    try:
        commits = await fetch_all_commits(owner, repo)
        return {"count": len(commits), "data": commits}

    except httpx.HTTPStatusError as e:
        logger.error(f"Commits fetch error: {e.response.text}")

        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Repository not found")

        raise HTTPException(
            status_code=e.response.status_code,
            detail="Failed to fetch Commits for particular Repo!!"
        )