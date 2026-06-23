---
title: "EmployerAggregateRating"
source_url: https://schema.org/EmployerAggregateRating
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EmployerAggregateRating

# EmployerAggregateRating

A Schema.org Type

- Canonical URL: https://schema.org/EmployerAggregateRating
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EmployerAggregateRating)

An aggregate rating of an Organization related to its role as an employer.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[itemReviewed](/itemReviewed)

[Thing](/Thing)```
```[ratingCount](/ratingCount)

[Integer](/Integer)```
```[reviewCount](/reviewCount)

[Integer](/Integer)[Rating](/Rating)

```
```[author](/author)

[Organization](/Organization)or[Person](/Person)```
```[bestRating](/bestRating)

[Number](/Number)or[Text](/Text)```
```[ratingExplanation](/ratingExplanation)

[Text](/Text)[ClaimReview](/ClaimReview).```
```[ratingValue](/ratingValue)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[reviewAspect](/reviewAspect)

[StructuredValue](/StructuredValue)or[Text](/Text)```
```[worstRating](/worstRating)

[Number](/Number)or[Text](/Text)[Thing](/Thing)

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

[https://github.com/schemaorg/schemaorg/issues/1689](https://github.com/schemaorg/schemaorg/issues/1689)

### Examples

[Example 1](#eg-0247)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "EmployerAggregateRating", "description": "ACME Corp gets 4/5 stars as an employer based on 42 ratings.", "itemReviewed": { "@type": "Organization", "name": "ACME Corp" }, "ratingCount": 42, "ratingValue": 4, "worstRating": 1, "bestRating": 5 } </script>

Structured representation of the JSON-LD example.
