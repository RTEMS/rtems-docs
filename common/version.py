#
# RTEMS Documentation Project (http://www.rtems.org/)
# Copyright 2019 Chris Johns (chrisj@rtems.org)
# Copyright (C) 2019 embedded brains GmbH
# All rights reserved.
#
# This file is part of the RTEMS Documentation package in 'rtems-docs'.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

#
# Releasing RTEMS Documentation
# -----------------------------
#
# The VERSION file format is:
#
#  The format is INI. The file requires a `[version`] section and a `revision`
#  and 'date' values:
#
#   [version]
#   revision = <version-string>
#   date = <date-string>
#
#  The `<version-string>` has the `version` and `revision` delimited by a
#  single `.`. An example file is:
#
#   [version]
#   revision = 5.0.not_released
#   date = 1st February 2019
#
#  where the `version` is `5` and the revision is `0` and the package is not
#  released. The label `not_released` is reversed to mean the package is not
#  released. A revision string can contain extra characters after the
#  `revision` number for example `5.0-rc1` or is deploying a package
#  `5.0-nasa-cfs`
#
# User deployment:
#
#  Create a git archive and then add a suitable VERSION file to the top
#  directory of the package.
#

from __future__ import print_function

import os.path

_version = 'invalid'
_date = 'unknown date'
_released = False

def _pretty_day(day):
    if day == 3:
        s = 'rd'
    elif day == 11:
        s = 'th'
    elif day == 12:
        s = 'th'
    elif day == 13:
        s = 'th'
    elif day % 10 == 1:
        s = 'st'
    elif day % 10 == 2:
        s = 'nd'
    else:
        s = 'th'
    return str(day) + s

def get(ctx, rtems_major_version):
    global _version
    global _date
    global _released
    if _version == 'invalid':
        version = rtems_major_version
        date = _date
        released = False
        #
        # Is there a VERSION file for a release or deployed source.
        #
        vc = 'VERSION'
        if os.path.exists(vc):
            try:
                import configparser
            except ImportError:
                import ConfigParser as configparser
            v = configparser.SafeConfigParser()
            try:
                v.read(vc)
            except Exception as e:
                ctx.fatal('Invalid version config format: %s: %s' % (vc, e))
            try:
                version = v.get('version', 'revision')
                date = v.get('version', 'date')
            except Exception as e:
                ctx.fatal('Invalid version file: %s: %s' % (vc, e))
            if not 'not_released' in version:
                _released = True
        else:
            #
            # Get date and version from Git
            #
            if ctx.exec_command(['git', 'diff-index', '--quiet', 'HEAD']) == 0:
                modified = ''
            else:
                modified = '-modified'
            try:
                out = ctx.cmd_and_log(['git', 'log', '-1',
                                       '--format=%h,%cd', '--date=format:%e,%B,%Y'],
                                      quiet = True)
                f = out.strip('\n').split(',')
                version = version + '.' + f[0] + modified
                date = _pretty_day(int(f[1])) + ' ' + f[2] + ' ' + f[3]
            except waflib.Build.Errors.WafError:
                date = 'unknown date'
        _version = version
        _date = date
        _release = released
    return version, date

def string():
    return '%s (%s)' % (_version, _date)

def version():
    return _version

def date():
    return _date

def released():
    return _released
