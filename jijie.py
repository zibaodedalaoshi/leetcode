from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "nba")

    # Click text=百度一下
    with page.expect_navigation():
        page.click("text=百度一下")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


