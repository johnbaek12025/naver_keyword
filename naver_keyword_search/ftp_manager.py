# TODO: file.py 의 334 라인을 아래와 같이 수정했는데,
#  상속받아서 수정하는 방식으로 처리하자
#  return line if self._flags
#  & self.FLAG_BINARY else u(line, encoding=encoding)

import paramiko as paramiko
import logging

logger = logging.getLogger(__name__)

class FTPManager(object):

    def __init__(self):
        self.conn = None

    def connect(self, ftp_host, ftp_port,
                         ftp_user, ftp_pass):
        logger.info(f"connect to ftp server {ftp_host}/{ftp_port}")
        try:
            transport = paramiko.Transport((ftp_host, ftp_port))
            transport.connect(username=ftp_user, password=ftp_pass)
            self.conn = paramiko.SFTPClient.from_transport(transport)
            #self.session.chdir(ftp_path)
        except Exception as err:
            logger.error(f"ftp connection to {ftp_host}/{ftp_port} failed: {err}")
            raise

    def disconnect(self):
        if self.conn:
            logger.info(f"disconnect from ftp server")
            self.conn.close()

    def send(self, from_path, to_path):
        try:
            self.conn.put(from_path, to_path)
        except Exception as err:
            logger.error(f"[ftp] seding from {from_path} to {to_path} failed: {err}")
            raise