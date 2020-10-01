#!/usr/bin/python

import json
import winrm
import sys
from charamel import Detector




def main():
    try:
        host = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]
        command = sys.argv[4]

        session = winrm.Session(host, auth=(username, password))
        result = session.run_ps(command)

        result.std_out = result.std_out.decode("utf-8", "replace")
        result.std_err = result.std_err.decode("utf-8", "replace")

        stdOut = result.std_out
        stdErr = result.std_err




        resultDict = {
            'std_out': stdOut,
            'std_err': stdErr,
            'status_code': result.status_code
        }
        print(json.dumps(resultDict))
    except BaseException as e:
        print(json.dumps({'std_out': '', 'std_err': str(e), 'status_code': 1}))

if __name__ == "__main__":
    main()