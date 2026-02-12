import unittest
from unittest.mock import MagicMock
from src.use_cases.get_market_snapshot import GetMarketSnapshot
from src.domain.entities.market_quote import MarketQuote
from src.domain.ports.market_data_port import MarketDataPort

class TestGetMarketSnapshot(unittest.TestCase):
    def setUp(self):
        # 1. Create a mock of the Port (The Interface)
        self.mock_port = MagicMock(spec=MarketDataPort)
        # 2. Inject the mock into the Use Case
        self.use_case = GetMarketSnapshot(market_data_port=self.mock_port)

    def test_execute_returns_list_of_quotes(self):
        # Arrange: Setup what the mock should return
        mock_quotes = [
            MarketQuote(ticker="AAPL", bid=150.0, ask=150.1, last=150.05),
            MarketQuote(ticker="MSFT", bid=400.0, ask=400.2, last=400.1)
        ]
        self.mock_port.get_bulk_quotes.return_value = mock_quotes

        # Act
        tickers = ["AAPL", "MSFT"]
        result = self.use_case.execute(tickers)

        # Assert
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].ticker, "AAPL")
        self.mock_port.get_bulk_quotes.assert_called_once_with(tickers)

    def test_execute_with_empty_list(self):
        # Act
        result = self.use_case.execute([])
        
        # Assert
        self.assertEqual(result, [])
        self.mock_port.get_bulk_quotes.assert_not_called()

if __name__ == '__main__':
    unittest.main()
