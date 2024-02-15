from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.locator = HomePageLocators()

    def goto_home_page(self):
        self.driver.get(self.base_url)

    def accept_website_cookies(self):
        self.driver.find_element(By.ID, self.locator.WEB_SITE_COOKIE_ACCEPT_BUTTON).click()

    def home_page_should_be_opened_successfully(self):
        assert self.locator.PAGE_TITLE in self.driver.title
        self.wait.until(EC.presence_of_element_located(self.locator.HOME_CTA_CONTAINER))
        print("Home Page Opened Successfully")

    def ensure_home_page_should_be_opened_successfully(self):
        self.home_page_should_be_opened_successfully()
        self.accept_website_cookies()


class HomePageLocators:
    PAGE_TITLE = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    HOME_CTA_CONTAINER = (By.CLASS_NAME, "home_cta_container")
    WEB_SITE_COOKIE_ACCEPT_BUTTON = 'wt-cli-accept-all-btn'
