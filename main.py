from crewai import Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

from agents.procurement_researcher import procurement_research_agent, procurement_research_task
from agents.market_analyst import market_analyst_agent, market_analysis_task
from agents.compliance_writer import compliance_writer_agent, compliance_report_task
from agents.report_enhancer import report_enhancer_agent, report_enhancer_task

# Shared context/knowledge source for all agents
company_context = StringKnowledgeSource(
    content=(
        "This project involves researching and procuring Lithium Polymer (LiPo) battery packs in Egypt. "
        "The goal is to identify suppliers, analyze market trends, ensure compliance with local and international standards, "
        "and produce a comprehensive report."
    ),
)

procurement_crew = Crew(
    agents=[
        procurement_research_agent,
        market_analyst_agent,
        compliance_writer_agent,
        report_enhancer_agent,
    ],
    tasks=[
        procurement_research_task,
        market_analysis_task,
        compliance_report_task,
        report_enhancer_task,
    ],
    process=Process.sequential,  # Run tasks sequentially
    knowledge_sources=[company_context],  # Pass shared context
    verbose=True,
)

if __name__ == "__main__":
    results = procurement_crew.kickoff()
    print("Crew run completed.")
    # Optionally, print or handle results here
