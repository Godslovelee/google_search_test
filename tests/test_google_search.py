from pages.google_main import GoogleMainPage

def test_google_search(browser):
    google_page = GoogleMainPage(browser)
    google_page.load()
    google_page.search('Selenium')
    assert 'Selenium' in browser.title
