import jenkins


class jConn:
    def __init__(self, ip, username, token):
        self._ip = ip
        self._user = username
        self._token = token
        self._conn = jenkins.Jenkins(self._ip, username=self._user, password=self._token)
        # print(self._conn.get_version())

    def _connection(self):
        if self._conn is None:
            return jenkins.Jenkins("http://" + self._ip, username=self._user, password=self._token)

    def test(self):
        self._connection().get_version()
