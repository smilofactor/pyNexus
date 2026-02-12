from typing import List
from src.domain.entities.market_quote import MarketQuote
from src.domain.ports.market_data_port import MarketDataPort

class GetMarketSnapshot:
    """
    Use Case: Orchestrates the retrieval of market data for a list of tickers.
    Follows Hexagonal Architecture by depending only on the Outbound Port.
    """
    def __init__(self, market_data_port: MarketDataPort):
        self.market_data_port = market_data_port

    def execute(self, tickers: List[str]) -> List[MarketQuote]:
        if not tickers:
            return []
        
        # In a more complex version, this is where we would add:
        # - Validation (Are these valid tickers?)
        # - Caching (Do we already have this data?)
        # - Logging/Tracing (Porting your 'Tracer' logic from PLNexus)
        
        try:
            return self.market_data_port.get_bulk_quotes(tickers)
        except Exception as e:
            # Senior Move: Don't let infrastructure errors crash the domain
            print(f"Domain Error: Use case failed to retrieve market data. {e}")
            raise e
