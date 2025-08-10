from pydantic import BaseModel, Field
from typing import List

class ComplianceReportOutput(BaseModel):
    egyptian_standards: List[str] = Field(..., title="Relevant Egyptian standards (EOS)")
    international_certifications: List[str] = Field(..., title="Applicable international certifications (e.g., CE, UN38.3, IEC)")
    transport_restrictions: List[str] = Field(..., title="Restrictions related to transport and storage of LiPo batteries")
    trade_regulations: List[str] = Field(..., title="Trade and import regulations for LiPo batteries in Egypt")
    compliance_actions: List[str] = Field(..., title="Recommended compliance actions to avoid penalties or delays")
    regulatory_bodies: List[str] = Field(..., title="Relevant Egyptian government or regulatory bodies")
    documentation_requirements: List[str] = Field(..., title="Required documentation and testing procedures")
