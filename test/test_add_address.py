# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from model.date import Date
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address(app):
    app.session.login("admin", "secret")
    app.contact.add(
        Contact("test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                "test", "test", "test", "test", "test", "test", "test", "test"),
        Date("2", "January", "1999"), Date("2", "January", "2018"))
    app.session.logout()


def test_add_address_empty(app):
    app.session.login("admin", "secret")
    app.contact.add(Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
                    Date("", "-", ""), Date("", "-", ""))
    app.session.logout()