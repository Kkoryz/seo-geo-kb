---
title: "ListenAction"
source_url: https://schema.org/ListenAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ListenAction

# ListenAction

A Schema.org Type

- Canonical URL: https://schema.org/ListenAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ListenAction)

The act of consuming audio content.

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

[Example 1](#eg-0057)

Copied

Example notes or example HTML without markup.

John listened to Pink.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John listened to Pink. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ListenAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "MusicGroup", "name": "Pink!" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0058)

Copied

Example notes or example HTML without markup.

John listened to star 101.3.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John listened to star 101.3. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ListenAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "RadioStation", "name": "Star 101.3" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0059)

Copied

Example notes or example HTML without markup.

John listened to an Elvis playlist.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John listened to an Elvis playlist. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ListenAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "MusicPlaylist", "name": "All Elvis Songs" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0253)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "MusicRecording", "potentialAction": { "@type": "ListenAction", "actionAccessibilityRequirement": { "@type": "ActionAccessSpecification", "availabilityStarts": "2017-01-01T00:00", "availabilityEnds": "2017-12-31T00:00", "eligibleRegion": { "@type": "Country", "sameAs": "https://www.wikidata.org/wiki/Q166433", "name": "US" }, "requiresSubscription": { "@type": "MediaSubscription", "name": "ACME streaming music monthly subscription", "authenticator": { "@type": "Organization", "name": "ACME Media" } }, "expectsAcceptanceOf": { "@type": "Offer", "itemOffered": { "@type": "MusicRecording", "name": "Song I want to stream that is only available for streaming after I buy it." } } } } } </script>

Structured representation of the JSON-LD example.
