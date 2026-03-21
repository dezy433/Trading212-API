from src.apitConnect.session import AsyncSessionManager


class API:
    """
    High-level API wrapper that exposes Trading212 REST endpoints
    via an authenticated aiohttp session.
    """

    def __init__(self, session: AsyncSessionManager):
        self._session = session

    async def get_account(self) -> dict:
        """Fetch account details."""
        endpoint = "/rest/v1/accounts"
        resp = await self._session.get(endpoint)
        if not resp.ok:
            raise RuntimeError(f"Failed to fetch account details from {endpoint}: HTTP {resp.status}")
        return await resp.json()

    async def get_summary(self) -> dict:
        """Fetch the account summary (open positions, etc.)."""
        endpoint = "/rest/v1/customers/accounts/summary"
        resp = await self._session.get(endpoint)
        if not resp.ok:
            raise RuntimeError(f"Failed to fetch account summary from {endpoint}: HTTP {resp.status}")
        return await resp.json()

    async def get_funds(self) -> dict:
        """Fetch available funds."""
        endpoint = "/rest/v1/customers/accounts/funds"
        resp = await self._session.get(endpoint)
        if not resp.ok:
            raise RuntimeError(f"Failed to fetch funds from {endpoint}: HTTP {resp.status}")
        return await resp.json()

    async def get_supported_tickers(self) -> dict:
        """Fetch the list of supported tickers."""
        endpoint = "/rest/instrument-analyses/v1/summaries/supported-tickers"
        resp = await self._session.get(endpoint)
        if not resp.ok:
            raise RuntimeError(f"Failed to fetch supported tickers from {endpoint}: HTTP {resp.status}")
        return await resp.json()
