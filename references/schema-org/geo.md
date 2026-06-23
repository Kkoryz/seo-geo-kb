---
title: "geo"
source_url: https://schema.org/geo
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# geo

# geo

A Schema.org Property

- Canonical URL: https://schema.org/geo
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+geo)

The geo coordinates of the place.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0005)

Copied

Example notes or example HTML without markup.

<h1>What is the latitude and longitude of the Empire State Building?</h1> Answer: Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 sec W

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Place"> <h1>What is the latitude and longitude of the <span itemprop="name">Empire State Building</span>?</h1> Answer: <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCoordinates"> Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 dec W <meta itemprop="latitude" content="40.75" /> <meta itemprop="longitude" content="-73.98" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Place"> <h1>What is the latitude and longitude of the <span property="name">Empire State Building</span>?</h1> Answer: <div property="geo" typeof="GeoCoordinates"> Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 dec W <meta property="latitude" content="40.75" /> <meta property="longitude" content="-73.98" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Place", "geo": { "@type": "GeoCoordinates", "latitude": "40.75", "longitude": "-73.98" }, "name": "Empire State Building" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0363)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">Technikerstrasse 21</span> <span itemprop="postalCode">6020</span> <span itemprop="addressLocality">Innsbruck</span> <span itemprop="addressRegion">Tyrol</span>, <span itemprop="addressCountry">Austria</span> </div> <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCoordinates"> <meta itemprop="latitude" content="47.2649990" /> <meta itemprop="longitude" content="11.3428720" /> </div> </div>
