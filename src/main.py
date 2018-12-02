#!/usr/bin/env python3

""" suricata-logstalgia
Streams Suricata EVE logs to Logstalgia Custom Log Format.
See README.md for documentation.
"""

import json
import socket
import sys
import time

import tailer
from dateutil import parser


class SuricataLogstalgia(object):
    def __init__(self):
        socket.setdefaulttimeout(5.0)

    def __call__(self):
        try:
            for s_line in tailer.follow(open("/eve.json")):
                try:
                    j_line = json.loads(s_line)

                    dt_ts = parser.parse(j_line['timestamp'])

                    unix_ts = time.mktime(dt_ts.timetuple())

                    try:
                        t_hostname = socket.gethostbyaddr(j_line['src_ip'])
                        hostname = t_hostname[0]
                    except:
                        hostname = j_line['src_ip']

                    try:
                        t_path = socket.gethostbyaddr(j_line['dest_ip'])
                        path = t_path[0]
                    except:
                        path = j_line['dest_ip']

                    response_code = '200'
                    response_size = '1024'
                    success = '1'

                    logstalgia_line = "{}|{}|{}|{}|{}|{}".format(
                        unix_ts,
                        hostname,
                        path,
                        response_code,
                        response_size,
                        success,
                        # response_colour,
                        # referrer_url,
                        # user_agent,
                        # virtual_host,
                        # pid_other
                    )

                    print(logstalgia_line)

                except:
                    continue

        except IOError as e:
            print("Failed to open \"{}\" with error:\n"
                  "{}".format(self.eve_path, e))

            sys.exit(1)


if __name__ == "__main__":
    daemon = SuricataLogstalgia()
    daemon()
