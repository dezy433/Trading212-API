import aiohttp

from src.apitConnect.session import AsyncSessionManager


class API:
    """
    Provides structured REST API endpoints using the authenticated session manager.
    """

    def __init__(self, session: AsyncSessionManager):
        self._session = session

    async def get_account(self) -> dict:
        """Returns account data."""
        resp = await self._session.get("/rest/v1/accounts")
        try:
            return await resp.json(content_type=None)
        except (aiohttp.ContentTypeError, ValueError) as e:
            print(f"get_account error: {e}")
            return {}

    async def auth_validate(self) -> dict:
        """Validates the current session."""
        resp = await self._session.get("/auth/validate")
        try:
            return await resp.json(content_type=None)
        except (aiohttp.ContentTypeError, ValueError) as e:
            print(f"auth_validate error: {e}")
            return {}

    async def get_funds(self) -> dict:
        """Returns account funds."""
        resp = await self._session.get("/rest/v2/customer/accounts/funds")
        try:
            return await resp.json(content_type=None)
        except (aiohttp.ContentTypeError, ValueError) as e:
            print(f"get_funds error: {e}")
            return {}

    async def get_summary(self) -> dict:
        """Returns account summary (positions)."""
        resp = await self._session.get(
            "/rest/v1/customers/accounts/summary"
        )
        try:
            return await resp.json(content_type=None)
        except (aiohttp.ContentTypeError, ValueError) as e:
            print(f"get_summary error: {e}")
            return {}
