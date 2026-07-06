class ScanProgress:

    total = 0
    current = 0
    success = 0
    failed = 0
    current_website = ""
    running = False

    @classmethod
    def reset(cls, total):
        cls.total = total
        cls.current = 0
        cls.success = 0
        cls.failed = 0
        cls.current_website = ""
        cls.running = True

    @classmethod
    def update(cls, website, success):
        cls.current += 1
        cls.current_website = website

        if success:
            cls.success += 1
        else:
            cls.failed += 1

    @classmethod
    def finish(cls):
        cls.running = False

    @classmethod
    def data(cls):
        return {
            "running": cls.running,
            "total": cls.total,
            "current": cls.current,
            "success": cls.success,
            "failed": cls.failed,
            "current_website": cls.current_website,
        }