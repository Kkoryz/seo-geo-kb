---
title: "lifeEvent"
source_url: https://schema.org/lifeEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# lifeEvent

# lifeEvent

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/lifeEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+lifeEvent)

A life event like baptism, communions, Bar Mitzvahs, Aqiqah, Namakarana, Miyamairi, burial, ....

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/4540](https://github.com/schemaorg/schemaorg/issues/4540)

### Examples

[Example 1](#eg-4540)

Copied

Example notes or example HTML without markup.

See JSON example. Background, https://docs.google.com/document/d/1LNew5OEon4uir2D5Zzp0AkUPA7c9nO8reJ_M1pOy-3s/edit#

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "schema:Person", "givenName": "Gotthilf Wilhelm", "familyName": "Bach", "lifeEvent": [ { "@type": "schema:Event", "name": "Baptism", "startDate": "1754-08-02", "location": { "@type": "schema:Place", "name": "Halle (Saale)" } }, { "@type": "schema:Event", "name": "Burial", "startDate": "1756-01-18", "location": { "@type": "schema:Place", "name": "Halle (Saale)" } } ] } </script>

Structured representation of the JSON-LD example.
