import time

import pytest

day_list = [
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье'
]


@pytest.mark.parametrize('day_data', (1, 2, 15, 16, 30, 31))
@pytest.mark.parametrize('month_data', (1, 7, 12))
@pytest.mark.parametrize('year_data', (2000, 2099, 2100))
def test_day_field(driver, day_data, month_data, year_data):
    day_field = driver.find_element_by_xpath('//input[@name="day"]')
    month_field = driver.find_element_by_xpath('//input[@name="month"]')
    year_field = driver.find_element_by_xpath('//input[@name="year"]')

    driver.implicitly_wait(3)
    day_field.clear()
    day_field.send_keys(day_data)
    month_field.clear()
    month_field.send_keys(month_data)
    year_field.clear()
    year_field.send_keys(year_data)

    button_submit = driver.find_element_by_xpath('//input[@type="submit"]')
    button_submit.click()

    result = driver.find_element_by_xpath('//span[@id="day-of-week"]')
    text = result.text

    assert text in day_list
