#! /usr/bin/env python
#
# Convert the CSV compliance data to ReST Format.
#

from __future__ import print_function

import copy
import csv
import os
import sys

standards = [
    'RTEMS',
    'POSIX-2008',
    'PSE51',
    'PSE52',
    'PSE53',
    'PSE54',
    'C99',
    'FACE 2.1 Security',
    'FACE 2.1 Safety Base',
    'FACE 2.1 Safety Extended',
    'FACE 2.1 General Purpose'
]

standard_names = {
    'RTEMS'                   : 'RTEMS Complete Profile',
    'POSIX-2008'              : 'POSIX-2008',
    'PSE51'                   : 'POSIX PSE51 - Minimal',
    'PSE52'                   : 'POSIX PSE52 - Real-Time Controller',
    'PSE53'                   : 'POSIX PSE53 - Dedicated',
    'PSE54'                   : 'POSIX PSE54 - Multipurpose',
    'C99'                     : 'C99 Standard Library',
    'FACE 2.1 Security'       : 'FACE 2.1 Security',
    'FACE 2.1 Safety Base'    : 'FACE 2.1 Safety Base',
    'FACE 2.1 Safety Extended': 'FACE 2.1 Safety Extended',
    'FACE 2.1 General Purpose': 'FACE 2.1 General Purpose'
}

col_names = {
    'api'                      : 'Methods',
    'header'                   : 'Header File',
    'rtems-net'                : 'RTEMS w/ Networking',
    'rtems-impl'               : 'RTEMS Impl Note',
    'POSIX-2008'               : 'IEEE Std 1003.1-2008',
    'PSE51'                    : 'PSE51',
    'PSE52'                    : 'PSE52',
    'PSE53'                    : 'PSE53',
    'PSE54'                    : 'PSE54',
    'C99'                      : 'C99',
    'FACE 2.1 Security'        : 'FACE 2.1 Security',
    'FACE 2.1 Safety Base'     : 'FACE 2.1 Safety Base',
    'FACE 2.1 Safety Extended' : 'FACE 2.1 Safety Extended',
    'FACE 2.1 General Purpose' : 'FACE 2.1 General Purpose'
}

#
# The columns here contain the logic to determine the
#
categories = {
    'order': ['supported', 'enosys', 'not-supported'],
    'name' : {
        'supported'    : 'Supported',
        'enosys'       : 'ENOSYS',
        'not-supported': 'Not supported'
    },
    'supported': ['The following methods and variables in ``<@HEADER@>``',
                  'are supported:',
                  ''],
    'not-supported': ['The following methods and variables in ``<@HEADER@>``',
                      'are not supported:',
                      ''],
    'enosys': ['The following methods in ``<@HEADER@>`` are implemented as',
               'stubs returning ``-1`` and setting ``errno`` to ``ENOSYS``:',
               '']
}

cat_columns = {
    'order': ['rtems-net', 'rtems-impl'],
    'rtems-net': {
        'supported' : {
            'CTS-YES' : ['invalid'],
            'RT-YES'  : ['invalid'],
            'HAND-YES': ['invalid']
        },
        'not-supported': {
            'CTS-NO' : ['invalid'],
            'RT-NO'  : ['invalid'],
            'HAND-NO': ['invalid']
        }
    },
    'rtems-impl': {
        'enosys': {
            'ENOSYS': ['supported']
        }
    }
}

rst_defaults = {
    'header': ['.. comment SPDX-License-Identifier: CC-BY-SA-4.0',
               '',
               'This chapter has a subsection per header file to detail the methods',
               'provided by RTEMS that are in that header file.',
               '']
}

class error(Exception):
    pass

class compliance:
    def __init__(self):
        self.data = None

    def load(self, name):
        with open(name, 'rb') as f:
            data = csv.reader(f, delimiter = ',', quotechar = '"')
            hdr = None
            rows = []
            for row in data:
                if hdr is None:
                    hdr = row
                else:
                    rows += [row]
        for col in col_names:
            if col_names[col] not in hdr:
                raise error('column not found: %s' % (col_names[col]))
        cdata = { 'columns': hdr, 'headers': {}, 'apis': {} }
        apic = hdr.index(col_names['api'])
        hfc = hdr.index(col_names['header'])
        for row in rows:
            api = row[apic]
            header = row[hfc]
            if len(api) == 0 or len(header) == 0:
                continue
            if header not in cdata['headers']:
                cdata['headers'][header] = [api]
            else:
                cdata['headers'][header] += [api]
            if api in cdata['apis']:
                raise error('duplicate api: %s' % (api))
            cdata['apis'][api] = row
        self.data = cdata

    def summary(self, standard = 'RTEMS'):
        results = { }
        for header in self.data['headers']:
            hr = self.process_header(header, standard)
            if 'invalid' in hr:
                error('header contains "invalid": %s' % (header))
            for cat in hr:
                if cat not in results:
                    results[cat] = len(hr[cat])
                else:
                    results[cat] += len(hr[cat])
        if standard == 'RTEMS':
            std_line = 'The follow table summarizes RTEMS supported' \
                       ' methods for all tracked standards:'
        else:
            std_line = 'The follow table summarizes alignment with ' \
                       'the %s standard:' % (standard_names[standard])
        s = ['Summary',
             '=======',
             '',
             std_line,
             '']
        cols = [0, 1]
        for cat in categories['order']:
            if len(categories['name'][cat]) > cols[0]:
                cols[0] = len(categories['name'][cat])
            if cat in results:
                num = '%d' % results[cat]
                if len(num) > cols[1]:
                    cols[1] = len(num)
        table_def = ' %s  %s' % ('=' * cols[0], '=' * cols[1])
        s += [table_def]
        for cat in categories['order']:
            if cat in results:
                s += [' %-*s  %d' % (cols[0], categories['name'][cat], results[cat])]
            else:
                s += [' %-*s  %d' % (cols[0], categories['name'][cat], 0)]
        s += [table_def, '']
        return s

    def output(self, standard = 'RTEMS'):
        def _category_filter(text, patterns):
            for l in range(0, len(text)):
                for pat in patterns:
                    if pat in text[l]:
                        text[l] = text[l].replace(pat, patterns[pat])
            return text

        if standard not in standards:
            error('invalid standard": %s' % (standard))
        s = rst_defaults['header'] + self.summary(standard)
        for header in sorted(self.data['headers'].keys()):
            hr = self.process_header(header, standard)
            if 'invalid' in hr:
                error('header contains "invalid": %s' % (header))
            print_heading = True
            for cat in categories['order']:
                if cat in hr:
                    if print_heading:
                        s += ['``<%s>``' % (header),
                              '=' * (len(header) + 2),
                              '']
                        print_heading = False
                    patterns = { '@HEADER@': header }
                    cat_text = copy.copy(categories[cat])
                    _category_filter(cat_text, patterns)
                    s += cat_text
                    for api in hr[cat]:
                        s += ['* ``%s``' % (api)]
                    s += ['']
        return s

    def process_header(self, header, standard = 'RTEMS'):
        results = { }
        if standard != 'RTEMS':
            std_col = self.data['columns'].index(col_names[standard])
        else:
            std_col = -1
        for api in sorted(self.data['headers'][header]):
            api_row = self.data['apis'][api]
            if std_col > 0:
                if api_row[std_col] != 'INCL':
                    continue
            state = 'invalid'
            for test in cat_columns['order']:
                col = self.data['columns'].index(col_names[test])
                value = api_row[col]
                for test_state in cat_columns[test]:
                    if value in cat_columns[test][test_state]:
                        if state in cat_columns[test][test_state][value]:
                            state = test_state
            if state not in results:
                results[state] = [api]
            else:
                results[state] += [api]
        return results

if __name__ == "__main__":
    try:
        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        if len(sys.argv) != 2:
            raise error('not enough arguments')
        c = compliance()
        c.load(sys.argv[1])
        for h in sorted(c.data['headers']):
            print('-- %s' % (h), '-' * 50)
            hr = c.process_header(h)
            if 'invalid' in hr:
                error('header contains invalid: %s' % (h))
            hr = c.process_header(h, 'PSE51')
            if 'invalid' in hr:
                error('header contains invalid: %s' % (h))
            pp.pprint(hr)
        print('=' * 80)
        print(os.linesep.join(c.output('PSE51')))
        print('=' * 80)
        print(os.linesep.join(c.output()))
        for s in standards:
            print('=-' * 40)
            print(os.linesep.join(c.summary(s)))
    except error as e:
        print('error: %s' % (e), file = sys.stderr)
