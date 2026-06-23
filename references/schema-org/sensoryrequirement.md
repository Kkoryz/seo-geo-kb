---
title: "sensoryRequirement"
source_url: https://schema.org/sensoryRequirement
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# sensoryRequirement

# sensoryRequirement

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/sensoryRequirement
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+sensoryRequirement)

A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2384](https://github.com/schemaorg/schemaorg/issues/2384)

### Examples

[Example 1](#eg-0283)

Copied

Example notes or example HTML without markup.

Job posting for an electrician. Must be able to discriminate colors.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "electrician", "sensoryRequirement": { "@type": "DefinedTerm", "termCode": "1.A.4.a.3", "inDefinedTermSet": "https://www.onetonline.org/find/descriptor/browse/Abilities/", "name": "Visual Color Discrimination", "description": "The ability to match or detect differences between colors, including shades of color and brightness." } } </script>

Structured representation of the JSON-LD example.
