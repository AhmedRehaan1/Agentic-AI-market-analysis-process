import os
from crewai import Agent, Task, LLM
from schemas.market_analysis_output import MarketAnalysisOutput

output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)

basic_llm = LLM(model="gpt-4o-mini", temperature=0)

market_analyst_agent = Agent(
    role="Market Analyst",
    goal=(
        "Analyze the Egyptian market for Lithium Polymer (LiPo) battery packs based on procurement data. "
        "Identify market size, demand trends, growth rate, competition levels, import/export activities, "
        "consumer segments, and pricing fluctuations over the last 3 years. Highlight opportunities and risks "
        "for procurement decisions."
    ),
    backstory=(
        "You are a data-driven market intelligence expert with experience in renewable energy components "
        "and battery markets in North Africa. Your expertise lies in translating market data into actionable "
        "strategies for procurement and investment teams."
    ),
    llm=basic_llm,
    verbose=True,
)

market_analysis_task = Task(
    description=(
        "Conduct an in-depth market analysis of Lithium Polymer (LiPo) battery packs in Egypt. "
        "Summarize market size, growth forecasts, demand trends, competition, import/export volumes, "
        "consumer segments, pricing fluctuations, opportunities, and risks. "
        "Return output in JSON format matching the defined schema."
    ),
    expected_output="JSON object matching MarketAnalysisOutput schema",
    output_json=MarketAnalysisOutput,
    output_file=os.path.join(output_dir, "market_analysis_output.json"),
    agent=market_analyst_agent
)
