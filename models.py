from pydantic import BaseModel

class IssueCreate(BaseModel):
    title: str
    body: str