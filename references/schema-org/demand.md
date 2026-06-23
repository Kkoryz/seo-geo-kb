---
title: "Demand"
source_url: https://schema.org/Demand
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Demand

# Demand

A Schema.org Type

- Canonical URL: https://schema.org/Demand
- Equivalent Class: unece:RequestForQuotation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Demand)

A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[acceptedPaymentMethod](/acceptedPaymentMethod)

[LoanOrCredit](/LoanOrCredit)or[PaymentMethod](/PaymentMethod)or[Text](/Text)```
```[advanceBookingRequirement](/advanceBookingRequirement)

[QuantitativeValue](/QuantitativeValue)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[asin](/asin)

[Text](/Text)or[URL](/URL)[Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.

```
```[availability](/availability)

[ItemAvailability](/ItemAvailability)```
```[availabilityEnds](/availabilityEnds)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[availabilityStarts](/availabilityStarts)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[availableAtOrFrom](/availableAtOrFrom)

[Place](/Place)```
```[availableDeliveryMethod](/availableDeliveryMethod)

[DeliveryMethod](/DeliveryMethod)```
```[businessFunction](/businessFunction)

[BusinessFunction](/BusinessFunction)```
```[deliveryLeadTime](/deliveryLeadTime)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleCustomerType](/eligibleCustomerType)

[BusinessEntityType](/BusinessEntityType)```
```[eligibleDuration](/eligibleDuration)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleQuantity](/eligibleQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleRegion](/eligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[ineligibleRegion](/ineligibleRegion).```
```[eligibleTransactionVolume](/eligibleTransactionVolume)

[PriceSpecification](/PriceSpecification)```
```[gtin](/gtin)

[Text](/Text)or[URL](/URL)[GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.A correct

[gtin](/gtin)value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a[valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)and meet the other rules for valid GTINs. See also[GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)and[Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number)for more details. Left-padding of the gtin values is not required or encouraged. The[gtin](/gtin)property generalizes the earlier[gtin8](/gtin8),[gtin12](/gtin12),[gtin13](/gtin13), and[gtin14](/gtin14)properties.The GS1

[digital link specifications](https://www.gs1.org/standards/Digital-Link/)expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the[hasGS1DigitalLink](/hasGS1DigitalLink)attribute.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

```
```[gtin12](/gtin12)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin13](/gtin13)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin14](/gtin14)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin8](/gtin8)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[includesObject](/includesObject)

[TypeAndQuantityNode](/TypeAndQuantityNode)[Offer](/Offer)or[ProductCollection](/ProductCollection).```
```[ineligibleRegion](/ineligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[eligibleRegion](/eligibleRegion).```
```[inventoryLevel](/inventoryLevel)

[QuantitativeValue](/QuantitativeValue)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[itemOffered](/itemOffered)

[AggregateOffer](/AggregateOffer)or[CreativeWork](/CreativeWork)or[Event](/Event)or[MenuItem](/MenuItem)or[Product](/Product)or[Service](/Service)or[Trip](/Trip)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[offers](/offers)```
```[mpn](/mpn)

[Text](/Text)```
```[priceSpecification](/priceSpecification)

[PriceSpecification](/PriceSpecification)```
```[seller](/seller)

[Organization](/Organization)or[Person](/Person)[vendor](/vendor),[merchant](/merchant).```
```[serialNumber](/serialNumber)

[Text](/Text)```
```[sku](/sku)

[Text](/Text)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[warranty](/warranty)

[WarrantyPromise](/WarrantyPromise)[warrantyPromise](/warrantyPromise).[Thing](/Thing)

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

[Demand](/Demand)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[AggregateOffer](/AggregateOffer)or[CreativeWork](/CreativeWork)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[Event](/Event)or[MenuItem](/MenuItem)or[Product](/Product)or[Service](/Service)or[Trip](/Trip)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.[seeks](/seeks)
