"""KJDM configuration — load from environment variables."""
import os
from dataclasses import dataclass


@dataclass
class KJDMConfig:
    """Runtime config loaded from environment."""
    api_base: str = os.getenv("KJDM_API_BASE", "https://copilot.kljj365.com/ai")
    ai_token: str = os.getenv("KJDM_AI_TOKEN", "")
    location_id: str = os.getenv("KJDM_LOCATION_ID", "8aFwDTRcK3eSimUXIFZv")
    from_number: str = os.getenv("KJDM_FROM_NUMBER", "+18558570683")
    timezone: str = "America/Chicago"

    # Brand
    brand_name: str = "Kyle Johnson Digital Marketing"
    brand_bg: str = "#090911"
    brand_primary: str = "#F97316"
    brand_text: str = "#F0F0FF"
    brand_font: str = "Inter"

    def validate(self) -> None:
        if not self.ai_token:
            raise EnvironmentError(
                "KJDM_AI_TOKEN is not set. "
                "Add it to your .env file: KJDM_AI_TOKEN=<your-token>"
            )


# Singleton
config = KJDMConfig()
