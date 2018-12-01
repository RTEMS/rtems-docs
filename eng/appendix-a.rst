.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project


Appendix: Core Qualification Artifacts/Documents
************************************************

An effort at NASA has been performed to suggest a core set of artifacts
(as defined by **BOTH** NASA NPR 7150.2B and DO-178B) that can be utilized
by a mission as a baselined starting point for “pre-qualification”
for (open-source) software that is intended to be utilized for flight
purposes.  This effort analyzed the overlap between NPR 7150.2B
and DO-178B and highlighted a core set of artifacts to serve as a
starting point for any open-source project.  These artifacts were also
cross-referenced with similar activities for other NASA flight software
qualification efforts, such as the open-source Core Flight System (cFS).
Along with the specific artifact, the intent of the artifact was also
captured; in some cases open-source projects, such as RTEMS, are already
meeting the intent of the artifacts with information simply needing
organized and formalized.  The table below lists the general category,
artifact name, and its intent.  Please note that this table does **NOT**
represent all the required artifacts for qualification per the standards;
instead, this table represents a subset of the most basic/core artifacts
that form a strong foundation for a software engineering qualification
effort.

.. COMMENT: TBD convert to a table; see original PDF for guidance on desired look
.. COMMENT: TBD The PDF is in https://ftp.rtems.org/pub/rtems/people/joel/sw_eng_hb/

.. table:: Table 1. Core Qualification Artifacts
   :class: rtems-table

   +----------------+-----------------------+---------------------------------+
   | Category       | Artifact              | Intent                          |
   +================+=======================+=================================+
   | Requirements   | Software Requirements | The project shall document the  |
   |                | Specification (SRS)   | software requirements.          |
   |                |                       |                                 |
   |                |                       | The project shall collect and   |
   |                |                       | manage changes to the software  |
   |                |                       | requirements.                   |
   |                | Requirements          |                                 |
   |                | Management            | The project shall identify,     |
   |                |                       | initiate corrective actions,    |
   |                |                       | and track until closure         |
   |                |                       | inconsistencies among           |
   |                |                       | requirements, project plans,    |
   |                |                       | and software products.          |
   |                +-----------------------+---------------------------------+
   |                | Requirements Test and | The project shall perform,      |
   |                | Traceability Matrix   | document, and maintain          |
   |                |                       | bidirectional traceability      |
   |                |                       | between the software            |
   |                |                       | requirement and the             |
   |                |                       | higher-level requirement.       |
   |                +-----------------------+---------------------------------+
   |                | Validation            | The project shall perform       |
   |                |                       | validation to ensure that the   |
   |                |                       | software will perform as        |
   |                |                       | intended in the customer        |
   |                |                       | environment.                    |
   +----------------+-----------------------+---------------------------------+
   | Design and     | Software Development  | A plan for how you will develop |
   | Implementation | or Management Plan    | the software that you are       |
   |                |                       | intent upon developing and      |
   |                |                       | delivering.                     |
   |                |                       |                                 |
   |                |                       | The Software Development Plan   |
   |                |                       | includes the objectives,        |
   |                |                       | standards and life cycle(s) to  |
   |                |                       | be used in the software         |
   |                |                       | development process. This plan  |
   |                |                       | should include: Standards:      |
   |                |                       | Identification of the Software  |
   |                |                       | Requirements Standards,         |
   |                |                       | Software Design Standards,      |
   |                |                       | and Software Code Standards for |
   |                |                       | the project.                    |
   |                +-----------------------+---------------------------------+
   |                | Software              | To identify and control major   |
   |                | Configuration         | software changes, ensure that   |
   |                | Management Plan       | change is being properly        |
   |                |                       | implemented, and report changes |
   |                |                       | to any other personnel or       |
   |                |                       | clients who may have an         |
   |                |                       | interest.                       |
   |                +-----------------------+---------------------------------+
   |                | Implementation        | The project shall implement the |
   |                |                       | software design into software   |
   |                |                       | code.                           |
   |                |                       |                                 |
   |                |                       | Executable Code to applicable   |
   |                |                       | tested software.                |
   |                +-----------------------+---------------------------------+
   |                | Coding Standards      | The project shall ensure that   |
   |                | Report                | software coding methods,        |
   |                |                       | standards, and/or criteria are  |
   |                |                       | adhered to and verified.        |
   |                +-----------------------+---------------------------------+
   |                | Version Description   | The project shall provide a     |
   |                | Document (VDD)        | Software Version Description    |
   |                |                       | document for each software      |
   |                |                       | release.                        |
   +----------------+-----------------------+---------------------------------+
   | Testing and    | Software Test Plan    | Document describing the testing |
   | Software       |                       | scope and activities.           |
   | Assurance      +-----------------------+---------------------------------+
   | Activities     | Software              | To define the techniques,       |
   |                | Assurance/Testing     | procedures, and methodologies   |
   |                | Procedures            | that will be used.              |
   |                +-----------------------+---------------------------------+
   |                | Software Change       | The project shall regularly     |
   |                | Report / Problem      | hold reviews of software        |
   |                | Report                | activities, status, and results |
   |                |                       | with the project stakeholders   |
   |                |                       | and track issues to resolution. |
   |                +-----------------------+---------------------------------+
   |                | Software Schedule     | Milestones have schedule and    |
   |                |                       | schedule is updated             |
   |                |                       | accordingly.                    |
   |                +-----------------------+---------------------------------+
   |                | Software Test         | The project shall record,       |
   |                | Report / Verification | address, and track to closure   |
   |                | Results               | the results of software         |
   |                |                       | verification activities.        |
   +----------------+-----------------------+---------------------------------+
   | Usability      | Software User’s       | The Software User Manual        |
   |                | Manual                | defines user instructions for   |
   |                |                       | the software.                   |
   +----------------+-----------------------+---------------------------------+

In an effort to remain lightweight and sustainable for open-source
projects, Table 1 above was condensed into a single artifact outline
that encompasses the artifacts’ intents.  The idea is that this living
qualification document will reside under RTEMS source control and be
updated with additional detail accordingly.  The artifact outline is
as follows:
