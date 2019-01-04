# -*- coding: utf-8 -*-

import time
import logging
from threading import Thread

from StubEventHandler import StaticEventHandler, ViewEventHandler
from watchdog.observers import Observer
from flask_mock import app

STATIC_PATH = "static"
VIEW_PATH = "flask_mock"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def static_watcher():
    event_handler = StaticEventHandler()
    observer = Observer()
    observer.schedule(event_handler, STATIC_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def view_watcher():
    event_handler = ViewEventHandler()
    observer = Observer()
    observer.schedule(event_handler, VIEW_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.start()
    observer.join()


if __name__ == '__main__':
    static_thread = Thread(target=static_watcher)
    view_thread = Thread(target=view_watcher)
    view_thread.start()
    view_thread.join()
    app.run(host='0.0.0.0', debug=True, port=5555)
    static_thread.start()
    static_thread.join()
