import pytest
from app import app

@pytest.fixture
def CovalentAPI():
    with app.test_client() as CovalentAPI:
        yield CovalentAPI

# 4 classes:
# each one related tests

class TestHomePage:
    def test_home(self, CovalentAPI):
        response = CovalentAPI.get('/')
        assert response.data == b'Covalent Crypto Wallet API'

class TestAssets:
    def test_get_assets(self, CovalentAPI):
        response = CovalentAPI.get('/assets?wallet_address=0x6105f0b07341eE41562fd359Ff705a8698Dd3109')
        assert response.status_code == 200

class TestTotalBalance:
    def test_get_total_value_data(self, CovalentAPI):
        response = CovalentAPI.get('/total_value?wallet_address=0x6105f0b07341eE41562fd359Ff705a8698Dd3109')
        assert response.status_code == 200
    
    def test_total_balance_not_negative(self, CovalentAPI):
        # balance cannot be negative
        response = CovalentAPI.get('/total_value?wallet_address=0x6105f0b07341eE41562fd359Ff705a8698Dd3109')
        assert response.status_code == 200
        data = response.get_json()
        total_usd_value = data['total_usd_value']
        assert isinstance(total_usd_value, (int, float))
        assert total_usd_value >= 0  

class TestTransactions:
    def test_get_transactions(self, CovalentAPI):
        response = CovalentAPI.get('/transactions?wallet_address=0x6105f0b07341eE41562fd359Ff705a8698Dd3109')
        assert response.status_code == 200

