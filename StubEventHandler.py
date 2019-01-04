from watchdog.events import LoggingEventHandler
from make_structure import create_stub_views


class StaticEventHandler(LoggingEventHandler):

    def on_moved(self, event):
        create_stub_views()

    def on_created(self, event):
        create_stub_views()

    def on_deleted(self, event):
        create_stub_views()


class ViewEventHandler(LoggingEventHandler):
    def on_moved(self, event):
        create_stub_views()

    def on_created(self, event):
        create_stub_views()

    def on_deleted(self, event):
        create_stub_views()
