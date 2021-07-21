import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True, scope='session')
def driver():
    driver = WebDriver(executable_path='/home/eswot/PycharmProjects/self_testing/software-testing.ru_testing'
                                       '/chromedriver')
    # driver.implicitly_wait(3)
    yield driver
    driver.close()


@pytest.fixture(autouse=True, scope='function')
def start_connection(driver):
    driver.get('https://software-testing.ru/edu/dow/fields.php')
    yield start_connection
    driver.refresh()


@pytest.fixture(scope='function', name='fix')
def get_driver_field(driver):
    day_field = driver.find_element_by_xpath('//input[@name="day"]')
    month_field = driver.find_element_by_xpath('//input[@name="month"]')
    year_field = driver.find_element_by_xpath('//input[@name="year"]')
    return day_field, month_field, year_field
