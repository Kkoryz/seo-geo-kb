---
title: "JoinAction"
source_url: https://schema.org/JoinAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# JoinAction

# JoinAction

A Schema.org Type

- Canonical URL: https://schema.org/JoinAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+JoinAction)

An agent joins an event/group with participants/friends at a location.


Related actions:



Related actions:

[RegisterAction](/RegisterAction): Unlike RegisterAction, JoinAction refers to joining a group/team of people.[SubscribeAction](/SubscribeAction): Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.[FollowAction](/FollowAction): Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[event](/event)

[Event](/Event)[events](/events).[Action](/Action)

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

[Example 1](#eg-0104)

Copied

Example notes or example HTML without markup.

John joined the basketball team.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John joined the basketball team. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JoinAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "SportsTeam", "name": "Chicago Bulls" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0105)

Copied

Example notes or example HTML without markup.

John joined the Beatles.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John joined the Beatles. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JoinAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "MusicGroup", "name": "The Beatles" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0106)

Copied

Example notes or example HTML without markup.

John joined the Cats cast.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John joined the Cats cast. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JoinAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "TheaterGroup", "name": "Cats" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0107)

Copied

Example notes or example HTML without markup.

John joined the festival.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John joined the festival. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JoinAction", "agent": { "@type": "Person", "name": "John" }, "event": { "@type": "Festival", "name": "Woodstock" } } </script>

Structured representation of the JSON-LD example.
