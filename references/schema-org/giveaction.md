---
title: "GiveAction"
source_url: https://schema.org/GiveAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# GiveAction

# GiveAction

A Schema.org Type

- Canonical URL: https://schema.org/GiveAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+GiveAction)

The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.


Related actions:



Related actions:

[TakeAction](/TakeAction): Reciprocal of GiveAction.[SendAction](/SendAction): Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[recipient](/recipient)

[Audience](/Audience)or[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Person](/Person)[TransferAction](/TransferAction)

```
```[fromLocation](/fromLocation)

[Place](/Place)```
```[toLocation](/toLocation)

[Place](/Place)[Action](/Action)

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

[Example 1](#eg-0152)

Copied

Example notes or example HTML without markup.

John gave a book to Steve.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John gave a book to Steve.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GiveAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Book", "name": "Outliers" }, "recipient": { "@type": "Person", "name": "Steve" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0157)

Copied

Example notes or example HTML without markup.

John took a book from Steve.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John gave a book to Steve.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GiveAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Book", "name": "Outliers" }, "recipient": { "@type": "Person", "name": "Steve" } } </script>

Structured representation of the JSON-LD example.
