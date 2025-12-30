import os
import pytest
from playwright.async_api import expect

class LinkedAccountPage:
    def __init__(self, page):
        self.page = page
        self.linked_account_url = os.getenv("BASE_URL") + "/credit-life/pre-quotes/linked-account"

        # Loan card container - searched by card title text
        self.loan_cards = page.locator("//p[contains(text(), 'Loan Account Details')]/ancestor::div[contains(@class,'bbbdbadfcdbafaffdbfcddccdbfafddb')]")

        # Proceed button inside card (found after clicking card)
        self.card_proceed_button = page.get_by_role("button", name="Proceed")
        self.popup_coborrower_yes = page.get_by_role("button", name="Yes")


    @pytest.mark.asyncio
    async def select_account_and_proceed(self):
        await self.page.wait_for_url("**/linked-account")
        await self.page.wait_for_timeout(1500)

        count = await self.loan_cards.count()
        print(f"🔎 Loan Cards Visible: {count}")

        if count == 0:
            raise AssertionError("❌ No loan account cards found!")

        # Click first loan card ONLY
        card = self.loan_cards.nth(0)
        await expect(card).to_be_visible()
        print("✔ Clicking first loan card")
        await card.click(force=True)

        # Stop automation BEFORE clicking Proceed
        print("⏸️ Manual control from here → You click Proceed if needed")
        await self.page.pause()

        return self.page


    
#Code for further automation can be added here
#     @pytest.mark.asyncio
#     async def select_account_and_proceed(self):
#         await self.page.wait_for_url("**/linked-account")
#         await self.page.wait_for_timeout(1500)

#         count = await self.loan_cards.count()
#         print(f"🔎 Loan Cards Visible: {count}")

#         if count == 0:
#             raise AssertionError("❌ No loan account cards found!")

#         # Click first loan card
#         card = self.loan_cards.nth(0)
#         await expect(card).to_be_visible()
#         print("✔ Clicking first loan card")
#         await card.click(force=True)

#         # Now click proceed INSIDE card
#         print("➡ Clicking Proceed inside loan card")
#         await expect(self.card_proceed_button).to_be_enabled(timeout=7000)
#         await self.card_proceed_button.click()

#         # Optional popup
#         try:
#             if await self.popup_coborrower_yes.is_visible(timeout=3000):
#                 await self.popup_coborrower_yes.click()
#         except:
#             print("ℹ Skip popup step")

#         await self.page.wait_for_url("**/customer-detail-form")
#         print("🎯 Successfully navigated to Customer Details!")

#         return self.page
