.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)
.. COMMENT: All rights reserved.

Key Manager
###########

Introduction
============

The key manager allows for the creation and deletion of Data keys
specific to threads.

The directives provided by the key manager are:

- pthread_key_create_ - Create Thread Specific Data Key

- pthread_key_delete_ - Delete Thread Specific Data Key

- pthread_setspecific_ - Set Thread Specific Key Value

- pthread_getspecific_ - Get Thread Specific Key Value

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the key manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. _pthread_key_create:

pthread_key_create - Create Thread Specific Data Key
----------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_key_create(
        pthread_key_t *key,
        void (*destructor)( void )
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - There were not enough resources available to create another key.
 * - ``ENOMEM``
   - Insufficient memory exists to create the key.

**DESCRIPTION**

The ``pthread_key_create()`` function shall create a thread-specific data key
visible to all threads in the process. Key values provided by
``pthread_key_create()`` are opaque objects used to locate thread-specific
data. Although the same key value may be used by different threads, the values
bound to the key by ``pthread_setspecific()`` are maintained on a per-thread
basis and persist for the life of the calling thread.

Upon key creation, the value ``NULL`` shall be associated with the new key in
all active threads. Upon thread creation, the value ``NULL`` shall be
associated with all defined keys in the new thread.

**NOTES**

An optional destructor function may be associated with each key value.  At
thread exit, if a key value has a non-``NULL`` destructor pointer, and the
thread has a non-``NULL`` value associated with that key, the value of the key
is set to NULL, and then the function pointed to is called with the previously
associated value as its sole argument. The order of destructor calls is
unspecified if more than one destructor exists for a thread when it exits.

.. _pthread_key_delete:

pthread_key_delete - Delete Thread Specific Data Key
----------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_key_delete(
        pthread_key_t key
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The key was invalid

**DESCRIPTION:**

The ``pthread_key_delete()`` function shall delete a thread-specific data key
previously returned by ``pthread_key_create()``. The thread-specific data
values associated with key need not be NULL at the time
``pthread_key_delete()`` is called. It is the responsibility of the application
to free any application storage or perform any cleanup actions for data
structures related to the deleted key or associated thread-specific data in any
threads; this cleanup can be done either before or after
``pthread_key_delete()`` is called. Any attempt to use key following the call
to ``pthread_key_delete()`` results in undefined behavior.

**NOTES:**

The ``pthread_key_delete()`` function shall be callable from within destructor
functions. No destructor functions shall be invoked by
``pthread_key_delete()``. Any destructor function that may have been associated
with key shall no longer be called upon thread exit.

.. _pthread_setspecific:

pthread_setspecific - Set Thread Specific Key Value
---------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_setspecific(
        pthread_key_t  key,
        const void    *value
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified key is invalid.

**DESCRIPTION:**

The ``pthread_setspecific()`` function shall associate a thread-specific value
with a key obtained via a previous call to ``pthread_key_create()``.  Different
threads may bind different values to the same key. These values are typically
pointers to blocks of dynamically allocated memory that have been reserved for
use by the calling thread.

**NOTES:**

The effect of calling ``pthread_setspecific()`` with a key value not obtained
from ``pthread_key_create()`` or after key has been deleted with
``pthread_key_delete()`` is undefined.

``pthread_setspecific()`` may be called from a thread-specific data destructor
function. Calling ``pthread_setspecific()`` from a thread-specific data
destructor routine may result either in lost storage (after at least
``PTHREAD_DESTRUCTOR_ITERATIONS`` attempts at destruction) or in an infinite
loop.

.. _pthread_getspecific:

pthread_getspecific - Get Thread Specific Key Value
---------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    void *pthread_getspecific(
        pthread_key_t key
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``NULL``
   - There is no thread-specific data associated with the specified key.
 * - ``non-NULL``
   - The data associated with the specified key.

**DESCRIPTION:**

The ``pthread_getspecific()`` function shall return the value currently bound
to the specified key on behalf of the calling thread.

**NOTES:**

The effect of calling ``pthread_getspecific()`` with a key value not obtained
from ``pthread_key_create()`` or after key has been deleted with
``pthread_key_delete()`` is undefined.

``pthread_getspecific()`` may be called from a thread-specific data destructor
function. A call to ``pthread_getspecific()`` for the thread-specific data key
being destroyed shall return the value ``NULL``, unless the value is changed
(after the destructor starts) by a call to ``pthread_setspecific()``.
