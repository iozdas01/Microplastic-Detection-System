"""scripts.data — shared data-access layer.

Every module here exposes:
  * a Python API (importable functions), and
  * a CLI (`python -m scripts.data.<module> ...`) that emits JSON to stdout.

Callers: `startup-outreach-intel/scripts/intel_lib.py` (thin orchestrator),
`startup-ideate-shotgun` subagents (invoke via Bash), method cards, ad-hoc use.
"""
