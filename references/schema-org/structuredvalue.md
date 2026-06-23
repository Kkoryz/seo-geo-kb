---
title: "StructuredValue"
source_url: https://schema.org/StructuredValue
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# StructuredValue

# StructuredValue

A Schema.org Type

- Canonical URL: https://schema.org/StructuredValue
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+StructuredValue)

Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[StructuredValue](/StructuredValue)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Course](/Course)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)[pronouns](/pronouns)

[Person](/Person)In English, formulations such as "they/them", "she/her", and "he/him" are commonly used online and can also be used here. We do not intend to enumerate all possible micro-syntaxes in all languages. More structured and well-defined external values for pronouns can be referenced using the

[StructuredValue](/StructuredValue)or[DefinedTerm](/DefinedTerm)values.[reviewAspect](/reviewAspect)

[Guide](/Guide)or[Rating](/Rating)or[Review](/Review)[typicalCreditsPerTerm](/typicalCreditsPerTerm)

[EducationalOccupationalProgram](/EducationalOccupationalProgram)[value](/value)

[MonetaryAmount](/MonetaryAmount)or[PropertyValue](/PropertyValue)or[QuantitativeValue](/QuantitativeValue)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

[valueReference](/valueReference)

[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)#### More specific Types

-
[CDCPMDRecord](/CDCPMDRecord) -
[ContactPoint](/ContactPoint) -
[DefinedRegion](/DefinedRegion) -
[EngineSpecification](/EngineSpecification) -
[ExchangeRateSpecification](/ExchangeRateSpecification) -
[GeoCoordinates](/GeoCoordinates) -
[GeoShape](/GeoShape) -
[InstantaneousEvent](/InstantaneousEvent) -
[InteractionCounter](/InteractionCounter) -
[MonetaryAmount](/MonetaryAmount) -
[NutritionInformation](/NutritionInformation) -
[OfferShippingDetails](/OfferShippingDetails) -
[OpeningHoursSpecification](/OpeningHoursSpecification) -
[OrderItem](/OrderItem) -
[OwnershipInfo](/OwnershipInfo) -
[PostalCodeRangeSpecification](/PostalCodeRangeSpecification) -
[PriceSpecification](/PriceSpecification) -
[PropertyValue](/PropertyValue) -
[QuantitativeValue](/QuantitativeValue) -
[QuantitativeValueDistribution](/QuantitativeValueDistribution) -
[RepaymentSpecification](/RepaymentSpecification) -
[ServicePeriod](/ServicePeriod) -
[ShippingConditions](/ShippingConditions) -
[ShippingDeliveryTime](/ShippingDeliveryTime) -
[ShippingRateSettings](/ShippingRateSettings) -
[ShippingService](/ShippingService) -
[TypeAndQuantityNode](/TypeAndQuantityNode) -
[WarrantyPromise](/WarrantyPromise)
