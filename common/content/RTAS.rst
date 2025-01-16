Real-time Application Systems
=============================

Real-time application systems are a special class of computer applications.
They have a complex set of characteristics that distinguish them from other
software problems.  Generally, they must adhere to more rigorous requirements.
The correctness of the system depends not only on the results of computations,
but also on the time at which the results are produced.  The most important and
complex characteristic of real-time application systems is that they must
receive and respond to a set of external stimuli within rigid and critical time
constraints referred to as deadlines.  Systems can be buried by an avalanche of
interdependent, asynchronous or cyclical event streams.

Deadlines can be further characterized as either hard or soft based upon the
value of the results when produced after the deadline has passed.  A deadline
is hard if the results have no value or if their use will result in a
catastrophic event.  In contrast, results which are produced after a soft
deadline may have some value.

Another distinguishing requirement of real-time application systems is the
ability to coordinate or manage a large number of concurrent activities. Since
software is a synchronous entity, this presents special problems.  One
instruction follows another in a repeating synchronous cycle.  Even though
mechanisms have been developed to allow for the processing of external
asynchronous events, the software design efforts required to process and manage
these events and tasks are growing more complicated.

The design process is complicated further by spreading this activity over a set
of processors instead of a single processor. The challenges associated with
designing and building real-time application systems become very complex when
multiple processors are involved.  New requirements such as interprocessor
communication channels and global resources that must be shared between
competing processors are introduced.  The ramifications of multiple processors
complicate each and every characteristic of a real-time system.