---
title: "LimitedAvailability"
source_url: https://schema.org/LimitedAvailability
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# LimitedAvailability

# LimitedAvailability

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/LimitedAvailability
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+LimitedAvailability)

Indicates that the item has limited availability.

A member value for enumeration type:

[ItemAvailability](/ItemAvailability)

### Examples

[Example 1](#eg-0174)

Copied

Example notes or example HTML without markup.

JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" } </script>

Structured representation of the JSON-LD example.
