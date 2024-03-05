from selenium import webdriver
from fake_useragent import UserAgent
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument(f'user-agent={useragent.chrome}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)


# profile = FirefoxProfile()
# # profile.set_preference("layout.css.devPixelsPerPx", "2")
#
# options = FirefoxOptions()
# options.profile = profile
# # options.add_argument("--headless")
# options.set_preference("general.useragent.override", useragent.firefox)
# options.set_preference("dom.webdriver.enabled", False)
# options.set_preference("useAutomationExtension", False)
# options.set_preference("privacy.trackingprotection.enabled", True)
#
#
# driver = webdriver.Firefox(options=options)
