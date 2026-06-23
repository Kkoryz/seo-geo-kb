---
title: "ShippingService"
source_url: https://schema.org/ShippingService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ShippingService

# ShippingService

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ShippingService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ShippingService)

ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[fulfillmentType](/fulfillmentType)

[FulfillmentTypeEnumeration](/FulfillmentTypeEnumeration)[ShippingService](/ShippingService).```
```[handlingTime](/handlingTime)

[QuantitativeValue](/QuantitativeValue)or[ServicePeriod](/ServicePeriod)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), Typical properties: minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.In the context of

[ShippingService](/ShippingService), use the[ServicePeriod](/ServicePeriod)format, that contains the same information in a structured form, with cut-off time, business days and duration.```
```[shippingConditions](/shippingConditions)

[ShippingConditions](/ShippingConditions)[ShippingService](/ShippingService).```
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)[Thing](/Thing)

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

[ShippingService](/ShippingService)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[OfferShippingDetails](/OfferShippingDetails)or[Organization](/Organization)#### Source

[https://github.com/schemaorg/schemaorg/issues/3617](https://github.com/schemaorg/schemaorg/issues/3617)

### Examples

[Example 1](#eg-3617a)

Copied

Example notes or example HTML without markup.

Offer with free shipping in the US and Canada (in the V2 Shipping format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "0.3 m", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "shippingRate": "0" } } } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-3617b)

Copied

Example notes or example HTML without markup.

Organization with free shipping worldwide for members (in the V2 Shipping format) and paid shipping for non-members.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Organization", "name": "Example Inc.", "hasShippingService": [ { "@type": "ShippingService", "name": "Members Free Shipping", "description": "Free shipping worldwide for Gold and Platinum members.", "validForMemberTier": [ { "@id": "https://www.example.com/membership-plus#tier_gold" }, { "@id": "https://www.example.com/membership-plus#tier_platinum" } ], "shippingConditions": { "@type": "ShippingConditions", "shippingRate": "0" } }, { "@type": "ShippingService", "name": "Standard Shipping", "description": "Flat-fee worldwide shipping.", "shippingConditions": { "@type": "ShippingConditions", "shippingRate": { "@type": "MonetaryAmount", "value": "9.99", "currency": "USD" } } } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-3617c)

Copied

Example notes or example HTML without markup.

Offer with shipping costs of $10 + $1/kg for orders $35-$200, to the US and Canada, with a handling time of 3.5 hours on weekdays (in the V2 format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "300 mm", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "handlingTime": { "@type": "ServicePeriod", "cutoffTime": "14:30:00-07:00", "duration": { "@type": "QuantitativeValue", "maxValue": "30", "unitCode": "min" } }, "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "orderValue": { "@type": "MonetaryAmount", "minValue": "35", "maxValue": "200" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "10", "currency": "USD" }, "weightPercentage": "1.0" }, "transitTime": { "@type": "ServicePeriod", "duration": { "maxValue": "3.5", "unitCode": "h" }, "businessDays": [ { "dayOfWeek": "Monday" }, { "dayOfWeek": "Tuesday" }, { "dayOfWeek": "Wednesday" }, { "dayOfWeek": "Thursday" }, { "dayOfWeek": "Friday" } ] } } } } } } </script>

Structured representation of the JSON-LD example.
