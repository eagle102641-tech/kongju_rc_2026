import threading
import time
import webview

from app import app


def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()

    # Flask 서버가 시작될 시간을 조금 준다.
    time.sleep(2)

    webview.create_window(
        "RC CAR Dashboard",
        "http://127.0.0.1:5000",
        width=1200,
        height=800
    )

    webview.start(gui="qt", debug=True)