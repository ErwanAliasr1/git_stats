#!/usr/bin/python

import getopt
import json
import urllib
import sys


def print_help():
    print 'git_stats help '
    print
    print '-h --help                  : Print this help'
    print '-u <url>  or --url <url>   : Select the git repo to analyze'
    print


if __name__ == '__main__':
    url = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:", ['help', 'url'])
    except getopt.GetoptError:
        print "Error: One option passed to the cmdline was not supported"
        print "Please fix your command line or read the help (-h option)"
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif opt in ("-u", "--url"):
            url = arg

    if url is None:
        print "Error: Url option is mandatory"
        print_help()
        sys.exit(1)

    try:
        raw_data = urllib.urlopen(url)
    except IOError as e:
        print "Error: Cannot open %s with error %s " % (url, e.strerror)
    except:
        print "Error: Unexpected error on %s with %s" % (url, sys.exc_info()[0])
        raise

    json_data = json.load(raw_data)
