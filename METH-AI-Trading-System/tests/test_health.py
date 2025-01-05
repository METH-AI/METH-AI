from meth_ai.health import portfolio_health_check

def test_portfolio_health_check():
    result = portfolio_health_check({"SOL": 50, "USDC": 1000})
    assert result["status"] == "healthy"
