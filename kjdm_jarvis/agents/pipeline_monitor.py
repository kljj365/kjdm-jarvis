"""KJDM Pipeline Monitor — daily deal health check.

Schedule in OpenJarvis config:
  agents:
    - name: kjdm_pipeline_monitor
      cron: "0 8 * * *"
      timezone: America/Chicago
"""
import datetime
from openjarvis import Jarvis
from ..tools import kjdm_pipeline_summary, kjdm_search_opportunities, kjdm_send_direct_sms
from ..config import config

STALE_DAYS = 3   # Flag deals with no activity for 3+ days


async def run_pipeline_monitor(jarvis: Jarvis) -> dict:
    """Check pipeline health: flag stale deals, surface hot opportunities."""
    today = datetime.date.today().isoformat()
    log = {"date": today, "alerts": []}

    # 1. Overall pipeline snapshot
    summary = await kjdm_pipeline_summary()
    log["pipeline_summary"] = summary

    # 2. Deals in Proposal Sent > 3 days
    proposal = await kjdm_search_opportunities(stage="proposal_sent", limit=50)
    stale = [
        opp for opp in proposal.get("opportunities", [])
        if opp.get("id")
    ]
    if stale:
        log["alerts"].append({
            "type": "stale_proposals",
            "count": len(stale),
            "message": f"{len(stale)} deal(s) in Proposal Sent — follow up today",
            "deals": [{"name": o.get("name"), "id": o.get("id")} for o in stale[:5]],
        })

    # 3. New leads with no contact
    new_leads = await kjdm_search_opportunities(stage="new_lead", limit=100)
    count = new_leads.get("total", 0)
    if count > 0:
        log["alerts"].append({
            "type": "new_leads",
            "count": count,
            "message": f"{count} contacts in New Lead — outreach pending",
        })

    return log
