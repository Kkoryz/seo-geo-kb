---
title: "MerchantReturnPolicySeasonalOverride"
source_url: https://schema.org/MerchantReturnPolicySeasonalOverride
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MerchantReturnPolicySeasonalOverride

# MerchantReturnPolicySeasonalOverride

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/MerchantReturnPolicySeasonalOverride
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MerchantReturnPolicySeasonalOverride)

A seasonal override of a return policy, for example used for holidays.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[merchantReturnDays](/merchantReturnDays)

[Date](/Date)or[DateTime](/DateTime)or[Integer](/Integer)[returnPolicyCategory](/returnPolicyCategory)property is specified as[MerchantReturnFiniteReturnWindow](/MerchantReturnFiniteReturnWindow). Supersedes[productReturnDays](/productReturnDays).```
```[refundType](/refundType)

[RefundTypeEnumeration](/RefundTypeEnumeration)```
```[restockingFee](/restockingFee)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)[MonetaryAmount](/MonetaryAmount)to specify a fixed restocking fee for product returns, or use[Number](/Number)to specify a percentage of the product price paid by the customer.```
```[returnFees](/returnFees)

[ReturnFeesEnumeration](/ReturnFeesEnumeration)```
```[returnMethod](/returnMethod)

[ReturnMethodEnumeration](/ReturnMethodEnumeration)```
```[returnPolicyCategory](/returnPolicyCategory)

[MerchantReturnEnumeration](/MerchantReturnEnumeration)```
```[returnShippingFeesAmount](/returnShippingFeesAmount)

[MonetaryAmount](/MonetaryAmount)[returnFees](/returnFees)equals[ReturnShippingFees](/ReturnShippingFees).```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).[Thing](/Thing)

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

[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MerchantReturnPolicy](/MerchantReturnPolicy)#### Source

[https://github.com/schemaorg/schemaorg/issues/2880](https://github.com/schemaorg/schemaorg/issues/2880)
