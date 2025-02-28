# RTEMS Project Documentation

[TOC]

## Introduction

The documents are written in ReST and built using Sphinx. The waf build system
will check the version of Sphinx and ensure you have a suitable version
available. If your host does not provide a packaged version, use PIP to fetch a
recent version. The Sphinx website provides details on doing this.

ReST is the Re-Structured-Text format. It is a simple markup language that
allows us to create quality documentation which can easily be converted to
multiple different formats. This flexibility is convenient, but you still need
to test any new way of presenting something on all output formats. What may look
great in one format may not translate with the same clarity to another output
format.

The RTEMS Documentation output formats are:

- HTML - Multi-page HTML with files in a single directory per manual.
- PDF - Single PDF per manual.
- Single HTML - Single HTML, one file per manual.

The PDF format is created using Latex and that uses texlive packages. This
exposes us to the complex world of Latex however the quality of the documents
created is worth it.

Images can be created from source using PlantUML and Ditaa.

A Sphinx cheatsheet is:

- https://sphinx-tutorial.readthedocs.io/cheatsheet/#rst-cheat-sheet

## Production Quality Hosts

We allow the building of PDF documentation on hosts that do not have a fully
suitable texlive environment and this results in quality that is not at the
production level.

The hosts which produce production quality are:

- FreeBSD
- CentOS 6 and 7 (if using texlive, not RPMs of texlive)

> **Note:** RedHat Enterprise Linux (RHEL) and Fedora should be the same as CentOS.

## Images

All images should be placed in the `images` directory and referenced from the
ReST with a relative path. This lets us share and control images.

We prefer being able to build images from source. This is not always possible
so SVG format is preferred with generated PNG images to make sure the quality
is consistent when building PDF output.

Building images requires the source with an appropriate file extension
is placed in the images directory. The built output image is written
back to the images directory. All images may be built or rebuilt when
building images is enabled via the waf configure command line. Please
only add and commit those images that have changed.

We support building images in:

1. PlantUML (`.puml`), enable with `--plantuml`

2. Ditaa (`.ditaa`), enable with `--ditaa`

We support the PlantUML image language. The PlantUML home page is:

- http://plantuml.com/

The page as a link to an "online demo server" you can use to create images
rather than installing PlantUML. Save you source then View and save the PNG
format image. The PlantUML language reference guide is:

- http://plantuml.com/PlantUML_Language_Reference_Guide.pdf

And the web site has online documentation. The image source extension is
`.puml`.

We also support Ditaa image language. The Ditaa home page is:

- http://ditaa.sourceforge.net/

The home page contains the language options. The PlantUML online demo server
supports Ditaa so use that resource as an online tool. The Ditaa image source
extension is `.ditaa`.

You do not need PlantUML or Ditaa installed to build our documentation. The
online resources can be used. Save the source and the generated PNG file in the
same directory under `images`.

> **Note:**
> Please consider using PlantUML and Ditaa before other tools because we
> can generate the images from source automatically and it gives the
> documentation a similar look and feel. Other options may be considered
> if the image cannot be easily created by PlantUML or Ditaa but please
> ask before starting down that path because it may not be accepted.

Image editing tools tend to have a specific look and feel and this
characterizes the images they create. Altering an image often means
the original tool is required. An open output format allows us to
integrate the image into the document however we are then required to
monitor and maintain that tool if we need to make changes. The fewer
alternatives we have to maintain the easier it is for the project over
a long period of time.

## Host Setup

HTML builds directly with Sphinx, PDF requires a full Latex (`texlive`) install,
and building a Single HTML page requires the `inliner` tool. The
sphinxcontrib-bibtex extension is mandatory. PlantUML requires the Node.js
package called `node-plantuml` which installs the `puml` command and Ditaa needs
the `ditaa` command and package. Ditaa images are built using the `puml`
command.

Please add your host to this section as you set it up.

The best results are produced with Python3 and a virtual environment. It can
create a specific python environment using `pip`.

Similarly, `npm` packages can be installed into a users `$HOME` directory.

### Versions

| Package                         | Version |
| ------------------------------- | ------- |
| `Sphinx`                        | 7.2.6   |
| `sphinx-book-theme`             | 1.1.3   |
| `sphinxcontrib-applehelp`       | 1.0.7   |
| `sphinxcontrib-bibtex`          | 2.6.1   |
| `sphinxcontrib-devhelp`         | 1.0.5   |
| `sphinxcontrib-htmlhelp`        | 2.0.4   |
| `sphinxcontrib-jquery`          | 4.1     |
| `sphinxcontrib-jsmath`          | 1.0.1   |
| `sphinxcontrib-qthelp`          | 1.0.6   |
| `sphinxcontrib-serializinghtml` | 1.1.9   |
| `sphinx-copybutton`             | 0.5.2   |
| `myst-parser`                   | 4.0.0   |
| `sphinx-design`                 | 0.6.1   |
| `sphinx-togglebutton`           | 0.3.2   |
| `sphinxext-opengraph`           | 0.9.1   |
| `sphinx-tippy`                  | 0.4.3   |

### Python Virtual Environment

The project recommends virtual environments for building RTEMS
documentation using Sphinx. A virtual environment lets you install and
maintain a Sphinx build environment without installing and depending
on system wide packages.

Create a directory to house the virtual environment, create the environment,
and then activate it. This example assumes Python3 and the `venv` module:

```bash
$ mkdir sphinx
$ python3 -m venv sphinx
$ . ./sphinx/bin/activate
```

Alternatively you can use the `virtualenv` command:

```bash
$ mkdir sphinx
$ virtualenv sphinx
$ . ./sphinx/bin/activate
```

Either way, the prompt will now change. You can install Sphinx with:

```bash
$ pip install sphinx
$ pip install sphinxcontrib-bibtex
$ pip install sphinxcontrib-jquery
$ pip install sphinx-book-theme
$ pip install sphinx-copybutton
$ pip install linkify-it-py
$ pip install myst-parser
$ pip install sphinx-design
$ pip install sphinx-togglebutton
$ pip install sphinxext-opengraph
$ pip install sphinx-tippy
```

When you have finished using sphinx and building documentation you
enter `deactivate`.

## NPM Per User Environment

Change npm's default directory to a local one:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

Subsequent packages installed via `npm install` will be local
to the user. The following shows the PATH changes needed.

```bash
export PATH=${HOME}/.npm-global/bin:$PATH
```

### Sphinx Per User Install

You can use this method to install a personal version of Sphinx if your host
does not provide a suitable package:

```bash
$ pip install -U --user sphinx
$ pip install --user sphinxcontrib-bibtex
$ pip install --user sphinxcontrib-jquery
$ pip install --user sphinx-book-theme
$ pip install --user sphinx-copybutton
```

On some hosts, this may complain that a newer version of pip is available.
If so, then upgrade pip into your personal area.

```bash
$ pip install --upgrade --user pip
```

The personal area for these tools is \$\{HOME}/.local/bin. It should
be PREPENDED to your path. On a 32-bit install of CentOS, RHEL, or
Fedora, these were the PATH modifications to use the local install of
Texlive and sphinx:

```bash
export PATH=/usr/local/texlive/2016/bin/i386-linux/:${PATH}
export PATH=${HOME}/.local/bin:${PATH}
```

If on a 64-bit install of CentOS, RHEL, or Fedora, these will
be the PATH modifications to use the local install of Texlive
and Sphinx:

```bash
export PATH=/usr/local/texlive/2016/bin/x86_64-linux/:${PATH}
export PATH=${HOME}/.local/bin:${PATH}
```

### Windows

To build the documentation on Windows you need to install an official Python
build from https://www.python.org/. We suggest you install a recent 3.x series
64bit build. The versions 2.7.9 and after include pip.

Note: you cannot use the MSYS2 versions of Python because the pip libraries
that contain C or C++ code are built with MSVC libraries and cannot integrate
with the MSYS2 built python.

The following assumes Python is installed to a default path of C:\\Python313.
The actual path will be set during the install, possibly to a default like
C:\\Users\\username\\Local Settings\\Application Data\\Programs\\Python\\Python313.
You should avoid having paths with space characters in the install path, as
they will cause problems in the shell.

Open an MSYS2 terminal window and add the needed paths to Python and its
scripts:

```bash
$ export PATH=/c/Python313/Scripts:/c/Python313:$PATH
```

You should not add this to your default `PATH` (i.e., in your `.bashrc`),
because you need other versions of Python to be found for building RTEMS.
You can put this in a file e.g., `pyenv.sh` and then source it into your
environment:

```bash
$ . pyenv.sh
```

Upgrade pip:

```bash
$ python -m pip install --upgrade pip
```

Create a directory to house the virtual environment, create the environment,
and then activate it. This is slightly different than the procedure in
[Python Virtual Environment](#python-virtual-environment).

```bash
$ mkdir sphinx
$ python -m venv sphinx
$ . ./sphinx/Scripts/activate
```

The prompt will now change. You can install Sphinx with:

```bash
$ pip install sphinx
$ pip install sphinxcontrib-bibtex
$ pip install sphinxcontrib-jquery
$ pip install sphinx-book-theme
$ pip install sphinx-copybutton
```

You may want to update pip in your virtual environment as well.

Windows does not provide `python3` so you will need to create a wrapper in the
virtual environment. A simple workaround is:

```bash
echo '#!/usr/bin/env bash' > ./sphinx/Scripts/python3
echo 'python $*' >> ./sphinx/Scripts/python3
```

In Windows10 you may need to replace `python` with `py -3`.

Continue from [Building](#building).

When you have finished building the documentation run `deactivate` in the
terminal to leave the virtual environment.

### FreeBSD

PDF Quality: production

- Sphinx:

  Use a virtual environment and `pip`.

- PDF:

  ```bash
  # pkg install texlive-full
  ```

- Single HTML:

  ```bash
  # pkg install npm
  # npm install -g inliner
  ```

- Plant UML:

  Install NPM as shown in Single HTML then:

  ```bash
  # npm install -g node-plantuml
  ```

- Ditaa:

  ```bash
  # pkg install ditaa
  ```

### CentOS 7

PDF Quality: production

- Python 3:

  By default, CentOS 7 has Python 2.x. Luckily they now have Software
  Collections which lets you install and use a "collection" of newer
  software. As root,

  ```bash
  # yum install centos-release-scl
  # yum install rh-python36
  ```

  Then you can create your own virtual Python environment for use with
  the Sphinx toolchain.

  ```bash
  $ cd ~
  $ python -m venv rtemsdocs
  ```

  When you want to use the Sphinx toolchain.

  ```bash
  $ scl enable rh-python36 bash
  $ source ~/rtemsdocs/bin/activate
  ```

- Sphinx:

  ```bash
  $ pip install -U sphinx
  ```

- PDF:

  > **WARNING:** Do NOT use the RPMs for texlive. They are incomplete
  > and, in the best case, result in ugly PDFs.

  As root, install texlive per the instructions at
  http://tug.org/texlive/acquire-netinstall.html

  ```bash
  # wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
  # tar xf install-tl-unx.tar.gz
  # cd install-tl-20161106
  ```

  > **NOTE:** The date in the name of the directory will change.

  ```bash
  # ./install-tl
  ```

  - Use the command line system. Select "O" for options if you want to
    change from A4 to US letter paper size by default.
  - Select "I" to install
  - The tools will be installed into a directory like the following:
    /usr/local/texlive/2016/bin/i386-linux/
  - **NOTE:** The year (2016) and host OS (i386-linux) will change to
    reflect 32 or 64 bit and OS name.

  You will also likely need to install the aspell RPM.

- Single HTML:

  > **NOTE:** npm appears to be part of the EPEL repository for RHEL
  > and CentOS. You may have to add that repository to your
  > configuration.

  ```bash
  # yum install npm
  # npm install -g inliner
  ```

- Plant UML:

  Install NPM as shown in Single HTML then:

  ```bash
  # npm install -g node-plantuml
  ```

- Spell check:

  ```bash
  # yum install aspell
  ```

- PATH:

  Ensure the appropriate directories are PREPENDED to your PATH before
  building the documentation. Examples are shown below:

  ```bash
  export PATH=/usr/local/texlive/2016/bin/i386-linux/:${PATH}
  export PATH=${HOME}/.local/bin:${PATH}
  ```

### CentOS 8

The steps for Centos 8 are similar to the steps for CentOS 7.
There are just a couple differences.

First, CentOS 8 uses Python 3.x as the default, so installing the
centos-release-scl and rh-python36 packages are unnecessary.
Second, Centos 8 uses dnf as its package manager instead of yum, so
packages such as npm should be installed using dnf instead.

### Ubuntu

- Host Tools:

  ```bash
  $ sudo apt install python3-venv npm aspell
  ```

- PDF

  ```bash
  $ sudo apt install texlive-base texlive-latex-extra texlive-fonts-extra
  ```

- Single-HTML

  ```bash
  $ sudo npm install -g inliner
  ```

- PlantUML

  ```bash
  $ sudo npm install -g node-plantuml
  ```

- Ditaa

  ```bash
  $ sudo apt install ditaa
  ```

### Arch Linux

- Sphinx:

  ```bash
  # pacman -S python-sphinx
  # pacman -S python-sphinxcontrib-bibtex
  ```

- PDF:

  ```bash
  # pacman -S texlive-bin texlive-core texlive-latexextra texlive-fontsextra
  ```

### OpenSUSE

The instructions in the `Dockerfile` below should provide an
inspiration how to set up an OpenSUSE leap machine and to build the
RTEMS documentation. The build process of the container image does not
only install all needed packages in the image but also builds the
documentation.

In the `Dockerfile` the `root` user executes `waf`. This is not
necessary. Any ordinary user can build the documentation. Moreover,
in the container image the resulting document files are installed
into directory `/srv/www/htdocs`. This is the directory used by the
`lighttpd` ("lighty") web-server which is run when the container
is started after the build.

To build the container image, create the following `Dockerfile`
in an empty directory of your choice.

```bash
cat >Dockerfile <<"EOF"
# Dockerfile to build the RTEMS documentation

FROM opensuse/leap:15.6
RUN <<EOT bash
    set -exu -o pipefail
    # ==== Install required packages ====
    zypper --non-interactive refresh
    zypper --non-interactive update
    zypper --non-interactive install \
            --solver-focus=Update --force-resolution \
        aspell \
        git \
        graphviz \
        lighttpd \
        npm-default \
        plantuml \
        poppler-tools \
        python311 \
        python311-poetry \
        texinfo \
        texlive-inconsolata \
        texlive-lato \
        texlive-scheme-tetex \
        texlive-anyfontsize \
        texlive-eqparbox \
        texlive-fncychap \
        texlive-sectsty \
        texlive-threeparttable \
        texlive-wrapfig \
        unzip \
        wget
    npm install -g inliner
    npm install -g node-plantuml
    # Note: OpenSUSE does not provide package ditaa.
    wget --output-document=/root/ditaa0_9.zip \
            https://sourceforge.net/projects/ditaa/files/latest/download
    unzip /root/ditaa0_9.zip ditaa0_9.jar -d /usr/local/bin
    /bin/echo -e '#! /bin/bash\n\nexec java -jar \
            /usr/local/bin/ditaa0_9.jar \$@' >/usr/local/bin/ditaa
    chmod a+rx /usr/local/bin/ditaa

    # ==== Obtain rtems-docs sources and setup Python packages ====
    git -C \${HOME} clone https://gitlab.rtems.org/rtems/docs/rtems-docs.git
    cd \${HOME}/rtems-docs
    poetry init --name=rtems-docs --no-interaction
    poetry add sphinx
    poetry add sphinxcontrib-bibtex
    poetry add sphinxcontrib-jquery
    poetry add sphinx-book-theme
    poetry add sphinx-copybutton

    # ==== Build the RTEMS documentation ====
    cd \${HOME}/rtems-docs
    poetry run ./waf configure --singlehtml --plantuml --ditaa \
            --pdf --prefix="/srv/www/htdocs"
    poetry run ./waf
    poetry run ./waf install
EOT

# This container starts a web-server
CMD ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
EOF
```

Podman is used in the shell commands below. If you prefer Docker
simply replace `podman` through `docker`.

Build the container image `rtems-docs-server_img` with this command:

```bash
podman build -t rtems-docs-server_img -f Dockerfile .
```

Create and start a container with (effectively, this "only" starts the
web-server):

```bash
podman run -d -p 8080:80 --rm --name rtems-docs-server rtems-docs-server_img
```

Point a web-browser to `http://localhost:8080/` to browse the
documentation created during the build of the container image.
For example:

```bash
firefox http://localhost:8080/
```

Notes:

- Accesses from remote hosts to port 8080 may be blocked by a firewall.

- The single html pages may be empty. This is a
  [known bug](https://gitlab.rtems.org/rtems/rtos/rtems-release/-/issues/7).

To stop the container and to delete the image, use these commands:

```bash
podman stop rtems-docs-server
podman rmi rtems-docs-server_img
```

### Latex Setup

Latex is used to create the PDF document. The setup of Latex varies from host
to host operating system due to the way each host packages the texlive
packages. There is no common naming and no real way to figure what texlive
package is present in a host's packaging. It seems not all of texlive is
available.

The RTEMS Documentation waf configure phase checks for each texlive package used
in the generated output and the styles. If you complete configure with the
`--pdf` option you should be able to build PDF documentation.

The texlive package requirements come from the Latex styles we are using and
Sphinx.

An example of failures are:

```
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
```

If you find there is an issue please post the developers list.

## Building

To build enter in the top directory and configure with suitable options:

```bash
./waf configure [--pdf] [--singlehtml] [--prefix] \
               [--sphinx-options] \
               [--sphinx-nit-pick] \
               [--plantuml] \
               [--ditaa] \
               [--disable-extra-fonts]
```

To build:

```bash
$ ./waf
```

The `--pdf` and `--singlehtml` options can be added to configure to build those
output formats.

Sphinx options can be added using the `--sphinx-options` option. If you have
more than option use a quoted argument. This is an advanced feature that can
be useful when experimenting with the `sphinx-build` command.

Sphinx nit-picky mode adds `-n` to the `sphinx-build` command line to generate
warnings and extra information about the source to help make sure our
documentation source is as clean as possible. Please use this when writing
documentation or making updates.

The `--disable-extra-fonts` allows you to build PDF documents without the
fonts we use for a better quality document. Use this option to build without
needing the extra fonts accepting you will get poor quality documents.

To build and install to a specific location:

```bash
$ ./waf configure --prefix=/foo/my/location
$ ./waf build install
```

To build the PlantUML and Ditaa images:

```bash
$ ./waf configure --plantuml --ditaa
$ ./waf clean build
```

To nit-pick the source use:

```bash
$ ./waf configure --sphinx-nit-pick
$ ./waf clean build
```

If you need to debug what is happening use configure with a suitable Sphinx
verbose level:

```bash
$ ./waf configure --sphinx-options "-V -V"
$ ./waf clean build
```

You can enter a manual's directory and run the same configure command and build
just that manual.

## Documentation Standard

This following details the documentation standard. If in doubt first search the
existing documentation for an example and if unsure ask.

01. All text is to be formatted to wrap at 80 columns. Do not manually line feed
    before 80.

02. Do not insert tab characters, use spaces, no trailing white space.

03. Pasted text such as console output can exceed 80 columns; however, it is
    preferred even this text is wrapped at 80 columns. Long lines in code block
    text causes issues with the PDF output.

04. The headings use the following:

    ```
       Heading   Description
    1  ###### Part
    2  ****** Section
    3  ====== Sub-section
    4  ------ Sub-sub-section
    5  ^^^^^^ Sub-sub-sub-section
    6  ~~~~~~ Sub-sub-sub-sub-section
    ```

05. For literal output such as shell commands and code, do not use `::`
    at the trailing edge of the previous paragraph as it generates
    warnings as the autodetect fails to find a suitable format. Use the
    `.. code-block::` with a suitable lexical label. The lexers are:

    - http://pygments.org/docs/lexers/

    Use the short names. For C code use `c` code and `shell` for shell
    scripts and for terminal output use `none`. If you need line
    numbers use:

    ```
    .. code-block:: shell
       :linenos:
    ```

    We support two forms of commands and outputs.

    The first is to have a shell command block with just the commands
    and if required an output block with the output or some of the
    output. Use `none` for the output block. Make sure the text clearly
    states the block is the output, if it has been edited to shorten
    the amount of output and if there are any special operating modes,
    for example needing to be `root`.

    The second is to use a single block of type `none` with the command
    and output together as seen in a terminal session. The commands are
    identified by the standard shell prompt characters where `$` is a
    user prompt and `#` is a `root` prompt.

    Do not embed the version or version major number in the literal
    commands or examples. Use the replacements listed in 10.

06. Use the directives for `note`, `warning`, and `topic`. Do not add `TIP`,
    `Important` or `Warning` to the text. Let the mark-up language handle
    this. The supported directives are:

    ```
    .. warning::
    .. note::
    .. topic::
    ```

    These directives reference specific CSS style support.

07. Images are placed in the `images` directory. Do not place images in the
    source directories. Using a common `images` tree of images promotes sharing
    of images. To add an image use:

    ```
    .. figure:: ../images/my-image.png
       :width: 75%
       :align: center
       :alt: This is the alt text for some output types.
    ```

08. Callouts can be implemented manually using a literal block (`::`)
    or a code block. Either way, a topic block is used for the items. For
    example:

    ```
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
    ```

    **Note:** the topic items are manually numbered, which makes it easier to see
    which item matches the text. Use `<>` for the number and align at a position
    that makes the number as visible as possible. Use hanging indents
    if an item extends past a single line.

09. Use the RTEMS domain references for URLs and mailing lists. For example to
    insert the RTEMS developers list use:

    ```
    :r:list:`devel`
    :r:url:`git`
    ```

    The valid lists are:

    | Label      | Description                  |
    | ---------- | ---------------------------- |
    | `announce` | Announce Mailing List        |
    | `bugs`     | Bugs Mailing List            |
    | `devel`    | Developers Mailing List      |
    | `build`    | Build Logs                   |
    | `users`    | Users Mailing List           |
    | `vc`       | Version Control Mailing List |

    The valid URLs are:

    | Label    | URL                                          |
    | -------- | -------------------------------------------- |
    | trac     | https://gitlab.rtems.org/                    |
    | devel    | https://gitlab.rtems.org/                    |
    | www      | https://www.rtems.org/                       |
    | buildbot | https://buildbot.rtems.org/                  |
    | builder  | https://builder.rtems.org/                   |
    | docs     | https://docs.rtems.org/                      |
    | lists    | https://lists.rtems.org/                     |
    | git      | https://gitlab.rtems.org/                    |
    | ftp      | https://ftp.rtems.org/                       |
    | review   | https://review.rtems.org/                    |
    | bugs     | https://gitlab.rtems.org/                    |
    | gsoc     | https://gitlab.rtems.org/rtems/programs/gsoc |
    | socis    | https://gitlab.rtems.org/                    |

10. Use the following to embed the version number in any part of the
    documentation source:

    1. `@rtems-version@`

       The complete version string of the documentation.

    2. `@rtems-ver-major@`

       The version major number.

    3. `@rtems-ver-minor@`

       The version minor number.

    4. `@rtems-ver-revision@`

       The version revision number.

    The replacement happens during the source read phase of the build
    and is not context specific. The substitution will happen in code
    blocks and other normally quoted areas.

    It is a requirement these be used then embedded commands or
    related text in the documentation to let the documentation track
    the release. For example `microblaze-rtems6-gdb` should be written
    as `microblaze-rtems@rtems-ver-major@-gdb`.
