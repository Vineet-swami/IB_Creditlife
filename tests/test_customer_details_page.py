import os
import pytest

from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_customer_details_and_linked_account(page):
    login_page = LoginPage(page)

    select_page = await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )

    customer_details_page = await select_page.select_credit_life_insurance()
    await customer_details_page.enter_cif_and_continue("123456789")

    assert page.url == os.getenv("BASE_URL") + "/credit-life/pre-quotes/linked-account"

