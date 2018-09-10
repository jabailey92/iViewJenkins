import tkinter
from functools import partial

BLUE="#5495ff"
RED="#fc3c3c"

class GUI():
    def __init__(self, jobs, log):
        root = tkinter.Tk()
        root.title("Jenkins Viewer 1.0")
        root.minsize(200, 200)
        root.configure(bg="#464649")
        topLabel = tkinter.Label(root, text="Total Jobs: {}".format(len(jobs)), font='Helvetica 18 bold', bg="#464649", fg="white", width=25)
        topLabel.pack()
        self._jobs = jobs
        self._log = log
        self.build_job_menu(root)
        root.mainloop()

    def build_job_menu(self, root):
        for job in self._jobs:
            click_with_arg=partial(self.job_clicked, job)
            button = tkinter.Button(root, text=job.get_name(), width=25, command=click_with_arg, bg=self._sort_colouring(job.get_status()))
            button.pack()
        # rescan = tkinter.Button(root, text="Rescan jobs", width=25, command=self.rescan_jobs)
        # rescan.pack()

    def rescan_jobs(self):
        self._log.debug("Rescanning jobs")

    def job_clicked(self, job):
        self._log.debug("Job {} clicked".format(job.get_name()))
        print(job)

    def _sort_colouring(self, status):
        if status == "blue":
            return BLUE
        else:
            return RED