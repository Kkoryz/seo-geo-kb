---
title: "employmentUnit"
source_url: https://schema.org/employmentUnit
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# employmentUnit

# employmentUnit

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/employmentUnit
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+employmentUnit)

Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2296](https://github.com/schemaorg/schemaorg/issues/2296)

### Examples

[Example 1](#eg-0281)

Copied

Example notes or example HTML without markup.

JobPosting for Junior Software Developer in ITS Division C of ACME Corp

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JobPosting", "title": "Junior software developer", "hiringOrganization" : { "@type": "Organization", "@id": "http://www.example.com/acme#Organization", "name": "ACME Corp.", "url": "www.example.com" }, "employmentUnit" : { "@type": "Organization", "name": "ITS - Division C", "parentOrganization" : { "@id": "http://www.example.com/acme#Organization" } } } </script>

Structured representation of the JSON-LD example.
