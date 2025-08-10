from pydantic import BaseModel, Field
from typing import List

class ProcurementResearchOutput(BaseModel):
    suppliers: List[str] = Field(..., title="List of verified LiPo battery suppliers in Egypt")
    prices_egp: List[float] = Field(..., title="Corresponding prices in EGP")
    prices_usd: List[float] = Field(..., title="Corresponding prices in USD")
    stock_levels: List[int] = Field(..., title="Available stock quantities")
    technical_specs: List[str] = Field(..., title="Key technical specifications")
    moq: List[int] = Field(..., title="Minimum order quantities")
    warranty_terms: List[str] = Field(..., title="Warranty terms offered by suppliers")
    shipping_options: List[str] = Field(..., title="Available shipping options within Egypt")
    import_restrictions: List[str] = Field(..., title="Import restrictions applicable")
    regulatory_standards: List[str] = Field(..., title="Applicable Egyptian and international regulatory standards")
    market_forecast_2025: str = Field(..., title="Market forecast information for Egypt up to 2025")
