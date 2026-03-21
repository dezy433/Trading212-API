# Troubleshooting Selenium Login for Trading212 Bot

## 1. File-based Debug Output
- The bot now writes all detected input fields and their attributes to `selenium_input_debug.txt` in the project root.
- After running the bot, open this file to see what Selenium sees on the login page.
- If the file is empty or missing, Selenium may not be loading the page correctly (possible headless/browser/driver issue).

## 2. GitHub Actions Workflow for Selenium + Chrome
- See `.github/workflows/run-bot.yml` for a ready-to-use workflow.
- It installs Chrome, sets up Python, and runs the bot with a 3-minute timeout.
- Store your Trading212 credentials as GitHub repository secrets: `TRADING212_USERNAME` and `TRADING212_PASSWORD`.

## 3. Local Environment Setup for Selenium
- **Install Google Chrome:**
  - Ubuntu: `sudo apt update && sudo apt install -y google-chrome-stable`
  - Mac: `brew install --cask google-chrome`
  - Windows: Download from [google.com/chrome](https://www.google.com/chrome/)
- **Install chromedriver:**
  - Ubuntu: `sudo apt install -y chromium-chromedriver` or download from https://chromedriver.chromium.org/downloads
  - Mac: `brew install chromedriver`
  - Windows: Download and add to PATH
- **Install Python dependencies:**
  - `pip install -r requirements.txt`
- **Test locally:**
  - Run: `python3 bot_example.py`
  - Check `selenium_input_debug.txt` for input field info if login fails.

## 4. Common Issues
- If the bot cannot find the email field, check the debug file for what Selenium sees.
- If the debug file is empty, check Chrome/chromedriver installation and PATH.
- For headless issues, try removing `--headless` in `apit212.py` to see the browser window.

## 5. Getting Help
- Share the contents of `selenium_input_debug.txt` if you need further assistance.
- Make sure your credentials are correct and not expired.
