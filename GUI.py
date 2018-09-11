import tkinter
import threading
from functools import partial
import time

BLUE="#5495ff"
RED="#fc3c3c"
GREY="#CCCCCC"

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
        topLabel = tkinter.Label(self._root, text="Total Jobs: {}".format(len(self._jobs)),
                                 font='Helvetica 18 bold', bg="#464649",
                                 fg="white", width=25)
        topLabel.pack()
        for job in self._jobs:
            click_with_arg=partial(self.job_clicked, job)
            button = tkinter.Button(self._root, text=job.get_name(), width=25, command=click_with_arg,
                                    bg=self._sort_colouring(job.get_status()))
            button.pack()
            self._mainButtons.append(button)
        self._root.mainloop()

    def rescan_jobs(self):
        self._log.debug("Rescanning jobs")

    def job_clicked(self, job):
        self._log.debug("Job {} clicked".format(job.get_name()))
        self.build_job_view(self._jenkinsConnection.get_job_info(job.get_name()), job.get_name())

    def _build_clicked(self, buildNumber, buildInfo, jobName):
        # self._log.debug("Clicked build: {}".format(buildNumber))
        self.build_build_view(buildInfo, buildNumber, jobName)

    def build_job_view(self, jobInfo, jobName):
        self._log.debug("Getting job info for: {}".format(jobName))

        jobView = tkinter.Tk()
        jobView.title(jobName)
        jobView.minsize(200, 200)
        jobView.configure(bg="#464649")

        for build in jobInfo['builds']:
            build_info = self._jenkinsConnection.get_build_info(jobName, build['number'])
            click_button_arg = partial(self._build_clicked, build['number'], build_info, jobName)
            button = tkinter.Button(jobView, text="Build " + str(build['number']), width=25,
                                    command=click_button_arg, bg=self._sort_colouring(build_info['result']))
            button.pack()

    def build_build_view(self, buildInfo, buildNumber, jobName):
        self._log.debug("Job: {}".format(jobName))
        self._log.debug("Build: {}".format(buildNumber))
        print(buildInfo)
        buildView = tkinter.Tk()
        buildView.title("{} : #{}".format(jobName, buildNumber))
        buildView.geometry("500x500")
        buildView.resizable(0, 0)
        buildView.pack_propagate(0)
        buildView.configure(bg=self._sort_colouring(buildInfo['result']))
        status = tkinter.Label(buildView, text="Status: {}".format(buildInfo['result']), font='Helvetica 18 bold',
                               bg=self._sort_colouring(buildInfo['result']), fg="black", width=25)
        status.pack()
        console_heading = tkinter.Label(buildView, text="Console:", font='Helvetica 18 bold',
                               bg=self._sort_colouring(buildInfo['result']), fg="black", anchor="w")
        console_heading.pack()
        console = tkinter.Label(buildView, text=self._jenkinsConnection.get_build_output(jobName, buildNumber), font='Helvetica 10',
                                        bg=self._sort_colouring(buildInfo['result']), fg="black", anchor="w")
        console.pack()



    def _sort_colouring(self, status):
        if (status == "blue") or (status == "SUCCESS"):
            return BLUE
        elif (status == None):
            return GREY
        else:
            return RED

    def _update_button_colouring(self):
        if self._mainButtons != []:
            for button in self._mainButtons:
                button.configure(bg=self._sort_colouring(self._jobs[self._mainButtons.index(button)].get_status()))

    def _update_thread(self, interval=10):
        while True:
            self._log.debug("Checking status of jobs")
            self._jobs = self._jenkinsConnection.get_all_jobs()
            self._update_button_colouring()
            time.sleep(interval)