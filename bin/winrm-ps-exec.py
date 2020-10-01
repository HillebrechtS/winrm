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

        detector = Detector()
        the_encoding = detector.detect(result.std_out)
        stdOut = result.std_out.decode(the_encoding)

        the_encoding = detector.detect(result.std_err)
        stdErr = result.std_err.decode(the_encoding)

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