#!/usr/bin/python3
#
# CherryMusic - a standalone music server
# Copyright (c) 2012 Tom Wallroth & Tilman Boerner
#
# Project page:
#   http://fomori.org/cherrymusic/
# Sources on github:
#   http://github.com/devsnd/cherrymusic/
#
# CherryMusic is based on
#   jPlayer (GPL/MIT license) http://www.jplayer.org/
#   CherryPy (BSD license) http://www.cherrypy.org/
#
# licensed under GNU GPL version 3 (or later)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
import unittest

from cherrymusicserver import log
log.setTest()

from cherrymusicserver import userdb

class TestAuthenticate(unittest.TestCase):
    '''test authentication functions of userdb'''

    def setUp(self):
        self.users = userdb.UserDB(':memory:')
        self.users.addUser('user', 'password', False)


    def tearDown(self):
        pass


    def testRegisteredUserCanLogin(self):
        '''successful authentication must return authenticated user'''

        authuser = self.users.auth('user', 'password')

        self.assertEqual('user', authuser.name,
                         'authentication must return authenticated user')


    def testNoLoginWithWrongPassword(self):
        '''valid username and invalid password = authentication failure'''

        authuser = self.users.auth('user', 'passwordtypo')

        self.assertTupleEqual(userdb.User.nobody(), authuser,
                         'authentication failure must return invalid user')


    def testNoLoginWithInvalidUser(self):
        '''invalid username = authentication failure'''

        authuser = self.users.auth('!@#$%^&*(', ')(*&^%$#')

        self.assertTupleEqual(userdb.User.nobody(), authuser,
                         'authentication failure must return invalid user')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()