---
title: "governmentBenefitsInfo"
source_url: https://schema.org/governmentBenefitsInfo
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# governmentBenefitsInfo

# governmentBenefitsInfo

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/governmentBenefitsInfo
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+governmentBenefitsInfo)

governmentBenefitsInfo provides information about government benefits associated with a SpecialAnnouncement.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2534](https://github.com/schemaorg/schemaorg/issues/2534)

### Examples

[Example 1](#eg-0301)

Copied

Example notes or example HTML without markup.

Government benefits coverage for SpecialAnnouncement pertaining to the covid-19 situation.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "New Paycheck Protection Program for small business", "text": "Example Administration announces a new loan that helps small businesses keep their workforce employed during the Coronavirus (COVID-19) crisis.", "datePosted": "2020-03-30T08:00", "expires": "2020-04-24T23:59", "category": "https://www.wikidata.org/wiki/Q81068910", "spatialCoverage": { "type": "Country", "name": "US" }, "governmentBenefitsInfo": { "@type": "GovernmentService", "name": "Paycheck Protection Program", "url": "https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program-ppp", "provider": { "@type": "GovernmentOrganization", "name": "US Small Business Administration" }, "serviceType": "https://schema.org/BusinessSupport", "audience": { "@type": "Audience", "name": "Small businesses" } } } </script>

Structured representation of the JSON-LD example.
