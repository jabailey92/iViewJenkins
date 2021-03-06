import jenkins
from job import job

class jConn:
    def __init__(self, ip, username, token, log):
        self._log = log
        self._ip = self._sort_ip_if_needed(ip)
        self._user = username
        self._token = token
        self._conn = None

    def _sort_ip_if_needed(self, ip):
        self._log.debug("Checking the ip address has HTTP in it")
        if "http://" in ip:
            return ip
        elif "http://" not in ip:
            return "http://" + ip
        else:
            raise Exception("Something went wrong when trying to figure out if to use HTTP or not.")

    def _connection(self):
        if self._conn is None:
            self._log.debug("Creating a connection as _conn is None")
            self._conn = jenkins.Jenkins(self._ip, username=self._user, password=self._token)
        return self._conn

    def get_all_jobs(self):
        jobs = []
        jenkinsJobs = self._connection().get_jobs()
        for json in jenkinsJobs:
            jobs.append(job(json))

        return jobs

    def update_status(self):
        self._log.debug("Checking status")

    def get_job_info(self, job_name):
        # print(self._connection().get_build_info(job_name, 2))
        # print(self._connection().get_build_console_output(job_name, 2))
        return self._connection().get_job_info(job_name)

    def get_build_info(self, job_name, build_number):
        return self._connection().get_build_info(job_name, build_number)

    def get_build_output(self, job_name, build_number):
        return self._connection().get_build_console_output(job_name, build_number)