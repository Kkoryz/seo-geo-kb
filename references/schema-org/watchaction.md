---
title: "WatchAction"
source_url: https://schema.org/WatchAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# WatchAction

# WatchAction

A Schema.org Type

- Canonical URL: https://schema.org/WatchAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+WatchAction)

The act of consuming dynamic/moving visual content.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[actionAccessibilityRequirement](/actionAccessibilityRequirement)

[ActionAccessSpecification](/ActionAccessSpecification)```
```[expectsAcceptanceOf](/expectsAcceptanceOf)

[Offer](/Offer)[Action](/Action)

```
```[actionProcess](/actionProcess)

[HowTo](/HowTo)```
```[actionStatus](/actionStatus)

[ActionStatusType](/ActionStatusType)```
```[agent](/agent)

[Organization](/Organization)or[Person](/Person)*John*wrote a book.```
```[endTime](/endTime)

[DateTime](/DateTime)or[Time](/Time)*December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[error](/error)

[Thing](/Thing)```
```[instrument](/instrument)

[Thing](/Thing)*a pen*.```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[object](/object)

[Thing](/Thing)*a book*.```
```[participant](/participant)

[Organization](/Organization)or[Person](/Person)*Steve*.```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[result](/result)

[Thing](/Thing)*a book*.```
```[startTime](/startTime)

[DateTime](/DateTime)or[Time](/Time)*January*to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[target](/target)

[EntryPoint](/EntryPoint)or[URL](/URL)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0069)

Copied

Example notes or example HTML without markup.

John watched Friends.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John watched Friends. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WatchAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "TVEpisode", "name": "Friends!" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0070)

Copied

Example notes or example HTML without markup.

John watched The Big Bang Theory

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John watched The Big Bang Theory --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WatchAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "TVSeries", "name": "The Big Bang Theory" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0071)

Copied

Example notes or example HTML without markup.

John watched The Internship

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John watched The Internship --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WatchAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Movie", "name": "The Internship" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0072)

Copied

Example notes or example HTML without markup.

John watched The Bolshoi Ballet group in Russia.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John watched The Bolshoi Ballet group in Russia.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WatchAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "PerformingGroup", "name": "Bolshoi" }, "location": { "@type": "PerformingArtsTheater", "name": "Chuvash State Opera and Ballet Theater" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0187)

Copied

Example notes or example HTML without markup.

<!-- A Movie named "Footloose" with a WatchAction as a potentialAction, with a target of http://example.com/player?id=123. --> <div> <a href="http://example.com/player?id=123">Watch <cite>Footloose</cite></a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Movie"> <meta itemprop="name" content="Footloose"> <div itemprop="potentialAction" itemscope itemtype="https://schema.org/WatchAction"> <a itemprop="target" href="http://example.com/player?id=123">Watch <cite>Footloose</cite></a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Movie"> <meta property="name" content="Footloose"> <div property="potentialAction" typeof="WatchAction"> <a property="target" href="http://example.com/player?id=123">Watch <cite>Footloose</cite></a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "Footloose", "potentialAction" : { "@type": "WatchAction", "target" : "http://example.com/player?id=123" } } </script>

Structured representation of the JSON-LD example.
