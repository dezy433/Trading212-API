"""
Simple Trading212 Bot Example
Run this script to connect to your Trading 212 account and execute trading operations.
"""

import os
import re
from dotenv import load_dotenv
from apit212_legacy import Apit212

# Load environment variables from .env file (if it exists)
load_dotenv()


def expand_env_var(value):
    """Expand ${VAR_NAME} references in environment variable values"""
    if not value:
        return value
    
    def replace_var(match):
        var_name = match.group(1)
        return os.getenv(var_name, match.group(0))
    
    return re.sub(r'\$\{([^}]+)\}', replace_var, str(value))


def main():
    # Get credentials from environment variables
    # First try TRADING212_* vars, which may contain ${SECRET_*} references that need expansion
    username = expand_env_var(os.getenv("TRADING212_USERNAME")) or os.getenv("USERNAME")
    password = expand_env_var(os.getenv("TRADING212_PASSWORD")) or os.getenv("PASSWORD")
    mode = os.getenv("TRADING212_MODE", "demo")
    
    if not username or not password:
        print("Error: Credentials not found!")
        print("Make sure you have set:")
        print("  - TRADING212_USERNAME (or USERNAME)")
        print("  - TRADING212_PASSWORD (or PASSWORD)")
        print("\nOr add them to .env file:")
        print("  TRADING212_USERNAME=your-email@example.com")
        print("  TRADING212_PASSWORD=your-password")
        return
    
    try:
        print(f"Connecting to Trading212 ({mode} mode)...")
        print(f"Username: {username[:10]}...")  # Show only first 10 chars
        
        # Initialize the client
        client = Apit212()
        
        # Setup with credentials
        client.setup(username=username, password=password, mode=mode, _beauty=False)
        
        print("✓ Connected to Trading 212!")
        
        # Get account information
        print("\n--- Account Information ---")
        account_info = client.get_account()
        print(f"Account: {account_info}")
        
        # Check if validation passed
        if client.auth_validate():
            print("\n✓ Authentication validated successfully!")
        
        # Get funds information
        print("\n--- Account Funds ---")
        funds = client.get_funds()
        print(f"Funds: {funds}")
        
        # Get summary (positions)
        print("\n--- Account Summary ---")
        summary = client.get_summary()
        print(f"Summary: {summary}")
        
        print("\n✓ Bot execution completed successfully!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
