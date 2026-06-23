---
title: "EngineSpecification"
source_url: https://schema.org/EngineSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EngineSpecification

# EngineSpecification

A Schema.org Type

- Canonical URL: https://schema.org/EngineSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EngineSpecification)

Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[engineDisplacement](/engineDisplacement)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches * Note 1: You can link to information about how the given value has been determined using the

[valueReference](/valueReference)property. * Note 2: You can use[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.```
```[enginePower](/enginePower)

[QuantitativeValue](/QuantitativeValue)- Note 1: There are many different ways of measuring an engine's power. For an overview, see
[http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes). - Note 2: You can link to information about how the given value has been determined using the
[valueReference](/valueReference)property. - Note 3: You can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

```
```[engineType](/engineType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[fuelType](/fuelType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[torque](/torque)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch

- Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the
[valueReference](/valueReference)property. - Note 2: You can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[Thing](/Thing)

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

[EngineSpecification](/EngineSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Vehicle](/Vehicle)### Acknowledgements

Automotive Ontology Working Group

[www.automotive-ontology.org](http://www.automotive-ontology.org)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.
