---
title: "BusOrCoach"
source_url: https://schema.org/BusOrCoach
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# BusOrCoach

- Canonical URL: https://schema.org/BusOrCoach
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BusOrCoach)

A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury buses, usually in service for long distance travel.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[acrissCode](/acrissCode)

[Text](/Text)```
```[roofLoad](/roofLoad)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference) - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[Vehicle](/Vehicle)

```
```[accelerationTime](/accelerationTime)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): SEC for seconds

- Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue), or use[valueReference](/valueReference)with a[QuantitativeValue](/QuantitativeValue)of 0..60 mph or 0..100 km/h to specify the reference speeds.

```
```[bodyType](/bodyType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[callSign](/callSign)

[Text](/Text)[callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.```
```[cargoVolume](/cargoVolume)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): LTR for liters, FTQ for cubic foot/feet

Note: You can use

[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.```
```[dateVehicleFirstRegistered](/dateVehicleFirstRegistered)

[Date](/Date)```
```[driveWheelConfiguration](/driveWheelConfiguration)

[DriveWheelConfigurationValue](/DriveWheelConfigurationValue)or[Text](/Text)```
```[emissionsCO2](/emissionsCO2)

[Number](/Number)```
```[fuelCapacity](/fuelCapacity)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).

```
```[fuelConsumption](/fuelConsumption)

[QuantitativeValue](/QuantitativeValue)- Note 1: There are unfortunately no standard unit codes for liters per 100 km. Use
[unitText](/unitText)to indicate the unit of measurement, e.g. L/100 km. - Note 2: There are two ways of indicating the fuel consumption,
[fuelConsumption](/fuelConsumption)(e.g. 8 liters per 100 km) and[fuelEfficiency](/fuelEfficiency)(e.g. 30 miles per gallon). They are reciprocal. - Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use
[valueReference](/valueReference)to link the value for the fuel consumption to another value.

```
```[fuelEfficiency](/fuelEfficiency)

[QuantitativeValue](/QuantitativeValue)- Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use
[unitText](/unitText)to indicate the unit of measurement, e.g. mpg or km/L. - Note 2: There are two ways of indicating the fuel consumption,
[fuelConsumption](/fuelConsumption)(e.g. 8 liters per 100 km) and[fuelEfficiency](/fuelEfficiency)(e.g. 30 miles per gallon). They are reciprocal. - Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use
[valueReference](/valueReference)to link the value for the fuel economy to another value.

```
```[fuelType](/fuelType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[knownVehicleDamages](/knownVehicleDamages)

[Text](/Text)```
```[meetsEmissionStandard](/meetsEmissionStandard)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[mileageFromOdometer](/mileageFromOdometer)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KMT for kilometers, SMI for statute miles.

```
```[modelDate](/modelDate)

[Date](/Date)```
```[numberOfAirbags](/numberOfAirbags)

[Number](/Number)or[Text](/Text)```
```[numberOfAxles](/numberOfAxles)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62.

```
```[numberOfDoors](/numberOfDoors)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62.

```
```[numberOfForwardGears](/numberOfForwardGears)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62.

```
```[numberOfPreviousOwners](/numberOfPreviousOwners)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62.

```
```[payload](/payload)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of
[weight](/weight)and[payload](/payload) - Note 2: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 3: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 4: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

```
```[productionDate](/productionDate)

[Date](/Date)```
```[purchaseDate](/purchaseDate)

[Date](/Date)```
```[seatingCapacity](/seatingCapacity)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62 for persons.

```
```[speed](/speed)

[QuantitativeValue](/QuantitativeValue)[maxValue](/maxValue)) should be the maximum speed achievable under regular conditions.Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot

*Note 1: Use

[minValue](/minValue)and[maxValue](/maxValue)to indicate the range. Typically, the minimal value is zero. * Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the[valueReference](/valueReference)property.```
```[steeringPosition](/steeringPosition)

[SteeringPositionValue](/SteeringPositionValue)```
```[tongueWeight](/tongueWeight)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

```
```[trailerWeight](/trailerWeight)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KGM for kilogram, LBR for pound * Note 1: You can indicate additional information in the

[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. * Note 2: You may also link to a[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). * Note 3: Note that you can use[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.```
```[vehicleConfiguration](/vehicleConfiguration)

[Text](/Text)```
```[vehicleEngine](/vehicleEngine)

[EngineSpecification](/EngineSpecification)```
```[vehicleIdentificationNumber](/vehicleIdentificationNumber)

[Text](/Text)```
```[vehicleInteriorColor](/vehicleInteriorColor)

[Text](/Text)```
```[vehicleInteriorType](/vehicleInteriorType)

[Text](/Text)```
```[vehicleModelDate](/vehicleModelDate)

[Date](/Date)```
```[vehicleSeatingCapacity](/vehicleSeatingCapacity)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)Typical unit code(s): C62 for persons.

```
```[vehicleSpecialUsage](/vehicleSpecialUsage)

[CarUsageType](/CarUsageType)or[Text](/Text)```
```[vehicleTransmission](/vehicleTransmission)

[QualitativeValue](/QualitativeValue)or[Text](/Text)or[URL](/URL)```
```[weightTotal](/weightTotal)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

```
```[wheelbase](/wheelbase)

[QuantitativeValue](/QuantitativeValue)Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet.

[Product](/Product)

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[asin](/asin)

[Text](/Text)or[URL](/URL)[Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.

```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[color](/color)

[Text](/Text)```
```[colorSwatch](/colorSwatch)

[ImageObject](/ImageObject)or[URL](/URL)[Product](/Product). Should match the textual description specified in the[color](/color)property. This can be a URL or a fully described ImageObject.```
```[countryOfAssembly](/countryOfAssembly)

[Text](/Text)```
```[countryOfLastProcessing](/countryOfLastProcessing)

[Text](/Text)[Product](/Product)) was last processed and tested before importation.```
```[countryOfOrigin](/countryOfOrigin)

[Country](/Country)In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

```
```[depth](/depth)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[displayLocation](/displayLocation)

[Place](/Place)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
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
```[hasAdultConsideration](/hasAdultConsideration)

[AdultOrientedEnumeration](/AdultOrientedEnumeration)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasEnergyConsumptionDetails](/hasEnergyConsumptionDetails)

[EnergyConsumptionDetails](/EnergyConsumptionDetails)```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMeasurement](/hasMeasurement)

[QuantitativeValue](/QuantitativeValue)```
```[hasMerchantReturnPolicy](/hasMerchantReturnPolicy)

[MerchantReturnPolicy](/MerchantReturnPolicy)[hasProductReturnPolicy](/hasProductReturnPolicy).```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[inProductGroupWithID](/inProductGroupWithID)

[Text](/Text)[productGroupID](/productGroupID)for a[ProductGroup](/ProductGroup)that this product[isVariantOf](/isVariantOf).```
```[isAccessoryOrSparePartFor](/isAccessoryOrSparePartFor)

[Product](/Product)```
```[isConsumableFor](/isConsumableFor)

[Product](/Product)```
```[isFamilyFriendly](/isFamilyFriendly)

[Boolean](/Boolean)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[isVariantOf](/isVariantOf)

[ProductGroup](/ProductGroup)or[ProductModel](/ProductModel)[ProductModel](/ProductModel), this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a[ProductGroup](/ProductGroup), the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with[ProductGroup](/ProductGroup), this property can apply to any[Product](/Product)included in the group.Inverse property:

[hasVariant](/hasVariant)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[manufacturer](/manufacturer)

[Organization](/Organization)```
```[material](/material)

[Product](/Product)or[Text](/Text)or[URL](/URL)```
```[mobileUrl](/mobileUrl)

[Text](/Text)[mobileUrl](/mobileUrl)property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on

[Product](/Product)and[Offer](/Offer), rather than[Thing](/Thing). The general trend in web technology is towards[responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established[url](/url)property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all[url](/url)markup to use[mobileUrl](/mobileUrl)for more mobile-oriented pages. The property is intended for the case when items (primarily[Product](/Product)and[Offer](/Offer)) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.```
```[model](/model)

[ProductModel](/ProductModel)or[Text](/Text)```
```[mpn](/mpn)

[Text](/Text)```
```[negativeNotes](/negativeNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[positiveNotes](/positiveNotes)). For symmetryIn the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find[negativeNotes](/negativeNotes)used in this way. Nevertheless for the sake of symmetry,[negativeNotes](/negativeNotes)can be used on[Product](/Product).The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).

```
```[nsn](/nsn)

[Text](/Text)[NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)(nsn) of a[Product](/Product).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[pattern](/pattern)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[positiveNotes](/positiveNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

```
```[productID](/productID)

[Text](/Text)`meta itemprop="productID" content="isbn:123-456-789"`

.
```
```[productionDate](/productionDate)

[Date](/Date)```
```[purchaseDate](/purchaseDate)

[Date](/Date)```
```[releaseDate](/releaseDate)

[Date](/Date)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[size](/size)

[DefinedTerm](/DefinedTerm)or[QuantitativeValue](/QuantitativeValue)or[SizeSpecification](/SizeSpecification)or[Text](/Text)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.```
```[sku](/sku)

[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
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

[URL](/URL)### Acknowledgements

Automotive Ontology Working Group

[www.automotive-ontology.org](http://www.automotive-ontology.org)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.
