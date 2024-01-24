import { test, expect } from '@playwright/test';

// npx playwright test
// npx playwright show-trace trace.json


test('test', async ({ browser }) => {
  const context = await browser.newContext();
  await context.tracing.start();
  const page = await context.newPage();
  await page.goto('https://i.hr.dmerej.info/');
  await page.getByRole('link', { name: 'Add new employee' }).click();
  await page.getByPlaceholder('Name').click();
  await page.getByPlaceholder('Name').fill('name1');
  await page.getByPlaceholder('Email').click();
  await page.getByPlaceholder('Email').fill('email1@efrei.net');
  await page.locator('#id_address_line1').click();
  await page.locator('#id_address_line1').fill('address1');
  await page.locator('#id_address_line2').click();
  await page.locator('#id_address_line2').fill('address2');
  await page.getByPlaceholder('City').click();
  await page.getByPlaceholder('City').fill('paris');
  await page.getByPlaceholder('Zip code').click();
  await page.getByPlaceholder('Zip code').fill('75011');
  await page.getByPlaceholder('Hiring date').fill('2020-02-23');
  await page.getByPlaceholder('Job title').click();
  await page.getByPlaceholder('Job title').fill('dev full stack');
  await page.getByRole('button', { name: 'Add' }).click();
  await context.tracing.stop({ path: 'trace.json' });
});

