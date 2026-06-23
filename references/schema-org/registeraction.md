---
title: "RegisterAction"
source_url: https://schema.org/RegisterAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# RegisterAction

# RegisterAction

A Schema.org Type

- Canonical URL: https://schema.org/RegisterAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+RegisterAction)

The act of registering to be a user of a service, product or web page.


Related actions:



Related actions:

[JoinAction](/JoinAction): Unlike JoinAction, RegisterAction implies you are registering to be a user of a service,*not*a group/team of people.[FollowAction](/FollowAction): Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.[SubscribeAction](/SubscribeAction): Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object.

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

[URL](/URL)### Examples

[Example 1](#eg-0110)

Copied

Example notes or example HTML without markup.

John registered for the IEEE.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John registered for the IEEE. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "RegisterAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Organization", "name": "IEEE" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0111)

Copied

Example notes or example HTML without markup.

John registered to Twitter.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John registered to Twitter. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "RegisterAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Product", "name": "Twitter" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0112)

Copied

Example notes or example HTML without markup.

John registered to Comcast.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John registered to Comcast. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "RegisterAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "Product", "name": "Comcast" } } </script>

Structured representation of the JSON-LD example.
