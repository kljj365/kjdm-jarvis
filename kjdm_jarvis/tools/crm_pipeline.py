"""OpenJarvis tool — KJDM pipeline: search opportunities, move stages, get summary."""
from ..client import client
from ..config import config

PIPELINE_ID = "kc3gfNOzkZjDO55cgBEf"
STAGES = {
    "new_lead":       "da6a71a2-4f33-4e45-af93-f247bdaf7e35",
    "contacted":      "656b04a5-931a-4d7e-b0d5-e3b17d93ad05",
    "qualified":      "94e6a5d8-e91d-4c2c-8b75-0b53cd7a5fef",
    "proposal_sent":  "e488882b-43ad-4fba-b7f1-ec49ce375a57",
    "negotiating":    "8e75b2d9-17f6-4469-b24e-a927f777a0e5",
    "closed_won":     "6d1b93e7-ceab-4cc0-ab36-08e8eeeb694a",
    "closed_lost":    "a4a64118-f6c7-42ba-8350-f6de10f6a366",
}


async def kjdm_pipeline_summary() -> dict:
    """Get a summary of the KJDM sales pipeline — total deals and value per stage.

    Returns:
        dict with stage counts and total open value.
    """
    payload = {
        "locationId": config.location_id,
        "limit": 1,
        "page": 0,
        "filters": [
            {"field": "pipeline_id", "operator": "eq", "value": PIPELINE_ID},
            {"field": "status", "operator": "eq", "value": "open"},
        ],
    }
    result = await client.post("/opportunities/search", payload)
    aggs = result.get("aggregations", {}).get("stageAggregations", [])
    stage_names = {v: k for k, v in STAGES.items()}
    summary = {}
    for stage in aggs:
        name = stage_names.get(stage.get("pipelineStageId", ""), "unknown")
        summary[name] = {
            "count": stage.get("totalCount", 0),
            "open_value": stage.get("openValue", 0),
        }
    return {"total": result.get("total", 0), "stages": summary}


async def kjdm_search_opportunities(query: str = "", stage: str = "", limit: int = 20) -> dict:
    """Search KJDM opportunities by contact name or stage.

    Args:
        query: Free-text search on contact name or opportunity name.
        stage: Filter by stage name: new_lead, contacted, qualified, proposal_sent, negotiating, closed_won, closed_lost.
        limit: Max results (default 20).

    Returns:
        dict with 'opportunities' list and 'total'.
    """
    filters = [
        {"field": "pipeline_id", "operator": "eq", "value": PIPELINE_ID},
    ]
    if stage and stage in STAGES:
        filters.append({"field": "pipeline_stage_id", "operator": "eq", "value": STAGES[stage]})

    payload = {
        "locationId": config.location_id,
        "limit": min(limit, 100),
        "page": 0,
        "filters": filters,
    }
    if query:
        payload["query"] = query[:75]

    result = await client.post("/opportunities/search", payload)
    return {"opportunities": result.get("opportunities", []), "total": result.get("total", 0)}
