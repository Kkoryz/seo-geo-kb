---
title: "DeliveryTimeSettings"
source_url: https://schema.org/DeliveryTimeSettings
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DeliveryTimeSettings

# DeliveryTimeSettings

A Schema.org Type


**Note:**This term has been[superseded](#supersededby).**Note:**This term has been

**from the vocabulary.**

[retired](docs/attic.home.html)- Canonical URL: https://schema.org/DeliveryTimeSettings
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DeliveryTimeSettings)

A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the

[shippingSettingsLink](/shippingSettingsLink)property of an[OfferShippingDetails](/OfferShippingDetails). Several occurrences can be published, distinguished (and identified/referenced) by their different values for[transitTimeLabel](/transitTimeLabel).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[deliveryTime](/deliveryTime)

[ShippingDeliveryTime](/ShippingDeliveryTime)```
```[isUnlabelledFallback](/isUnlabelledFallback)

[Boolean](/Boolean)[DeliveryTimeSettings](/DeliveryTimeSettings)or[ShippingRateSettings](/ShippingRateSettings)are intended to apply to all[OfferShippingDetails](/OfferShippingDetails)published by the same merchant, when referenced by a[shippingSettingsLink](/shippingSettingsLink)in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for[DeliveryTimeSettings](/DeliveryTimeSettings)) or shippingLabel (for[ShippingRateSettings](/ShippingRateSettings)), since this property is for use with unlabelled settings.```
```[shippingDestination](/shippingDestination)

[DefinedRegion](/DefinedRegion)[Thing](/Thing)

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

[URL](/URL)| SupersededBy |
|---|
```
``` |

#### Source

[https://github.com/schemaorg/schemaorg/issues/2506](https://github.com/schemaorg/schemaorg/issues/2506)
