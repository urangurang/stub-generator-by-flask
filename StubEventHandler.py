from watchdog.events import LoggingEventHandler
from make_structure import create_stub_views
import logging


class StaticEventHandler(LoggingEventHandler):

    def on_moved(self, event):
        create_stub_views()

    def on_created(self, event):
        create_stub_views()

    def on_deleted(self, event):
        create_stub_views()


class ViewEventHandler(LoggingEventHandler):
    def on_moved(self, event):
        print(event)
        logging.info("!!!!!!!!!123")

    def on_modified(self, event):
        print(event)
        logging.info("!!!!!!!!!modi")

    def on_created(self, event):
        print(event)
        logging.info("!!!!!!!!!45")

    def on_deleted(self, event):
        print(event)
        logging.info("!!!!!!!!!765 ")
