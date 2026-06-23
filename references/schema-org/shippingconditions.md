---
title: "ShippingConditions"
source_url: https://schema.org/ShippingConditions
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ShippingConditions

# ShippingConditions

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ShippingConditions
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ShippingConditions)

ShippingConditions represent a set of constraints and information about the conditions of shipping a product. Such conditions may apply to only a subset of the products being shipped, depending on aspects of the product like weight, size, price, destination, and others. All the specified conditions must be met for this ShippingConditions to apply.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[depth](/depth)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[doesNotShip](/doesNotShip)

[Boolean](/Boolean)[shippingDestination](/shippingDestination)is not available.```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[numItems](/numItems)

[QuantitativeValue](/QuantitativeValue)```
```[orderValue](/orderValue)

[MonetaryAmount](/MonetaryAmount)```
```[seasonalOverride](/seasonalOverride)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[shippingDestination](/shippingDestination)

[DefinedRegion](/DefinedRegion)```
```[shippingOrigin](/shippingOrigin)

[DefinedRegion](/DefinedRegion)```
```[shippingRate](/shippingRate)

[MonetaryAmount](/MonetaryAmount)or[ShippingRateSettings](/ShippingRateSettings)[MonetaryAmount](/MonetaryAmount)) are most appropriate.```
```[transitTime](/transitTime)

[QuantitativeValue](/QuantitativeValue)or[ServicePeriod](/ServicePeriod)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), use the[QuantitativeValue](/QuantitativeValue). Typical properties: minValue, maxValue, unitCode (d for DAY).In the context of

[ShippingConditions](/ShippingConditions), use the[ServicePeriod](/ServicePeriod). It has a duration (as a[QuantitativeValue](/QuantitativeValue)) and also business days and a cut-off time.```
```[weight](/weight)

[Mass](/Mass)or[QuantitativeValue](/QuantitativeValue)```
```[width](/width)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)[Thing](/Thing)

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

[ShippingConditions](/ShippingConditions)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ShippingService](/ShippingService)[ShippingService](/ShippingService).| Supersedes |
|---|
```
``` |

#### Source

[https://github.com/schemaorg/schemaorg/issues/3617](https://github.com/schemaorg/schemaorg/issues/3617)
