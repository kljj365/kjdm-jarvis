"""KJDM OpenJarvis Agents — scheduled autonomous agents."""
from .daily_outreach import run_daily_outreach
from .pipeline_manager import run_pipeline_manager
from .content_creator import run_content_creator

KJDM_AGENTS = {
    "kjdm_daily_outreach": run_daily_outreach,
    "kjdm_pipeline_manager": run_pipeline_manager,
    "kjdm_content_creator": run_content_creator,
}

__all__ = ["KJDM_AGENTS", "run_daily_outreach", "run_pipeline_manager", "run_content_creator"]
