# Example: loops monitoring events forever.
#
import pyinotify


class Configuration:
    WATCH_FOLDERS = [ "/tv", "/movies"]

class Daemon:


    def __init__(watch_folders=Configuration.WATCH_FOLDERS):
        wm = pyinotify.WatchManager()
        # Instanciate a new WatchManager (will be used to store watches).

        # Associate this WatchManager with a Notifier (will be used to report and
        # process events).
        notifier = pyinotify.Notifier(wm)

        for folder in watch_folders:
            # Add a new watch on /tmp for ALL_EVENTS.
            wm.add_watch(Configuration.folder, pyinotify.ALL_EVENTS)

    def start():
        # Loop forever and handle events.
        notifier.loop()

daemon = Daemon()
daemon.start()
