import os
from playwright.async_api import Page
import pytest

from pages.select_insurance_page import SelectInsurancePage

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_url = os.getenv("BASE_URL") + "/login"
        self.username_input = page.locator("//input[contains(@placeholder,'Enter Employee ID')]")
        self.password_input = page.locator("//input[contains(@placeholder,'Enter Password')]")
        self.login_button = page.locator("//button[contains(text(),'LOGIN')]")
        self.select_insurance_url = os.getenv("BASE_URL") + "/pre-quotes/select-insurance"


    @pytest.mark.asyncio
    async def login(self, username: str, password: str) -> SelectInsurancePage:
        await self.page.goto(self.login_url)
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()

        await self.page.wait_for_url(self.select_insurance_url)
        return SelectInsurancePage(self.page)