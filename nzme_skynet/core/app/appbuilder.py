# coding=utf-8
import logging

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder
from nzme_skynet.core.browsers.remotebrowserbuilder import RemoteBrowserBuilder

CAPABILITIES = {"firefox": DesiredCapabilities.FIREFOX,
                "chrome": DesiredCapabilities.CHROME,
                "safari": DesiredCapabilities.SAFARI,
                "ie": DesiredCapabilities.INTERNETEXPLORER,
                "opera": DesiredCapabilities.OPERA,
                "phantomjs": DesiredCapabilities.PHANTOMJS,
                "iphone": DesiredCapabilities.IPHONE,
                "ipad": DesiredCapabilities.IPAD,
                "android": DesiredCapabilities.ANDROID}

logger = logging.getLogger(__name__)


# Browser
def build_desktop_browser(browser_options, base_url=None):
    logger.debug("Creating local browser instance")
    builder = LocalBrowserBuilder(browser_options, base_url)
    return builder.build()


# Docker
def build_docker_browser(sel_grid_url, desired_cap, base_url=None):
    logger.debug("Creating a browser instance using selenium-grid")
    desired_cap['javascriptEnabled'] = True
    builder = RemoteBrowserBuilder(sel_grid_url, desired_capabilities=desired_cap,
                                   base_url=base_url)
    return builder.build()


def build_real_mobile_browser():
    raise NotImplementedError


def build_simulator_mobile_browser():
    raise NotImplementedError


# Mobile App
def build_real_mobile_native_app():
    raise NotImplementedError


def build_simulator_mobile_app():
    raise NotImplementedError

