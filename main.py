from timer import PomodoroTimer

# Somebody's bound to try installing ts without python installed.
import sys

if sys.version_info < (3, 10):
    print("Python 3.10+ is required to run Focus-Lock. Install Python from the official website, then try running again.")
    input("Press Enter to exit.")
    sys.exit(1)

def parse_time_hms(time_str: str) -> int:
    """
    Parse time in HH:MM:SS format into total seconds.
    """
    try:
        parts = time_str.strip().split(':')
        if len(parts) != 3:
            raise ValueError("Expected format HH:MM:SS (e.g. 00:20:00)")

        hours, minutes, seconds = map(int, parts)

        if hours < 0:
            raise ValueError("Hours cannot be negative")

        if not (0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Minutes and seconds must be between 0 and 59")

        return hours * 3600 + minutes * 60 + seconds

    except ValueError as e:
        raise ValueError(f"Invalid time format: {e}")



if __name__ == "__main__":
    timer = PomodoroTimer()
    try:
        work_str = input("Work Time {HH:MM:SS}:\t")
        brk_str = input("Break Time {HH:MM:SS}:\t")
 
        work_seconds = parse_time_hms(work_str)
        break_seconds = parse_time_hms(brk_str)
 
        timer.configure_seconds(work_seconds, break_seconds)
    except ValueError as e:
        print(e)
        sys.exit(1)

    choice = input("Enable App-Block? (y/n):\t")
    if choice.lower() == 'n':
        timer.blocker.disable()

    timer.start_work()
    timer.run()
