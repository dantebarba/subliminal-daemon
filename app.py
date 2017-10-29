# Example: loops monitoring events forever.
#
import pyinotify
import sys
import logging
from datetime import timedelta
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos



class Configuration:
    WATCH_FOLDERS = [ "/tv", "/movies"]
    logging.basicConfig(level=logging.ERROR)

class Daemon:


    def __init__(self, watch_folders=Configuration.WATCH_FOLDERS):
        logging.debug("Daemon init started")
        self.wm = pyinotify.WatchManager()
        # Instanciate a new WatchManager (will be used to store watches).

        # Associate this WatchManager with a Notifier (will be used to report and
        # process events).
        self.notifier = pyinotify.Notifier(self.wm)
        logging.debug("Notifier is set")


        for folder in Configuration.WATCH_FOLDERS:
            # Add a new watch on /tmp for ALL_EVENTS.
            self.wm.add_watch(folder, pyinotify.IN_CREATE)
            logging.debug("Found folder: "+folder)

    def start(self):
        try:
            self.notifier.loop(callback=Daemon.pull_subtitles)
            logging.debug("Daemon started.")
        except pyinotify.NotifierError as err:
            logging.error(err)
            print >> sys.stderr, err

    def pull_subtitles(notifier):
        try:
            SubliminalClient.pull_subtitles()
        except Exception as ex:
            logging.error(ex, exc_info=True)

class SubliminalClient:
    # configure the cache
    region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
    def pull_subtitles():
        for folder in Configuration.WATCH_FOLDERS:
            logging.debug("Pulling subtitles for: "+folder)
            # scan for videos newer than 2 weeks and their existing subtitles in a folder
            videos = scan_videos(folder, age=timedelta(weeks=1))
            # download best subtitles
            subtitles = download_best_subtitles(videos, {Language('eng'), Language('spa')})
            for v in videos:
                save_subtitles(v, subtitles[v])
                if v.title is not None:
                    logging.debug("Pulling video: "+v.title)

logging.debug("Start up")
daemon = Daemon()
daemon.start()
