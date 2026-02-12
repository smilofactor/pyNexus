from dataclasses import dataclass

@dataclass(frozen=True) # Immutable entities are safer for finance
class MarketQuote:
    ticker: str
    bid: float
    ask: float
    last: float

    @property
    def spread(self) -> float:
        return round(self.ask - self.bid, 4)

    @property
    def mid_price(self) -> float:
        return (self.bid + self.ask) / 2
