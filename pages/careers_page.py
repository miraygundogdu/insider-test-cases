from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CareersPageLocators()

    def goto_careers_page(self):
        self.click_company_nav_bar_menu()
        self.click_careers_nav_bar_item()

    def click_company_nav_bar_menu(self):
        self.driver.find_element(By.LINK_TEXT, self.locator.COMPANY_NAV_BAR_MENU).click()

    def click_careers_nav_bar_item(self):
        self.driver.find_element(By.LINK_TEXT, self.locator.CAREERS_NAV_BAR_ITEM).click()

    def careers_page_should_be_opened_successfully(self):
        assert self.locator.PAGE_TITLE in self.driver.title

    def ensure_location_block_is_visible(self):
        self.driver.find_element(By.ID, self.locator.LOCATION_CONTAINER)

    def ensure_teams_block_is_visible(self):
        self.driver.find_element(By.ID, self.locator.TEAMS_CONTAINER)

    def ensure_life_block_is_visible(self):
        self.driver.find_element(By.CLASS_NAME, self.locator.LIFE_CONTAINER)

    def ensure_careers_page_should_be_opened_successfully(self):
        self.careers_page_should_be_opened_successfully()
        self.ensure_location_block_is_visible()
        self.ensure_teams_block_is_visible()
        self.ensure_life_block_is_visible()
        print("Careers Page Opened Successfully")


class CareersPageLocators:
    COMPANY_NAV_BAR_MENU = "Company"
    CAREERS_NAV_BAR_ITEM = "Careers"
    PAGE_TITLE = "Careers"
    HOME_CTA_TEXT_LOCATOR = (By.CLASS_NAME, "big-title")
    HOME_CTA_TEXT = "Ready to disrupt? "
    LOCATION_CONTAINER = "career-our-location"
    TEAMS_CONTAINER = "career-find-our-calling"
    LIFE_CONTAINER = "elementor-heading-title"
