from tasks import send1, send2, send, send3
import tasks.interaction

# いま関数 send() は引数で受け取った文字列を receive() にそのまま渡さなければならないという仕様があったとします。このとき、 send() が仕様どおりに実装されているかどうかをテストするためには

# モックによるモンキーパッチ
def test_send1(mocker):
    receive = mocker.patch('tasks.interaction.receive')

    send('Hello World!')

    # send1() は receive() を1回だけ呼び出しているか？
    # send1() が受け取った文字列は receive() にそのまま渡されているか？
    # receive.assert_called_once_with('Hello World!')
    assert receive.call_args_list == [
        mocker.call('Hello World!'),
    ]

# モックが２回呼ばれる場合
def test_send2(mocker):
    receive = mocker.patch('tasks.interaction.receive')

    send2('Hello World!')

    # send2() は receive() を2回だけ呼び出しているか？
    # send2() が受け取った文字列は receive() にそのまま渡されているか？
    assert receive.call_args_list == [
        mocker.call('[1]: Hello World!'),
        mocker.call('[2]: Hello World!'),
    ]

# モックの戻り値の偽装
def test_send(mocker, capsys):
    # recieve 戻り値が False の場合
    receive = mocker.patch('tasks.interaction.receive', return_value=False)
    # メッセージを送る
    send('Hello World!')
    # メッセージが１回のみかつ送ったメッセージが受け取られたか
    receive.assert_called_once_with('Hello World!')
    # recieve 戻り値が False の場合、標準出力が 'failure'
    out, _ = capsys.readouterr()
    assert out == "failure\n"

    # recieve 戻り値が True の場合
    receive = mocker.patch('tasks.interaction.receive', return_value=True)
    # メッセージを送る
    send('Hello World!')
    # メッセージが１回のみかつ送ったメッセージが受け取られたか
    receive.assert_called_once_with('Hello World!')
    # recieve 戻り値が True の場合、標準出力が 'success'
    out, _ = capsys.readouterr()
    assert out == "success\n"

# スパイ
def test_send3(mocker, capsys):
    receive = mocker.spy(tasks.interaction, 'receive')
    # メッセージを送る
    send3('Hello World!')
    # メッセージが１回のみかつ送ったメッセージが受け取られたか
    receive.assert_called_once_with('Hello World!')
    # recieve の標準出力が 'received: Hello World!'
    out, _ = capsys.readouterr()
    assert out == "received: Hello World!\n"
