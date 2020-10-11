# 関数 send() は引数で受け取った文字列を receive() にそのまま渡さなければならない

def send1(message: str):
    """１回のみ呼び出し

    Args:
        message (str): メッセージ
    """
    receive(message)

def send2(message: str):
    """２回のみ呼び出し

    Args:
        message (str): メッセージ
    """
    receive('[1]: {}'.format(message))
    receive('[2]: {}'.format(message))


def send(message: str):
    """受け取ったメッセージに応じて動作を変える

    Args:
        message (str): メッセージ
    """
    ans = receive(message)

    if ans:
        print('success')
    else:
        print('failure')

def send3(message: str):
    """１回のみ呼び出し

    Args:
        message (str): メッセージ
    """
    receive(message)


def receive(message: str) -> bool:
    print('received: {}'.format(message))

    return True