---
title: "leaseLength"
source_url: https://schema.org/leaseLength
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# leaseLength

# leaseLength

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/leaseLength
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+leaseLength)

Length of the lease for some

[Accommodation](/Accommodation), either particular to some[Offer](/Offer)or in some cases intrinsic to the property.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2373](https://github.com/schemaorg/schemaorg/issues/2373)

### Examples

[Example 1](#eg-0422)

Copied

Example notes or example HTML without markup.

Single family residence example with min and max occupancy limits, floor size of 2500 square foots and lease length of 6 months(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SingleFamilyResidence", "name": "1331 St George Street - Family House", "description": "Great opportunity to own this 2500 sqft originally built in 1988 family home with 4 bedroom, 3 bathroom. which was RENOVATED IN 2014:( New Windows, New Bathroom, New Hardwood Floors, Air Condition, New Kitchen, etc.)", "numberOfRooms": 5, "occupancy": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5 }, "floorSize": { "@type": "QuantitativeValue", "value": 2500, "unitCode": "FTK" }, "leaseLength": { "@type": "QuantitativeValue", "value": 6, "unitText": "months" }, "numberOfBathroomsTotal": 3, "numberOfBedrooms": 4, "permittedUsage": "Perfectly suitable for a family with two kids.", "petsAllowed": "Only cats are allowed", "yearBuilt": 1988, "address": { "@type": "PostalAddress", "addressCountry": "CA", "addressLocality": "Vancouver", "addressRegion": "British Columbia", "postalCode": "V5T 1Z7", "streetAddress": "1331 St George Street" }, "telephone": "+1-604-829-6070" } </script>

Structured representation of the JSON-LD example.
