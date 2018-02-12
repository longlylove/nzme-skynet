# -*- coding: utf-8 -*-
import logging

from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.controls import highlight_state
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
logger = logging.getLogger(__name__)


class BaseElement(object):
    def __init__(self, by, locator):
        self._by = by
        self._locator = locator

    def _find_element(self):
        logger.debug('_finding_element: {}  {}'.format(self._by, self._locator))
        try:
            return WebDriverWait(self.driver, DefaultTimeouts.LARGE_TIMEOUT).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            raise

    def find_sub_elements(self, by, locator):
        # TODO: return list of Element objects
        return self._find_element().find_elements(by, locator)

    @property
    def driver(self):
        return DriverRegistry.get_webdriver()

    @property
    def location(self):
        return self._find_element().location

    @property
    def size(self):
        return self._find_element().size

    def exists(self):
        try:
            self._find_element()
            return True
        except Exception:
            return False

    def _highlight(self):
        if highlight_state():
            elem = self.will_be_visible()

            def apply_style(style):
                self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                           elem, style)
            previous_style = self.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(0.3)
            apply_style(previous_style)

    def get_attribute(self, attribute):
        return self._find_element().get_attribute(attribute)

    def has_attribute(self, attribute):
        try:
            return self.get_attribute(attribute)
        except Exception:
            return False

    def get_css_property(self, css_property):
        return self._find_element().value_of_css_property(css_property)

    def scroll_to_element(self, offset=200):
        self.driver.execute_script("window.scrollBy(0," + str(self.location['y'] - offset) + ");")

    # Visibility, Presence, Clickability

    def is_currently_visible(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_visible(time=time)

    def will_be_visible(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((self._by, self._locator)))
        except Exception:
            return False

    def is_currently_present(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_present(time=time)

    def will_be_present(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            return False

    def is_not_displayed(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_not_be_displayed(time=time)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((self._by, self._locator)))
        except Exception:
            return False

    def is_ready_to_interact(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_ready_to_interact(time=time)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((self._by, self._locator)))
        except Exception:
            return False

    def hover_over(self):
        raise NotImplementedError

    def focus(self):
        raise NotImplementedError
