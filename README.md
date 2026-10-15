# Project Phoenix AISF lab

This repository is a synthetic application for testing a GitHub Copilot AI Software Factory workflow.

The factory uses three custom agents:

- `aisf-planner`
- `aisf-executor`
- `aisf-judge`

## Application

`phoenix_config` validates the deployment environment for Project Phoenix.

Allowed values:

- `development`
- `staging`
- `production`

Run the tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

The initial repository intentionally lacks coverage for invalid environment values. The first AISF task should identify the missing test, make the smallest correction, and leave the result for human review.
