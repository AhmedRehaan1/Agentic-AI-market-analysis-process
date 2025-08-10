import os
from crewai import Agent, Task, LLM
from schemas.compliance_report_output import ComplianceReportOutput

output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)

basic_llm = LLM(model="gpt-4o-mini", temperature=0)

compliance_writer_agent = Agent(
    role="Regulatory Compliance Officer",
    goal=(
        "Review procurement and market research findings for LiPo battery packs in Egypt, "
        "and identify all relevant safety, quality, and trade regulations. Include Egyptian standards (EOS), "
        "international certifications (CE, UN38.3, IEC), and any restrictions on transport or storage. "
        "Recommend compliance actions to avoid penalties or delays."
    ),
    backstory=(
        "You are a regulatory compliance consultant with a decade of experience in electronics "
        "and battery manufacturing sectors. You are highly skilled at navigating Egypt’s standards frameworks "
        "and aligning procurement processes with both domestic and international legal requirements."
    ),
    llm=basic_llm,
    verbose=True,
)

compliance_report_task = Task(
    description=(
        "Review Egyptian regulations, safety standards, and certification requirements for importing "
        "and selling Lithium Polymer (LiPo) battery packs. Include relevant government bodies, required "
        "documentation, testing procedures, and compliance recommendations. "
        "Return output in JSON format matching the defined schema."
    ),
    expected_output="JSON object matching ComplianceReportOutput schema",
    output_json=ComplianceReportOutput,
    output_file=os.path.join(output_dir, "compliance_report_output.json"),
    agent=compliance_writer_agent
)
