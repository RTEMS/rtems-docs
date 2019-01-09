.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _tracing-framework:

Tracing
*******
.. index:: Tracing Framework

RTEMS Tracing Framework is an on-target software based system which helps track
the ongoings inside the operation of applications, 3rd party packages, and the
kernel in real time.

Software based tracing is a complex process which requires components on both
the target and the host to work together. However its portability across all
architectures and board support packages makes it a useful asset. A key
requirement in RTEMS trace process is to take existing code in compiled format
(ELF) and instrument it in order to log various events and records in real time.
However instrumenting of the code for tracing should happen without rebuilding
the code from the source and without annotating the source with trace code.

.. toctree::

   introduction
   examples
   captureengine
   tracelinker
