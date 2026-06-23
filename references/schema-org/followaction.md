---
title: "FollowAction"
source_url: https://schema.org/FollowAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# FollowAction

# FollowAction

A Schema.org Type

- Canonical URL: https://schema.org/FollowAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+FollowAction)

The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.


Related actions:



Related actions:

[BefriendAction](/BefriendAction): Unlike BefriendAction, FollowAction implies that the connection is*not*necessarily reciprocal.[SubscribeAction](/SubscribeAction): Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.[RegisterAction](/RegisterAction): Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.[JoinAction](/JoinAction): Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.[TrackAction](/TrackAction): Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[followee](/followee)

[Organization](/Organization)or[Person](/Person)[Action](/Action)

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

[Example 1](#eg-0103)

Copied

Example notes or example HTML without markup.

John followed Steve on Twitter.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John followed Steve on Twitter. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "FollowAction", "agent": { "@type": "Person", "name": "John" }, "followee": { "@type": "Person", "name": "Steve" }, "object": { "@type": "Product", "name": "Twitter" } } </script>

Structured representation of the JSON-LD example.
