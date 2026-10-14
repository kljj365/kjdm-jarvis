"""KJDM Daily Outreach Agent — runs at 9 AM CDT via OpenJarvis cron scheduler.

Schedule in ~/.openjarvis/config.yaml:
  agents:
    - name: kjdm_daily_outreach
      schedule: "0 9 * * *"
      timezone: America/Chicago
"""
import datetime
from ..tools.crm_contacts import kjdm_search_contacts
from ..tools.crm_sms import kjdm_send_bulk_sms
from ..tools.crm_pipeline import kjdm_pipeline_summary


async def run_daily_outreach() -> dict:
    """KJDM daily outreach agent — pull new leads, send batch SMS, log pipeline summary.

    Runs every morning at 9 AM CDT.
    1. Pull contacts tagged 'new-prospect-received' with no SMS sent today.
    2. Send batch intro SMS to up to 50 contacts.
    3. Log pipeline summary to stdout.
    4. Return summary dict.
    """
    today = datetime.date.today().isoformat()

    # 1. Find new prospects (recently added, not yet contacted)
    result = await kjdm_search_contacts(
        query="new-prospect-received",
        limit=50,
    )
    contacts = result.get("contacts", [])
    contact_ids = [c["id"] for c in contacts if c.get("id")]

    outreach_result = {}
    if contact_ids:
        outreach_result = await kjdm_send_bulk_sms(
            contact_ids=contact_ids,
            message=(
                "Hey - I'm Kyle, local digital marketing in STL. "
                "Built your business a free updated website. "
                "Hosting is $97/year. Want me to send it over? "
                "Reply STOP to opt out."
            ),
            campaign_name=f"Daily Outreach — {today}",
        )

    # 2. Pipeline summary
    pipeline = await kjdm_pipeline_summary()

    return {
        "date": today,
        "contacts_messaged": len(contact_ids),
        "sms_request_id": outreach_result.get("id", "none"),
        "pipeline_total": pipeline.get("total", 0),
        "pipeline_stages": pipeline.get("stages", {}),
    }
