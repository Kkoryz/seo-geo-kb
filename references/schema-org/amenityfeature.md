---
title: "amenityFeature"
source_url: https://schema.org/amenityFeature
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# amenityFeature

# amenityFeature

A Schema.org Property

- Canonical URL: https://schema.org/amenityFeature
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+amenityFeature)

An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.

### Values expected to be one of these types


### Used on these types


### Acknowledgements

STI Accommodation Ontology

[http://ontologies.sti-innsbruck.at/acco/ns.html](http://ontologies.sti-innsbruck.at/acco/ns.html)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.

### Examples

[Example 1](#eg-0366)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Hotel Features: <ul> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Sauna</span> <meta itemprop="value" content="True"> </li> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Gym</span> <meta itemprop="value" content="True"> </li> </ul> </div>

[Example 2](#eg-0367)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Hotel Features: <ul> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Sauna</span> <meta itemprop="value" content="True"> <div itemprop="hoursAvailable" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="http://purl.org/goodrelations/v1#Thursday" />(Open Thursdays <time itemprop="opens" content="16:00:00"> 4:00 PM</time> - <time itemprop="closes" content="21:00:00"> 9:00 PM</time>) </div> </li> </ul> </div>
