---
title: "starRating"
source_url: https://schema.org/starRating
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# starRating

# starRating

A Schema.org Property

- Canonical URL: https://schema.org/starRating
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+starRating)

An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).

### Values expected to be one of these types


### Used on these types


### Acknowledgements

STI Accommodation Ontology

[http://ontologies.sti-innsbruck.at/acco/ns.html](http://ontologies.sti-innsbruck.at/acco/ns.html)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.

### Examples

[Example 1](#eg-0359)

Copied

Example notes or example HTML without markup.

<h1>ACME Hotel Innsbruck</h1> <span>A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Star rating: **** Room rates: $100 - $240 </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Star rating: <span itemprop="starRating" itemscope itemtype="https://schema.org/Rating"> <meta itemprop="ratingValue" content="4">****</span> Room rates: <span itemprop="priceRange">$100 - $240</span> </div>

[Example 2](#eg-0360)

Copied

Example notes or example HTML without markup.

<h1>ACME Hotel Innsbruck</h1> <span>A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Star rating: **** (DEHOGA) Room rates: $100 - $240 </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Star rating: <span itemprop="starRating" itemscope itemtype="https://schema.org/Rating"> <span itemprop="author" itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">DEHOGA</span> </span> <meta itemprop="ratingValue" content="4">**** </span> Room rates: <span itemprop="priceRange">$100 - $240</span> </div>
