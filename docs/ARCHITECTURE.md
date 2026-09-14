# ORPHEUS Architecture Documentation

## Overview
ORPHEUS is structured as a Unified Personal Assistant infrastructure designed for high-precision, evidence-traceable operations under local-first principles.

## Data Flow & Integration Hierarchy
```
[ ORPHEUS / Agent O ]
        │
        ▼
[ Hermes Agent (Profile: best-condition) ]
        │
        ▼ (Local HTTP / OpenAI Compatible)
[ 9Router Gateway (localhost:20128) ]
        │
        ▼
[ Cloud / Free Elite Models (Gemini Flash Lite, Nemotron, Deepseek) ]
```

## External Resource Roles
- **GitHub (`OAPFAY/orpheus-core`)**: Source control for automation scripts, non-secret configuration templates, skill definitions, documentation, and audit reports.
- **Hugging Face (`OAPFAY`)**: Remote AI resources, dataset storage, and private model artifacts.
