from selenium import (webdriver)
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://example.com")

assert "Example" in driver.title, "Заголовок не содержит 'Example'"

more_info_link = driver.find_element("css selector", "a[href*='iana.org']")
more_info_link.click()

assert driver.current_url == "https://www.iana.org/help/example-domains", "URL не совпадает!"

