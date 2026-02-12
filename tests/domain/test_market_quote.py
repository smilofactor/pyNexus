import unittest
from src.domain.entities.market_quote import MarketQuote

class TestMarketQuote(unittest.TestCase):
    def test_spread_calculation(self):
        # Arrange
        quote = MarketQuote(ticker="AAPL", bid=150.00, ask=150.10, last=150.05)
        # Act & Assert
        self.assertEqual(quote.spread, 0.10)

    def test_mid_price(self):
        quote = MarketQuote(ticker="NVDA", bid=700.00, ask=701.00, last=700.50)
        self.assertEqual(quote.mid_price, 700.50)

if __name__ == '__main__':
    unittest.main()
