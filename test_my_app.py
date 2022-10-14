import re

from playwright.sync_api import Page, expect



def test(page: Page):
    
    username = page.locator("id=Email")
    pwd = page.locator("id=Senha")
    loginButton = page.locator("button", has_text="Login")

    page.goto("https://aliviumterapia1.websiteseguro.com/app/")
    username.click()
    username.fill("")
    pwd.click()
    pwd.fill("")
    loginButton.click()
    expect(page.locator("h2", has_text="AGENDAR"))
    page.locator("id=AgendaId").click()
    page.locator("id=AgendaId").select_option("635")
  
    page.locator("label", has_text="15:00").click()
    page.locator("id=btnSalvar").click()
   
