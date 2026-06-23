---
title: "Property"
source_url: https://schema.org/Property
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Property

- Canonical URL: https://schema.org/Property
- Equivalent Class: rdf:Property
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Property)

A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[domainIncludes](/domainIncludes)

[Class](/Class)```
```[inverseOf](/inverseOf)

[Property](/Property)```
```[rangeIncludes](/rangeIncludes)

[Class](/Class)```
```[supersededBy](/supersededBy)

[Class](/Class)or[Enumeration](/Enumeration)or[Property](/Property)[Thing](/Thing)

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

[URL](/URL)Instances of

[Property](/Property)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ConstraintNode](/ConstraintNode)[StatisticalVariable](/StatisticalVariable). The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.[inverseOf](/inverseOf)

[Property](/Property)[measuredProperty](/measuredProperty)

[Observation](/Observation)or[StatisticalVariable](/StatisticalVariable)[Observation](/Observation), typically via its[StatisticalVariable](/StatisticalVariable). There are various kinds of applicable[Property](/Property): a schema.org property, a property from other RDF-compatible systems, e.g. W3C RDF Data Cube, Data Commons, Wikidata, or schema.org extensions such as[GS1's](https://www.gs1.org/voc/?show=properties).[statType](/statType)

[StatisticalVariable](/StatisticalVariable)[StatisticalVariable](/StatisticalVariable), e.g. mean, count etc. The value of statType is a property, either from within Schema.org (e.g.[median](/median),[marginOfError](/marginOfError),[maxValue](/maxValue),[minValue](/minValue)) or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.[supersededBy](/supersededBy)

[Class](/Class)or[Enumeration](/Enumeration)or[Property](/Property)[variableMeasured](/variableMeasured)
