# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Table(Component):
    def __init__(self, driver, by_locator):
        super(Table, self).__init__(driver, by_locator)
