# -*- coding: utf-8 -*-

import os
import time
import logging

from StubEventHandler import StaticEventHandler, ViewEventHandler
from watchdog.observers import Observer
from flask_mock import app
from multiprocessing import Process

STATIC_PATH = "static"
VIEW_PATH = "flask_mock"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def static_watcher():
    print("----static_watcher")
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

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
    print("----view_watcher")
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

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


import subprocess

def run_server():
    app.run()


def shutdown_server():
    subprocess.call("ls -al")


if __name__ == '__main__':
    server_process = Process(target=run_server)
    static_process = Process(target=static_watcher)
    view_process = Process(target=view_watcher)

    server_process.start()
    static_process.start()
    view_process.start()

    server_process.join()
    static_process.join()
    view_process.join()
