import requests
from src.domain.ports.market_data_port import MarketDataPort
from src.domain.entities.market_quote import MarketQuote

class FinnhubAdapter(MarketDataPort):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://finnhub.io/api/v1"

    def get_quote(self, ticker: str) -> MarketQuote:
        # The 'Real' fetch logic
        response = requests.get(
            f"{self.base_url}/quote", 
            params={"symbol": ticker, "token": self.api_key}
        )
        response.raise_for_status() # Heavyweight move: Handle HTTP errors immediately
        data = response.json()
        
        # Mapping the external API response (c, b, a) to our internal Entity
        return MarketQuote(
            ticker=ticker,
            bid=data.get('b', 0.0),
            ask=data.get('a', 0.0),
            last=data.get('c', 0.0)
        )

    def get_bulk_quotes(self, tickers: list[str]) -> list[MarketQuote]:
        return [self.get_quote(t) for t in tickers]
