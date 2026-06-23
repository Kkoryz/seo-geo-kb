---
title: "Error"
source_url: https://schema.org/Error
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2025-11-17
---

# Error

# Error

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/Error
- Equivalent Class: hydra:Error
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Error)

Representation of an Error.

**Subclass of:**

- sarif:Result

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[errorCode](/errorCode)

[DefinedTerm](/DefinedTerm)or[Integer](/Integer)or[StatusEnumeration](/StatusEnumeration)or[Text](/Text)[InstantaneousEvent](/InstantaneousEvent)

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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/4579](https://github.com/schemaorg/schemaorg/issues/4579)

### Examples

[Example 1](#eg-4579)

Copied

Example notes or example HTML without markup.

<code>Out of Cheese Error: DEADBEEF</code>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Error", "timestamp": "2025-11-17T18:23:00Z", "description": "Out of Cheese Error", "source": { "@type": "SoftwareApplication", "name": "Cheese Machine" }, "errorCode": "DEADBEEF" } </script>

Structured representation of the JSON-LD example.
