import os
import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_login_and_select_credit_life(page):
    login_page = LoginPage(page)

    select_page = await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )
    await select_page.select_credit_life_insurance()

    assert page.url == os.getenv("CUSTOMER_DETAILS_URL")

