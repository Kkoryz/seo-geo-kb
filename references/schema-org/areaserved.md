---
title: "areaServed"
source_url: https://schema.org/areaServed
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# areaServed

# areaServed

A Schema.org Property

- Canonical URL: https://schema.org/areaServed
- Equivalent Property: fibo-fnd-pas-pas:hasServiceArea
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+areaServed)

The geographic area where a service or offered item is provided.

### Values expected to be one of these types


### Used on these types


#### Sub-properties

| Supersedes |
|---|
```
``` |

### Examples

[Example 1](#eg-0403)

Copied

Example notes or example HTML without markup.

Police station example (JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "PoliceStation", "name": "Youngstown Central Police Station", "description": "Central police station", "openingHours": "Mo-Su", "telephone": "+13303301888", "email": "ohio.police.example@example.com", "image": "https://homepages.cae.wisc.edu/~ece533/images/lena.png", "address": { "@type": "PostalAddress", "addressLocality": "Youngstown", "addressRegion": "OH", "postalCode": "44507", "streetAddress": "270 Derek Drive" }, "areaServed": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 41.108237, "longitude": -80.642982 }, "geoRadius": 1000 }, "aggregateRating": { "@type": "AggregateRating", "bestRating": 100, "worstRating": 0, "ratingValue": 88, "reviewCount": 122 } } </script>

Structured representation of the JSON-LD example.
