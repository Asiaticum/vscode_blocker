import datetime
import os
import subprocess
import sys
import time

import psutil
import pyautogui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QInputDialog,
    QMenu,
    QMessageBox,
    QSystemTrayIcon,
)

# アイコンのパスを設定
icon_path = "/path/to/your/icon.jpg"

# 開始時間と終了時間のデフォルト値
start_time_limit = 30
end_time_limit = 59


def is_within_time_range():
    current_time = datetime.datetime.now()
    return start_time_limit <= current_time.minute <= end_time_limit


def set_time_limits():
    global start_time_limit, end_time_limit
    while True:
        new_start_limit, start_ok = QInputDialog.getInt(
            None,
            "Set Start Time Limit",
            "Enter new start time limit (minute):",
            value=start_time_limit,
            min=0,
            max=59,
        )
        if start_ok:
            new_end_limit, end_ok = QInputDialog.getInt(
                None,
                "Set End Time Limit",
                "Enter new end time limit (minute):",
                value=end_time_limit,
                min=0,
                max=59,
            )
            if end_ok:
                if new_end_limit <= new_start_limit:
                    QMessageBox.warning(
                        None,
                        "Invalid Time Range",
                        "End time must be greater than start time.",
                    )
                    continue  # ユーザーが条件を満たすまでループを続ける
                else:
                    start_time_limit = new_start_limit
                    end_time_limit = new_end_limit
                    break  # 正しい入力が得られたらループを抜ける
            else:
                break  # End timeのダイアログでCancelが選択された場合
        else:
            break  # Start timeのダイアログでCancelが選択された場合


def is_vscode_running():
    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"] == "Code.exe":
            return True
    return False


def save_all_in_vscode():
    windows = pyautogui.getWindowsWithTitle("Visual Studio Code")
    if windows:
        try:
            print("VS Code is running.")
            windows[0].activate()

            # 「全て保存」のショートカットを実行
            pyautogui.hotkey("ctrl", "k")
            time.sleep(0.2)  # キー入力の間に短い遅延を設ける
            pyautogui.press("s")
        except:
            pass


def kill_vscode():
    try:
        subprocess.run(
            ["taskkill", "/f", "/im", "Code.exe"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        pass  # Visual Studio Code is not running or already closed.


def check_vscode():
    if is_within_time_range() and is_vscode_running():
        save_all_in_vscode()
        time.sleep(3)  # 3秒待ってからVS Codeを終了
        kill_vscode()


def create_tray_icon(app):
    tray_icon = QSystemTrayIcon(QIcon(icon_path), app)
    tray_icon.setToolTip("VS Code Time Lock")

    menu = QMenu()
    set_time_limits_action = menu.addAction("Set Time Limits")
    set_time_limits_action.triggered.connect(set_time_limits)

    exit_action = menu.addAction("Exit")
    exit_action.triggered.connect(app.quit)

    tray_icon.setContextMenu(menu)
    tray_icon.show()
    return tray_icon


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # この行を追加
    tray_icon = create_tray_icon(app)

    timer = QTimer()
    timer.timeout.connect(check_vscode)
    timer.start(10000)  # 10秒ごとに実行

    sys.exit(app.exec_())  # イベントループを開始


if __name__ == "__main__":
    main()
