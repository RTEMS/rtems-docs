#! /usr/bin/env python
#
# Convert the CSV compliance data to ReST Format.
#

from __future__ import print_function
from py_markdown_table.markdown_table import markdown_table

import copy
import csv
import os
import sys

standards = [
    'RTEMS',
    'POSIX-2024',
    'POSIX-2017',
    'POSIX-2008',
    'POSIX-2003',
    'PSE51',
    'PSE52',
    'PSE53',
    'PSE54',
    'C99',
    'C11',
    'C17',
    'FACE 2.1 Security',
    'FACE 2.1 Safety Base',
    'FACE 2.1 Safety Extended',
    'FACE 2.1 General Purpose',
    'FACE 3.0 Security',
    'FACE 3.0 Safety Base',
    'FACE 3.0 Safety Extended',
    'FACE 3.0 General Purpose',
    'FACE 3.1 Security',
    'FACE 3.1 Safety Base',
    'FACE 3.1 Safety Extended',
    'FACE 3.1 General Purpose',
    'FACE 3.2 Security',
    'FACE 3.2 Safety Base',
    'FACE 3.2 Safety Extended',
    'FACE 3.2 General Purpose',
    'SCA 2.2.2 AEP',
    'SCA 4.1 Ultra Lightweight AEP',
    'SCA 4.1 Lightweight AEP',
    'SCA 4.1 [Full] AEP'
]

standard_names = {
    'RTEMS'                   : 'RTEMS Complete Profile',
    'POSIX-2024'              : 'POSIX-2024 (Issue 8)',
    'POSIX-2017'              : 'POSIX-2017 (Issue 7 TC2)',
    'POSIX-2008'              : 'POSIX-2008 (Issue 7)',
    'POSIX-2003'              : 'POSIX-2003 (Issue 6)',
    'PSE51'                   : 'POSIX PSE51 - Minimal',
    'PSE52'                   : 'POSIX PSE52 - Real-Time Controller',
    'PSE53'                   : 'POSIX PSE53 - Dedicated',
    'PSE54'                   : 'POSIX PSE54 - Multipurpose',
    'C99'                     : 'C99 Standard Library',
    'C11'                     : 'C11 Standard Library',
    'C17'                     : 'C17 Standard Library',
    'FACE 2.1 Security'       : 'FACE Technical Standard, Edition 2.1 Security',
    'FACE 2.1 Safety Base'    : 'FACE Technical Standard, Edition 2.1 Safety Base',
    'FACE 2.1 Safety Extended': 'FACE Technical Standard, Edition 2.1 Safety Extended',
    'FACE 2.1 General Purpose': 'FACE Technical Standard, Edition 2.1 General Purpose',
    'FACE 3.0 Security'       : 'FACE Technical Standard, Edition 3.0 Security',
    'FACE 3.0 Safety Base'    : 'FACE Technical Standard, Edition 3.0 Safety Base',
    'FACE 3.0 Safety Extended': 'FACE Technical Standard, Edition 3.0 Safety Extended',
    'FACE 3.0 General Purpose': 'FACE Technical Standard, Edition 3.0 General Purpose',
    'FACE 3.1 Security'       : 'FACE Technical Standard, Edition 3.1 Security',
    'FACE 3.1 Safety Base'    : 'FACE Technical Standard, Edition 3.1 Safety Base',
    'FACE 3.1 Safety Extended': 'FACE Technical Standard, Edition 3.1 Safety Extended',
    'FACE 3.1 General Purpose': 'FACE Technical Standard, Edition 3.1 General Purpose',
    'FACE 3.2 Security'       : 'FACE Technical Standard, Edition 3.2 Security',
    'FACE 3.2 Safety Base'    : 'FACE Technical Standard, Edition 3.2 Safety Base',
    'FACE 3.2 Safety Extended': 'FACE Technical Standard, Edition 3.2 Safety Extended',
    'FACE 3.2 General Purpose': 'FACE Technical Standard, Edition 3.2 General Purpose',
    'SCA 2.2.2 AEP'           : 'Software Communications Architecture 2.2.2 AEP',
    'SCA 4.1 Ultra Lightweight AEP' : 'Software Communications Architecture 4.1 Ultra Lightweight Application Environment Profile',
    'SCA 4.1 Lightweight AEP' : 'Software Communications Architecture 4.1 Lightweight Application Environment Profile',
    'SCA 4.1 [Full] AEP'      : 'Software Communications Architecture 4.1 [Full] Appliation Environment Profile'
}

col_names = {
    'api'                      : 'Methods',
    'header'                   : 'Header File',
    'rtems-net'                : 'RTEMS w/ Networking',
    'rtems-impl'               : 'RTEMS Impl Note',
    'POSIX-2024'               : 'IEEE Std 1003.1-2024 (Issue 8)',
    'POSIX-2017'               : 'IEEE Std 1003.1-2017 (Issue 7 TC2)',
    'POSIX-2008'               : 'IEEE Std 1003.1-2008 (Issue 7)',
    'POSIX-2003'               : 'IEEE Std 1003.1-2003 (Issue 6)',
    'PSE51'                    : 'PSE51',
    'PSE52'                    : 'PSE52',
    'PSE53'                    : 'PSE53',
    'PSE54'                    : 'PSE54',
    'C99'                      : 'C99',
    'C11'                      : 'C11',
    'C17'                      : 'C17',
    'FACE 2.1 Security'        : 'FACE 2.1 Security',
    'FACE 2.1 Safety Base'     : 'FACE 2.1 Safety Base',
    'FACE 2.1 Safety Extended' : 'FACE 2.1 Safety Extended',
    'FACE 2.1 General Purpose' : 'FACE 2.1 General Purpose',
    'FACE 3.0 Security'        : 'FACE 3.0 Security',
    'FACE 3.0 Safety Base'     : 'FACE 3.0 Safety Base',
    'FACE 3.0 Safety Extended' : 'FACE 3.0 Safety Extended',
    'FACE 3.0 General Purpose' : 'FACE 3.0 General Purpose',
    'FACE 3.1 Security'        : 'FACE 3.1 Security',
    'FACE 3.1 Safety Base'     : 'FACE 3.1 Safety Base',
    'FACE 3.1 Safety Extended' : 'FACE 3.1 Safety Extended',
    'FACE 3.1 General Purpose' : 'FACE 3.1 General Purpose',
    'FACE 3.2 Security'        : 'FACE 3.2 Security',
    'FACE 3.2 Safety Base'     : 'FACE 3.2 Safety Base',
    'FACE 3.2 Safety Extended' : 'FACE 3.2 Safety Extended',
    'FACE 3.2 General Purpose' : 'FACE 3.2 General Purpose',
    'SCA 2.2.2 AEP'            : 'SCA 2.2.2 AEP',
    'SCA 4.1 Ultra Lightweight AEP' : 'SCA 4.1 Ultra Lightweight AEP',
    'SCA 4.1 Lightweight AEP' : 'SCA 4.1 Lightweight AEP',
    'SCA 4.1 [Full] AEP'      : 'SCA 4.1 [Full] AEP'
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

md_defaults = {
    'header': ['',
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
        with open(name, 'r') as f:
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
        s = [std_line,
             '']

        table = []

        for cat in categories['order']:
            amount = 0
            if cat in results:
                amount = results[cat]

            table.append({
                "Support": categories['name'][cat],
                "Amount": amount,
            })

        s += markdown_table(table) \
             .set_params(quote=False, row_sep="markdown") \
             .get_markdown().splitlines() + [""]
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
        s = md_defaults['header'] + self.summary(standard)
        for header in sorted(self.data['headers'].keys()):
            hr = self.process_header(header, standard)
            if 'invalid' in hr:
                error('header contains "invalid": %s' % (header))
            print_heading = True
            for cat in categories['order']:
                if cat in hr:
                    if print_heading:
                        s += ['## ``<%s>``' % (header),
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
