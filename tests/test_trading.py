from meth_ai.trading import execute_trade

def test_execute_trade():
    result = execute_trade({"asset": "SOL", "action": "buy", "amount": 10})
    assert result["status"] == "success"
