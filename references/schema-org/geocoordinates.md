---
title: "GeoCoordinates"
source_url: https://schema.org/GeoCoordinates
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# GeoCoordinates

# GeoCoordinates

A Schema.org Type

- Canonical URL: https://schema.org/GeoCoordinates
-
Equivalent Class: cmns-loc:GeographicCoordinate

Equivalent Class: unece:GeographicalCoordinate [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+GeoCoordinates)

The geographic coordinates of a place or event.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[address](/address)

[PostalAddress](/PostalAddress)or[Text](/Text)```
```[addressCountry](/addressCountry)

[Country](/Country)or[Text](/Text)[ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1)format, for example "US". For backward compatibility, a 3-letter[ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)country code such as "SGP" or a full country name such as "Singapore" can also be used.```
```[elevation](/elevation)

[Number](/Number)or[Text](/Text)[WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT_OF_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.```
```[latitude](/latitude)

[Number](/Number)or[Text](/Text)`37.42242`

([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).```
```[longitude](/longitude)

[Number](/Number)or[Text](/Text)`-122.08585`

([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).```
```[postalCode](/postalCode)

[Text](/Text)[Thing](/Thing)

```
```[additionalType](/additionalType)

[Text](/Text)or[URL](/URL)[style guide](https://schema.org/docs/styleguide.html).```
```[alternateName](/alternateName)

[Text](/Text)```
```[description](/description)

[Text](/Text)or[TextObject](/TextObject)```
```[disambiguatingDescription](/disambiguatingDescription)

[Text](/Text)```
```[identifier](/identifier)

[PropertyValue](/PropertyValue)or[Text](/Text)or[URL](/URL)[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.```
```[image](/image)

[ImageObject](/ImageObject)or[URL](/URL)[URL](/URL)or a fully described[ImageObject](/ImageObject).```
```[mainEntityOfPage](/mainEntityOfPage)

[CreativeWork](/CreativeWork)or[URL](/URL)[background notes](/docs/datamodel.html#mainEntityBackground)for details.Inverse property:

[mainEntity](/mainEntity)```
```[name](/name)

[Text](/Text)```
```[owner](/owner)

[Organization](/Organization)or[Person](/Person)Inverse property:

[owns](/owns)```
```[potentialAction](/potentialAction)

[Action](/Action)```
```[sameAs](/sameAs)

[URL](/URL)```
```[subjectOf](/subjectOf)

[CreativeWork](/CreativeWork)or[Event](/Event)Inverse property:

[about](/about)```
```[url](/url)

[URL](/URL)Instances of

[GeoCoordinates](/GeoCoordinates)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Place](/Place)[geoMidpoint](/geoMidpoint)

[GeoCircle](/GeoCircle)### Examples

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
