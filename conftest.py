import pytest_asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page
        input("Press ENTER to close the browser...")

