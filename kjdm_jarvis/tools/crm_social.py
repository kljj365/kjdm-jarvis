"""OpenJarvis tool — KJDM Social: schedule posts across all 5 platforms."""
from ..client import client
from ..config import config

ACCOUNT_IDS = [
    "69fbec894eda2642fed2e2fb_8aFwDTRcK3eSimUXIFZv_104245428833133_page",   # Facebook KJDM
    "69fbecab26d51158c66ecfb8_8aFwDTRcK3eSimUXIFZv_17841440554103249",      # Instagram
    "69fbed0753c746f852f5e2e0_8aFwDTRcK3eSimUXIFZv_81511988_page",          # LinkedIn
    "6a59bfd371fc08c4d3b09623_8aFwDTRcK3eSimUXIFZv_25157117683967140_profile",  # Threads
    "6a1611ba680c26fab2c75c90_8aFwDTRcK3eSimUXIFZv_did:plc:fxiykzoepe63j6acbmyhzh5h_profile",  # Bluesky
]


async def kjdm_schedule_social_post(
    caption: str,
    image_url: str = "",
    schedule_iso: str = "",
) -> dict:
    """Schedule a social media post to all 5 KJDM platforms simultaneously.

    Args:
        caption: Post caption / body text. Max 30 hashtags for Instagram.
        image_url: Optional public URL of the image to attach.
        schedule_iso: ISO 8601 datetime for scheduled send (e.g. '2026-10-15T21:00:00Z').
                      Required — provide at least 5 minutes in the future.

    Returns:
        dict with 'postId' on success.
    """
    if not schedule_iso:
        raise ValueError("schedule_iso is required. Provide an ISO datetime at least 5 minutes in the future.")

    payload = {
        "type": "post",
        "accountIds": ACCOUNT_IDS,
        "summary": caption,
        "status": "scheduled",
        "scheduleDate": schedule_iso,
        "userId": "RCQkx5dEK5MjZ98JOUeS",
    }
    if image_url:
        payload["media"] = [{"url": image_url, "type": "image/png"}]

    return await client.post(f"/social-media-posting/{config.location_id}/posts", payload)
