---
title: "MerchantReturnPolicy"
source_url: https://schema.org/MerchantReturnPolicy
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MerchantReturnPolicy

# MerchantReturnPolicy

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/MerchantReturnPolicy
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MerchantReturnPolicy)

A MerchantReturnPolicy provides information about product return policies associated with an

[Organization](/Organization),[Product](/Product), or[Offer](/Offer).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[applicableCountry](/applicableCountry)

[Country](/Country)or[Text](/Text)```
```[customerRemorseReturnFees](/customerRemorseReturnFees)

[ReturnFeesEnumeration](/ReturnFeesEnumeration)```
```[customerRemorseReturnLabelSource](/customerRemorseReturnLabelSource)

[ReturnLabelSourceEnumeration](/ReturnLabelSourceEnumeration)```
```[customerRemorseReturnShippingFeesAmount](/customerRemorseReturnShippingFeesAmount)

[MonetaryAmount](/MonetaryAmount)[customerRemorseReturnFees](/customerRemorseReturnFees)equals[ReturnShippingFees](/ReturnShippingFees).```
```[inStoreReturnsOffered](/inStoreReturnsOffered)

[Boolean](/Boolean)[returnMethod](/returnMethod)property.)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[itemDefectReturnFees](/itemDefectReturnFees)

[ReturnFeesEnumeration](/ReturnFeesEnumeration)```
```[itemDefectReturnLabelSource](/itemDefectReturnLabelSource)

[ReturnLabelSourceEnumeration](/ReturnLabelSourceEnumeration)```
```[itemDefectReturnShippingFeesAmount](/itemDefectReturnShippingFeesAmount)

[MonetaryAmount](/MonetaryAmount)[itemDefectReturnFees](/itemDefectReturnFees)equals[ReturnShippingFees](/ReturnShippingFees).```
```[merchantReturnDays](/merchantReturnDays)

[Date](/Date)or[DateTime](/DateTime)or[Integer](/Integer)[returnPolicyCategory](/returnPolicyCategory)property is specified as[MerchantReturnFiniteReturnWindow](/MerchantReturnFiniteReturnWindow). Supersedes[productReturnDays](/productReturnDays).```
```[merchantReturnLink](/merchantReturnLink)

[URL](/URL)[productReturnLink](/productReturnLink).```
```[refundType](/refundType)

[RefundTypeEnumeration](/RefundTypeEnumeration)```
```[restockingFee](/restockingFee)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)[MonetaryAmount](/MonetaryAmount)to specify a fixed restocking fee for product returns, or use[Number](/Number)to specify a percentage of the product price paid by the customer.```
```[returnFees](/returnFees)

[ReturnFeesEnumeration](/ReturnFeesEnumeration)```
```[returnLabelSource](/returnLabelSource)

[ReturnLabelSourceEnumeration](/ReturnLabelSourceEnumeration)```
```[returnMethod](/returnMethod)

[ReturnMethodEnumeration](/ReturnMethodEnumeration)```
```[returnPolicyCategory](/returnPolicyCategory)

[MerchantReturnEnumeration](/MerchantReturnEnumeration)```
```[returnPolicyCountry](/returnPolicyCountry)

[Country](/Country)or[Text](/Text)[name](/name)property of[Country](/Country). You can also provide the two-letter[ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this can be different from the country where the product was originally shipped from or sent to.```
```[returnPolicySeasonalOverride](/returnPolicySeasonalOverride)

[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)```
```[returnShippingFeesAmount](/returnShippingFeesAmount)

[MonetaryAmount](/MonetaryAmount)[returnFees](/returnFees)equals[ReturnShippingFees](/ReturnShippingFees).```
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

[MerchantReturnPolicy](/MerchantReturnPolicy)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Offer](/Offer)or[Organization](/Organization)or[Product](/Product)| Supersedes |
|---|
```
``` |

#### Source

[https://github.com/schemaorg/schemaorg/issues/2288](https://github.com/schemaorg/schemaorg/issues/2288)
