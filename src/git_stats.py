#!/usr/bin/python

import getopt
import json
import pprint
import urllib
import sys
import time


def print_help():
    print 'git_stats help '
    print
    print '-h --help                  : Print this help'
    print '-u <url>  or --url <url>   : Select the git repo to analyze'
    print


def extract_commits_from_json(json_data):
    output = []
    for commit in json_data:
        try:
            str_date = commit['commit']['author']['date']
            # '2016-02-16T14:04:24Z
            pattern = '%Y-%m-%dT%H:%M:%SZ'
            epoch = int(time.mktime(time.strptime(str_date, pattern)))
            output.append({epoch: commit['commit']['author']['name']})
        except KeyError as e:
            print "Unexcepted input format :" . e.strerror()
            print "The input format may have change, Exiting"
            sys.exit(1)
        except:
            print "Unexpected error :"
            raise

    return sorted(output)

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

    try:
        json_data = json.load(raw_data)
    except ValueError as e:
        print "Error: The pointed URL is not a valid JSON format"

    if json_data is None:
        print "Error: no data can be read from the pointed URL, Exiting"
        sys.exit(1)

    commits = extract_commits_from_json(json_data)

    pprint.pprint(commits)
