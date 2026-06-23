---
title: "SizeSpecification"
source_url: https://schema.org/SizeSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SizeSpecification

# SizeSpecification

A Schema.org Enumeration Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/SizeSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SizeSpecification)

Size related properties of a product, typically a size code (

[name](/name)) and optionally a[sizeSystem](/sizeSystem),[sizeGroup](/sizeGroup), and product measurements ([hasMeasurement](/hasMeasurement)). In addition, the intended audience can be defined through[suggestedAge](/suggestedAge),[suggestedGender](/suggestedGender), and suggested body measurements ([suggestedMeasurement](/suggestedMeasurement)).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[hasMeasurement](/hasMeasurement)

[QuantitativeValue](/QuantitativeValue)```
```[sizeGroup](/sizeGroup)

[SizeGroupEnumeration](/SizeGroupEnumeration)or[Text](/Text)```
```[sizeSystem](/sizeSystem)

[SizeSystemEnumeration](/SizeSystemEnumeration)or[Text](/Text)```
```[suggestedAge](/suggestedAge)

[QuantitativeValue](/QuantitativeValue)```
```[suggestedGender](/suggestedGender)

[GenderType](/GenderType)or[Text](/Text)```
```[suggestedMeasurement](/suggestedMeasurement)

[QuantitativeValue](/QuantitativeValue)[QualitativeValue](/QualitativeValue)

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[equal](/equal)

[QualitativeValue](/QualitativeValue)```
```[greater](/greater)

[QualitativeValue](/QualitativeValue)```
```[greaterOrEqual](/greaterOrEqual)

[QualitativeValue](/QualitativeValue)```
```[lesser](/lesser)

[QualitativeValue](/QualitativeValue)```
```[lesserOrEqual](/lesserOrEqual)

[QualitativeValue](/QualitativeValue)```
```[nonEqual](/nonEqual)

[QualitativeValue](/QualitativeValue)```
```[valueReference](/valueReference)

[DefinedTerm](/DefinedTerm)or[Enumeration](/Enumeration)or[MeasurementTypeEnumeration](/MeasurementTypeEnumeration)or[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)or[StructuredValue](/StructuredValue)or[Text](/Text)[Enumeration](/Enumeration)

```
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

[SizeSpecification](/SizeSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)or[Product](/Product)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.#### Source

[https://github.com/schemaorg/schemaorg/issues/2811](https://github.com/schemaorg/schemaorg/issues/2811)

### Examples

[Example 1](#eg-0464)

Copied

Example notes or example HTML without markup.

Complete example for a men's jacket with comprehensive size specification: - Size system: US - Size group: Men's Big & Tall - Size code: 3XL - Jacket measurements: chest: 52 inches, and length 42 inches. - Suggested age group: 13 years and up - Suggested body measurements: chest: 51-54 inches; height: 6-6.3 feet

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "sku": "44E01-M11000", "inProductGroupWithID": "44E01", "gtin14": "98766051104218", "image": "https://www.example.com/jacket_large_green.jpg", "name": "Large green jacket", "description": "Large wool green jacket for the winter months", "brand": { "@type": "Brand", "name": "A fashion brand" }, "color": "green", "size": { "@type": "SizeSpecification", "sizeSystem": "https://schema.org/WearableSizeSystemUS", "sizeGroup": [ "https://schema.org/WearableSizeGroupMens", "https://schema.org/WearableSizeGroupBig", "https://schema.org/WearableSizeGroupTall" ], "name": "3XL", "hasMeasurement": [ { "@type": "QuantitativeValue", "valueReference": "https://schema.org/WearableMeasurementChestOrBust", "unitCode": "INH", "value": 52 }, { "@type": "QuantitativeValue", "valueReference": "https://schema.org/WearableMeasurementLength", "unitCode": "INH", "value": 42 } ], "suggestedGender": "male", "suggestedAge": { "@type": "QuantitativeValue", "name": "adult", "unitCode": "ANN", "minValue": 13 }, "suggestedMeasurement": [ { "@type": "QuantitativeValue", "valueReference": "https://schema.org/BodyMeasurementChest", "unitCode": "INH", "minValue": 51, "maxValue": 54 }, { "@type": "QuantitativeValue", "valueReference": "https://schema.org/BodyMeasurementHeight", "unitCode": "FOT", "minValue": 6, "maxValue": 6.3 } ] }, "offers": { "@type": "Offer", "url": "https://www.example.com/jacket?s=l&c=g", "priceCurrency": "USD", "price": 239.99, "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock" } } </script>

Structured representation of the JSON-LD example.
