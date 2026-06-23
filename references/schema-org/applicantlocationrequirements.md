---
title: "applicantLocationRequirements"
source_url: https://schema.org/applicantLocationRequirements
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# applicantLocationRequirements

# applicantLocationRequirements

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/applicantLocationRequirements
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+applicantLocationRequirements)

The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2083](https://github.com/schemaorg/schemaorg/issues/2083)

### Examples

[Example 1](#eg-0268)

Copied

Example notes or example HTML without markup.

A job where one must be in the United States to apply.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "name": "Telecommute from anywhere in USA!", "applicantLocationRequirements": { "@type": "Country", "sameAs": "https://www.wikidata.org/wiki/Q30", "name": "USA" } } </script>

Structured representation of the JSON-LD example.
