from tasks import is_prime, load_numbers_sorted
import pytest
import os
from typing import List, Tuple

# def test_is_prime():
#     assert not is_prime(1)
#     assert is_prime(2)
#     assert is_prime(3)
#     assert not is_prime(4)
#     assert is_prime(5)
#     assert not is_prime(6)
#     assert is_prime(7)
#     assert not is_prime(8)
#     assert not is_prime(9)
#     assert not is_prime(10)

@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected

# フィクスチャの使い方: ファイルを作成する例
# @pytest.fixture
# def txt() -> str:
#     with open('numbers.txt', 'w') as f:
#         for n in [2, 5, 4, 3, 1]:
#             f.write('{}\n'.format(n))

#     yield 'numbers.txt'
#     os.remove('numbers.txt')

# フィクスチャの使い方、テンポラリディレクトリ tmpdir にファイルを作成する例
# フィクスチャがあまりにも冗長で動作が遅いときは、フィクスチャのスコープを指定できる。
# スコープはfunction, class, module, session がある。
# @pytest.fixture(scope='funciton') のように書く。
@pytest.fixture()
def txt(tmpdir) -> str:
    tmpfile = tmpdir.join('numbers.txt')

    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)

    tmpfile.remove()

# フィクスチャの連携
@pytest.fixture()
def txt_and_list(txt) -> Tuple[str, List[int]]:
    yield txt, [1, 2, 3, 4, 5]

# フィクスチャを使ったテスト
def test_load_numbers_sorted(txt_and_list):
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]

# def test_load_numbers_sorted(txt):
#     assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
