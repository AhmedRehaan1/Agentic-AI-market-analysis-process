import os
from crewai import Agent, Task, LLM
from schemas.latex_report_output import LatexReportOutput

output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)

basic_llm = LLM(model="gpt-4o-mini", temperature=0)

report_enhancer_agent = Agent(
    role="Technical Report Editor",
    goal=(
        "Convert the combined procurement, market, and compliance JSON outputs on LiPo battery packs in Egypt "
        "into a fully formatted LaTeX report suitable for Overleaf. The LaTeX code must compile without errors "
        "and include: title page, table of contents, executive summary, sections for Procurement Research, "
        "Market Analysis, Compliance Review, tables, bullet points for key findings, conclusion, and references."
    ),
    backstory=(
        "You are an expert technical writer and LaTeX formatting specialist, known for producing "
        "publication-ready reports for procurement and market research projects. You transform raw technical data "
        "into structured, professional, and visually appealing documents."
    ),
    llm=basic_llm,
    verbose=True,
)

report_enhancer_task = Task(
    description=(
        "Take JSON outputs from Procurement Research, Market Analysis, and Compliance Review and generate a "
        "complete LaTeX report suitable for Overleaf. The LaTeX must include a title page, table of contents, "
        "executive summary, sections with detailed content, tables, bullet points, conclusions, and references. "
        "Output a string containing the entire LaTeX document."
    ),
    expected_output="JSON object matching LatexReportOutput schema",
    output_json=LatexReportOutput,
    output_file=os.path.join(output_dir, "final_report.tex"),
    agent=report_enhancer_agent
)
