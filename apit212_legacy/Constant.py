HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Cookie": ""
}



URL = 'https://www.trading212.com/'

# Login button - multiple selectors for cross-browser compatibility
LOGIN_BUTTON = [
    "//header//p",  # Simple p tag in header
    "//header//button",  # Or button in header
    "//*[@id=\"__next\"]/header/div/div/div[2]/div[1]/div[2]/p"  # Fallback to original
]

# Cookie popup selectors - using more flexible XPath that works across browsers
# Try multiple methods to find the cookie accept button
COOKIE_POPUP = [
    "//button[contains(text(), 'Accept')]",  # Button with "Accept" text
    "//button[@aria-label*='cookie' or @aria-label*='Cookie']",  # Aria label approach
    "/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div[2]/div[1]"  # Fallback to original
]


# Email and password field selectors (add more generic options)
EMAIL_FIELD_SELECTORS = [
    ("NAME", "email"),
    ("CSS_SELECTOR", "input[type='email']"),
    ("CSS_SELECTOR", "input[name*='email']"),
    ("XPATH", "//input[@type='text'][1]"),  # First text input
    ("CSS_SELECTOR", "input[data-testid='login-form-email-input-base-component']"),
    ("XPATH", "//input[@data-testid='login-form-email-input-base-component']"),
]

PASSWORD_FIELD_SELECTORS = [
    ("NAME", "password"),
    ("CSS_SELECTOR", "input[type='password']"),
    ("CSS_SELECTOR", "input[name*='password']"),
    ("XPATH", "//input[@type='password']"),
    ("CSS_SELECTOR", "input[data-testid='login-form-password-input-base-component']"),
    ("XPATH", "//input[@data-testid='login-form-password-input-base-component']"),
]
# Submit button - more robust selector
SUBMIT_BUTTON = [
    "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'log')]",  # Button containing "Login/Log in"
    "//button[@type='submit']",
    "//button[contains(@class, 'submit') or contains(@class, 'login')]",
    "//button[contains(text(), 'Sign in') or contains(text(), 'Log in') or contains(text(), 'Login')]",
    "/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div/form/div[5]"  # Fallback
]

POPUP_CLOSE = '//*[@id="app"]/div[6]/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/span/div'
REMEBER_ME_TOGGLE = '//*[@id="__next"]/main/div[2]/div/div[2]/div/div[2]/div/form/div[4]/div[2]/input'
USER_NAME = '//*[@id="app"]/div[5]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]'

# Start menu - more flexible selector
START_I_MENU = [
    "//div[@class*='menu']//div[@class*='trading']",
    "/html/body/div[1]/div[5]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/div",
    "/html/body/div[1]/div[6]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/div"
]
