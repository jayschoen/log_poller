import asyncore
import pyinotify

watched_handle = "/home/jschoen/log_poller/test_log.log"
watched_contents = ''
with open(watched_handle) as f:
  watched_contents = f.readlines()


def diff_files(previous_contents, handle):
  
  modified_contents = ''
  with open(watched_handle, 'r') as f:
    modified_contents = f.readlines()

  print list(set(modified_contents) - set(previous_contents))

####

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

    def process_IN_MODIFY(self, event):
        #print event
        global watched_handle, watched_contents
        diff_files(watched_contents, watched_handle)
        with open(watched_handle, 'r') as f:
          watched_contents = f.readlines() 

notifier = pyinotify.AsyncNotifier(wm, EventHandler())
wdd = wm.add_watch('/home/jschoen/log_poller', mask, rec=True)

asyncore.loop()
