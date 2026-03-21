"""
Trading212 API - Main entry point.

Run bot_example.py for a ready-to-use trading bot, or import
src.apitConnect.client.Client to build your own integration.
"""

import os
import re
from dotenv import load_dotenv
from apit212_legacy import Apit212, CFD

load_dotenv()


def expand_env_var(value):
    """Expand ${VAR_NAME} references in environment variable values."""
    if not value:
        return value

    def replace_var(match):
        var_name = match.group(1)
        return os.getenv(var_name, match.group(0))

    return re.sub(r'\$\{([^}]+)\}', replace_var, str(value))


def main():
    username = expand_env_var(os.getenv("TRADING212_USERNAME"))
    password = expand_env_var(os.getenv("TRADING212_PASSWORD"))
    mode = os.getenv("TRADING212_MODE", "demo")

    if not username or not password:
        print("Error: Credentials not found.")
        print("Set TRADING212_USERNAME and TRADING212_PASSWORD environment variables.")
        return

    print(f"Connecting to Trading212 ({mode} mode)...")
    auth_client = Apit212()
    auth_client.setup(username=username, password=password, mode=mode, _beauty=False)
    print("Connected to Trading212.")

    cfd_client = CFD(cred=auth_client)
    print(f"Account: {cfd_client.get_account()}")
    print(f"Funds:   {cfd_client.get_funds()}")


if __name__ == "__main__":
    main()
