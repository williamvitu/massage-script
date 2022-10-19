import re
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv

load_dotenv()

def test(page: Page):
    
    USR = os.getenv("USERNAME")
    PWD = os.getenv("PWD")
    
    username = page.locator("id=Email")
    pwd = page.locator("id=Senha")
    loginButton = page.locator("button", has_text="Login")

    page.goto("https://aliviumterapia1.websiteseguro.com/app/")
    username.click()
    username.fill(USR)
    pwd.click()
    pwd.fill(PWD)
    loginButton.click()
    expect(page.locator("h2", has_text="AGENDAR"))
    page.locator("id=AgendaId").click()
    page.locator("id=AgendaId").select_option("635")
  
    page.locator("label", has_text="15:00").click()
    page.locator("id=btnSalvar").click()
   
