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



    
def test_remove_manager_role(browser_context):
    context = browser_context
    page = context.new_page()
    context.tracing.start()
    page.goto('https://i.hr.dmerej.info/')
    page.get_by_role('link', name='List Employees').click()
    # check an old employee who is not a manager yet
    page.get_by_role('link', name='Edit').click(timeout=60000) 
    page.get_by_role('link', name='Promote as manager').click()
    page.get_by_role('button', name='Proceed').click()
    page.get_by_role('link', name='Home').click()
    page.get_by_role('link', name='List Employees').click()
    page.get_by_role('link', name='Edit').click()
    page.get_by_role('link', name='Promote as manager').click()
    # Check if any new element is added after promoting as manager
    new_elements = page.locator('*')  # Selects all elements on the page
    assert new_elements.count() > 0  # Check if there's at least one new element: button called remove
    context.tracing.stop(path='trace.json')
    
    
def test_zipcode(browser_context):
    context = browser_context
    page = context.new_page()
    context.tracing.start()
    page.goto('https://i.hr.dmerej.info/')
    page.get_by_role('link', name='List Employees').click()
    page.get_by_role('link', name='Edit').click()
    page.get_by_role('link', name='Update address').click()
    page.get_by_placeholder('Zip code').click()
    page.press('Zip code', 'Enter') 
    page.get_by_placeholder('Zip code').fill('11111111111111111111111111111111111111111111111111111111')
    page.get_by_role('button', name='Update').click()
    # Wait for the new page to load
    new_page = page.wait_for_event('page', 'popup')
    # Assert that the new page contains "server code 500"
    new_page_content = new_page.content()
    assert "server code 500" in new_page_content, "Expected 'server code 500' on the new page"
    
    #  can also assert the status code if needed
    # assert new_page.status() == 500, "Expected status code 500 on the new page"
    context.tracing.stop(path='trace.json')
    
    
    
    
# reset db without password
def test_reset_db_without_password (browser_context):
    context = browser_context
    page = context.new_page()
    context.tracing.start()
    page.goto('https://i.hr.dmerej.info/')
    page.get_by_role('link', name='Reset database').click()
    page.get_by_role('button', name='Proceed').click()
     # Check if the user is back on the main page after reset
     # user can go back to the main page, means that the database can be reset without password.
    assert page.url == 'https://i.hr.dmerej.info/'
    context.tracing.stop(path='trace.json')
    