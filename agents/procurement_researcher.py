import os
from crewai import Agent, Task, LLM
from schemas.procurement_research_output import ProcurementResearchOutput

output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)

basic_llm = LLM(model="gpt-4o-mini", temperature=0)

procurement_research_agent = Agent(
    role="Procurement Researcher",
    goal=(
        "Conduct detailed procurement research for Lithium Polymer (LiPo) battery packs specifically "
        "within the Egyptian market. Gather verified data on suppliers, prices in EGP and USD, stock levels, "
        "technical specifications, MOQs, warranty terms, shipping, import restrictions, regulatory standards, "
        "and relevant market forecasts up to 2025."
    ),
    backstory=(
        "Experienced procurement specialist focused on high-tech battery components for manufacturing "
        "and consumer electronics in Egypt, skilled in sourcing, negotiation, and regulatory compliance."
    ),
    llm=basic_llm,
    verbose=True,
)

procurement_research_task = Task(
    description=(
        "Perform procurement research for Lithium Polymer (LiPo) battery packs available in Egypt. "
        "Provide detailed, structured data covering suppliers, pricing (EGP/USD), stock, specifications, MOQs, "
        "warranty, shipping within Egypt, import rules, regulatory standards, and market forecasts. "
        "Return output in JSON format matching the defined schema."
    ),
    expected_output="JSON object matching ProcurementResearchOutput schema",
    output_json=ProcurementResearchOutput,
    output_file=os.path.join(output_dir, "procurement_research_output.json"),
    agent=procurement_research_agent
)
