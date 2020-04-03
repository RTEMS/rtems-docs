RTEMS Project Documentation
===========================

The documents are written in ReST and built using Sphinx. The build system will
check the version of Sphinx and ensure you have a suitable version
available. If your host does not provide a packaged version use PIP to fetch a
recent version. The Sphinx website provides details on doing this.

ReST is the Re-Structured-Text format. It is a simple markup language that allows
us to create quality documentaion. It is flexible and powerful however does not
attempt to train it to create a specific format. You need to test any new way
of presenting something on all output formats. What may look great in one
format may not translate with the same clarity to another output format.

The RTEMS Documentation output formats are:

 HTML        - Multi-page HTML with files in a single directory per manual.
 PDF         - Single PDF per manual.
 Single HTML - Single HTML, one file per manual.

The PDF format is created using Latex and that uses texlive packages. This
exposes us to the complex world of Latex however the quality of the documents
created is worth it.

Images can be created from source using PlantUML and Ditaa.

A Sphinx checksheet is:

 http://docs.sphinxdocs.com/en/latest/cheatsheet.html#rst-cheat-sheet

Production Quality Hosts
------------------------

We allow the building of PDF documentation on hosts that do not have a fully
suitable texlive environment and this results in quality that is not at the
production level.

The hosts which produce production quality are:

 FreeBSD
 CentOS 6 and 7 (if using texlive, not RPMs of texlive)

NOTE: RedHat Enterprise Linux (RHEL) and Fedora should be the same as CentOS.

Images
------

All images should be placed int he 'images' directory and referenced from the
ReST with a relative path. This lets us shared and control images.

We prefer being able to build images from source. This is not always possible
so SVG format is preferred with generated PNG images to make sure the quality
is consistent when building PDF output.

Building images requires the source with an apporoiate file extension
is placed in the images directory. The built output image is written
back to the images directory. All images may be built or rebuilt when
building images is enabled via the waf configure command line. Please
only add and commit those images that have changed.

We support building images in:

1. PlantUML (.puml), enable with `--plantuml`

2. Ditaa (.ditaa), enable with `--ditaa`

We support the PlantUML image language. The PlantUML home page is:

 http://plantuml.com/

The page as a link to an 'online demo server' you can use to create images
rathre than installing PlantUML. Save you source then View and save the PNG
format image. The PlantUML language reference guide is:

 http://plantuml.com/PlantUML_Language_Reference_Guide.pdf

And the web site has online documentation. The image source extension is
'.puml'.

We also support Ditaa image language. The Ditaa home page is:

 http://ditaa.sourceforge.net/

The home page contain the language options. The PlantUML online demo server
supports Ditaa so use that resource as an online tool. The Ditaa image source
extension is '.ditaa'.

You do not need PlantUML or Ditaa install to build our documentation. The
online resources can be used. Save the source and the generated PNG file in the
same directory under 'images'.

Host Setup
----------

HTML builds directly with Sphinx, PDF requires a full Latex (texlive) install,
and building a Single HTML page requires the 'inliner' tool. The
sphinxcontrib-bibtex extension is mandatory. PlantUML requres the Node.js
package called 'node-plantuml' which installs the 'puml' command and Ditaa needs
the 'ditaa' command and package. Ditaa images are built using the 'puml'
command.

Please add your host as you set it up.

The best environment to use is `virtualenv`. It can create a specific python
environment using `pip`.

Virtualenv
~~~~~~~~~~

Create a directory to house the virtualenv, create the envrionment and the
activate it:

  $ mkdir sphinx
  $ virtualenv sphinx
  $ . ./sphinx/bin/activate

The prompt will now change. You can install Sphinx with:

  $ pip install sphinx
  $ pip install sphinxcontrib-bibtex

When you have finished you enter `deactivate`.

Sphinx Per User Install
~~~~~~~~~~~~~~~~~~~~~~~

You can use this method to install a personal version of Sphinx if your host
does not provide a suitable package:

  $ pip install -U --user sphinx
  $ pip install --user sphinxcontrib-bibtex

On some hosts, this may complain that a newer version of pip is available.
If so, then upgrade pip into your personal area.

 $ pip install --upgrade --user pip

The personal area for these tools is ${HOME}/.local/bin. It should
be PREPENDED to your path. On a 32-bit install of CentOS, RHEL, or
Fedora, these were the PATH modifications to use the local install of
Texlive and sphinx:

  export PATH=/usr/local/texlive/2016/bin/i386-linux/:${PATH}
  export PATH=${HOME}/.local/bin:${PATH}

If on a 64-bit install of CentOS, RHEL, or Fedora, these will
be the PATH modifications to use the local install of Texlive
and sphinx:

  export PATH=/usr/local/texlive/2016/bin/x86_64-linux/:${PATH}
  export PATH=${HOME}/.local/bin:${PATH}

Windows
~~~~~~~

To build the documentation on Windows you need to install an offical Python
build from https://www.python.org/. We suggest you install a recent 2.7 series
64bit build. The versions 2.7.9 and after include pip.

Note: you cannot use the MSYS2 versions of Python because the pip libraries
that contain C or C++ code are built with MSVC libraries and cannot integrate
with the MSYS2 built python.

The following assumes Python is installed to its default path of C:\Python27.

Open an MSYS2 terminal window and add the needed paths to Python and its
scripts:

 $ export PATH=/c/Python27/Scripts:/c/Python27:$PATH

Install Sphinx and any needed extensions:

 $ pip install sphinx
 $ pip install sphinxcontrib-bibtex

FreeBSD
~~~~~~~

PDF Quality: production

Sphinx:

  # pkg install py27-sphinx

PDF:

  # pkg install texlive-full

Single HTML:

  # pkg install npm
  # npm install -g inliner

Plant UML:

Install NPM as shown in Single HTML then:

  # npm install -g node-plantuml

Ditaa:

  # pkg install ditaa

CentOS 7
~~~~~~~~

PDF Quality: production

Python 3:

By default, CentOS 7 has Python 2.x. Luckily they now have Software
Collections which lets you install and use a "collection" of newer
software. As root,

  # yum install centos-release-scl
  # yum install rh-python36

Then you can create your own virtual Python environment
for use with the Sphinx toolchain.

  $ cd ~
  $ python -m venv rtemsdocs

When you want to use the Sphinx toolchain.

  $ scl enable rh-python36 bash
  $ source ~/rtemsdocs/bin/activate

Sphinx:

  $ pip install -U sphinx

PDF:

  WARNING: Do NOT use the RPMs for texlive. They are incomplete and, in
           the best case, result in ugly PDFs.

  As root, install texlive per the instructions at
  http://tug.org/texlive/acquire-netinstall.html

  # wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
  # tar xf install-tl-unx.tar.gz
  # cd install-tl-20161106
    NOTE: The date in the name of the directory will change.
  # ./install-tl
    - Use the command line system. Select "O" for options if you want to
      change from A4 to US letter paper size by default.
    - Select "I" to install
    - The tools will be installed into a directory like the following:
      /usr/local/texlive/2016/bin/i386-linux/

     NOTE: The year (2016) and host OS (i386-linux) will change to
           reflect 32 or 64 bit and OS name.

  You will also likely need to install the aspell RPM.

Single HTML:

NOTE: npm appears to be part of the EPEL repository for RHEL and CentOS.
You may have to add that repository to your configuration.

  # yum install npm
  # npm install -g inliner

Plant UML:

Install NPM as shown in Single HTML then:

  # npm install -g node-plantuml

Spell check:

  # yum install aspell

PATH:

  Ensure the appropriate directories are PREPENDED to your PATH before
  building the documentation. Examples are shown below:

  export PATH=/usr/local/texlive/2016/bin/i386-linux/:${PATH}
  export PATH=${HOME}/.local/bin:${PATH}

Arch Linux
~~~~~~~~~~

Sphinx:

  # pacman -S python-sphinx

PDF:

  # pacman -S texlive-bin texlive-core texlive-latexextra texlive-fontsextra

openSUSE
~~~~~~~~

Packages:

  # zypper in python-pip 'texlive*'

Sphinx:

  # pip install -U Sphinx

Using pip to install Sphinx destroys the python-Sphinx package if installed via
RPM.

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

An example of failures are:

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

Note: waf-1.9.5 is a little noisy when running tex builds and tests. I hope
      to have this resolved soon.

To build enter in the top directory:

  $ ./waf configure [--pdf] [--singlehtml] [--prefix] \
                    [--sphinx-options] \
                    [--sphinx-nit-pick] \
                    [--plantuml] \
                    [--ditaa] \
                    [--disable-extra-fonts]

  $ ./waf

The '--pdf' and '--singlehtml' options can be added to configure to build those
output formats.

Sphinx options can be added using the `--sphinx-options` option. If you have
more than option use a quoted argument. This is an advanced feature that can
be useful when experimenting with the `sphinx-build` command.

Sphinx nit-picky mode adds `-n` to the `sphinx-build` command line to generate
warnings and extra information about the source to help make sure our
documentation source is as clean as possible. Please use this when writing
documentation or making updates.

The '--disable-extra-fonts' allows you to build PDF documents with out the
fonts we use for a better quality document. Use this option to build without
needing the extra fonts accepting you will get poor quality documents.

To build and install to a specific location:

  $ ./waf configure --prefix=/foo/my/location
  $ ./waf build install

To build the PlantUML and Ditaa images:

  $ ./waf configure --plantuml --ditaa
  $ ./waf clean build

To nit-pick the source use:

  $ ./waf configure --sphinx-nit-pick
  $ ./waf clean build

If you need to debug what is happening use configure with a suitable Sphinx
verbose level:

  $ ./waf configure --sphinx-options "-V -V"
  $ ./waf clean build

You can enter a manual's directory and run the same configure command and build
just that manual.

Documentation Standard
----------------------

This following details the documentation standard. If in doubt first search the
existing documentation for an example and if unsure ask.

1. All text is to be formatted to wrap at 80 columns. Do not manually line feed
   before 80.

2. Do not insert tab characters, use spaces, no trailing white space.

3. Pasted text such as console output can exceed 80 columns however it is
   preferred even this text is wrapped at 80 columns. Long lines in code block
   text causes issues with the PDF output.

4. The headings use the following:

      Heading   Description
      1  ###### Part
      2  ****** Section
      3  ====== Sub-section
      4  ------ Sub-sub-section
      5  ^^^^^^ Sub-sub-sub-section
      6  ~~~~~~ Sub-sub-sub-sub-section

5. For literal output, such as shell commands and code do not use '::'
   at the trailing edge of the previous paragraph as it generates
   warnings as the autodetect fails to find a suitable format. Use the
   '.. code-block::' with a suitable lexical label. The lexers are:

     http://pygments.org/docs/lexers/

   Use the short names. For C code use 'c' code and 'shell' for shell
   scripts and for terminal output use 'none'. If you need line
   numbers use:

    .. code-block:: shell
       :linenos:

   We support two forms of commands and outputs.

   The first is to have a shell command block with just the commands
   and if required an output block with the output or some of the
   output. Use 'none' for the output block. Make sure the text clearly
   states the block is the output, if it has been edited to shorten
   the amount of output and if there are any special operating modes,
   for example needing to be 'root'.

   The second is to use a single block of type 'none' with the command
   and output together as seen in a terminal session. The commands are
   identifed by the standard shell prompt characters where '$' is a
   user prompt and '#' is a 'root' prompt.

6. Use the directives for 'note', 'warning', and 'topic'. Do not add 'TIP',
   'Important' or 'Warning' to the text. Let the mark-up language handle
   this. The supported directives are:

     .. warning::
     .. note::
     .. topic::

   These directives reference specific CSS style support.

7. Images are placed in the 'images' directory. Do not place images in the
   source directories. Using a common 'images' tree of images promotes sharing
   of images. To add an image use:

    .. figure:: ../images/my-image.png
       :wdith: 75%
       :align: center
       :alt: This is the alt text for some output types.

8. Callouts can be implemented manually using a literal block which can use
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

       4. Exit with an exit code of 0. This value can be checked by the
          caller of this program.

   Note, the topic items are manually numbered, which makes it easier to see
   which item matches the text. Use <> for the number and align at a position
   that works and makes the number as visible as possible. Use hanging indents
   if an items extends past a single line.

9. Use the RTEMS domain references for URLs and mailing lists. For example to
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

  The valid URLs are:

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
