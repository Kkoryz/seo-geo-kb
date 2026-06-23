---
title: "conditionsOfAccess"
source_url: https://schema.org/conditionsOfAccess
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# conditionsOfAccess

# conditionsOfAccess

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/conditionsOfAccess
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+conditionsOfAccess)

Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an


For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ".

[ArchiveComponent](/ArchiveComponent)held by an[ArchiveOrganization](/ArchiveOrganization). This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ".

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2173](https://github.com/schemaorg/schemaorg/issues/2173)

### Examples

[Example 1](#eg-0273)

Copied

Example notes or example HTML without markup.

<!-- Dataset with restricted access -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- Dataset with restricted access --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Dataset", "@id": "https://doi.org/10.7910/DVN/0OLJLM", "name": "Restricted Access WFHS Leef Manager Linking Data, Version 1.0", "conditionsOfAccess": "Access to this dataset can be obtained by visiting the Work, Family & Health Network web page and following the instructions: http://projects.iq.harvard.edu/wfhn/restricted-access-data." } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0274)

Copied

Example notes or example HTML without markup.

<!-- ArchiveComponent with restricted access -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- ArchiveComponent with restricted access --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": ["CreativeWork","ArchiveComponent"], "url": "https://purl.stanford.edu/bp158wj7223", "name": "Margaret Mitchell letter to Herschel Bricknell, 1936 August 22", "conditionsOfAccess": "Online content is available for access via the Special Collections Reading Room.", "holdingArchive": { "@type": "ArchiveOrganization", "name": "Stanford Digital Repository", "url": "https://purl.stanford.edu/" } } </script>

Structured representation of the JSON-LD example.
