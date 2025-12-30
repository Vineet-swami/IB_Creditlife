import os
import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_valid_login(page):
    login_page = LoginPage(page)
    
    await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )

    assert page.url == os.getenv("SELECT_INSURANCE_URL")

