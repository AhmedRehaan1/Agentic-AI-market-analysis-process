from pydantic import BaseModel, Field

class LatexReportOutput(BaseModel):
    latex_code: str = Field(..., title="Complete LaTeX code for the final report ready for Overleaf")
