---
title: "ShippingDeliveryTime"
source_url: https://schema.org/ShippingDeliveryTime
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ShippingDeliveryTime

# ShippingDeliveryTime

A Schema.org Type

- Canonical URL: https://schema.org/ShippingDeliveryTime
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ShippingDeliveryTime)

ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[businessDays](/businessDays)

[DayOfWeek](/DayOfWeek)or[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[cutoffTime](/cutoffTime)

[Time](/Time)[ShippingRateSettings](/ShippingRateSettings)publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).```
```[handlingTime](/handlingTime)

[QuantitativeValue](/QuantitativeValue)or[ServicePeriod](/ServicePeriod)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), Typical properties: minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.In the context of

[ShippingService](/ShippingService), use the[ServicePeriod](/ServicePeriod)format, that contains the same information in a structured form, with cut-off time, business days and duration.```
```[transitTime](/transitTime)

[QuantitativeValue](/QuantitativeValue)or[ServicePeriod](/ServicePeriod)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), use the[QuantitativeValue](/QuantitativeValue). Typical properties: minValue, maxValue, unitCode (d for DAY).In the context of

[ShippingConditions](/ShippingConditions), use the[ServicePeriod](/ServicePeriod). It has a duration (as a[QuantitativeValue](/QuantitativeValue)) and also business days and a cut-off time.[Thing](/Thing)

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

[ShippingDeliveryTime](/ShippingDeliveryTime)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[DeliveryTimeSettings](/DeliveryTimeSettings)or[OfferShippingDetails](/OfferShippingDetails)#### Source

[https://github.com/schemaorg/schemaorg/issues/2506](https://github.com/schemaorg/schemaorg/issues/2506)

### Examples

[Example 1](#eg-0392)

Copied

Example notes or example HTML without markup.

Offer shipping details example with nested delivery time(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "OfferShippingDetails", "deliveryTime": { "@type": "ShippingDeliveryTime", "businessDays": { "@type": "OpeningHoursSpecification", "dayOfWeek": [ "https://schema.org/Monday", "https://schema.org/Tuesday", "https://schema.org/Wednesday", "https://schema.org/Thursday", "https://schema.org/Friday" ] }, "cutoffTime": "12:00:15Z", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitCode": "d" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 10, "unitCode": "d" } }, "shippingRate": { "@type": "MonetaryAmount", "value": 4.95, "currency": "USD" } } </script>

Structured representation of the JSON-LD example.
