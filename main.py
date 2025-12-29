from timer import PomodoroTimer

# Somebody's bound to try installing ts without python on em.
import sys

if sys.version_info < (3, 10):
    print("Python 3.10+ is required to run Focus-Lock. Install Python from the official website, then try running again.")
    input("Press Enter to exit.")
    sys.exit(1)

if __name__ == "__main__":
    timer = PomodoroTimer()

    work = int(input("Work minutes:\t"))
    brk = int(input("Break minutes:\t "))

    choice = input("Enable App-Block? (y/n):\t")
    if choice.lower() == 'n':
        timer.blocker.disable()

    timer.configure(work,brk)
    timer.start_work()
    timer.run()
