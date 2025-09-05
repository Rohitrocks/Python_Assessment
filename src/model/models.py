from pydantic import BaseModel, Field
from typing import Union, List

class FixDocumentRequest(BaseModel):
    text: str = Field(..., description="The text of the document to be fixed.")

class ComplianceDetail(BaseModel):
    message: str
    context: str
    replacements: List[str]

class ReportSummary(BaseModel):
    issue_count: int
    clarity_score: Union[int, str]

class ComplianceReport(BaseModel):
    summary: ReportSummary
    details: List[ComplianceDetail]
    ai_analysis: str

class CheckDocumentResponse(BaseModel):
    report: ComplianceReport
    original_text: str