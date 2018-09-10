import tkinter


class GUI():
    def __init__(self, jobs, log):
        root = tkinter.Tk()
        root.title("Jenkins Viewer 1.0")
        self._jobs = jobs
        self._log = log
        self.build_job_menu(root)
        root.mainloop()

    def build_job_menu(self, root):
        for job in self._jobs:
            print(job)
        rescan = tkinter.Button(root, text="Rescan jobs", width=25, command=self.rescan_jobs)
        rescan.pack()

    def rescan_jobs(self):
        self._log.debug("Rescanning jobs")