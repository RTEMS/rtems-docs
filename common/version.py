#
# RTEMS Documentation Project (http://www.rtems.org/)
# Copyright 2019, 2020 Chris Johns (chrisj@rtems.org)
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
_major = 0
_minor = 0
_revision = 0
_date = 'unknown date'
_released = False

def _pretty_day(ctx, date):
    ''' Format is YYYY-MM-DD'''
    import datetime
    ds = date.split('-')
    if len(ds) != 3:
        ctx.fatal('invalid date format from git: %s' % (date))
    try:
        year = int(ds[0])
    except:
        ctx.fatal('invalid date format from git, converting year: %s' % (date))
    try:
        month = int(ds[1])
    except:
        ctx.fatal('invalid date format from git, converting month: %s' % (date))
    try:
        day = int(ds[2])
    except:
        ctx.fatal('invalid date format from git, converting day: %s' % (date))
    try:
        when = datetime.date(year, month, day)
    except:
        ctx.fatal('invalid date format from git: %s' % (date))
    if day == 3:
        s = 'rd'
    elif day == 11 or day == 12:
        s = 'th'
    elif day % 10 == 1:
        s = 'st'
    elif day % 10 == 2:
        s = 'nd'
    else:
        s = 'th'
    s = when.strftime('%%d%s %%B %%Y' % (s))
    if day < 10:
        s = s[1:]
    return s

def get(ctx, rtems_major_version):
    global _version
    global _date
    global _released
    version = _version
    date = _date
    released = _released
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
            if ctx.exec_command([ctx.env.GIT[0], 'diff-index', '--quiet', 'HEAD']) == 0:
                modified = ''
            else:
                modified = '-modified'
            out = ctx.cmd_and_log([ctx.env.GIT[0], 'log', '-1',
                                   '--format=%h,%cd', '--date=short'],
                                  quiet = True)
            f = out.strip('\n').split(',')
            version = version + '.' + f[0] + modified
            date = _pretty_day(ctx, f[1])
        _version = version
        _date = date
        _release = released
    if version != 'invalid':
        vs = _version.split('.')
        _major = vs[0]
        if len(vs) == 3:
            _minor = vs[1]
            _revision = vs[2]
        elif len(vs) == 2:
            _minor = 0
            _revision = vs[1]
        else:
            ctx.fatal('Invalid version format: %s' % (_version))
    return version, date, released

def string():
    return '%s (%s)' % (_version, _date)

def version():
    return _version

def major():
    return _major

def minor():
    return _minor

def revision():
    return revision

def date():
    return _date

def released():
    return _released
