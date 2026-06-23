---
title: "ServicePeriod"
source_url: https://schema.org/ServicePeriod
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ServicePeriod

# ServicePeriod

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ServicePeriod
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ServicePeriod)

ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[businessDays](/businessDays)

[DayOfWeek](/DayOfWeek)or[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[cutoffTime](/cutoffTime)

[Time](/Time)[ShippingRateSettings](/ShippingRateSettings)publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).[Thing](/Thing)

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

[ServicePeriod](/ServicePeriod)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ShippingDeliveryTime](/ShippingDeliveryTime)or[ShippingService](/ShippingService)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), Typical properties: minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.In the context of

[ShippingService](/ShippingService), use the[ServicePeriod](/ServicePeriod)format, that contains the same information in a structured form, with cut-off time, business days and duration.[transitTime](/transitTime)

[ShippingConditions](/ShippingConditions)or[ShippingDeliveryTime](/ShippingDeliveryTime)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), use the[QuantitativeValue](/QuantitativeValue). Typical properties: minValue, maxValue, unitCode (d for DAY).In the context of

[ShippingConditions](/ShippingConditions), use the[ServicePeriod](/ServicePeriod). It has a duration (as a[QuantitativeValue](/QuantitativeValue)) and also business days and a cut-off time.#### Source

[https://github.com/schemaorg/schemaorg/issues/3617](https://github.com/schemaorg/schemaorg/issues/3617)
