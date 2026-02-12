from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.market_quote import MarketQuote

class MarketDataPort(ABC):
    @abstractmethod
    def get_quote(self, ticker: str) -> MarketQuote:
        """Fetch a single market quote for a given ticker."""
        pass

    @abstractmethod
    def get_bulk_quotes(self, tickers: List[str]) -> List[MarketQuote]:
        """Fetch multiple quotes at once for portfolio analysis."""
        pass
