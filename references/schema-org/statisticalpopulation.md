---
title: "StatisticalPopulation"
source_url: https://schema.org/StatisticalPopulation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# StatisticalPopulation

# StatisticalPopulation

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/StatisticalPopulation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+StatisticalPopulation)

A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property

[populationType](/populationType)is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a[StatisticalPopulation](/StatisticalPopulation)representing all[Person](/Person)s with a[homeLocation](/homeLocation)of East Podunk California would be described by applying the appropriate[homeLocation](/homeLocation)and[populationType](/populationType)properties to a[StatisticalPopulation](/StatisticalPopulation)item that stands for that set of people. The properties[numConstraints](/numConstraints)and[constraintProperty](/constraintProperty)are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statistical population, and does not imply that the population consists of people. For example, a[populationType](/populationType)of[Event](/Event)or[NewsArticle](/NewsArticle)could be used. See also[Observation](/Observation), where a[populationType](/populationType)such as[Person](/Person)or[Event](/Event)can be indicated directly. In most cases it may be better to use[StatisticalVariable](/StatisticalVariable)instead of[StatisticalPopulation](/StatisticalPopulation).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[populationType](/populationType)

[Class](/Class)[StatisticalPopulation](/StatisticalPopulation)or all cases within the scope of a[StatisticalVariable](/StatisticalVariable).[Thing](/Thing)

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

[https://github.com/schemaorg/schemaorg/issues/2291](https://github.com/schemaorg/schemaorg/issues/2291)
