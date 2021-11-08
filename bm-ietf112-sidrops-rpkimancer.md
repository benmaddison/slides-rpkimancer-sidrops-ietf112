---
title: rpkimancer - IETF 112
author: Ben Maddison
date: 2021-11-08
patat:
    wrap: true
    margins:
        left: 10
        right: 10
    incrementalLists: true
---

## rpkimancer

/ɑː-piː-keɪ-aɪ-mænsə/

> *"One who may be called upon to perform those secret rites and incantations
> necessary for the creation or interpretation of the mystical artifacts of the
> RPKI."*

---

## background

rpkimancer started out as an attempt to solve two RPKI tooling problems:

---

## problem #1

Wanted a *simple* way to read RPKI signed objects for debugging and education
purposes...

...without cracking out a **browser**

...without remembering **Byzantine `openssl` CLI options** and calculating
byte-offsets

---

## problem #2

While working on RSC I-D module I wanted a way to *check ASN.1 syntax* in CI
pipeline...

-   Tried scripting the "Job Snjiders" method. **Attempt abandoned** within 30 mins.

-   Tried re-purposing existing RP library code. Found that **no-one** actually
    generates code from ASN.1 (*)

-   Tried `asn1c`[1](https://github.com/vlm/asn1c). **Failed to compile** any of
    the PKIX/CMS dependencies.

---

## solution

-   much searching...

-   found the *only* OSS ASN.1 compiler capable of dealing
    with the necessary syntax constructs:
    `pycrate`[2](https://github.com/P1sec/pycrate)...

    ...but needed quite a lot of wrapping to make it useful

-   Began work on a Python library and CLI tool with the goal of being able to
    create and read arbitrary signed objects with only:

    - ASN.1 `CONTENT-TYPE` definition
    - Python class with a simple constructor

---

## status / features

-   Runtime ASN.1 module compilation

-   `import`-time discovery of `CONTENT-TYPE` instance definitions

-   Resource certificate implementations: TA (with TAL), CA and EE

-   Standards-track signed objects in base package: MFT, ROA and GBR

-   `rpkincant` CLI tool, demonstrates library usage:

    -   `rpkincant conjure`: create a self-contained object tree

    -   `rpkincant perceive`: decode and dump signed objects in various formats

-   Plug-in architecture for adding signed object types, CLI extensions.
    Existing plugins for:

    -   RSC [rpkimancer-rsc](https://github.com/job/draft-rpki-checklists)

    -   ASPA [rpkimancer-aspa](https://github.com/benmaddison/rpkimancer-aspa)

---

## use cases

-   Internet-draft module *validation* (CI)

-   Work-in-progress object *prototyping* for interop testing

-   RP/CA implementation *bug search* / confirmation

-   RP/CA *integration testing* and release qualification

-   Ad-hoc object *debugging*

At least two real bugs found so far:

-   Manifest loop handling in FORT
    [#55](https://github.com/NICMx/FORT-validator/issues/55)

-   EE certificate `commonName` length in krill/rpki-rs
    [#164](https://github.com/NLnetLabs/rpki-rs/issues/164)

---

## demo

---

## TODOs / ideas

-   BGPSec router certificates

-   plugable directory layout definitions for use in local RP testing

-   RRDP XML files generation

-   `diff` for signed objects

-   plug-in *template* repo

**help & suggestions (with/without PRs) welcome!**

---

## help wanted

-   CA/RP implementors:
    - preferred/recommended way to run against locally generated objects?
    - local cache directory layout plug-ins
    - test harness, machine readable logs, etc

-   Signed object I-D authors:
    -   plug-ins for proposed object definitions
    -   See [rpkimancer-rsc](https://github.com/job/draft-rpki-checklists) for
        integration example with I-D git repo

---

## fin

**questions?**

---
