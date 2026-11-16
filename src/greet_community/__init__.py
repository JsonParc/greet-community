"""A friendly greeting package."""


def greet(name: str) -> str:
    """Return a greeting for name, or for the world if name is blank."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
