import tkinter
import threading
from functools import partial
import time

BLUE="#5495ff"
RED="#fc3c3c"

class GUI():
    def __init__(self, jobs, log, jenkins):
        self._jenkinsConnection = jenkins
        self._root = None
        self._mainButtons = []
        self._jobs = jobs
        self._log = log
        t = threading.Thread(target=self._update_thread, daemon=True)
        t.start()
        self.build_job_menu()

    def build_job_menu(self):
        self._root = tkinter.Tk()
        self._root.title("Jenkins Viewer 1.0")
        self._root.minsize(200, 200)
        self._root.configure(bg="#464649")
        topLabel = tkinter.Label(self._root, text="Total Jobs: {}".format(len(self._jobs)), font='Helvetica 18 bold', bg="#464649",
                                 fg="white", width=25)
        topLabel.pack()
        for job in self._jobs:
            click_with_arg=partial(self.job_clicked, job)
            button = tkinter.Button(self._root, text=job.get_name(), width=25, command=click_with_arg, bg=self._sort_colouring(job.get_status()))
            button.pack()
            self._mainButtons.append(button)
        self._root.mainloop()

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

    def _update_button_colouring(self):
        if self._mainButtons != []:
            for button in self._mainButtons:
                button.configure(bg=self._sort_colouring(self._jobs[self._mainButtons.index(button)].get_status()))

    def _update_thread(self, interval=10):
        while(True):
            self._log.debug("Checking status of jobs")
            self._jobs = self._jenkinsConnection.get_all_jobs()
            self._update_button_colouring()
            time.sleep(interval)