#
# Copyright (C) 2016 Redhat
#
# Author: Erwan Velu <erwan@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import pprint
import unittest
from git_stats import stats


class TestStats(unittest.TestCase):

    def test_get_json(self):
        json_struct = [{u'author': {u'avatar_url': u'https://avatars.githubusercontent.com/u/59071?v=3',
              u'events_url': u'https://api.github.com/users/tchaikov/events{/privacy}',
              u'followers_url': u'https://api.github.com/users/tchaikov/followers',
              u'following_url': u'https://api.github.com/users/tchaikov/following{/other_user}',
              u'gists_url': u'https://api.github.com/users/tchaikov/gists{/gist_id}',
              u'gravatar_id': u'',
              u'html_url': u'https://github.com/tchaikov',
              u'id': 59071,
              u'login': u'tchaikov',
              u'organizations_url': u'https://api.github.com/users/tchaikov/orgs',
              u'received_events_url': u'https://api.github.com/users/tchaikov/received_events',
              u'repos_url': u'https://api.github.com/users/tchaikov/repos',
              u'site_admin': False,
              u'starred_url': u'https://api.github.com/users/tchaikov/starred{/owner}{/repo}',
              u'subscriptions_url': u'https://api.github.com/users/tchaikov/subscriptions',
              u'type': u'User',
              u'url': u'https://api.github.com/users/tchaikov'},
  u'comments_url': u'https://api.github.com/repos/ceph/ceph/commits/22c6d3549e1eb27145686e5b3daaf412765e00c7/comments',
  u'commit': {u'author': {u'date': u'2016-02-17T09:21:29Z',
                          u'email': u'tchaikov@gmail.com',
                          u'name': u'Kefu Chai'},
              u'comment_count': 0,
              u'committer': {u'date': u'2016-02-17T09:21:29Z',
                             u'email': u'tchaikov@gmail.com',
                             u'name': u'Kefu Chai'},
              u'message': u'Merge pull request #7603 from roidayan/xio_fixes\n\nXio fixes\r\n\r\nReviewed-by: Matt Benjamin <mbenjamin@redhat.com>\r\nReviewed-by: Casey Bodley <cbodley@redhat.com>',
              u'tree': {u'sha': u'50a939b87fd9dd96a5757d1f44c51653cde39449',
                        u'url': u'https://api.github.com/repos/ceph/ceph/git/trees/50a939b87fd9dd96a5757d1f44c51653cde39449'},
              u'url': u'https://api.github.com/repos/ceph/ceph/git/commits/22c6d3549e1eb27145686e5b3daaf412765e00c7'},
  u'committer': {u'avatar_url': u'https://avatars.githubusercontent.com/u/59071?v=3',
                 u'events_url': u'https://api.github.com/users/tchaikov/events{/privacy}',
                 u'followers_url': u'https://api.github.com/users/tchaikov/followers',
                 u'following_url': u'https://api.github.com/users/tchaikov/following{/other_user}',
                 u'gists_url': u'https://api.github.com/users/tchaikov/gists{/gist_id}',
                 u'gravatar_id': u'',
                 u'html_url': u'https://github.com/tchaikov',
                 u'id': 59071,
                 u'login': u'tchaikov',
                 u'organizations_url': u'https://api.github.com/users/tchaikov/orgs',
                 u'received_events_url': u'https://api.github.com/users/tchaikov/received_events',
                 u'repos_url': u'https://api.github.com/users/tchaikov/repos',
                 u'site_admin': False,
                 u'starred_url': u'https://api.github.com/users/tchaikov/starred{/owner}{/repo}',
                 u'subscriptions_url': u'https://api.github.com/users/tchaikov/subscriptions',
                 u'type': u'User',
                 u'url': u'https://api.github.com/users/tchaikov'},
  u'html_url': u'https://github.com/ceph/ceph/commit/22c6d3549e1eb27145686e5b3daaf412765e00c7',
  u'parents': [{u'html_url': u'https://github.com/ceph/ceph/commit/64c1d54354a09a8485193dce9d5da1c526d1aadd',
                u'sha': u'64c1d54354a09a8485193dce9d5da1c526d1aadd',
                u'url': u'https://api.github.com/repos/ceph/ceph/commits/64c1d54354a09a8485193dce9d5da1c526d1aadd'},
               {u'html_url': u'https://github.com/ceph/ceph/commit/bfafc3b3fd7305a39a507d11e443f93a2ae22f31',
                u'sha': u'bfafc3b3fd7305a39a507d11e443f93a2ae22f31',
                u'url': u'https://api.github.com/repos/ceph/ceph/commits/bfafc3b3fd7305a39a507d11e443f93a2ae22f31'}],
  u'sha': u'22c6d3549e1eb27145686e5b3daaf412765e00c7',
  u'url': u'https://api.github.com/repos/ceph/ceph/commits/22c6d3549e1eb27145686e5b3daaf412765e00c7'}]
 
        data = stats.to_json(stats.get_raw_file("file://%s/git_stats/tests/sample_1_commit" %
            os.getcwd()))
        self.assertEqual(data, json_struct)

if __name__ == "__main__":
    unittest.main()
