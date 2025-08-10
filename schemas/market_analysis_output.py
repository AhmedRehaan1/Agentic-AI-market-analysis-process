from pydantic import BaseModel, Field
from typing import List

class MarketAnalysisOutput(BaseModel):
    market_size_egp: float = Field(..., title="Estimated market size in EGP")
    growth_rate_percent: float = Field(..., title="Annual growth rate percentage")
    demand_trends: List[str] = Field(..., title="Key demand trends and drivers")
    competition_levels: str = Field(..., title="Description of competition landscape")
    import_export_volumes: str = Field(..., title="Import and export activity details")
    consumer_segments: List[str] = Field(..., title="Major consumer segments")
    pricing_fluctuations: List[str] = Field(..., title="Recent pricing fluctuations over last 3 years")
    opportunities: List[str] = Field(..., title="Key opportunities in the market")
    risks: List[str] = Field(..., title="Major risks and challenges in the market")
