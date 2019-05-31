# hol a python?
which python
#vagy which python2.7


#igy hozok letre virtualenv-et:
virtualenv -p /usr/bin/python2.7 python2.7
virtualenv -p /usr/bin/python3.5 python3.5


#igy aktivalom:
source python2.7/bin/activate

# es igy deaktivalom:
deactivate




virtualenv -p  ~/workspace/tensorflow tensorflow --system-site-packages

#igy volt jo
virtualenv --system-site-packages ~/workspace/tensorflow
