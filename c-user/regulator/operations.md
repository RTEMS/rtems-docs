% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2023 On-Line Applications Research Corporation (OAR)

(regulatormanageroperations)=

# Operations

## Application Sourcing Data

The application interacting with the Source will obtain buffers from
the regulator instance, fill them with information, and send them to
the regulator instance. This allows the regulator to buffer bursty input.

A regulator instance is used as follows from the Source side:

```c
while (1) {
  use rtems_regulator_obtain_buffer to obtain a buffer
  // Perform some input operation to fetch data into the buffer
  rtems_regulator_send(buffer, size of message)
}
```

The delivery of message buffers to the Destination and subsequent release is
performed in the context of the delivery thread by either the delivery
function or delivery thread. Details are below.

The sequence diagram below shows the interaction between a message Source,
a Regulator instance, and RTEMS, given the usage described in the above
paragraphs.

(fig-regulator-input-sequence)=

```{figure} ../../images/c_user/regulator_input_sequence.png
:alt: Regulator Application Input Source Usage
:figclass: align-center
:width: 90%
```

As illustrated in the preceding sequence diagram, the Source usually
corresponds to application software reading a system input. The Source
obtains a buffer from the Regulator instance and fills it with incoming
data. The application explicitly obtaining a buffer and filling it in
allows for zero copy operations on the Source side.

After the Source has sent the message to the Regulator instance,
the Source is free to process another input and the Regulator
instance will ensure that the buffer is delivered to the Delivery
function and Destination.

## Delivery Function

The Delivery function is provided by the application for a specific
Regulator instance. Depending on the Destination, it may use a function which
copies the buffer contents (e.g., write()) or which operates directly
on the buffer contents (e.g. DMA from buffer). In the case of a
Destination which copies the buffer contents, the buffer can be released
via {ref}`InterfaceRtemsRegulatorReleaseBuffer` as soon as the function
or copying completes. In the case where the delivery uses the buffer
and returns, the call to {ref}`InterfaceRtemsRegulatorReleaseBuffer`
will occur when the use of the buffer is complete (e.g. completion
of DMA transfer). This explicit and deliberate exposure of buffering
provides the application with the ability to avoid copying the contents.
