from timer import PomodoroTimer

# Somebody's bound to try installing ts without python on em.
import sys

if sys.version_info < (3, 10):
    print("Python 3.10+ is required to run Focus-Lock. Install Python from the official website, then try running again.")
    input("Press Enter to exit.")
    sys.exit(1)

# I have come to the startling realisation that this code accepts 0.5 as 30 seconds. No one remembers seconds as fractions of a minutes
# okay I do but I'm just built different. Maybe even built incorrectly.
#
# This will take an input in the form of HH:MM:SS and then return the total seconds in there.
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

    #work = int(input("Work minutes:\t"))
    #brk = int(input("Break minutes:\t "))
        # had a little bug with the timer input: couldn't add time in seconds. Now we can run a timer in seconds.
    work = float(input("Work minutes:\t"))
    if work <= 0:
        raise ValueError("Work time must be greater than 0")

    brk = float(input("Break minutes:\t"))
    if brk <= 0:
    raise ValueError("Break time must be greater than 0")

    choice = input("Enable App-Block? (y/n):\t")
    if choice.lower() == 'n':
        timer.blocker.disable()

    timer.configure(work,brk)
    timer.start_work()
    timer.run()
