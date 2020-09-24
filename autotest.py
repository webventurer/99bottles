import os
import subprocess
import sys
import time
import watchdog.observers
import watchdog.events


class ChangeHandler(watchdog.events.FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        if self.extension(event.src_path) == '.py':
            self.run_tests(event)

    def extension(self, filename):
        return os.path.splitext(filename)[-1].lower()

    def run_tests(self, event):
        if not isinstance(event, watchdog.events.FileCreatedEvent):
            return
        output = subprocess.run(
            "clear; nosetests %s" % event.src_path,
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(output)



if __name__ == "__main__":
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]
    event_handler = ChangeHandler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()