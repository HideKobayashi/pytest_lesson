from typing import List, Tuple


def is_prime(n: int) -> bool:
    """素数判定を行う

    Args:
        n (int): 整数

    Returns:
        bool: 素数なら True
    """

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def load_numbers_sorted(txt: str) -> List[int]:
    """ファイルから番号を読み込みソートしてリストを返す

    Args:
        txt (str): ファイルのパス

    Returns:
        List[int]: 番号のリスト
    """

    numbers = []

    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))

    return numbers
