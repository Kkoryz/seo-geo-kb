---
title: "InstantaneousEvent"
source_url: https://schema.org/InstantaneousEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2025-11-11
---

# InstantaneousEvent

# InstantaneousEvent

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/InstantaneousEvent
- Equivalent Class: prov:InstantaneousEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+InstantaneousEvent)

An event with no duration, like for instance a computer log entry.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[data](/data)

[Thing](/Thing)```
```[source](/source)

[Thing](/Thing)```
```[timestamp](/timestamp)

[DateTime](/DateTime)[Thing](/Thing)

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

#### Source

[https://github.com/schemaorg/schemaorg/issues/4527](https://github.com/schemaorg/schemaorg/issues/4527)

### Examples

[Example 1](#eg-4527)

Copied

Example notes or example HTML without markup.

Process 123456 (/opt/X11/bin/xeyes) Terminated (XCPU).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org", "@type": "InstantaneousEvent", "timestamp": "2025-11-11T15:17:21Z", "description": "Process 123456 (/opt/X11/bin/xeyes) Terminated (XCPU).", "source": { "@type": "SoftwareApplication", "name": "Unix" }, "data": [ { "@type": "PropertyValue", "name": "username", "value": "johndoe" }, { "@type": "PropertyValue", "name": "PID", "value": "123456" }, { "@type": "PropertyValue", "name": "PID", "value": "123456" }, { "@type": "PropertyValue", "name": "process", "value": "/opt/X11/bin/xeyes" }, { "@type": "PropertyValue", "name": "signal", "value": "XCPU" } ] }

Structured representation of the JSON-LD example.
