.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018, 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 2018, 2020 Sebastian Huber

File Templates
==============

Every source code file shall have a copyright and license block.  Corresponding
to the license, every file shall have an
`SPDX License Identifier <https://spdx.org/ids-how>`_ in the first possible line
of the file.  C/C++ files should have a Doxygen file comment block.

The preferred license for source code is
`BSD-2-Clause <https://spdx.org/licenses/BSD-2-Clause.html>`_.  The preferred
license for documentation is
`CC-BY-SA-4.0 <https://creativecommons.org/licenses/by-sa/4.0/legalcode>`_.

.. _FileHeaderCopyright:

Copyright and License Block
---------------------------

You are the copyright holder.  Use the following copyright and license block for
your source code contributions to the RTEMS Project.  Place it after the SPDX
License Identifier line and the optional file documentation block.  Replace the
<FIRST YEAR> placeholder with the year of your first substantial contribution to
this file.  Update the <LAST YEAR> with the year of your last substantial
contribution to this file.  If the first and last years are the same, then
remove the <LAST YEAR> placeholder with the comma.  Replace the <COPYRIGHT
HOLDER> placeholder with your name.

In case you are a real person, then use the following format for
<COPYRIGHT HOLDER>: <FIRST NAME> <MIDDLE NAMES> <LAST NAME>.  The <FIRST NAME>
is your first name (also known as given name), the <MIDDLE NAMES> are your
optional middle names, the <LAST NAME> is your last name (also known as family
name).

If more than one copyright holder exists for a file, then sort the copyright
lines by the first year (earlier years are below later years) followed by the
copyright holder in alphabetical order (A is above B in the file).

Use the following template for a copyright and license block.  Do not change the
license text.

.. code-block:: none

     Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>

     Redistribution and use in source and binary forms, with or without
     modification, are permitted provided that the following conditions
     are met:
     1. Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
     2. Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.

     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
     ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
     LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
     CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
     SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
     INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
     CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
     ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
     POSSIBILITY OF SUCH DAMAGE.

Check the top-level :file:`COPYING` file of the repository.  If you are a new
copyright holder, then add yourself to the top of the list.  If your last year
of a substantial contribution changed, then please update your copyright line.

C/C++ Header File Template
--------------------------

Use the following guidelines and template for C and C++ header files (here
:file:`<foo/bar/baz.h>`):

* Place the SPDX License Identifier in the first line of the file.

* Add a Doxygen file documentation block.

* Place the copyright and license comment block after the documentation block.

* For the <FIRST YEAR>, <LAST YEAR>, and <COPYRIGHT HOLDER> placeholders see
  :ref:`FileHeaderCopyright`.

* Separate comment blocks by exactly one blank line.

* Separate the Doxygen comment block from the copyright and license, so that
  the copyright and license information is not included in the Doxygen output.

* For C++ header files discard the extern "C".

.. code-block:: c

    /* SPDX-License-Identifier: BSD-2-Clause

    /**
     * @file
     *
     * @ingroup TheGroupForThisFile
     *
     * @brief Short "Table of Contents" Description of File Contents
     *
     * A short description of the purpose of this file.
     */

    /*
     * Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>
     *
     * Redistribution and use in source and binary forms, with or without
     * modification, are permitted provided that the following conditions
     * are met:
     * 1. Redistributions of source code must retain the above copyright
     *    notice, this list of conditions and the following disclaimer.
     * 2. Redistributions in binary form must reproduce the above copyright
     *    notice, this list of conditions and the following disclaimer in the
     *    documentation and/or other materials provided with the distribution.
     *
     * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
     * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
     * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
     * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
     * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
     * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
     * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
     * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
     * POSSIBILITY OF SUCH DAMAGE.
     */

    #ifndef _FOO_BAR_BAZ_H
    #define _FOO_BAR_BAZ_H

    #include <foo/bar/xyz.h>

    #ifdef __cplusplus
    extern "C" {
    #endif

    /* Declarations, defines, macros, inline functions, etc. */

    #ifdef __cplusplus
    }
    #endif

    #endif /* _FOO_BAR_BAZ_H */

C/C++/Assembler Source File Template
------------------------------------

Use the following template for C, C++, and assembler source files (here
implementation of :file:`<foo/bar/baz.h>`).  For the <FIRST YEAR>, <LAST YEAR>,
and <COPYRIGHT HOLDER> placeholders see :ref:`FileHeaderCopyright`.

.. code-block:: c

    /* SPDX-License-Identifier: BSD-2-Clause */

    /**
     * @file
     *
     * @ingroup TheGroupForThisFile
     *
     * @brief Short "Table of Contents" Description of File Contents
     *
     * A short description of the purpose of this file.
     */

    /*
     * Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>
     *
     * Redistribution and use in source and binary forms, with or without
     * modification, are permitted provided that the following conditions
     * are met:
     * 1. Redistributions of source code must retain the above copyright
     *    notice, this list of conditions and the following disclaimer.
     * 2. Redistributions in binary form must reproduce the above copyright
     *    notice, this list of conditions and the following disclaimer in the
     *    documentation and/or other materials provided with the distribution.
     *
     * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
     * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
     * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
     * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
     * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
     * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
     * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
     * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
     * POSSIBILITY OF SUCH DAMAGE.
     */

    #ifdef HAVE_CONFIG_H
    #include "config.h"
    #endif

    #include <foo/bar/baz.h>

    /* Definitions, etc. */

Python File Template
--------------------

Use the following template for Python source files and other files which accept
a ``#``-style comment block.  For the <FIRST YEAR>, <LAST YEAR>, and
<COPYRIGHT HOLDER> placeholders see :ref:`FileHeaderCopyright`.

.. code-block:: python

    #!/usr/bin/env python
    # SPDX-License-Identifier: BSD-2-Clause

    # File documentation block

    # Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>
    #
    # Redistribution and use in source and binary forms, with or without
    # modification, are permitted provided that the following conditions
    # are met:
    # 1. Redistributions of source code must retain the above copyright
    #    notice, this list of conditions and the following disclaimer.
    # 2. Redistributions in binary form must reproduce the above copyright
    #    notice, this list of conditions and the following disclaimer in the
    #    documentation and/or other materials provided with the distribution.
    #
    # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    # AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    # ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
    # LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    # CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    # SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    # INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    # CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    # ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    # POSSIBILITY OF SUCH DAMAGE.

reStructuredText File Template
------------------------------

Use the following template for reStructuredText (reST) source files.  For the
<FIRST YEAR>, <LAST YEAR>, and <COPYRIGHT HOLDER> placeholders see
:ref:`FileHeaderCopyright`.

.. code-block:: rest

    .. SPDX-License-Identifier: CC-BY-SA-4.0

    .. Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>
