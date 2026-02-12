import unittest
from src.infrastructure.adapters.mock_adapter import MockMarketAdapter
from src.domain.entities.market_quote import MarketQuote

class TestMockAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = MockMarketAdapter()

    def test_adapter_returns_valid_quote_type(self):
        # Act
        quote = self.adapter.get_quote("AAPL")
        
        # Assert
        self.assertIsInstance(quote, MarketQuote)
        self.assertEqual(quote.ticker, "AAPL")
        self.assertGreater(quote.ask, quote.bid) # Financial Sanity Check

if __name__ == '__main__':
    unittest.main()
