"""OpenJarvis tool — KJDM Courses: list available training courses."""
from ..client import client
from ..config import config


async def kjdm_list_courses(limit: int = 20) -> dict:
    """List all KJDM training courses available for ambassadors.

    Args:
        limit: Max courses to return (default 20).

    Returns:
        dict with 'courses' list (id, title, description).
    """
    result = await client.get(
        f"/membership/locations/{config.location_id}/products",
        params={"limit": limit, "offset": 0},
    )
    courses = [
        {"id": c.get("id"), "title": c.get("title"), "description": c.get("description", "")[:120]}
        for c in result.get("products", [])
    ]
    return {"courses": courses, "total": result.get("count", len(courses))}
