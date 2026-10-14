"""OpenJarvis tool — KJDM CRM contacts: search, create, tag."""
from ..client import client
from ..config import config


async def kjdm_search_contacts(query: str, limit: int = 20) -> dict:
    """Search KJDM CRM contacts by name, email, phone, or company.

    Args:
        query: Free-text search (name, email, phone, or company).
        limit: Max results to return (default 20, max 100).

    Returns:
        dict with 'contacts' list and 'total' count.
    """
    payload = {
        "locationId": config.location_id,
        "pageLimit": min(limit, 100),
        "page": 1,
        "query": query[:75],
        "projection": ["id", "firstName", "lastName", "email", "phone", "city", "state", "companyName", "tags"],
    }
    result = await client.post("/contacts/search", payload)
    contacts = result.get("contacts", [])
    return {"contacts": contacts, "total": result.get("total", len(contacts))}


async def kjdm_create_contact(
    first_name: str,
    last_name: str = "",
    email: str = "",
    phone: str = "",
    company: str = "",
    city: str = "",
    state: str = "",
    tags: list[str] | None = None,
) -> dict:
    """Create a new contact in the KJDM CRM.

    Args:
        first_name: Contact first name (required).
        last_name: Contact last name.
        email: Email address.
        phone: Phone in E.164 format (e.g. +13145551234).
        company: Company or business name.
        city: City.
        state: State abbreviation (e.g. MO).
        tags: List of tags to apply.

    Returns:
        dict with the new contact 'id' and 'firstName'.
    """
    payload = {
        "locationId": config.location_id,
        "firstName": first_name,
    }
    if last_name:  payload["lastName"] = last_name
    if email:      payload["email"] = email
    if phone:      payload["phone"] = phone
    if company:    payload["companyName"] = company
    if city:       payload["city"] = city
    if state:      payload["state"] = state
    if tags:       payload["tags"] = tags

    return await client.post("/contacts/", payload)
