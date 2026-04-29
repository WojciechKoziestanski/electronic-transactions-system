import httpx
from config import settings

class StripeClient:
    def __init__(self):
        self.base_url = "https://api.stripe.com/v1"
        self.headers = {"Authorization": f"Bearer {settings.stripe_secret_key_sandbox}"}

    async def create_payment_intent(self, amount: int):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/payment_intents",
                headers=self.headers,
                data={"amount": amount, "currency": "usd"}
            )
            response.raise_for_status()
            return response.json()

class AiraloClient:
    def __init__(self):
        self.base_url = "https://sandbox-api.airalo.com/v2"
        self.headers = {
            "client_id": settings.airalo_api_key,
            "client_secret": settings.airalo_api_secret
        }

    async def get_esim_packages(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/packages", headers=self.headers)
            response.raise_for_status()
            return response.json()