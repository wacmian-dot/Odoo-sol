## Purpose

These are hard technical questions worth putting to RRUP's engineering team directly, ideally in a technical call once a technical point of contact is established (likely after the commercial questions in Folder 13 are settled). They were originally drafted as a Polish-language technical briefing and have been translated and verified here as genuinely the right category of question to ask before committing.

## The questions

1. **SAP/API integration.** How are your REST APIs or web-service schemas optimized for real-time transfer of finalized contracts, project tokens, and e-signatures into a SAP S/4HANA database without transactional latency?
2. **Data migration tooling.** What ETL tools or standardized bulk-migration scripts does your engineering team use to safely map historical customer metrics from HubSpot/Salesforce/spreadsheets into SalesOps?
3. **Offline field sync.** How does the local browser storage/offline sync engine protect data integrity and prevent file loss for field technicians working in low-signal UK areas, before the office dashboard next updates?
4. **CPQ localization depth.** How modular is the pricing/calculation logic for adapting to UK-specific technical metrics — BTU units, heat pump COP coefficients, regional roof-pitch/shading factors for solar?
5. **Regulatory automation depth.** Are the MCS/ECO4/DNO "Procedure Patterns" hard-coded configuration templates, or does the implementation team build them from scratch per client? This materially affects onboarding speed and cost.
6. **Database/photo-storage performance at scale.** How is the central cloud repository built to handle high-volume multi-tier photo galleries with permission controls as the UK user base grows, without degrading real-time search/query speed?
7. **Onboarding telemetry.** What user telemetry or activity thresholds does RRUP monitor in the first 30 days that signal successful adoption, and can your team access this data to catch at-risk trial accounts early?
8. **Data residency/GDPR.** Will the UK operation run on a fully isolated, local multi-tenant cloud environment, or share instances with existing continental European data centres? This is a real UK GDPR question with a real compliance answer needed, not a formality.
9. **Technical debt guardrails.** What technical guardrails need to be established early to prevent configuration debt that would slow future system updates?
10. **Team-scaling permissions.** Do user access/permission levels allow cleanly isolating a prospecting environment from core sales data as the team grows past the initial pod, without system changes?
11. **The Polsat question, asked properly.** From a systems-architecture perspective, if a large enterprise deployment like Grupa Polsat Plus is real, how was it scaled across corporate divisions on the RRUP core, and what database/field-crew-coordination bottlenecks did the technical team have to solve? **This is the right way to raise Polsat — as a question for RRUP to answer and substantiate, not a claim to make first.** See Folder 01 and Folder 13, Question 6.

## When to use this list

After the commercial reset with the CEO (Folder 13) establishes the real deal structure and a working relationship, and ideally once you also have working demo access (currently blocked — see Folder 01, §6). Technical due diligence is most useful once you know what kind of relationship you're actually diligencing for.
