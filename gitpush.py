#!/usr/bin/env python3
import os
commitmsg = input('Add you Commit Message: ')
movedir = 'cd ~/mycode'
gitadd = 'git add *'
gitcommit = 'git commit -m "' + commitmsg + '"'
gitpush = 'git push origin main'
print("\nYour commit message was: " + commitmsg +"\n")
#cd ~/mycode
os.system(movedir)
# git add *
os.system(gitadd)
# git commit -m "{commitmsg}"
os.system(gitcommit)
# git push origin main
os.system(gitpush)
