---
title: "ReserveAction"
source_url: https://schema.org/ReserveAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2020-05-29
---

# ReserveAction

# ReserveAction

A Schema.org Type

- Canonical URL: https://schema.org/ReserveAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ReserveAction)

Reserving a concrete object.


Related actions:



Related actions:

[ScheduleAction](/ScheduleAction): Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[scheduledTime](/scheduledTime)

[Date](/Date)or[DateTime](/DateTime)[Action](/Action)

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

[Example 1](#eg-0132)

Copied

Example notes or example HTML without markup.

John reserved a table for May.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John reserved a table for May.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ReserveAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Reservation", "name": "Table at Bar Tartine" }, "scheduledTime": "2020-05-29T19:30:00" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0226)

Copied

Example notes or example HTML without markup.

A restaurant has links to reserve tables. One caters to Japanese speakers.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Restaurant", "potentialAction": { "@type": "ReserveAction", "target": [ "http://www.example.com/Reserve", { "@type": "LinkRole", "target": "http://www.example.com/Reserve-JP", "inLanguage": "ja", "linkRelationship": "alternate" } ] } } </script>

Structured representation of the JSON-LD example.
