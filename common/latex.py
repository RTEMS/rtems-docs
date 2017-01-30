#
# Support for Latex used to build the PDF output format.
#

import os
import platform
import re

package_test_preamble = ['\\newif\\ifsphinxKeepOldNames \\sphinxKeepOldNamestrue',
                         '\documentclass[a4paper,11pt,english]{report}']
package_test_postamble = ['\\begin{document} test \\end{document}']
package_tests = {
    'Bjarne'         : ['\\usepackage[Bjarne]{fncychap}'],
    'alltt'          : ['\\usepackage{alltt}'],
    'amsmath'        : ['\\usepackage{amsmath}'],
    'amssymb'        : ['\\usepackage{amssymb}'],
    'amstext'        : ['\\usepackage{amstext}'],
    'anyfontsize'    : ['\\usepackage{anyfontsize}'],
    'array'          : ['\\usepackage{array}'],
    'atbegshi'       : ['\\usepackage{atbegshi}'],
    'babel'          : ['\\usepackage{babel}'],
    'babel'          : ['\\usepackage{babel}'],
    'calc'           : ['\\usepackage{calc}'],
    'capt-of'        : ['\\usepackage{capt-of}'],
    'charter'        : ['\\usepackage{charter}'],
    'cmap'           : ['\\usepackage{cmap}'],
    'color'          : ['\\usepackage{color}'],
    'eqparbox'       : ['\\usepackage{eqparbox}'],
    'enumitem'       : ['\\usepackage{enumitem}'],
    'etoolbox'       : ['\\usepackage{etoolbox}'],
    'fancybox'       : ['\\usepackage{fancybox}'],
    'fancyhdr'       : ['\\usepackage{fancyhdr}'],
    'fancyvrb'       : ['\\usepackage{fancyvrb}'],
    'float'          : ['\\usepackage{float}'],
    'fncychap'       : ['\\usepackage{fncychap}'],
    'fontenc'        : ['\\usepackage[T1]{fontenc}'],
    'footnote'       : ['\\usepackage{footnote}'],
    'framed'         : ['\\usepackage{framed}'],
    'graphicx'       : ['\\usepackage{graphicx}'],
    'hypcap'         : ['\\usepackage{hyperref}',
                        '\\usepackage{hypcap}'],
    'hyperref'       : ['\\usepackage{hyperref}'],
    'inconsolata'    : ['\\usepackage{inconsolata}'],
    'ifplatform'     : ['\\usepackage{ifplatform}'],
    'ifthen'         : ['\\usepackage{ifthen}'],
    'inputenc'       : ['\\usepackage{inputenc}'],
    'keyval'         : ['\\usepackage{keyval}'],
    'kvoptions'      : ['\\usepackage{kvoptions}'],
    'lato'           : ['\\usepackage{lato}'],
    'lineno'         : ['\\usepackage{lineno}'],
    'longtable'      : ['\\usepackage{longtable}'],
    'makeidx'        : ['\\usepackage{makeidx}'],
    'multirow'       : ['\\usepackage{multirow}'],
    'parskip'        : ['\\usepackage{parskip}'],
    'pdftexcmds'     : ['\\usepackage{pdftexcmds}'],
    'textcomp'       : ['\\usepackage{textcomp}'],
    'threeparttable' : ['\\usepackage{threeparttable}'],
    'times'          : ['\\usepackage{times}'],
    'titlesec'       : ['\\usepackage{titlesec}'],
    'upquote'        : ['\\usepackage{upquote}'],
    'utf8'           : ['\\usepackage[utf8]{inputenc}'],
    'wrapfig'        : ['\\usepackage{wrapfig}'],
    'xcolor'         : ['\\usepackage{xcolor}'],
    'xstring'        : ['\\usepackage{xstring}'],
}
package_optional = ['inconsolata',
                    'lato']

#
# Add per host support. If there is a version clash for the same texlive
# package create a directory, add to that directory and use the path in this
# name here.
#
hosts = {
    # All versions of CentOS until told otherwise
    'Linux/centos' : { '.*' : ['capt-of.sty',
                               'eqparbox.sty',
                               'environ.sty',
                               'ifplatform.sty',
                               'trimspaces.sty',
                               'slantsc.sty',
                               'upquote.sty'] }
}

def tex_test(test):
    return os.linesep.join(package_test_preamble +
                           package_tests[test] +
                           package_test_postamble)

def host_name():
    uname = os.uname()
    if uname[0] == 'Linux':
        distro = platform.dist()
        name = '%s/%s' % (uname[0], distro[0])
        version = distro[1]
    else:
        name = uname[0]
        version = uname[2]
    return name, version

def local_packages():
    host, version = host_name()
    packages = None
    if host in hosts:
        for hv in list(hosts[host].keys()):
            if re.compile(hv).match(version) is not None:
                packages = hosts[host][hv]
    return packages

def configure_tests(conf):
    #
    # Using a hint from ita (thank you) :
    #  https://github.com/waf-project/waf/blob/master/demos/tex/wscript
    #
    def build_latex_test(bld):
        def write_tex_test(tsk):
            tsk.outputs[0].write(tex_test(tsk.env.TEST))

        test = bld.kw['tex_test']
        bld.env.TEST = test

        bld.to_log('%s.tex %s' % (test, '=' * (40 - len(test) + 5)))
        bld.to_log(tex_test(test))
        bld.to_log('=' * 40)

        bld(rule = write_tex_test, target = 'main.tex')
        bld(features = 'tex', type = 'pdflatex', source = 'main.tex', prompt = 0)

    tests = sorted(package_tests.keys())
    local_packs = local_packages()
    excludes = [p for p in package_optional]
    if local_packs is not None:
        excludes += [p[:p.rfind('.')] for p in local_packs]
    for e in excludes:
        if e in tests:
            tests.remove(e)

    fails = 0
    r = conf.find_program("pygmentize", mandatory = False)
    if r is None:
        fails += 1
    for t in tests:
        r = conf.test(build_fun = build_latex_test,
                      msg = "Checking for Tex package '%s'" % (t),
                      tex_test = t,
                      okmsg = 'ok',
                      errmsg = 'not found (please install)',
                      mandatory = False)
        if r is None:
            fails += 1
    if fails > 0:
        conf.fatal('There are %d Tex package failures. Please fix.' % (fails))

    fails = 0
    for t in package_optional:
        r = conf.test(build_fun = build_latex_test,
                      msg = "Checking for Tex package '%s'" % (t),
                      tex_test = t,
                      okmsg = 'ok',
                      errmsg = 'not found (degraded fonts)',
                      mandatory = False)
        if r is None:
            fails += 1
    if fails == 0:
        conf.env.RTEMSEXTRAFONTS = 'rtemsextrafonts.sty'
    else:
        if not conf.options.disable_extra_fonts:
            conf.fatal('Extra fonts not found, install or use --disable-extra-fonts')
        conf.env.RTEMSEXTRAFONTS = 'rtemsextrafonts-null.sty'
