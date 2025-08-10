# Lithium Polymer (LiPo) Battery Procurement & Market Analysis in Egypt




## Project Overview
This project implements an AI-powered multi-agent system designed to research, analyze, and report on the procurement of Lithium Polymer (LiPo) battery packs within the Egyptian market. Leveraging the CrewAI framework and large language models (LLMs), it automates data gathering, market analysis, regulatory compliance, and report generation.

The final output includes structured JSON data and a professionally formatted LaTeX report, ready for publication and presentation.

## Features
- Procurement Research Agent: Gathers supplier data, pricing, stock levels, technical specs, and more.
- Market Analyst Agent: Analyzes market size, trends, competition, risks, and opportunities.
- Regulatory Compliance Agent: Reviews local and international compliance requirements and standards.
- Report Enhancer Agent: Compiles all findings into a comprehensive LaTeX report ready for Overleaf.
- Sequential task execution: Ensures organized workflow with clear dependencies.
- Environment variable management: Secure API key handling using .env.
- Extensible architecture: Easily add or modify agents and tasks.
- Output: JSON structured outputs and a final LaTeX report.

## Project Structure
<img width="348" height="627" alt="Image" src="https://github.com/user-attachments/assets/0105cee7-203b-4f96-aa0f-d1a4405c2ad4" />

## Architecture & Crew Flow
<img width="1001" height="3840" alt="Image" src="https://github.com/user-attachments/assets/cdb6d3cf-0186-4a5c-9763-35ed542ab3eb" />
The solution is structured around a CREW of four agents, each responsible for a dedicated research or processing task. The agents execute sequentially, passing their outputs downstream:

Procurement Researcher Agent collects and structures supplier, pricing, stock, technical specs, warranty, shipping, import restrictions, and market forecast data.

Market Analyst Agent interprets procurement data to assess market size, growth, demand trends, competition, pricing fluctuations, opportunities, and risks.

Regulatory Compliance Officer Agent reviews research and analysis findings to identify applicable Egyptian and international standards, transport restrictions, certification needs, and recommends compliance strategies.

Technical Report Editor Agent consolidates all previous outputs and generates a fully formatted LaTeX report for Overleaf, including summaries, tables, bullet points, and references.

This pipeline ensures a thorough, expert-level synthesis of procurement intelligence, market insights, regulatory adherence, and report production.

## Detailed Agent Roles
# 1. Procurement Researcher Agent
Role: Procurement Research Specialist

Goal: Conduct exhaustive research on LiPo battery suppliers in Egypt, collecting verified data on prices (EGP & USD), stock levels, technical specs, minimum order quantities, warranty terms, shipping options, import restrictions, regulatory standards, and provide a market forecast for 2025.

Output: Structured JSON dataset detailing supplier and market info.

Expertise: Procurement, supplier vetting, regulatory knowledge in battery components.

# 2. Market Analyst Agent
Role: Market Intelligence Expert

Goal: Analyze procurement data to assess Egyptian LiPo battery market size, annual growth rate, demand trends, competition landscape, import/export volumes, consumer segmentation, pricing trends, and identify opportunities and risks.

Output: JSON report with market metrics and strategic insights.

Expertise: Market analysis, data-driven strategy, North African battery markets.

# 3. Regulatory Compliance Officer Agent
Role: Compliance & Safety Consultant

Goal: Review findings to identify Egyptian standards (EOS), international certifications (CE, UN38.3, IEC), transport/storage restrictions, trade regulations, and recommend compliance actions to mitigate risks and ensure smooth import and sales processes.

Output: JSON summary of compliance requirements and recommended actions.

Expertise: Regulatory frameworks, safety standards, import/export legalities.

# 4. Technical Report Editor Agent
Role: Technical Writer & LaTeX Specialist

Goal: Compile the procurement, market, and compliance outputs into a professional LaTeX report ready for Overleaf, including title page, table of contents, executive summary, sections with detailed findings, tables, bullet points, conclusions, and references.

Output: Complete LaTeX document source code.

Expertise: Technical writing, document formatting, LaTeX proficiency.
## Final report output
[Procurement_report.pdf](https://github.com/user-attachments/files/21707083/Procurement_report.pdf)


