---
title: "VenueMap"
source_url: https://schema.org/VenueMap
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# VenueMap

# VenueMap

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/VenueMap
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+VenueMap)

A venue map (e.g. for malls, auditoriums, museums, etc.).

A member value for enumeration type:

[MapCategoryType](/MapCategoryType)

### Examples

[Example 1](#eg-0384)

Copied

Example notes or example HTML without markup.

<p> Welcome to a fictional SF art museum. Here is our <a href="/map1234/">venue map</a> </p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<p itemscope itemtype="https://schema.org/Museum"> Welcome to a fictional <span itemprop="name">SF art museum.</span> Here is our <span itemscope itemprop="hasMap" itemtype="https://schema.org/Map"> <link itemprop="mapType" href="https://schema.org/VenueMap" /> <a itemprop="url" href="/map1234/">venue map</a></span> </p>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<p vocab="https://schema.org/" typeof="Museum"> Welcome to a fictional <span property="name">SF art museum.</span> Here is our <span property="hasMap" typeof="Map"> <link itemprop="mapType" href="https://schema.org/VenueMap" /> <a property="url" href="/map1234/">venue map</a></span> </p>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "Museum", "name": "SF art museum", "hasMap": { "@type": "Map", "mapType": { "@id": "https://schema.org/VenueMap" }, "url": "http://art-sf.example.com/map1234/" } }

Structured representation of the JSON-LD example.
