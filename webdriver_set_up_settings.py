from selenium import webdriver
from fake_useragent import UserAgent


useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.chrome}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)