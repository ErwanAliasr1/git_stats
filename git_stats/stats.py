#!/usr/bin/python

import getopt
import json
import pprint
import numpy
import sys
import time
import urllib
from collections import Counter

DEFAULT_CONTRIBUTOR_COUNT = 5


def print_help():
    print 'git_stats help '
    print
    print '-h --help                     : Print this help'
    print '-u <url>  or --url <url>      : Select the git repo to analyze'
    print '-c <count> or --count <count> : Top <count> contributors (Default: %s)' % DEFAULT_CONTRIBUTOR_COUNT
    print


def to_json(json_stream):
    json_data = None
    try:
        json_data = json.load(json_stream)
    except ValueError as e:
        print "Error: The pointed URL is not a valid JSON format"

    return json_data


def get_raw_file(url):
    raw_data = None
    try:
        raw_data = urllib.urlopen(url)
    except IOError as e:
        print "Error: Cannot open %s with error %s " % (url, e.strerror)
    except:
        print "Error: Unexpected error on %s with %s" % (url, sys.exc_info()[0])
        raise
    return raw_data


def compute_mean(commits):
    last = 0
    delta = []
    for i, commit in enumerate(commits):
        if last:
            delta.append(commit.keys()[0] - last)
        last = commit.keys()[0]
    return numpy.mean(delta)


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


def compute_authors_stats(commits):
    authors = []
    for i, commit in enumerate(commits):
        authors.append(commit[commit.keys()[0]])
    return Counter(authors).most_common()


if __name__ == '__main__':
    url = None
    contributors_count = DEFAULT_CONTRIBUTOR_COUNT
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:c:", ['help', 'url', 'count'])
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
        elif opt in ("-c", "--count"):
            contributors_count = int(arg)

    if url is None:
        print "Error: Url option is mandatory"
        print_help()
        sys.exit(1)

    json_data = to_json(get_raw_file(url))

    if json_data is None:
        print "Error: no data can be read from the pointed URL, Exiting"
        sys.exit(1)

    commits = extract_commits_from_json(json_data)
    mean = compute_mean(commits)
    print "The Average time between two commits is : %.2f minutes" % (mean / 60)

    stats = compute_authors_stats(commits)
    print
    print "The top %d contributors are :" % contributors_count
    print " %-32s : %5s" % ("Author", "Commits")
    print " %-32s : %5s" % ("--------------------------------", "-------")
    author_count = 0
    for author in stats:
        print " %-32s : %7d" %(author[0], author[1])
        author_count += 1
        if (author_count >= contributors_count):
            break
    if author_count < contributors_count:
            print " Only %d contributors. Unable to reach %d " % (author_count, contributors_count)
