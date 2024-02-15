from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class QAJobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = QAJobsPageLocators()

    def goto_qa_jobs_page(self):
        self.driver.get(self.base_url + self.locator.PAGE_URL)

    def qa_jobs_page_should_be_opened_successfully(self):
        assert self.locator.PAGE_TITLE in self.driver.title

    def click_see_all_qa_jobs_link(self):
        self.driver.find_element(By.LINK_TEXT, self.locator.SEE_ALL_QA_JOBS_LINK_TEXT).click()

    def search_and_click_on_dropdown(self, dropdown_locator, dropdown_selector, dropdown_search_locator,
                                     dropdown_choosing_locator):
        self.wait.until(EC.visibility_of_element_located(dropdown_locator))
        time.sleep(10)  # waiting to load datasource of dropdowns

        # click the dropdown to show list
        location_dropdown = self.driver.find_element(By.ID, dropdown_selector)
        location_dropdown.click()

        # find specific key in the list
        location_option = location_dropdown.find_element(By.XPATH, dropdown_search_locator)
        location_option.click()

        # select specific key item
        self.wait.until(EC.visibility_of_element_located((By.XPATH, dropdown_choosing_locator)))
        option = self.driver.find_element(By.XPATH, dropdown_choosing_locator)
        option.click()

    def filter_by_location_on_dropdown(self):
        self.search_and_click_on_dropdown(self.locator.LOCATION_DROPDOWN_LOCATOR,
                                          self.locator.LOCATION_DROPDOWN,
                                          self.locator.LOCATION_DROPDOWN_SEARCH_LOCATOR,
                                          self.locator.LOCATION_DROPDOWN_CHOOSING_LOCATOR)

    def filter_by_department_on_dropdown(self):
        self.search_and_click_on_dropdown(self.locator.DEPARTMENT_DROPDOWN_LOCATOR,
                                          self.locator.DEPARTMENT_DROPDOWN,
                                          self.locator.DEPARTMENT_DROPDOWN_SEARCH_LOCATOR,
                                          self.locator.DEPARTMENT_DROPDOWN_CHOOSING_LOCATOR)

    def check_that_all_jobs_contains_expected_values_in_position_list(self):
        position_list = self.driver.find_elements(By.CLASS_NAME, self.locator.POSITION_LIST_ITEM_LOCATOR)
        for position in position_list:
            self.check_position_title(position)
            self.check_department_title(position)
            self.check_location_title(position)

    def check_position_title(self, position):
        position_title_element = position.find_elements(By.CLASS_NAME, self.locator.POSITION_TITLE_LOCATOR)
        position_title = position_title_element[0].text.strip()
        if self.locator.DEPARTMENT_SEARCH_KEY in position_title:
            print(f"The text '{position_title}' contains '{self.locator.DEPARTMENT_SEARCH_KEY}'.")

    def check_department_title(self, position):
        position_department_element = position.find_elements(By.CLASS_NAME, self.locator.POSITION_DEPARTMENT_LOCATOR)
        position_department_title = position_department_element[0].text.strip()
        assert position_department_title == self.locator.DEPARTMENT_SEARCH_KEY

    def check_location_title(self, position):
        position_location_element = position.find_elements(By.CLASS_NAME, self.locator.POSITION_LOCATION_LOCATOR)
        position_location_title = position_location_element[0].text.strip()
        assert position_location_title == self.locator.LOCATION_SEARCH_KEY

    def click_first_view_role_button_on_positions_list(self):
        position_list = self.driver.find_elements(By.CLASS_NAME, self.locator.POSITION_LIST_ITEM_LOCATOR)
        position_card = position_list[0]
        view_role_button = position_card.find_element(By.CLASS_NAME, 'btn')
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))
        view_role_button.click()
        self.ensure_lever_application_form_page_is_opened_successfully()

    def ensure_lever_application_form_page_is_opened_successfully(self):
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        self.wait.until(EC.title_is("Insider. - Senior Software Quality Assurance Engineer"))

    def ensure_qa_jobs_page_should_be_opened_successfully(self):
        self.qa_jobs_page_should_be_opened_successfully()
        self.click_see_all_qa_jobs_link()
        self.filter_by_location_on_dropdown()
        self.filter_by_department_on_dropdown()
        self.check_that_all_jobs_contains_expected_values_in_position_list()
        self.click_first_view_role_button_on_positions_list()
        print("QA Jobs Page Opened Successfully")


class QAJobsPageLocators:
    PAGE_URL = '/careers/quality-assurance/'
    PAGE_TITLE = 'Insider quality assurance job opportunities'
    SEE_ALL_QA_JOBS_LINK_TEXT = 'See all QA jobs'
    LOCATION_DROPDOWN_LOCATOR = (By.ID, 'select2-filter-by-location-container')
    LOCATION_DROPDOWN = 'select2-filter-by-location-container'
    LOCATION_SEARCH_KEY = "Istanbul, Turkey"
    LOCATION_DROPDOWN_SEARCH_LOCATOR = f"//option[text()='{LOCATION_SEARCH_KEY}']"
    LOCATION_DROPDOWN_CHOOSING_LOCATOR = f"//li[text()='{LOCATION_SEARCH_KEY}']"
    DEPARTMENT_DROPDOWN_LOCATOR = (By.ID, 'select2-filter-by-department-container')
    DEPARTMENT_DROPDOWN = 'select2-filter-by-department-container'
    DEPARTMENT_SEARCH_KEY = 'Quality Assurance'
    DEPARTMENT_DROPDOWN_SEARCH_LOCATOR = f"//option[text()='{DEPARTMENT_SEARCH_KEY}']"
    DEPARTMENT_DROPDOWN_CHOOSING_LOCATOR = f"//li[text()='{DEPARTMENT_SEARCH_KEY}']"
    POSITION_LIST_ITEM_LOCATOR = 'position-list-item'
    POSITION_TITLE_LOCATOR = 'position-title'
    POSITION_LOCATION_LOCATOR = 'position-location'
    POSITION_DEPARTMENT_LOCATOR = 'position-department'
