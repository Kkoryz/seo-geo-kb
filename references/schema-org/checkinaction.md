---
title: "CheckInAction"
source_url: https://schema.org/CheckInAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2014-10-01
---

# CheckInAction

# CheckInAction

A Schema.org Type

- Canonical URL: https://schema.org/CheckInAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CheckInAction)

The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).


Related actions:



Related actions:

[CheckOutAction](/CheckOutAction): The antonym of CheckInAction.[ArriveAction](/ArriveAction): Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.[ConfirmAction](/ConfirmAction): Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the*start*of a previously reserved service rather than its validity/existence.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[about](/about)

[Thing](/Thing)Inverse property:

[subjectOf](/subjectOf)```
```[inLanguage](/inLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage). Supersedes[language](/language).```
```[recipient](/recipient)

[Audience](/Audience)or[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Person](/Person)[Action](/Action)

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

[Example 1](#eg-0091)

Copied

Example notes or example HTML without markup.

John checked in at Yandex.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John checked in at Yandex. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CheckInAction", "agent": { "@type": "Person", "name": "John" }, "location": { "@type": "Place", "address": { "@type": "PostalAddress", "name": "Yandex", "streetAddress": "16 Leo Tolstoy St", "addressLocality": "Moscow", "addressCountry": "Russia", "postalCode": "119021" } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0092)

Copied

Example notes or example HTML without markup.

John checked into a flight at the airport.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John checked into a flight at the airport. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CheckInAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Flight", "flightNumber": "110", "provider": "Aeroflot", "departureAirport": "SVO", "departureTime": "2014-10-01T15:30:00Z", "arrivalTime": "2014-10-02T12:00:00Z", "arrivalAirport": "SFO" }, "location": { "@type": "Place", "address": { "@type": "PostalAddress", "name": "Sheremetyevo International Airport", "addressLocality": "Khimki", "addressRegion": "Moscow Region", "addressCountry": "Russia", "postalCode": "141400" } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0093)

Copied

Example notes or example HTML without markup.

John checked into a flight online.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John checked into a flight online. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CheckInAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Flight", "flightNumber": "AA110" }, "instrument": { "@type": "WebApplication", "url": "http://aa.com" } } </script>

Structured representation of the JSON-LD example.
