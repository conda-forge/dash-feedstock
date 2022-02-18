import pytest


def test_dcc_not_found():
    with pytest.raises(ModuleNotFoundError):
        import dash_core_components

def test_html_not_found():
    with pytest.raises(ModuleNotFoundError):
        import dash_html_components

def test_table_not_found():
    with pytest.raises(ModuleNotFoundError):
        import dash_table
