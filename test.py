import functions4
import pytest


@pytest.mark.parametrize("color, expected_result", [('asdfg', None),
                                                    ('#11111N', None),
                                                    ('#A182B3', False),
                                                    ('#A9A9A9', True),
                                                    (1234, None)])
def test_is_gray_input(color, expected_result):
    assert functions4.is_gray(color) is expected_result


@pytest.mark.parametrize("color, expected_result", [('#A9A9A9', None),
                                                    ('#945412', (0, 64, 130)),
                                                    (1123, None),
                                                    ('FFFFFF', None),
                                                    ('#FFFFFM', None)])
def test_to_gray_input(color, expected_result):
    assert functions4.to_gray(color) == expected_result


test_is_gray_input("#F0F0F0", True)
test_to_gray_input('#A9A9A9', None)
