---
title: "Standard Fields"
author: Nachiket Sathaye
coauthors: Ankush Jain
description: "The wording that test cases share and therefore leave out: scoring, pass and fail criteria, reviewer notes, standard evidence and the setup each layer assumes."
parent: "Test Case Library"
nav_order: 6
---

# Standard Fields

Most test cases in this library share wording for how they are scored, what counts as a pass or a fail, what evidence a reviewer expects and what the lab looks like. Repeating that in every case made the cases long and hid what is different about each one. The shared wording now lives here, once. A case shows a field only when its text differs from the standard.

> **How to read a case.** If a case does not show one of the fields below, the standard wording on this page applies. Find the right row from the case's own details: its **Test Method** in the first table, whether it has an **Expected Detection** field (a detection case) or an **Expected Result** field (a result case), and its layer or domain from its ID (TC-L06-007 is layer L06).

**Copying a case.** Each case ends with a closed box, *Standard fields for this case*, that lists the wording from this page that applies to it. Open it and copy it with the case, and the copy is complete without this page. The [AI Security Test Case Tracker (.xlsx)](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) has the same wording filled into every row.

A case that does show one of these fields has its own wording, and that wording replaces the standard for that case. Anyone adding a case should leave a field out when the standard fits and write it out only when it does not. The build checks that no case repeats a standard word for word.

<!-- standard-fields -->

[Back to library overview](index.md)
