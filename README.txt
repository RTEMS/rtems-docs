RTEMS Project Documentation
===========================

The documents is written in ReST and built using Sphinx. The build system will
check the version and ensure you have a suitable version. If your host does not
provide a packaged version use PIP to fetch a recent version. The Sphinx
website provides details on doing this.

ReST is the Re-Structed-Text format. It is a simple markup language that allows
us to create quality documentaion. It is flexible and powerful however do not
attempt to train it to create a specific format. You need to test any new way
of present something on all output formats. What may look great in one format
may not translate with the same clarity to another output format.

The RTEMS Documentation output formats are:

 HTML        - Multi-page HTML with files in a single directory per manual.
 PDF         - Single PDF per manual.
 SIngle HTML - Single HTML, one file per manual.

Host Setup
----------

HTML builds directly with Sphinx, PDF requires a full Latex install, and
building a Single HTML page requires the 'inliner' tool.

Please add your host as you set it up.

FreeBSD
~~~~~~~

Sphinx:

  # pkg install py27-sphinx

PDF:

  # pkg install texlive-full

Single HTML:

  # pkg install npm
  # npm install -g inliner

CentOS 7
~~~~~~~~

PDF:

  # yum install -y texlive-*

Single HTML:

  # yum install npm
  # npm install -g inliner

This does not provide all the require packages. Missing are:

  capt-of
  eqparbox
  ifplatform
  inconsolata
  lato
  upquote

Latex Setup
~~~~~~~~~~~

Latex is used to create the PDF document.  The setup of Latex varies from host
to host operating system due to the way each host packages the texlive
packages. There is no common naming and no real way to figure what texlive
package is present in a host's packaging. It seems not all of texlive is
available.

The RTEMS Documentation waf configure phase check for each texlive package used
in the generated output and the styles. If you complete configure with the
--pdf option you should be able to build PDF documentation.

The texlive package requirments come from the Latex styles we are using and
Sphinx.

An example of a failure is a default CentOS 7:

  Checking for Tex package 'Bjarne'        : ok
  Checking for Tex package 'alltt'         : ok
  Checking for Tex package 'amsmath'       : ok
  Checking for Tex package 'amssymb'       : ok
  Checking for Tex package 'amstext'       : ok
  Checking for Tex package 'array'         : ok
  Checking for Tex package 'atbegshi'      : ok
  Checking for Tex package 'babel'         : ok
  Checking for Tex package 'calc'          : ok
  Checking for Tex package 'capt-of'       : not found (please install)
  Checking for Tex package 'charter'       : ok
  Checking for Tex package 'cmap'          : ok
  Checking for Tex package 'color'         : ok
  Checking for Tex package 'eqparbox'      : not found (please install)
  Checking for Tex package 'etoolbox'      : ok
  Checking for Tex package 'fancybox'      : ok
  Checking for Tex package 'fancyhdr'      : ok
  Checking for Tex package 'fancyvrb'      : ok
  Checking for Tex package 'float'         : ok
  Checking for Tex package 'fncychap'      : ok
  Checking for Tex package 'fontenc'       : ok
  Checking for Tex package 'footnote'      : ok
  Checking for Tex package 'framed'        : ok
  Checking for Tex package 'graphicx'      : ok
  Checking for Tex package 'hypcap'        : ok
  Checking for Tex package 'hyperref'      : ok
  Checking for Tex package 'ifplatform'    : not found (please install)
  Checking for Tex package 'ifthen'        : ok
  Checking for Tex package 'inconsolata'   : not found (please install)
  Checking for Tex package 'inputenc'      : ok
  Checking for Tex package 'keyval'        : ok
  Checking for Tex package 'kvoptions'     : ok
  Checking for Tex package 'lato'          : not found (please install)
  Checking for Tex package 'lineno'        : ok
  Checking for Tex package 'longtable'     : ok
  Checking for Tex package 'makeidx'       : ok
  Checking for Tex package 'multirow'      : ok
  Checking for Tex package 'parskip'       : ok
  Checking for Tex package 'pdftexcmds'    : ok
  Checking for Tex package 'textcomp'      : ok
  Checking for Tex package 'threeparttable' : ok
  Checking for Tex package 'times'          : ok
  Checking for Tex package 'titlesec'       : ok
  Checking for Tex package 'upquote'        : not found (please install)
  Checking for Tex package 'utf8'           : ok
  Checking for Tex package 'wrapfig'        : ok
  Checking for Tex package 'xcolor'         : ok
  Checking for Tex package 'xstring'        : ok
  There are 6 Tex package failures. Please fix.

If you find there is an issue please post the developers list.

Building
--------

To build enter in the top directory:

  $ ./waf configure [--pdf] [--singlehtml] [--prefix] [--sphinx-verbose]
  $ ./waf

The '--pdf' and '--singlehtml' options can be added to configure to build those
output formats.

To build and install to a specific location:

  $ ./waf configure --prefix=/foo/my/location
  $ ./waf build install

If you need to debug what is happening use configure with a suitable Sphinx
version level:

  $ ./waf configure --sphinx-verbose=-v
  $ ./waf clean build

You can enter a manual's directory and run the same configure command and build
just that manual.

Documentation Standard
----------------------

This following details the documentation standard. If in doubt first search the
existing documentation for an example and if unsure ask.

1. All text is to be formatted to wrap at 80 columns. Do not manually line feed
   before 80.

2. Pasted text such as console output can exceed 80 columns however it is
   preferred even this text is wrapped at 80 columns. Long lines in code block
   text causes issues with the PDF output.

3. The headings use the following:

      Heading
      1  ======
      2  ------
      3  ~~~~~~
      4  ^^^^^^

3. For literal output, such as shell commands and code use '::' at the trailing
   edge of the previous paragraph. If the '.. code-block::' with
   'c' for C code and 'shell' for shell code and terminal output. If you need
   line number use:

    .. code-block:: shell
       :linenos:

4. Use the directives for 'note', 'warning', and 'topic'. Do not add 'TIP',
   'Important' or 'Warning' to the text. Let the mark-up language handle
   this. The supported directives are:

     .. warning::
     .. note::
     .. topic::

   These directives reference specific CSS sytle support.

5. Images are placed in the 'images' directory. Do not place images in the
   source directories. Using a common 'images' tree of images promotes sharing
   of images. To add an image use:

    .. figure:: ../images/my-image.png
       :wdith: 75%
       :align: center
       :alt: This is the alt text for some output types.

6. Callouts can be implement manually using a liternal block which can using
   '::' or a code block and topic block is used for the items. For
   example:

     .. code-block: c

        #include <stdio.h>  <1>
        int main(int argc, char** argv)  <2>
        {
           printf("Hello world\n");  <3>
           return 0;   <4>
        }

     .. topic:: Items:

       1. Include the standard input/output header file.

       2. The program starts here.

       3. Print something to the standard output device.

       4. Exit with an exit code of 0. This is value can be checked by the
          caller of this program.

   Note, the topic items are manually number. This makes is easier to see which
   item matches the text. Use <> for the number and align at a position that
   works and makes the number as visible as possible. Use hanging indents if an
   items extends over a single line.

7. Use the RTEMS domain references for URLs and mailing lists. For example to
   insert the RTEMS developers list use:

     :r:list:`devel`
     :r:url:`git`

   The valid lists are:

     announce     : Announce Mailing List
     bugs         : Bugs Mailing List
     devel        : Developers Mailing List
     build        : Build Logs
     users        : Users Mailing List
     vc           : Version Control Mailing List

  The valif URLs are:

     trac         : https://devel.rtems.org/
     devel        : https://devel.rtems.org/
     www          : https://www.rtems.org/
     buildbot     : https://buildbot.rtems.org/
     builder      : https://builder.rtems.org/
     docs         : https://docs.rtems.org/
     lists        : https://lists.rtems.org/
     git          : https://git.rtems.org/
     ftp          : https://ftp.rtems.org/
     review       : https://review.rtems.org/
     bugs         : https://devel.rtems.org/wiki/Bugs/
     gsoc         : https://devel.rtems.org/wiki/GSoC/
     socis        : https://devel.rtems.org/wiki/SOCIS/
