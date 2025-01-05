from meth_ai.efficiency import optimize_strategy

def test_optimize_strategy():
    result = optimize_strategy({"risk_level": "medium"})
    assert "optimized_strategy" in result
