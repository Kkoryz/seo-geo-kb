---
title: "ConstraintNode"
source_url: https://schema.org/ConstraintNode
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ConstraintNode

# ConstraintNode

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ConstraintNode
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ConstraintNode)

The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A

[ConstraintNode](/ConstraintNode)can be described using[constraintProperty](/constraintProperty)and[numConstraints](/numConstraints). These constraint properties can serve a variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[constraintProperty](/constraintProperty)

[Property](/Property)or[URL](/URL)[StatisticalVariable](/StatisticalVariable). The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.```
```[numConstraints](/numConstraints)

[Integer](/Integer)[ConstraintNode](/ConstraintNode)such as[StatisticalVariable](/StatisticalVariable). This helps applications understand if they have access to a sufficiently complete description of a[StatisticalVariable](/StatisticalVariable)or other construct that is defined using properties on template-style nodes.[Thing](/Thing)

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

[https://github.com/schemaorg/schemaorg/issues/2564](https://github.com/schemaorg/schemaorg/issues/2564)
