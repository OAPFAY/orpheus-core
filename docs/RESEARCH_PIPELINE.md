# ORPHEUS Research & Intelligence Pipeline

## Pipeline Stages
1. **RESEARCH REQUEST**: Define the target (Kaimana socio-economic, market opportunity, tech stack, or product validation).
2. **WEB / DATA SOURCES**: Execute structured lookups via DuckDuckGo search, web extraction, and local BPS dataset caches.
3. **DOCUMENT EXTRACTION**: Parse local PDF/text sources via Python lightweight text extractors (PyMuPDF / pypdf) without heavy background daemons.
4. **ANALYSIS**: Synthesize findings using rigorous epistemological classification (FACT / INFERENCE / HYPOTHESIS / UNKNOWN).
5. **EVIDENCE / SOURCE TRACKING**: Attach explicit file paths, URLs, page numbers, and confidence levels to every claim.
6. **KNOWLEDGE OUTPUT**: Produce standardized markdown reports or structured Excel workbooks.
7. **GITHUB VERSIONING**: Automatically commit and push research artifacts to `orpheus-core` under `audits/` or `docs/`.
