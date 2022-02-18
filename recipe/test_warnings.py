import warnings
import pytest


def test_dcc_warning():
    with pytest.warns(UserWarning):
        import dash_core_components

def test_html_warning():
    with pytest.warns(UserWarning):
        import dash_html_components

def test_table_warning():
    with pytest.warns(UserWarning):
        import dash_table
