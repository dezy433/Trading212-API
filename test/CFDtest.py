from apit212_legacy import Apit212, CFD
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("TRADING212_USERNAME", "test@example.com")
password = os.getenv("TRADING212_PASSWORD", "test_password")
mode = os.getenv("TRADING212_MODE", "demo")

# Initialize and setup the client
client = Apit212()
client.setup(username=username, password=password, mode=mode)


#print(client.auth_validate())
#print(client.get_account())
#print(client.get_funds())
#print(client.get_instruments_info('TSLA'))
#print(client.get_max_min('BT'))
#print(client.limit_order('AAPL', 2, 120, 130))
#print(client.market_order('BT', 1.20, 3000))
#print(client.cancel_order(order_id)) # WILL DELETE PENDING LIMIT ORDERS WILL NEED TO GET THE POSITION ID
#print(client.get_summary()) # GET POSITION ID & PPL
