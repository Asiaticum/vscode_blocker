# vscode_blocker

## 概要
VS Code Time Blockerは、指定された時間帯にVisual Studio Code (VS Code) を自動的に保存し、終了させるツールです。このアプリケーションは、Pythonで書かれており、PyInstallerを使用して実行可能ファイル（.exe）に変換されます。アプリケーションはシステムトレイに常駐し、バックグラウンドで動作します。

## アイコン画像へのパス追加
vscode_blocker.pyの
```python
# アイコンのパスを設定
icon_path = "/path/to/your/icon.jpg"
```
の部分を、好きなアイコン画像へのパスに修正してください。

## ライブラリのインストール
ライブラリインストール:
このアプリケーションを実行するために必要なライブラリを以下でインストールします。
```bash
pip install pyautogui psutil PyQt5 pyinstaller
```

## exeファイルの作成
スクリプトファイル（vscode_blocker.py）があるディレクトリで以下のコマンドを実行してください。

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole .\vscode_blocker.py
```
これにより、distディレクトリ内にvscode_blocker.exeが生成されます。

## 使用方法
アプリケーションの起動:
distディレクトリ内のvscode_blocker.exeをダブルクリックしてアプリケーションを起動します。アイコンがシステムトレイに表示され、アプリケーションがバックグラウンドで実行を開始します。

時間帯の設定:
システムトレイのアイコンを右クリックし、「Set Time Limits」を選択して、VS Codeを終了させたい時間帯を設定します。

終了:
システムトレイのアイコンを右クリックし、「Exit」を選択することでアプリケーションを終了させることができます。
