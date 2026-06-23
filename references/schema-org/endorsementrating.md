---
title: "EndorsementRating"
source_url: https://schema.org/EndorsementRating
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EndorsementRating

# EndorsementRating

A Schema.org Type

- Canonical URL: https://schema.org/EndorsementRating
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EndorsementRating)

An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a
"Like" or "+1" on a social network. It can be considered the


An

[result](/result)of an[EndorseAction](/EndorseAction)in which the[object](/object)of the action is rated positively by some[agent](/agent). As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the[Action](/Action).An

[EndorsementRating](/EndorsementRating)may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive, endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[https://github.com/schemaorg/schemaorg/issues/1293](https://github.com/schemaorg/schemaorg/issues/1293)
