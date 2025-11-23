from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service


class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        elif browser_name == "firefox":
            service = Service(executable_path="drivers/geckodriver.exe")
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            return webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")