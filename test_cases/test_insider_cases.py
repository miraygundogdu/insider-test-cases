from pages.base_page import BasePage
from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.qa_jobs_page import QAJobsPage


def test_insider_cases():
    driver = BasePage.get_driver()
    home_page = HomePage(driver)
    home_page.goto_home_page()
    home_page.ensure_home_page_should_be_opened_successfully()

    careers_page = CareersPage(driver)
    careers_page.goto_careers_page()
    careers_page.ensure_careers_page_should_be_opened_successfully()

    qa_jobs_page = QAJobsPage(driver)
    qa_jobs_page.goto_qa_jobs_page()
    qa_jobs_page.ensure_qa_jobs_page_should_be_opened_successfully()

    driver.quit()
    print("All tests passed")