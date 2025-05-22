#!/usr/bin/python3

import subprocess
import shlex
import sys

args = sys.argv

# 初期値はで考えること
cnt = int(args[1]) -1
cnt_last = int(args[2])


while True:
    cnt += 1

# コマンドをリストで定義
    commands = [
        "git init",
        "git remote add origin git@github.com:dis-ecstraining/ecs" + str(cnt).zfill(2) + ".git",
        "git pull origin master",
        "git add .",
        "git commit -m 0",
        "git push -f origin master",
        "rm -rf .git",
    ]

# 各コマンドを実行

    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    
        print(f"Command: {command}")
        print(f"Output:\n{stdout.decode()}")
        if stderr:
            print(f"Error:\n{stderr.decode()}")
        print("-" * 40)

    if cnt >= cnt_last + 1:
        break

