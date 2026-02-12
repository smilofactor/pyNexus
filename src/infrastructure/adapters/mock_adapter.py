import random
from src.domain.ports.market_data_port import MarketDataPort
from src.domain.entities.market_quote import MarketQuote

class MockMarketAdapter(MarketDataPort):
    """
    Simulates a real-time feed. 
    Implements the MarketDataPort interface.
    """
    def get_quote(self, ticker: str) -> MarketQuote:
        # Simulate a price around a fixed point
        base_price = 150.0
        bid = round(base_price + random.uniform(-1, 1), 2)
        ask = round(bid + 0.10, 2)
        return MarketQuote(ticker=ticker, bid=bid, ask=ask, last=bid + 0.05)

    def get_bulk_quotes(self, tickers: list[str]) -> list[MarketQuote]:
        return [self.get_quote(t) for t in tickers]
