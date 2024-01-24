# test_frontend_with_playwright_pytest.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def test_display_of_employees(browser):
    # Create a new page
    page = browser.new_page()

    # Navigate to the webpage
    page.goto("https://i.hr.dmerej.info/employees")

    # Get the list of employees displayed on the webpage
    employees_from_webpage = page.inner_text('body > table > tbody:nth-child(3)')  # Replace with the actual selector of your employee list

    # Check if each simulated employee is displayed on the webpage
    assert 'name2' in employees_from_webpage, "Employee 'name2' not found on the webpage"
    assert 'name1' in employees_from_webpage, "Employee 'name1' not found on the webpage"

# To run the test, execute: pytest listEmployee.py
