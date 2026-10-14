"""Async HTTP client that bridges OpenJarvis tools to copilot.kljj365.com."""
import httpx
from .config import config


class KJDMClient:
    """Thin async wrapper around the KJDM AI connector API."""

    def __init__(self):
        self._base = config.api_base.rstrip("/")
        self._headers = {
            "Authorization": f"Bearer {config.ai_token}",
            "Content-Type": "application/json",
            "X-Location-Id": config.location_id,
        }

    async def post(self, path: str, payload: dict) -> dict:
        """POST to the KJDM AI connector and return parsed JSON."""
        url = f"{self._base}/{path.lstrip('/')}"
        async with httpx.AsyncClient(timeout=30) as http:
            r = await http.post(url, json=payload, headers=self._headers)
            r.raise_for_status()
            return r.json()

    async def get(self, path: str, params: dict | None = None) -> dict:
        """GET from the KJDM AI connector and return parsed JSON."""
        url = f"{self._base}/{path.lstrip('/')}"
        async with httpx.AsyncClient(timeout=30) as http:
            r = await http.get(url, params=params, headers=self._headers)
            r.raise_for_status()
            return r.json()


# Singleton
client = KJDMClient()
