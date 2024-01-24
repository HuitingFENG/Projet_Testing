from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()

@pytest.mark.playwright
def test_promotion_and_role_removal_issue(browser_context):
    context = browser_context
    page = context.new_page()
    context.tracing.start()
    page.goto('https://i.hr.dmerej.info/')

    # Navigate to 'List Employees' and edit the second employee
    page.get_by_role("link", name="List Employees").click()
    page.get_by_role("link", name="Edit").nth(1).click()

    # Promote the employee to manager
    page.get_by_role("link", name="Promote as manager").click()
    page.get_by_role("button", name="Proceed").click()

    # Try to remove the Manager role
    page.get_by_role("button", name="Remove Manager Role").click()

    # Going to seek for a button that does not exist and do a runtime error.

    context.tracing.stop(path='trace.json')
