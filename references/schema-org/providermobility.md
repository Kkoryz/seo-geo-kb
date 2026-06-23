---
title: "providerMobility"
source_url: https://schema.org/providerMobility
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# providerMobility

# providerMobility

A Schema.org Property

- Canonical URL: https://schema.org/providerMobility
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+providerMobility)

Indicates the mobility of a provided service (e.g. 'static', 'dynamic').

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0421)

Copied

Example notes or example HTML without markup.

Car for hire driver #123 is within 50 meters of a given location, but is moving.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TaxiService"> <div itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">driver #123</span> <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCircle"> <div itemprop="geoMidpoint" itemscope itemtype="https://schema.org/GeoCoordinates"> <meta itemprop="latitude" content="42.362757" /> <meta itemprop="longitude" content="-71.087109" /> </div> <meta itemprop="geoRadius" content="50" /> </div> </div> </div> <meta itemprop="providerMobility" content="dynamic" /> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TaxiService"> <div property="provider" typeof="LocalBusiness"> <span property="name">driver #123</span> <div property="location" typeof="Place"> <div property="geo" typeof="GeoCircle"> <div property="geoMidpoint" typeof="GeoCoordinates"> <meta property="latitude" content="42.362757" /> <meta property="longitude" content="-71.087109" /> </div> <meta property="geoRadius" content="50" /> </div> </div> </div> <meta property="providerMobility" content="dynamic" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "TaxiService", "provider": { "@type": "LocalBusiness", "name": "driver #123", "location": { "@type": "Place", "geo": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": "42.362757", "longitude": "-71.087109" }, "geoRadius": "50" } } }, "providerMobility": "dynamic" } </script>

Structured representation of the JSON-LD example.
