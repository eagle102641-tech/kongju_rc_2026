from pathlib import Path

import webview


def main():
    html_path = Path(__file__).resolve().parent.parent / 'front' / 'clock.html'
    window = webview.create_window(
        '탁상 시계',
        url=html_path.as_uri(),
        width=520,
        height=620,
        resizable=False,
        fullscreen=False,
        min_size=(520, 620),
    )
    try:
        webview.start(gui='qt')
    except Exception as exc:
        print('pywebview 실행 중 오류가 발생했습니다:', exc)
        print('시스템에 Qt/WebEngine 또는 GTK 런타임이 설치되어 있는지 확인하세요.')
        raise


if __name__ == '__main__':
    main()
