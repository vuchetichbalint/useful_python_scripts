#!/bin/bash

#change to develop branch
git checkout develop

#create new branch from develop
git checkout -b feature/dummy

git add dummy.py
git commit -m"added dummy.py"

#push to remote
git push -u origin feature/dummy

#after that is sufficient
git push