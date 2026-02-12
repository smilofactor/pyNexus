import streamlit as st
from src.infrastructure.adapters.api.finnhub_adapter import FinnhubAdapter
from src.use_cases.get_market_snapshot import GetMarketSnapshot

# Set up the UI configuration
st.set_page_config(page_title="pyNexus | Equities Monitor", layout="wide")

def main():
    st.title("📊 pyNexus Equities Monitor")
    
    # 1. Initialize the Adapter (Infrastructure Layer)
    # PRO TIP: In a real app, use st.secrets or environment variables for the API Key
    api_key = st.sidebar.text_input("Enter Finnhub API Key", type="password")
    
    if not api_key:
        st.warning("Please enter an API key to fetch live data.")
        return

    adapter = FinnhubAdapter(api_key=api_key)

    # 2. Inject it into the Use Case (Domain Layer)
    # This is "Dependency Injection" - the Use Case doesn't care which adapter it gets
    service = GetMarketSnapshot(market_data_port=adapter)

    # 3. Execution (The Action)
    tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]
    
    if st.button("Refresh Market Data"):
        with st.spinner("Fetching snapshot..."):
            try:
                snapshot = service.execute(tickers)
                st.write(snapshot) # We will format this into a nice table later
            except Exception as e:
                st.error(f"Failed to reconcile market data: {e}")

if __name__ == "__main__":
    main()
