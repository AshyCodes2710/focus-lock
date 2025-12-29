class Blocker:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def enable(self):
        self.enabled = True
        print("[BLOCK] Enabled.")

    def disable(self):
        self.enabled = False
        print("[BLOCK] Disabled.")

    def enforce(self):
        if not self.enabled:
            return
        print("[BLOCK] App-Block \'Enforced\'.")

    def release(self):
        if not self.enabled:
            return
        print("[BLOCK] App-Block \'Released\'.")


