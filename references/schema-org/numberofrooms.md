---
title: "numberOfRooms"
source_url: https://schema.org/numberOfRooms
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# numberOfRooms

# numberOfRooms

A Schema.org Property

- Canonical URL: https://schema.org/numberOfRooms
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+numberOfRooms)

The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.

### Values expected to be one of these types


### Used on these types


### Acknowledgements

STI Accommodation Ontology

[http://ontologies.sti-innsbruck.at/acco/ns.html](http://ontologies.sti-innsbruck.at/acco/ns.html)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.

### Examples

[Example 1](#eg-0364)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> <span itemprop="numberOfRooms">60</span> rooms. </div>

[Example 2](#eg-0365)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> <span itemprop="numberOfRooms" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">45</span> <span itemprop="unitText">double rooms</span> </span> <span itemprop="numberOfRooms" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">15</span> <span itemprop="unitText">single rooms</span> </span> </div>
