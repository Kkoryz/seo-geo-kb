---
title: "latitude"
source_url: https://schema.org/latitude
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# latitude

# latitude

A Schema.org Property

- Canonical URL: https://schema.org/latitude
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+latitude)

The latitude of a location. For example

`37.42242`

([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).**Subproperty of:**

- cmns-loc:hasLatitude

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
