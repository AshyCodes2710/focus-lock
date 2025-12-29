import time
from state import PomodoroState
from blocker import Blocker

class PomodoroTimer:
    def __init__(self):
        self.work_seconds = 0
        self.break_seconds = 0
        self.state = PomodoroState.IDLE
        self.remaining = 0
        self.running = False
        self.blocker = Blocker(enabled=True)

    def configure(self, work_minutes, break_minutes):
        self.work_seconds = int(60*work_minutes)
        self.break_seconds = int(60*break_minutes)

    def start_work(self):
        if self.work_seconds <= 0:
            raise ValueError("Hmm... That didn't work. Try setting up \"work duration\"?")

        self.state = PomodoroState.WORK
        self.remaining = self.work_seconds
        self.running = True
        print("[STATE] Work started~!!")

    def start_break(self):
        self.state = PomodoroState.BREAK
        self.remaining =self.break_seconds
        self.running = True
        print("[STATE] Break started~!!")

    def stop(self):
        self.running = False
        self.state = PomodoroState.IDLE
        self.remaining = 0
        print("[STATE] Stopped :<")

    def tick(self):
        if not self.running:
            return

        if self.remaining > 0:
            self.remaining -= 1
        else: 
            if self.state == PomodoroState.WORK:
                self.start_break()
            elif self.state == PomodoroState.BREAK:
                self.stop()

    def run(self):
        try:
            while self.running:
                mins, secs= divmod(self.remaining, 60)
                print(
                    f"\r[{self.state.name}] {mins:02d}:{secs:02d}",
                    end = '',
                    flush = True
                )
                # ENFORCE THE FUCKEN APP BLOCK AND *** ONLY *** DURING WORK.
                if self.state == PomodoroState.WORK:
                    self.blocker.enforce()

                time.sleep(1)
                self.tick()
        except KeyboardInterrupt:
            print("Inerrupted by Keyboard!! Timer stopped :<")
            self.stop()

