---
title: "membershipPointsEarned"
source_url: https://schema.org/membershipPointsEarned
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# membershipPointsEarned

# membershipPointsEarned

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/membershipPointsEarned
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+membershipPointsEarned)

The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2085](https://github.com/schemaorg/schemaorg/issues/2085)

### Examples

[Example 1](#eg-0269)

Copied

Example notes or example HTML without markup.

An email message describing the points earned.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@type": "ProgramMembership", "name": "ACME customer rewards", "membershipPointsEarned": { "@type": "QuantitativeValue", "unitText": "Starpoints", "value": 500 } } </script>

Structured representation of the JSON-LD example.
