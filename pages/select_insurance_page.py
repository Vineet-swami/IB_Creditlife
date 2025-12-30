import os
import pytest
from pages.customer_details_page import CustomerDetailsPage


class SelectInsurancePage:
    def __init__(self, page):
        self.page = page
        self.customer_details_url = os.getenv("BASE_URL") + "/credit-life/pre-quotes/customer-details"

        self.credit_life_option = page.locator("//div/child::p[contains(text(),'Credit Life')]")
        self.next_button = page.locator("//button[contains(text(),'NEXT')]")

    @pytest.mark.asyncio
    async def select_credit_life_insurance(self):
        # await self.page.goto(self.select_insurance_url)
        await self.credit_life_option.wait_for(state="visible")
        await self.credit_life_option.click()
        await self.next_button.wait_for(state="visible")
        await self.next_button.click()
        await self.page.wait_for_url("**/customer-details")

        return CustomerDetailsPage(self.page)