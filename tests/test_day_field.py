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

months = {
    1: 31,
    2: (28, 29),
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


@pytest.mark.parametrize('day_data', (1, 2, 15, 16, 30, 31))
@pytest.mark.parametrize('month_data', (1, 7, 12))
@pytest.mark.parametrize('year_data', (2000, 2099, 2100))
def test_day_field(fix, driver, day_data, month_data, year_data):
    driver.implicitly_wait(3)
    fix[0].clear()
    fix[0].send_keys(day_data)
    fix[1].clear()
    fix[1].send_keys(month_data)
    fix[2].clear()
    fix[2].send_keys(year_data)

    button_submit = driver.find_element_by_xpath('//input[@type="submit"]')
    button_submit.click()

    result = driver.find_element_by_xpath('//span[@id="day-of-week"]')
    text = result.text

    assert text in day_list


@pytest.mark.parametrize('day_data', (41,))
@pytest.mark.parametrize('month_data', (1, 2, 4, 12))
@pytest.mark.parametrize('year_data', (2000, 2099))
def test_wrong_data(fix, driver, day_data, month_data, year_data):
    fix[0].clear()
    fix[0].send_keys(day_data)
    fix[1].clear()
    fix[1].send_keys(month_data)
    fix[2].clear()
    fix[2].send_keys(year_data)

    button_submit = driver.find_element_by_xpath('//input[@type="submit"]')
    button_submit.click()

    day_count_in_the_month_limit = months.get(month_data)
    if month_data == 2:
        if year_data % 4 == 0:
            day_count_in_the_month_limit = day_count_in_the_month_limit[1]
        else:
            day_count_in_the_month_limit = day_count_in_the_month_limit[0]

    day_field_value = int(driver.find_element_by_xpath('//input[@name="day"]').get_attribute('value'))
    new_day_field_value = day_data % day_count_in_the_month_limit

    assert day_field_value == new_day_field_value
