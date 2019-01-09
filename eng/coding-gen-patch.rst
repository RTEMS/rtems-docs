.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

Generating a Tools Patch
************************

.. COMMENT:TBD - Convert the following to Rest and insert into this file
.. COMMENT:TBD - https://devel.rtems.org/wiki/Developer/Coding/GenerateAPatch

The RTEMS patches to the development tools are generated using a command like this

.. code block:: shell
  diff -N -P -r -c TOOL-original-image TOOL-with-changes >PATCHFILE

where the options are:

* -N and -P take care of adding and removing files (be careful not to
include junk files like file.mybackup)

* -r tells diff to recurse through subdirectories
* -c is a context diff (easy to read for humans)
* -u is a unified diff (easy for patch to apply)

Please look at the generated PATCHFILE and make sure it does not contain
anything you did not intend to send to the maintainers. It is easy to
accidentally leave a backup file in the modified source tree or have a
spurious change that should not be in the PATCHFILE.

If you end up with the entire contents of a file in the patch and can't
figure out why, you may have different CR/LF scheme in the two source
files. The GNU open-source packages usually have UNIX style CR/LF. If
you edit on a Windows platform, the line terminators may have been
transformed by the editor into Windows style.
