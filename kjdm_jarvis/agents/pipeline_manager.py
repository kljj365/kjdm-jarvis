"""KJDM Pipeline Manager Agent — monitors stale deals and alerts Kyle.

Schedule in ~/.openjarvis/config.yaml:
  agents:
    - name: kjdm_pipeline_manager
      schedule: "0 8 * * *"
      timezone: America/Chicago
"""
import datetime
from ..tools.crm_pipeline import kjdm_search_opportunities, kjdm_pipeline_summary

STALE_DAYS = {
    "new_lead": 3,
    "contacted": 5,
    "qualified": 7,
    "proposal_sent": 14,
    "negotiating": 7,
}


async def run_pipeline_manager() -> dict:
    """Check for stale deals and return a prioritized action list.

    A deal is 'stale' if it has been in its current stage longer than STALE_DAYS allows.
    Returns a list of stale opportunities sorted by value descending.
    """
    now = datetime.datetime.utcnow()
    stale = []

    for stage, max_days in STALE_DAYS.items():
        result = await kjdm_search_opportunities(stage=stage, limit=100)
        for opp in result.get("opportunities", []):
            last_changed = opp.get("lastStageChangeAt", "")
            if last_changed:
                try:
                    changed_dt = datetime.datetime.fromisoformat(last_changed.replace("Z", "+00:00"))
                    days_stale = (now.replace(tzinfo=datetime.timezone.utc) - changed_dt).days
                    if days_stale >= max_days:
                        stale.append({
                            "name": opp.get("name"),
                            "stage": stage,
                            "value": opp.get("monetaryValue", 0),
                            "days_stale": days_stale,
                            "contact": opp.get("contact", {}).get("name", "Unknown"),
                            "phone": opp.get("contact", {}).get("phone", ""),
                        })
                except Exception:
                    pass

    stale.sort(key=lambda x: x["value"], reverse=True)
    summary = await kjdm_pipeline_summary()

    return {
        "stale_deals": stale,
        "stale_count": len(stale),
        "pipeline_total": summary.get("total", 0),
        "top_priority": stale[0] if stale else None,
    }
