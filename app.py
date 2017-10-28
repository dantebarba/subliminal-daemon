# Example: loops monitoring events forever.
#
import pyinotify
import sys
from datetime import timedelta
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos



class Configuration:
    WATCH_FOLDERS = [ "/tv", "/movies"]

class Daemon:


    def __init__(watch_folders=Configuration.WATCH_FOLDERS):
        self.wm = pyinotify.WatchManager()
        # Instanciate a new WatchManager (will be used to store watches).

        # Associate this WatchManager with a Notifier (will be used to report and
        # process events).
        self.notifier = pyinotify.Notifier(wm)

        for folder in watch_folders:
            # Add a new watch on /tmp for ALL_EVENTS.
            self.wm.add_watch(Configuration.folder, pyinotify.ALL_EVENTS)

    def start(self):
        try:
            notifier.loop(daemonize=True, callback=self.pull_subtitles,
                          pid_file='/tmp/pyinotify.pid', stdout='/tmp/pyinotify.log')
        except pyinotify.NotifierError as err:
            print >> sys.stderr, err

    def pull_subtitles(self):
        SubliminalClient.pull_subtitles()

class SubliminalClient:
    # configure the cache
    region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
    def pull_subtitles():
        for folder in Configuration.WATCH_FOLDERS:
            # scan for videos newer than 2 weeks and their existing subtitles in a folder
            videos = scan_videos(folder, age=timedelta(weeks=1))
            # download best subtitles
            subtitles = download_best_subtitles(videos, {Language('eng'), Language('spa')})
            for v in videos:
                save_subtitles(v, subtitles[v])

daemon = Daemon()
daemon.start()
