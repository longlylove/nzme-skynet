import pytest

from nzme_skynet.core.driver.driverregistry import DriverRegistry

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"


@pytest.fixture(scope='module', params=["chrome", "firefox"])
def driver_setup(request):
    DriverRegistry.register_driver(driver_type=request.param, local=False)
    driver = DriverRegistry.get_driver()
    yield driver
    driver.quit()


def test_browser_setup(dsetup):
    # assert dsetup.baseurl == TEST_URL
    assert (TEST_URL in dsetup.current_url) is True
