#!/usr/bin/env python

import os
import subprocess

def run_shell(cmd):
    try:
        process = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            )
        stdout, stderr = process.communicate(timeout=30)
    except subprocess.TimeoutExpired as e:
        print(e)
        stdout, stderr = e
    except subprocess.CalledProcessError as e:
        print(e)
        stdout, stderr = e.stdout, e.stderr
    if stderr:
        return stderr
    return stdout

if __name__ == "__main__":
    print(run_shell('ls -al'))