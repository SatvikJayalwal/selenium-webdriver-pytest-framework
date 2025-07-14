import os
import datetime
import pytest
from selenium import webdriver


#Add custom CLI flag: --browser_name
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


#Fixture: browserInstance
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument("--start-maximized")
        chrome_opts.add_argument("--ignore-certificate-errors")
        # chrome_opts.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_opts)

    elif browser_name == "edge":
        edge_opts = webdriver.EdgeOptions()
        edge_opts.add_argument("--start-maximized")
        edge_opts.add_argument("--ignore-certificate-errors")
        driver = webdriver.Edge(options=edge_opts)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


#Helper: Get timestamp for screenshot filename
def _time_stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#PyTest Hook: Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browserInstance")
        if not driver:
            return

        #Create screenshots folder if it doesn't exist
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        #File name with test name and timestamp
        screenshot_file = f"{item.name}_{_time_stamp()}.png"
        screenshot_path = os.path.join(screenshots_dir, screenshot_file)

        #Take screenshot
        driver.save_screenshot(screenshot_path)

        #Attach screenshot to pytest-html report (if available)
        try:
            from pytest_html import extras
            extra = getattr(rep, "extra", [])
            extra.append(extras.image(screenshot_path, mime_type="image/png"))
            rep.extra = extra
        except ImportError:
            pass
