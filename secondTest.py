from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()

def test_add_new_employee(browser_context):
    context = browser_context
    page = context.new_page()
    context.tracing.start()
    page.goto('https://i.hr.dmerej.info/')
    page.get_by_role('link', name='Add new employee').click()
    page.get_by_placeholder('Name').click()
    page.get_by_placeholder('Name').fill('name1')
    page.get_by_placeholder('Email').click()
    page.get_by_placeholder('Email').fill('email1@efrei.net')
    page.locator('#id_address_line1').click()
    page.locator('#id_address_line1').fill('address1')
    page.locator('#id_address_line2').click()
    page.locator('#id_address_line2').fill('address2')
    page.get_by_placeholder('City').click()
    page.get_by_placeholder('City').fill('paris')
    page.get_by_placeholder('Zip code').click()
    page.get_by_placeholder('Zip code').fill('75011')
    page.get_by_placeholder('Hiring date').fill('2020-02-23')
    page.get_by_placeholder('Job title').click()
    page.get_by_placeholder('Job title').fill('dev full stack')
    page.get_by_role('button', name='Add').click()
    context.tracing.stop(path='trace.json')

