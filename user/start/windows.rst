.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _microsoft-windows-installation:

Microsoft Windows
-----------------
.. index:: Microsoft Windows Installation

This section details how you create an RTEMS development environment on
Windows. The installation documented here is on `Windows 7 64bit Professional`.

Developing on Windows
~~~~~~~~~~~~~~~~~~~~~

RTEMS supports Windows as a development host and the tools for most
architectures are available. The RTEMS Project relies on the GNU tools for
compilers and debuggers and we use the simulators that come with GDB and
QEMU. The Windows support for these tools varies and the RTEMS Project is
committed to helping the open source community improve the Windows
experience. If something is not working or supported please email the
:r:list:`users`.

The RTEMS Project's Windows tools are native Windows executables giving the
user the best possible experience on Windows. Native Windows programs use the
standard Windows DLLs and paths. Integration with standard Windows integrated
development tools such as editors is straight forward. POSIX emulation
environments such as Cygwin and the MSYS2 shell have special executables that
require a POSIX emulation DLL and these emulation DLLs add an extra layer of
complexity as well as a performance over-head. The RTEMS Project uses these
POSIX emulation shells to run configure scripts that come with various open
source packages such as `gcc` so they form an important and valued part of the
environment we describe here. The output of this procedure forms the tools you
use during your application development and they do not depend the emulation
DLLs.

The performance of the compiler is as good as you can have on Windows and the
performance compiling a single file will be similar to that on a host like
Linux or FreeBSD given the same hardware. Building the tools from source is
much slower on Windows because POSIX shells and related tools are used and the
POSIX emulation overhead it much much slower than a native POSIX operating
system like Linux and FreeBSD. This overhead is only during the building of the
tools and the RTEMS kernel and if you use a suitable build system that is
native to Windows your application development should be similar to other
operating systems.

Windows path length is limited and can cause problems when building the
tools. The standard Windows API has a ``MAX_PATH`` length of 260
characters. This can effect some of the tools used by RTEMS. It is recommended
you keep the top level directories as short as possible when building the RTEMS
tools and you also keep an eye on the path length when developing your
application. The RTEMS built tools can handle much longer path lengths however
some of the GNU tools such as those in the ``binutils`` package cannot.

POSIX Support
~~~~~~~~~~~~~

Building the RTEMS compilers, debugger, the RTEMS kernel and a number of other
3rd party packages requires a POSIX environment. On Windows you can use Cygwin
or MSYS2. This document focuses on MSYS2. It is smaller than Cygwin and comes
with the Arch Linux package manager ``pacman``.

MSYS2 provides MinGW64 support as well as a POSIX shell called MSYS2. The
MinGW64 compiler and related tools produce 64bit native Windows
executables. The shell is a standard Bourne shell and the MSYS2 environment is
a stripped Cygwin shell with enough support to run the various ``configure``
scripts needed to build the RTEMS tools and the RTEMS kernel.

MSYS2 is built around the ``pacman`` packing tool. This makes MSYS2 a
distribution and that is a welcome feature on Windows. You get a powerful tool
to manage your development environment on Windows.

Python
~~~~~~

We need Python to build the tools as the RSB is written in Python and we need
suitable Python libraries to link to GDB as RTEMS makes use of GDB's Python
support. This place specific demands on the Python we need installed and
available and MSYS2 provides suitable Python versions we can use. You need to
make sure you have the correct type and version of Python installed.

We cannot use the Python executables created by the Python project (python.org)
as they are built by Microsoft's C (MSC) compiler. Linking the MSC Python
libraries with the MinGW64 executables is not easy and MSYS provided us with a
simple solution so we do not support this.

MSYS2 provides two types and versions of Python executables, MinGW and MSYS and
Python version 2 and 3. For Windows we need the MinGW executable so we have
suitables libraries and we have to have Python vrrsion 2 because on Windows GDB
only builds with Python2.

You also need to install the MSYS version of Python along with the MinGW64
Python2 package. The MSYS Python is version 3 and the RSB can support version 2
and 3 of Python and it helps handle some of the long paths building GCC can
generate.

Installing MSYS2
~~~~~~~~~~~~~~~~

MSYS2 is installed on a new machine using the MSYS2 installer found on
https://msys2.github.io/. Please select the ``x86_64`` variant for 64bit
support. Run the installer followin the 7 steps listed on the page.

MSYS2 uses the ``pacman`` package manager. The Arch Linux project has detailed
documentation on how to use ``pacman``. What is shown here is a just few
examples of what you can do.

Open a 64bit MSYS shell from the Start Menu:

.. figure:: msys2-minw64-start-menu.png
   :width: 50%
   :align: center
   :alt: MSYS2 64bit Shell Start Menu

The packages we require are:

 * python
 * mingw-w64-x86_64-python2
 * mingw-w64-x86_64-gcc
 * git
 * bison
 * cvs
 * diffutils
 * make
 * patch
 * tar
 * texinfo
 * unzip

.. note::

   The actual output provided may vary due to changes in the dependent packages
   or newer package versions.

Install the packages using ``pacman``:

.. code-block:: shell

   ~
  $ pacman -S python mingw-w64-x86_64-python2 mingw-w64-x86_64-gcc \
  >           bison cvs diffutils git make patch tar texinfo unzip
  resolving dependencies...
  looking for conflicting packages...

  Packages (74) db-5.3.28-2  expat-2.1.0-2  gdbm-1.11-3  heimdal-1.5.3-8
                libgdbm-1.11-3  mingw-w64-x86_64-binutils-2.26-21
                mingw-w64-x86_64-bzip2-1.0.6-5
                mingw-w64-x86_64-ca-certificates-20150426-2
                mingw-w64-x86_64-crt-git-5.0.0.4627.03684c4-1
                mingw-w64-x86_64-expat-2.1.0-6  mingw-w64-x86_64-gcc-libs-5.3.0-2
                mingw-w64-x86_64-gdbm-1.11-3  mingw-w64-x86_64-gettext-0.19.6-2
                mingw-w64-x86_64-gmp-6.1.0-1
                mingw-w64-x86_64-headers-git-5.0.0.4627.53be55d-1
                mingw-w64-x86_64-isl-0.15-1  mingw-w64-x86_64-libffi-3.2.1-3
                mingw-w64-x86_64-libiconv-1.14-5
                mingw-w64-x86_64-libsystre-1.0.1-2
                mingw-w64-x86_64-libtasn1-4.7-1
                mingw-w64-x86_64-libtre-git-r122.c2f5d13-4
                mingw-w64-x86_64-libwinpthread-git-5.0.0.4573.628fdbf-1
                mingw-w64-x86_64-mpc-1.0.3-2  mingw-w64-x86_64-mpfr-3.1.3.p0-2
                mingw-w64-x86_64-ncurses-6.0.20160220-2
                mingw-w64-x86_64-openssl-1.0.2.g-1
                mingw-w64-x86_64-p11-kit-0.23.1-3
                mingw-w64-x86_64-readline-6.3.008-1  mingw-w64-x86_64-tcl-8.6.5-1
                mingw-w64-x86_64-termcap-1.3.1-2  mingw-w64-x86_64-tk-8.6.5-1
                mingw-w64-x86_64-windows-default-manifest-6.4-2
                mingw-w64-x86_64-winpthreads-git-5.0.0.4573.628fdbf-1
                mingw-w64-x86_64-zlib-1.2.8-9  openssh-7.1p2-1  perl-5.22.0-2
                perl-Authen-SASL-2.16-2  perl-Convert-BinHex-1.123-2
                perl-Encode-Locale-1.04-1  perl-Error-0.17024-1
                perl-File-Listing-6.04-2  perl-HTML-Parser-3.71-3
                perl-HTML-Tagset-3.20-2  perl-HTTP-Cookies-6.01-2
                perl-HTTP-Daemon-6.01-2  perl-HTTP-Date-6.02-2
                perl-HTTP-Message-6.06-2  perl-HTTP-Negotiate-6.01-2
                perl-IO-Socket-SSL-2.016-1  perl-IO-stringy-2.111-1
                perl-LWP-MediaTypes-6.02-2  perl-MIME-tools-5.506-1
                perl-MailTools-2.14-1  perl-Net-HTTP-6.09-1
                perl-Net-SMTP-SSL-1.02-1  perl-Net-SSLeay-1.70-1
                perl-TermReadKey-2.33-1  perl-TimeDate-2.30-2  perl-URI-1.68-1
                perl-WWW-RobotRules-6.02-2  perl-libwww-6.13-1  vim-7.4.1468-1
                bison-3.0.4-1  cvs-1.11.23-2  diffutils-3.3-3  git-2.7.2-1
                make-4.1-4  mingw-w64-x86_64-gcc-5.3.0-2
                mingw-w64-x86_64-python2-2.7.11-4  patch-2.7.5-1  python-3.4.3-3
                tar-1.28-3  texinfo-6.0-1  unzip-6.0-2

  Total Download Size:   114.10 MiB
  Total Installed Size:  689.61 MiB

  :: Proceed with installation? [Y/n] y
  :: Retrieving packages...
   mingw-w64-x86_64-gm...   477.1 KiB   681K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-li...    24.2 KiB   755K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-gc...   541.9 KiB   705K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-ex...   106.7 KiB   702K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-bz...    77.9 KiB   666K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-li...   600.2 KiB   703K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-ge...     3.0 MiB   700K/s 00:04 [#####################] 100%
   mingw-w64-x86_64-gd...   151.8 KiB   483K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-li...    34.5 KiB   705K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-li...    69.2 KiB   713K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-li...     9.3 KiB   778K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-nc...  1800.5 KiB   701K/s 00:03 [#####################] 100%
   mingw-w64-x86_64-li...   171.4 KiB   708K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-p1...   193.5 KiB   709K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-ca...   382.1 KiB   705K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-zl...   148.6 KiB   704K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-op...     3.3 MiB   624K/s 00:05 [#####################] 100%
   mingw-w64-x86_64-te...    12.6 KiB  76.7K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-re...   327.4 KiB   277K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-tc...     2.9 MiB   699K/s 00:04 [#####################] 100%
   mingw-w64-x86_64-tk...  1869.2 KiB   703K/s 00:03 [#####################] 100%
   mingw-w64-x86_64-py...    10.9 MiB   699K/s 00:16 [#####################] 100%
   mingw-w64-x86_64-bi...    12.7 MiB   688K/s 00:19 [#####################] 100%
   mingw-w64-x86_64-he...     5.0 MiB   645K/s 00:08 [#####################] 100%
   mingw-w64-x86_64-cr...     2.6 MiB   701K/s 00:04 [#####################] 100%
   mingw-w64-x86_64-is...   524.3 KiB   684K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-mp...   265.2 KiB   705K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-mp...    62.3 KiB  82.9K/s 00:01 [#####################] 100%
   mingw-w64-x86_64-wi...  1484.0   B  0.00B/s 00:00 [#####################] 100%
   mingw-w64-x86_64-wi...    33.2 KiB   346K/s 00:00 [#####################] 100%
   mingw-w64-x86_64-gc...    25.1 MiB   701K/s 00:37 [#####################] 100%
   python-3.4.3-3-x86_64     12.1 MiB   700K/s 00:18 [#####################] 100%
   bison-3.0.4-1-x86_64    1045.1 KiB   703K/s 00:01 [#####################] 100%
   heimdal-1.5.3-8-x86_64   543.7 KiB   703K/s 00:01 [#####################] 100%
   cvs-1.11.23-2-x86_64     508.2 KiB   388K/s 00:01 [#####################] 100%
   diffutils-3.3-3-x86_64   265.7 KiB   478K/s 00:01 [#####################] 100%
   expat-2.1.0-2-x86_64      13.1 KiB   817K/s 00:00 [#####################] 100%
   vim-7.4.1468-1-x86_64      6.1 MiB   700K/s 00:09 [#####################] 100%
   openssh-7.1p2-1-x86_64   653.4 KiB   703K/s 00:01 [#####################] 100%
   db-5.3.28-2-x86_64        41.7 KiB   719K/s 00:00 [#####################] 100%
   libgdbm-1.11-3-x86_64     20.4 KiB   754K/s 00:00 [#####################] 100%
   gdbm-1.11-3-x86_64       108.5 KiB   704K/s 00:00 [#####################] 100%
   perl-5.22.0-2-x86_64      12.4 MiB   702K/s 00:18 [#####################] 100%
   perl-Error-0.17024-...    17.1 KiB   742K/s 00:00 [#####################] 100%
   perl-Authen-SASL-2....    42.4 KiB   731K/s 00:00 [#####################] 100%
   perl-Encode-Locale-...     9.7 KiB   745K/s 00:00 [#####################] 100%
   perl-HTTP-Date-6.02...     8.6 KiB   784K/s 00:00 [#####################] 100%
   perl-File-Listing-6...     7.7 KiB   769K/s 00:00 [#####################] 100%
   perl-HTML-Tagset-3....    10.3 KiB   732K/s 00:00 [#####################] 100%
   perl-HTML-Parser-3....    76.9 KiB   516K/s 00:00 [#####################] 100%
   perl-LWP-MediaTypes...    18.0 KiB   752K/s 00:00 [#####################] 100%
   perl-URI-1.68-1-any       75.6 KiB   609K/s 00:00 [#####################] 100%
   perl-HTTP-Message-6...    71.3 KiB   625K/s 00:00 [#####################] 100%
   perl-HTTP-Cookies-6...    20.4 KiB   499K/s 00:00 [#####################] 100%
   perl-HTTP-Daemon-6....    14.2 KiB   749K/s 00:00 [#####################] 100%
   perl-HTTP-Negotiate...    11.4 KiB   817K/s 00:00 [#####################] 100%
   perl-Net-HTTP-6.09-...    19.8 KiB   732K/s 00:00 [#####################] 100%
   perl-WWW-RobotRules...    12.2 KiB   766K/s 00:00 [#####################] 100%
   perl-libwww-6.13-1-any   122.2 KiB   661K/s 00:00 [#####################] 100%
   perl-TimeDate-2.30-...    35.9 KiB   718K/s 00:00 [#####################] 100%
   perl-MailTools-2.14...    58.4 KiB   712K/s 00:00 [#####################] 100%
   perl-IO-stringy-2.1...    52.6 KiB   721K/s 00:00 [#####################] 100%
   perl-Convert-BinHex...    30.1 KiB   733K/s 00:00 [#####################] 100%
   perl-MIME-tools-5.5...   180.4 KiB   705K/s 00:00 [#####################] 100%
   perl-Net-SSLeay-1.7...   191.2 KiB   708K/s 00:00 [#####################] 100%
   perl-IO-Socket-SSL-...   112.5 KiB   703K/s 00:00 [#####################] 100%
   perl-Net-SMTP-SSL-1...     3.5 KiB   881K/s 00:00 [#####################] 100%
   perl-TermReadKey-2....    20.9 KiB   745K/s 00:00 [#####################] 100%
   git-2.7.2-1-x86_64         3.6 MiB   702K/s 00:05 [#####################] 100%
   make-4.1-4-x86_64        387.0 KiB   671K/s 00:01 [#####################] 100%
   patch-2.7.5-1-x86_64      75.9 KiB   684K/s 00:00 [#####################] 100%
   tar-1.28-3-x86_64        671.9 KiB   379K/s 00:02 [#####################] 100%
   texinfo-6.0-1-x86_64     992.7 KiB   625K/s 00:02 [#####################] 100%
   unzip-6.0-2-x86_64        93.1 KiB   705K/s 00:00 [#####################] 100%
  (74/74) checking keys in keyring                   [#####################] 100%
  (74/74) checking package integrity                 [#####################] 100%
  (74/74) loading package files                      [#####################] 100%
  (74/74) checking for file conflicts                [#####################] 100%
  (74/74) checking available disk space              [#####################] 100%
  :: Processing package changes...
  ( 1/74) installing python                          [#####################] 100%
  ( 2/74) installing mingw-w64-x86_64-gmp            [#####################] 100%
  ( 3/74) installing mingw-w64-x86_64-libwinpthr...  [#####################] 100%
  ( 4/74) installing mingw-w64-x86_64-gcc-libs       [#####################] 100%
  ( 5/74) installing mingw-w64-x86_64-expat          [#####################] 100%
  ( 6/74) installing mingw-w64-x86_64-bzip2          [#####################] 100%
  ( 7/74) installing mingw-w64-x86_64-libiconv       [#####################] 100%
  ( 8/74) installing mingw-w64-x86_64-gettext        [#####################] 100%
  ( 9/74) installing mingw-w64-x86_64-gdbm           [#####################] 100%
  (10/74) installing mingw-w64-x86_64-libffi         [#####################] 100%
  (11/74) installing mingw-w64-x86_64-libtre-git     [#####################] 100%
  (12/74) installing mingw-w64-x86_64-libsystre      [#####################] 100%
  (13/74) installing mingw-w64-x86_64-ncurses        [#####################] 100%
  (14/74) installing mingw-w64-x86_64-libtasn1       [#####################] 100%
  (15/74) installing mingw-w64-x86_64-p11-kit        [#####################] 100%
  (16/74) installing mingw-w64-x86_64-ca-certifi...  [#####################] 100%
  (17/74) installing mingw-w64-x86_64-zlib           [#####################] 100%
  (18/74) installing mingw-w64-x86_64-openssl        [#####################] 100%
  (19/74) installing mingw-w64-x86_64-termcap        [#####################] 100%
  (20/74) installing mingw-w64-x86_64-readline       [#####################] 100%
  (21/74) installing mingw-w64-x86_64-tcl            [#####################] 100%
  (22/74) installing mingw-w64-x86_64-tk             [#####################] 100%
  (23/74) installing mingw-w64-x86_64-python2        [#####################] 100%
  (24/74) installing mingw-w64-x86_64-binutils       [#####################] 100%
  (25/74) installing mingw-w64-x86_64-headers-git    [#####################] 100%
  (26/74) installing mingw-w64-x86_64-crt-git        [#####################] 100%
  (27/74) installing mingw-w64-x86_64-isl            [#####################] 100%
  (28/74) installing mingw-w64-x86_64-mpfr           [#####################] 100%
  (29/74) installing mingw-w64-x86_64-mpc            [#####################] 100%
  (30/74) installing mingw-w64-x86_64-windows-de...  [#####################] 100%
  (31/74) installing mingw-w64-x86_64-winpthread...  [#####################] 100%
  (32/74) installing mingw-w64-x86_64-gcc            [#####################] 100%
  (33/74) installing bison                           [#####################] 100%
  (34/74) installing heimdal                         [#####################] 100%
  (35/74) installing cvs                             [#####################] 100%
  (36/74) installing diffutils                       [#####################] 100%
  (37/74) installing expat                           [#####################] 100%
  (38/74) installing vim                             [#####################] 100%
  (39/74) installing openssh                         [#####################] 100%
  (40/74) installing db                              [#####################] 100%
  (41/74) installing libgdbm                         [#####################] 100%
  (42/74) installing gdbm                            [#####################] 100%
  (43/74) installing perl                            [#####################] 100%
  (44/74) installing perl-Error                      [#####################] 100%
  (45/74) installing perl-Authen-SASL                [#####################] 100%
  (46/74) installing perl-Encode-Locale              [#####################] 100%
  (47/74) installing perl-HTTP-Date                  [#####################] 100%
  (48/74) installing perl-File-Listing               [#####################] 100%
  (49/74) installing perl-HTML-Tagset                [#####################] 100%
  (50/74) installing perl-HTML-Parser                [#####################] 100%
  (51/74) installing perl-LWP-MediaTypes             [#####################] 100%
  (52/74) installing perl-URI                        [#####################] 100%
  (53/74) installing perl-HTTP-Message               [#####################] 100%
  (54/74) installing perl-HTTP-Cookies               [#####################] 100%
  (55/74) installing perl-HTTP-Daemon                [#####################] 100%
  (56/74) installing perl-HTTP-Negotiate             [#####################] 100%
  (57/74) installing perl-Net-HTTP                   [#####################] 100%
  (58/74) installing perl-WWW-RobotRules             [#####################] 100%
  (59/74) installing perl-libwww                     [#####################] 100%
  Optional dependencies for perl-libwww
      perl-LWP-Protocol-HTTPS: for https:// url schemes
  (60/74) installing perl-TimeDate                   [#####################] 100%
  (61/74) installing perl-MailTools                  [#####################] 100%
  (62/74) installing perl-IO-stringy                 [#####################] 100%
  (63/74) installing perl-Convert-BinHex             [#####################] 100%
  module test... pass.
  (64/74) installing perl-MIME-tools                 [#####################] 100%
  (65/74) installing perl-Net-SSLeay                 [#####################] 100%
  (66/74) installing perl-IO-Socket-SSL              [#####################] 100%
  (67/74) installing perl-Net-SMTP-SSL               [#####################] 100%
  (68/74) installing perl-TermReadKey                [#####################] 100%
  (69/74) installing git                             [#####################] 100%
  Optional dependencies for git
      python2: various helper scripts
      subversion: git svn
  (70/74) installing make                            [#####################] 100%
  (71/74) installing patch                           [#####################] 100%
  Optional dependencies for patch
      ed: for patch -e functionality
  (72/74) installing tar                             [#####################] 100%
  (73/74) installing texinfo                         [#####################] 100%
  (74/74) installing unzip                           [#####################] 100%

Building the Tools
~~~~~~~~~~~~~~~~~~

Create a workspace for RTEMS using the following shell command:

.. sidebar:: *Creating Tool Archives*

  Add ``--bset-tar-file`` to the ``sb-set-builder`` command line to create
  tar files of the built package set.

.. code-block:: shell

   ~
  $ mkdir -p /c/opt/rtems

The ``/c`` path is an internal MSYS2 mount point of the ``C:`` drive. The
command creates the RTEMS work space on the ``C:`` drive. If you wish to use
another drive please subsitute ``/c`` with your drive letter.

We build and install all RTEMS packages under the `prefix` we just created. Change to that
directory and get a copy of the RSB:

.. code-block:: shell

   ~
  $ cd /c/opt/rtems
   /c/opt/rtems
  $ git clone git://git.rtems.org/rtems-source-builder.git rsb
  Cloning into 'rsb'...
  remote: Counting objects: 5716, done.
  remote: Compressing objects: 100% (2183/2183), done.
  remote: Total 5716 (delta 3919), reused 5071 (delta 3494)
  Receiving objects: 100% (5716/5716), 2.46 MiB | 656.00 KiB/s, done.
  Resolving deltas: 100% (3919/3919), done.
  Checking connectivity... done.
  Checking out files: 100% (630/630), done.
   /c/opt/rtems
  $ cd rsb

We are building RTEMS 4.11 tools so select the *4.11* branch:

.. code-block:: shell

   /c/opt/rtems/rsb
  $ git checkout 4.11
  Branch 4.11 set up to track remote branch 4.11 from origin.
  Switched to a new branch '4.11'
   /c/opt/rtems/rsb
  $

Check the RSB has a valid environment:

.. code-block:: shell

   /c/opt/rtems/rsb
  $ cd rtems
   /c/opt/rtems/rsb/rtems
  $ ../source-builder/sb-check
  RTEMS Source Builder - Check, 4.11 (01ac76f2f90f)
  Environment is ok
   /c/opt/rtems/rsb/rtems
  $

To build a set of RTEMS tools for the Intel ``i386`` architecture:

.. code-block:: shell

   /c/opt/rtems/rsb/rtems
  $ ../source-builder/sb-set-builder --prefix=/c/opt/rtems/4.11 4.11/rtems-i386
  RTEMS Source Builder - Set Builder, 4.11 (01ac76f2f90f)
  Build Set: 4.11/rtems-i386
  Build Set: 4.11/rtems-autotools.bset
  Build Set: 4.11/rtems-autotools-internal.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-w64-mingw32-1
  Creating source directory: sources
  download: ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz -> sources/autoconf-2.69.tar.gz
  downloading: sources/autoconf-2.69.tar.gz - 1.8MB of 1.8MB (100%)
   building: autoconf-2.69-x86_64-w64-mingw32-1
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/automake/automake-1.12.6.tar.gz -> sources/automake-1.12.6.tar.gz
  downloading: sources/automake-1.12.6.tar.gz - 2.0MB of 2.0MB (100%)
   building: automake-1.12.6-x86_64-w64-mingw32-1
  cleaning: autoconf-2.69-x86_64-w64-mingw32-1
  cleaning: automake-1.12.6-x86_64-w64-mingw32-1
  Build Set: Time 0:00:42.515625
  Build Set: 4.11/rtems-autotools-base.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-w64-mingw32-1
  building: autoconf-2.69-x86_64-w64-mingw32-1
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-w64-mingw32-1.xml
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-w64-mingw32-1
  building: automake-1.12.6-x86_64-w64-mingw32-1
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-w64-mingw32-1.xml
  tarball: tar/rtems-4.11-autotools-x86_64-w64-mingw32-1.tar.bz2
  installing: autoconf-2.69-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: automake-1.12.6-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  cleaning: autoconf-2.69-x86_64-w64-mingw32-1
  cleaning: automake-1.12.6-x86_64-w64-mingw32-1
  Build Set: Time 0:00:37.718750
  Build Set: Time 0:01:20.234375
  config: devel/expat-2.1.0-1.cfg
  package: expat-2.1.0-x86_64-w64-mingw32-1
  download:   http://downloads.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz -> sources/expat-2.1.0.tar.gz
   redirect:  http://iweb.dl.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz
  downloading: sources/expat-2.1.0.tar.gz - 549.4kB of 549.4kB (100%)
   building: expat-2.1.0-x86_64-w64-mingw32-1
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-w64-mingw32-1.txt
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-w64-mingw32-1.xml
  config: tools/rtems-binutils-2.24-1.cfg
  package: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/binutils/binutils-2.24.tar.bz2 -> sources/binutils-2.24.tar.bz2
  downloading: sources/binutils-2.24.tar.bz2 - 21.7MB of 21.7MB (100%)
  building: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  reporting: tools/rtems-binutils-2.24-1.cfg -> i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-binutils-2.24-1.cfg -> i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1.xml
  config: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg
  package: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/gcc/gcc-4.9.3/gcc-4.9.3.tar.bz2 -> sources/gcc-4.9.3.tar.bz2
  downloading: sources/gcc-4.9.3.tar.bz2 - 85.8MB of 85.8MB (100%)
  download: ftp://sourceware.org/pub/newlib/newlib-2.2.0.20150423.tar.gz -> sources/newlib-2.2.0.20150423.tar.gz
  downloading: sources/newlib-2.2.0.20150423.tar.gz - 16.7MB of 16.7MB (100%)
  download: http://www.mpfr.org/mpfr-3.0.1/mpfr-3.0.1.tar.bz2 -> sources/mpfr-3.0.1.tar.bz2
  downloading: sources/mpfr-3.0.1.tar.bz2 - 1.1MB of 1.1MB (100%)
  download: http://www.multiprecision.org/mpc/download/mpc-0.8.2.tar.gz -> sources/mpc-0.8.2.tar.gz
  downloading: sources/mpc-0.8.2.tar.gz - 535.5kB of 535.5kB (100%)
  download: ftp://ftp.gnu.org/gnu/gmp/gmp-5.0.5.tar.bz2 -> sources/gmp-5.0.5.tar.bz2
  downloading: sources/gmp-5.0.5.tar.bz2 - 2.0MB of 2.0MB (100%)
  building: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
  i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
  i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1.xml
  config: tools/rtems-gdb-7.9-1.cfg
  package: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  download: http://ftp.gnu.org/gnu/gdb/gdb-7.9.tar.xz -> sources/gdb-7.9.tar.xz
  downloading: sources/gdb-7.9.tar.xz - 17.0MB of 17.0MB (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.11/gdb/gdb-sim-arange-inline.diff -> patches/gdb-sim-arange-inline.diff
  downloading: patches/gdb-sim-arange-inline.diff - 761.0 bytes of 761.0 bytes (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.11/gdb/gdb-sim-cgen-inline.diff -> patches/gdb-sim-cgen-inline.diff
  downloading: patches/gdb-sim-cgen-inline.diff - 706.0 bytes of 706.0 bytes (100%)
  building: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  reporting: tools/rtems-gdb-7.9-1.cfg ->
  i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-gdb-7.9-1.cfg ->
  i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1.xml
  config: tools/rtems-tools-4.11-1.cfg
  package: rtems-tools-4.11-1
  Creating source directory: sources/git
  git: clone: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: reset: git://git.rtems.org/rtems-tools.git
  git: fetch: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: checkout: git://git.rtems.org/rtems-tools.git => 4.11
  git: pull: git://git.rtems.org/rtems-tools.git
  building: rtems-tools-4.11-1
  reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11-1.txt
  reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11-1.xml
  config: tools/rtems-kernel-4.11.cfg
  installing: expat-2.1.0-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: rtems-tools-4.11-1 -> C:\opt\rtems\4.11
  cleaning: expat-2.1.0-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  cleaning: rtems-tools-4.11-1
  Build Set: Time 1:32:58.972919
   /c/opt/rtems/rsb/rtems
  $

Building the Kernel
~~~~~~~~~~~~~~~~~~~

We can now build the RTEMS kernel using the RTEMS tools we have just
built. First we need to set the path to the tools:

.. code-block:: shell

   /c/opt/rtems
  $ export PATH=/c/opt/rtems/4.11/bin:$PATH
   /c/opt/rtems
  $

We currently build RTEMS from the git release branch for 4.11:

.. code-block:: shell

   /c/opt/rtems
  $ mkdir kernel
   /c/opt/rtems
  $ cd kernel
   /c/opt/rtems/kernel
  $ git clone git://git.rtems.org/rtems.git rtems
  Cloning into 'rtems'...
  remote: Counting objects: 482766, done.
  remote: Compressing objects: 100% (88781/88781), done.
  remote: Total 482766 (delta 389610), reused 475155 (delta 383437)
  Receiving objects: 100% (482766/482766), 69.77 MiB | 697.00 KiB/s, done.
  Resolving deltas: 100% (389610/389610), done.
  Checking connectivity... done.
  Checking out files: 100% (10626/10626), done.
   /c/opt/rtems/kernel
  $ cd rtems
   /c/opt/rtems/kernel/rtems
  $ git checkout 4.11
  Checking out files: 100% (2553/2553), done.
  Branch 4.11 set up to track remote branch 4.11 from origin.
  Switched to a new branch '4.11'
   /c/opt/rtems/kernel
  $

The kernel code cloned from git needs to be `bootstrapped`. Bootstrapping
creates ``autoconf`` and ``automake`` generated files. To bootstrap we first
clean away any files, then generate the pre-install header file lists and
finally we generate the ``autoconf`` and ``automake`` files using the RSB's
bootstrap tool.

.. code-block:: shell

   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -c
  removing automake generated Makefile.in files
  removing configure files
  removing aclocal.m4 files
   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -p
  Generating ./c/src/ada/preinstall.am
  Generating ./c/src/lib/libbsp/arm/altera-cyclone-v/preinstall.am
  Generating ./c/src/lib/libbsp/arm/atsam/preinstall.am
  Generating ./c/src/lib/libbsp/arm/beagle/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb336/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb337/preinstall.am
  Generating ./c/src/lib/libbsp/arm/edb7312/preinstall.am
  Generating ./c/src/lib/libbsp/arm/gdbarmsim/preinstall.am
    .......
  Generating ./cpukit/score/cpu/mips/preinstall.am
  Generating ./cpukit/score/cpu/moxie/preinstall.am
  Generating ./cpukit/score/cpu/nios2/preinstall.am
  Generating ./cpukit/score/cpu/no_cpu/preinstall.am
  Generating ./cpukit/score/cpu/or1k/preinstall.am
  Generating ./cpukit/score/cpu/powerpc/preinstall.am
  Generating ./cpukit/score/cpu/sh/preinstall.am
  Generating ./cpukit/score/cpu/sparc/preinstall.am
  Generating ./cpukit/score/cpu/sparc64/preinstall.am
  Generating ./cpukit/score/cpu/v850/preinstall.am
  Generating ./cpukit/score/preinstall.am
  Generating ./cpukit/telnetd/preinstall.am
  Generating ./cpukit/wrapup/preinstall.am
  Generating ./cpukit/zlib/preinstall.am
   /c/opt/rtems/kernel/rtems
  $ /c/opt/rtems/rsb/source-builder/sb-bootstrap
  RTEMS Source Builder - RTEMS Bootstrap, 4.11 (76188ee494dd)
    1/139: autoreconf: configure.ac
    2/139: autoreconf: c/configure.ac
    3/139: autoreconf: c/src/configure.ac
    4/139: autoreconf: c/src/ada-tests/configure.ac
    5/139: autoreconf: c/src/lib/libbsp/arm/configure.ac
    6/139: autoreconf: c/src/lib/libbsp/arm/altera-cyclone-v/configure.ac
    7/139: autoreconf: c/src/lib/libbsp/arm/atsam/configure.ac
    8/139: autoreconf: c/src/lib/libbsp/arm/beagle/configure.ac
    9/139: autoreconf: c/src/lib/libbsp/arm/csb336/configure.ac
   10/139: autoreconf: c/src/lib/libbsp/arm/csb337/configure.ac
   11/139: autoreconf: c/src/lib/libbsp/arm/edb7312/configure.ac
    .......
  129/139: autoreconf: testsuites/samples/configure.ac
  130/139: autoreconf: testsuites/smptests/configure.ac
  131/139: autoreconf: testsuites/sptests/configure.ac
  132/139: autoreconf: testsuites/tmtests/configure.ac
  133/139: autoreconf: testsuites/tools/configure.ac
  134/139: autoreconf: testsuites/tools/generic/configure.ac
  135/139: autoreconf: tools/build/configure.ac
  136/139: autoreconf: tools/cpu/configure.ac
  137/139: autoreconf: tools/cpu/generic/configure.ac
  138/139: autoreconf: tools/cpu/nios2/configure.ac
  139/139: autoreconf: tools/cpu/sh/configure.ac
  Bootstrap time: 0:20:38.759766
   /c/opt/rtems/kernel/rtems
  $

We will build the RTEMS kernel for the ``i386`` target and the ``pc686``
BSP. You can check the available BSPs by running the ``rtems-bsps`` command
found in the to directory of the RTEMS kernel source. We build the Board
Support Package (BSP) outside the kernel source tree:

.. code-block:: shell

   /c/opt/rtems/kernel/rtems
  $ cd ..
   /c/opt/rtems/kernel
  $ mkdir pc686
   /c/opt/rtems/kernel
  $ cd pc686
   /c/opt/rtems/kernel/pc686
  $

Configure the RTEMS kernel to build ``pc686`` BSP for the ``i386`` target with
netwoeking disabled, We will build the externel libBSD stack later:

.. code-block:: shell

   /c/opt/rtems/kernel/pc686
  $ /c/opt/rtems/kernel/rtems/configure --prefix=/c/opt/rtems/4.11 \
         --target=i386-rtems4.11 --disable-networking --enable-rtemsbsp=pc686
  checking for gmake... no
  checking for make... make
  checking for RTEMS Version... 4.11.99.0
  checking build system type... x86_64-pc-mingw64
  checking host system type... x86_64-pc-mingw64
  checking target system type... i386-pc-rtems4.11
  checking for a BSD-compatible install... /usr/bin/install -c
  checking whether build environment is sane... yes
  checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
  checking for gawk... gawk
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
  configure: creating ./config.status
  configure: configuring in ./tools/build
    .......
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
  configure: creating ./config.status
  config.status: creating Makefile

  target architecture: i386.
  available BSPs: pc686.
  'make all' will build the following BSPs: pc686.
  other BSPs can be built with 'make RTEMS_BSP="bsp1 bsp2 ..."'

  config.status: creating Makefile
   /c/opt/rtems/kernel/pc686
  $

Build the kernel:

.. code-block:: shell

   /c/opt/rtems/kernel/pc686
  $ make
  Making all in tools/build
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  make  all-am
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  gcc -DHAVE_CONFIG_H -I. -I/c/opt/rtems/kernel/rtems/tools/build     -g -O2 -MT
  cklength.o -MD -MP -MF .deps/cklength.Tpo -c -o cklength.o
  /c/opt/rtems/kernel/rtems/tools/build/cklength.c
  gcc -DHAVE_CONFIG_H -I. -I/c/opt/rtems/kernel/rtems/tools/build     -g -O2 -MT
  eolstrip.o -MD -MP -MF .deps/eolstrip.Tpo -c -o eolstrip.o
  /c/opt/rtems/kernel/rtems/tools/build/eolstrip.c
    ..........
  i386-rtems4.11-objcopy -O binary nsecs.nxe nsecs.bin
  ../../../../../pc686/build-tools/bin2boot -v nsecs.ralf 0x00097E00
  ../../../../../pc686/lib/start16.bin 0x00097C00 0 nsecs.bin 0x00100000 0
  header address       0x00097e00, its memory size 0xzx
  first  image address 0x00097c00, its memory size 0x00000200
  second image address 0x00100000, its memory size 0x0003d800
  rm -f nsecs.nxe
  make[6]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples/nsecs'
  make[5]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples'
  make[4]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples'
  make[4]: Entering directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[4]: Nothing to be done for 'all-am'.
  make[4]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[3]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c'
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686'
  make[1]: Nothing to be done for 'all-am'.
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686'
   /c/opt/rtems/kernel/pc696
  $

Install the kernel to our prefix:

.. code-block:: shell

   /c/opt/rtems/kernel/pc686
  $ make install
  Making install in tools/build
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/bin'
    /usr/bin/install -c cklength.exe eolstrip.exe packhex.exe unhex.exe
    rtems-bin2c.exe '/c/opt/rtems/4.11/bin'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/bin'
   /usr/bin/install -c install-if-change '/c/opt/rtems/4.11/bin'
  make[2]: Nothing to be done for 'install-data-am'.
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/build'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/build'
  Making install in tools/cpu
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  Making install in generic
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[3]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
  make[3]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  make[3]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
    ..........
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686'
  make[2]: Nothing to be done for 'install-exec-am'.
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/make'
   /usr/bin/install -c -m 644 /c/opt/rtems/kernel/rtems/make/main.cfg
   /c/opt/rtems/kernel/rtems/make/leaf.cfg '/c/opt/rtems/4.11/make'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/share/rtems4.11/make/Templates'
   /usr/bin/install -c -m 644
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.dir
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.leaf
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.lib
   '/c/opt/rtems/4.11/share/rtems4.11/make/Templates'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/make/custom'
   /usr/bin/install -c -m 644 /c/opt/rtems/kernel/rtems/make/custom/default.cfg
   '/c/opt/rtems/4.11/make/custom'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686'
   /c/opt/rtems/kernel/pc686
  $

Building the LibBSD
~~~~~~~~~~~~~~~~~~~

The RTEMS BSD Library or libBSD as it is also know is a package of FreeBSD code
ported to RTEMS. It provides a number of advantanced services including a
networking stack
