import pytest

from .main import clean_unclosed_parens


@pytest.fixture(scope='function',
                params=[clean_unclosed_parens],
                ids=['without regexp'])
def func_for_test(request):
    return request.param


def test_boundary_values(func_for_test):
    assert func_for_test('') == ''
    assert func_for_test('aaa') == 'aaa'


def test_closed_parens(func_for_test):
    assert func_for_test('(aaa)') == '(aaa)'
    assert func_for_test('(aaa)(bbb)(ccc)') == '(aaa)(bbb)(ccc)'
    assert func_for_test('(aaa(bbb(ccc(ddd)qqq)www)iii)') == '(aaa(bbb(ccc(ddd)qqq)www)iii)'
    assert func_for_test('aaa(bbb(ccc(ddd)qqq)www)iii') == 'aaa(bbb(ccc(ddd)qqq)www)iii'
    assert func_for_test('aaa(bbb(ccc)ddd)') == 'aaa(bbb(ccc)ddd)'
    assert func_for_test('(bbb(ccc)ddd)aaa') == '(bbb(ccc)ddd)aaa'


def test_unclosed_parens(func_for_test):
    assert func_for_test('aaa((bbb)(ccc') == 'aaa((bbb)'
    assert func_for_test('aaa((bbb)ccc') == 'aaa((bbb)ccc'
    assert func_for_test('zzz)aaa)fff(ggg(kkk') == 'fff'
    assert func_for_test('zzz)(aaa)(qqq))ddd(fff(ccc))') == 'ddd(fff(ccc))'
    assert func_for_test('aaa((bbb)(') == 'aaa((bbb)'
    assert func_for_test('aaa(((bbb)ccc') == 'aaa'
    # about above value, I'm not sure, but if I have correctly understood the task conditions
    # after the first paren there is not a closed block and should be removed
    assert func_for_test('aaa(vvv(bbb)ccc') == 'aaa'
