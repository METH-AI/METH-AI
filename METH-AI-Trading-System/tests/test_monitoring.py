from meth_ai.monitoring import analyze_wallet

def test_analyze_wallet():
    result = analyze_wallet("test_wallet")
    assert "wallet" in result
