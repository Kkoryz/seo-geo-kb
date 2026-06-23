---
title: "OfferShippingDetails"
source_url: https://schema.org/OfferShippingDetails
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# OfferShippingDetails

# OfferShippingDetails

A Schema.org Type

- Canonical URL: https://schema.org/OfferShippingDetails
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+OfferShippingDetails)

OfferShippingDetails represents information about shipping destinations.


Multiple of these entities can be used to represent different shipping rates for different destinations:


One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.


Multiple of these entities can be used to represent different shipping costs and delivery times.


Two entities that are identical but differ in rate and time:


E.g. Cheaper and slower: $5 in 5-7 days or Fast and expensive: $15 in 1-2 days.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

E.g. Cheaper and slower: $5 in 5-7 days or Fast and expensive: $15 in 1-2 days.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[deliveryTime](/deliveryTime)

[ShippingDeliveryTime](/ShippingDeliveryTime)```
```[depth](/depth)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[doesNotShip](/doesNotShip)

[Boolean](/Boolean)[shippingDestination](/shippingDestination)is not available.```
```[hasShippingService](/hasShippingService)

[ShippingService](/ShippingService)```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[shippingDestination](/shippingDestination)

[DefinedRegion](/DefinedRegion)```
```[shippingOrigin](/shippingOrigin)

[DefinedRegion](/DefinedRegion)```
```[shippingRate](/shippingRate)

[MonetaryAmount](/MonetaryAmount)or[ShippingRateSettings](/ShippingRateSettings)[MonetaryAmount](/MonetaryAmount)) are most appropriate.```
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)```
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

[OfferShippingDetails](/OfferShippingDetails)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Offer](/Offer)[Offer](/Offer).#### Source

[https://github.com/schemaorg/schemaorg/issues/2506](https://github.com/schemaorg/schemaorg/issues/2506)

### Examples

[Example 1](#eg-0392)

Copied

Example notes or example HTML without markup.

Offer shipping details example with nested delivery time(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "OfferShippingDetails", "deliveryTime": { "@type": "ShippingDeliveryTime", "businessDays": { "@type": "OpeningHoursSpecification", "dayOfWeek": [ "https://schema.org/Monday", "https://schema.org/Tuesday", "https://schema.org/Wednesday", "https://schema.org/Thursday", "https://schema.org/Friday" ] }, "cutoffTime": "12:00:15Z", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitCode": "d" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 10, "unitCode": "d" } }, "shippingRate": { "@type": "MonetaryAmount", "value": 4.95, "currency": "USD" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-3617a)

Copied

Example notes or example HTML without markup.

Offer with free shipping in the US and Canada (in the V2 Shipping format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "0.3 m", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "shippingRate": "0" } } } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-3617c)

Copied

Example notes or example HTML without markup.

Offer with shipping costs of $10 + $1/kg for orders $35-$200, to the US and Canada, with a handling time of 3.5 hours on weekdays (in the V2 format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "300 mm", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "handlingTime": { "@type": "ServicePeriod", "cutoffTime": "14:30:00-07:00", "duration": { "@type": "QuantitativeValue", "maxValue": "30", "unitCode": "min" } }, "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "orderValue": { "@type": "MonetaryAmount", "minValue": "35", "maxValue": "200" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "10", "currency": "USD" }, "weightPercentage": "1.0" }, "transitTime": { "@type": "ServicePeriod", "duration": { "maxValue": "3.5", "unitCode": "h" }, "businessDays": [ { "dayOfWeek": "Monday" }, { "dayOfWeek": "Tuesday" }, { "dayOfWeek": "Wednesday" }, { "dayOfWeek": "Thursday" }, { "dayOfWeek": "Friday" } ] } } } } } } </script>

Structured representation of the JSON-LD example.
