"""OpenJarvis tool — KJDM SMS: bulk outreach and direct messages."""
import datetime
from ..client import client
from ..config import config


async def kjdm_send_bulk_sms(
    contact_ids: list[str],
    message: str,
    campaign_name: str = "",
    schedule_iso: str = "",
) -> dict:
    """Send a bulk SMS to a list of KJDM contacts.

    Args:
        contact_ids: List of CRM contact IDs (max 500 per batch).
        message: SMS body text. Keep under 160 chars for single segment. Always end with 'Reply STOP to opt out.'
        campaign_name: Optional internal campaign label (defaults to today's date).
        schedule_iso: Optional ISO 8601 datetime to schedule send (e.g. '2026-10-15T09:00:00Z'). Omit to send NOW.

    Returns:
        dict with 'id' (bulk request ID) and 'status'.
    """
    if not campaign_name:
        campaign_name = f"KJDM Outreach — {datetime.date.today().isoformat()}"
    if len(message) > 160 and "Reply STOP" not in message:
        message = message[:136] + " Reply STOP to opt out."

    payload = {
        "bulkActionType": "bulk-sms-v2",
        "title": campaign_name,
        "scheduleType": "SCHEDULED" if schedule_iso else "NOW",
        "locationId": config.location_id,
        "documentIds": contact_ids[:500],
        "opSpecs": {
            "opType": "bulk-sms-v2",
            "message": message,
            "fromNumber": config.from_number,
        },
    }
    if schedule_iso:
        payload["scheduleStartAt"] = schedule_iso

    return await client.post("/bulk-actions/request", payload)


async def kjdm_send_direct_sms(contact_id: str, message: str) -> dict:
    """Send a single direct SMS to one KJDM contact.

    Args:
        contact_id: The CRM contact ID.
        message: SMS body text.

    Returns:
        dict with 'messageId' and 'conversationId'.
    """
    payload = {
        "type": "SMS",
        "contactId": contact_id,
        "message": message,
        "fromNumber": config.from_number,
    }
    return await client.post("/conversations/messages", payload)
