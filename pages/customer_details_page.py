import os

import pytest

from pages.linked_account_page import LinkedAccountPage


class CustomerDetailsPage:
    def __init__(self, page):
        self.page = page
        # Initialize locators and other elements here
        self.cif_number_input = page.get_by_placeholder("Enter CIF")
        self.next_button = page.locator("button", has_text="NEXT")
        self.linked_account_url = os.getenv("BASE_URL") + "/credit-life/pre-quotes/linked-account"

    @pytest.mark.asyncio
    async def enter_cif_and_continue(self, cif_number):
        await self.page.wait_for_url("**/customer-details")
        await self.cif_number_input.wait_for(state="visible")
        await self.cif_number_input.fill(cif_number)
        await self.next_button.wait_for(state="visible")
        await self.next_button.click()
        # Add any necessary waits or verifications here
        await self.page.wait_for_url("**/linked-account")

        return LinkedAccountPage(self.page)