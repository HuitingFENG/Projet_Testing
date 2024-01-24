from playwright.sync_api import sync_playwright
import pytest

class EmployeePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto('https://i.hr.dmerej.info/')

    def add_employee(self, name, email, address1, address2, city, zipcode, hiring_date, job_title):
        self.page.locator('a:has-text("Add new employee")').click()
        self.page.locator('input[placeholder="Name"]').fill(name)
        self.page.locator('input[placeholder="Email"]').fill(email)
        self.page.locator('#id_address_line1').fill(address1)
        self.page.locator('#id_address_line2').fill(address2)
        self.page.locator('input[placeholder="City"]').fill(city)
        self.page.locator('input[placeholder="Zip code"]').fill(zipcode)
        self.page.locator('input[placeholder="Hiring date"]').fill(hiring_date)
        self.page.locator('input[placeholder="Job title"]').fill(job_title)
        self.page.locator('button:has-text("Add")').click()
        
    def reset_db_without_password(self):
        self.page.locator('a:has-text("Reset database")').click()
        self.page.locator('button:has-text("Proceed")').click()
        assert self.page.url == 'https://i.hr.dmerej.info/'

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()

def test_add_new_employee(browser_context):
    page = browser_context.new_page()
    employee_page = EmployeePage(page)
    employee_page.navigate()
    employee_page.add_employee('name1', 'email1@efrei.net', 'address1', 'address2', 'paris', '75011', '2020-02-23', 'dev full stack')
    
def test_reset_db_without_password(browser_context):
    page = browser_context.new_page()
    employee_page = EmployeePage(page)
    employee_page.navigate()
    employee_page.reset_db_without_password()