git_stats
=========

.. contents::

Introduction
------------

git_stats is a sample tool to compute some stats of a github repository.


Usage
-----

git_stats connect to a github repository to report the following items :
    - mean time between commits
    - top <n> contributors (5 is the default)


A typical usage looks like :

.. code:: bash

    [erwan@localhost]$ git_stats -u https://api.github.com/repos/ceph/ceph/commits?per_page=1000
    The Average time between two commits is : 1509.90 minutes

    The top 5 contributors are :
     Author                           : Commits
     -------------------------------- : -------
     Matt Benjamin                    :      64
     Orit Wasserman                   :       2
     Sage Weil                        :       7
     Josh Durgin                      :       1
     Kefu Chai                        :       4


Syntax
------
Options:

-    -h or --help
        Print the help message

-    -u <url> or --url <url>
        Select the github repository to analyze.

        Could be any http/https/ftp url style.

-    -c <count> or --count <count>
        Top <count> contributors (Default: 5)

        Note that if *count* is greater than the number of found contributors, then a small warning is shown like :

.. code:: bash

        The top 1000 contributors are :
         Author                           : Commits
         -------------------------------- : -------
         Matt Benjamin                    :      64
         Orit Wasserman                   :       2
         Sage Weil                        :       7
         Josh Durgin                      :       1
         Kefu Chai                        :       4
         Gregory Farnum                   :       4
         Mykola Golub                     :       1
         Greg Farnum                      :       2
         Yehuda Sadeh                     :       5
         Pete Zaitcev                     :       1
         Dan Mick                         :       1
         Loic Dachary                     :       1
         Jason Dillaman                   :       7
         Only 13 contributors. Unable to reach 1000
