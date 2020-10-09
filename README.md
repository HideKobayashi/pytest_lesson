# pytest_lesson
pytest を習得するためのサンプル

## はじめての pytest

### pytest を実行してみる

次のようなファイルを作成する。

ch1/test_one.py

```python
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
```

pytest を実行する。これは成功する例です。

```sh
$ cd ch1
$ pytest -v test_one.py
```

次は失敗する例です。

ch1/test_two.py

```python
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
```


### テストを１つだけ実行する

```sh
$ cd ch1
$ pytest -v tasks/test_four.py::test_asdict
```
### pytest のオプションを使用する

オプションのリストを表示する。

```sh
$ pytest --help
```
