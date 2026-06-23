---
title: "AllocateAction"
source_url: https://schema.org/AllocateAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2020-01-01
---

# AllocateAction

# AllocateAction

A Schema.org Type

- Canonical URL: https://schema.org/AllocateAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+AllocateAction)

The act of organizing tasks/objects/events by associating resources to it.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[URL](/URL)#### More specific Types

### Examples

[Example 1](#eg-0122)

Copied

Example notes or example HTML without markup.

John allocated 5 hours to exercise.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John allocated 5 hours to exercise.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "AllocateAction", "participant": { "@type": "Person", "name": "John" }, "agent": { "@type": "Person", "name": "John's trainer" }, "object": { "@type": "ExercisePlan", "name": "John's weight loss plan" }, "startTime": "2020-01-01T09:00:00" } </script>

Structured representation of the JSON-LD example.
