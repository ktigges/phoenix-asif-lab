from __future__ import annotations


ALLOWED_ENVIRONMENTS = frozenset(
    {
        "development",
        "staging",
        "production",
    }
)


def validate_environment(value: str) -> str:
    normalized = value.strip().lower()
    if not normalized:
        raise ValueError("Deployment environment is required.")
    if normalized not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Unsupported deployment environment: {normalized}.")
    return normalized
