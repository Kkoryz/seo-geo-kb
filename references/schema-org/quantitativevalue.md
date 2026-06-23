---
title: "QuantitativeValue"
source_url: https://schema.org/QuantitativeValue
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# QuantitativeValue

# QuantitativeValue

A Schema.org Type

- Canonical URL: https://schema.org/QuantitativeValue
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+QuantitativeValue)

A point value or interval for product characteristics and other purposes.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[maxValue](/maxValue)

[Number](/Number)```
```[minValue](/minValue)

[Number](/Number)```
```[unitCode](/unitCode)

[Text](/Text)or[URL](/URL)```
```[unitText](/unitText)

[Text](/Text)[unitCode](unitCode).```
```[value](/value)

[Boolean](/Boolean)or[Number](/Number)or[StructuredValue](/StructuredValue)or[Text](/Text)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[valueReference](/valueReference)

[DefinedTerm](/DefinedTerm)or[Enumeration](/Enumeration)or[MeasurementTypeEnumeration](/MeasurementTypeEnumeration)or[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)or[StructuredValue](/StructuredValue)or[Text](/Text)[Thing](/Thing)

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

[QuantitativeValue](/QuantitativeValue)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Vehicle](/Vehicle)Typical unit code(s): SEC for seconds

- Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue), or use[valueReference](/valueReference)with a[QuantitativeValue](/QuantitativeValue)of 0..60 mph or 0..100 km/h to specify the reference speeds.

[activityDuration](/activityDuration)

[ExercisePlan](/ExercisePlan)[activityFrequency](/activityFrequency)

[ExercisePlan](/ExercisePlan)[advanceBookingRequirement](/advanceBookingRequirement)

[Demand](/Demand)or[Offer](/Offer)[annualPercentageRate](/annualPercentageRate)

[FinancialProduct](/FinancialProduct)[billingDuration](/billingDuration)

[UnitPriceSpecification](/UnitPriceSpecification)[broadcastFrequencyValue](/broadcastFrequencyValue)

[BroadcastFrequencySpecification](/BroadcastFrequencySpecification)[cargoVolume](/cargoVolume)

[Vehicle](/Vehicle)Typical unit code(s): LTR for liters, FTQ for cubic foot/feet

Note: You can use

[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.[deliveryLeadTime](/deliveryLeadTime)

[Demand](/Demand)or[Offer](/Offer)[depth](/depth)

[OfferShippingDetails](/OfferShippingDetails)or[Product](/Product)or[ShippingConditions](/ShippingConditions)or[VisualArtwork](/VisualArtwork)[duration](/duration)

[Audiobook](/Audiobook)or[Episode](/Episode)or[Event](/Event)or[MediaObject](/MediaObject)or[Movie](/Movie)or[MusicRecording](/MusicRecording)or[MusicRelease](/MusicRelease)or[QuantitativeValueDistribution](/QuantitativeValueDistribution)or[Schedule](/Schedule)or[ServicePeriod](/ServicePeriod)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).[durationOfWarranty](/durationOfWarranty)

[WarrantyPromise](/WarrantyPromise)[eligibleDuration](/eligibleDuration)

[Demand](/Demand)or[Offer](/Offer)[eligibleQuantity](/eligibleQuantity)

[Demand](/Demand)or[Offer](/Offer)or[PriceSpecification](/PriceSpecification)[engineDisplacement](/engineDisplacement)

[EngineSpecification](/EngineSpecification)Typical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches * Note 1: You can link to information about how the given value has been determined using the

[valueReference](/valueReference)property. * Note 2: You can use[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.[enginePower](/enginePower)

[EngineSpecification](/EngineSpecification)- Note 1: There are many different ways of measuring an engine's power. For an overview, see
[http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes). - Note 2: You can link to information about how the given value has been determined using the
[valueReference](/valueReference)property. - Note 3: You can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[floorSize](/floorSize)

[Accommodation](/Accommodation)or[FloorPlan](/FloorPlan)[fuelCapacity](/fuelCapacity)

[Vehicle](/Vehicle)Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).

[fuelConsumption](/fuelConsumption)

[Vehicle](/Vehicle)- Note 1: There are unfortunately no standard unit codes for liters per 100 km. Use
[unitText](/unitText)to indicate the unit of measurement, e.g. L/100 km. - Note 2: There are two ways of indicating the fuel consumption,
[fuelConsumption](/fuelConsumption)(e.g. 8 liters per 100 km) and[fuelEfficiency](/fuelEfficiency)(e.g. 30 miles per gallon). They are reciprocal. - Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use
[valueReference](/valueReference)to link the value for the fuel consumption to another value.

[fuelEfficiency](/fuelEfficiency)

[Vehicle](/Vehicle)- Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use
[unitText](/unitText)to indicate the unit of measurement, e.g. mpg or km/L. - Note 2: There are two ways of indicating the fuel consumption,
[fuelConsumption](/fuelConsumption)(e.g. 8 liters per 100 km) and[fuelEfficiency](/fuelEfficiency)(e.g. 30 miles per gallon). They are reciprocal. - Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use
[valueReference](/valueReference)to link the value for the fuel economy to another value.

[handlingTime](/handlingTime)

[ShippingDeliveryTime](/ShippingDeliveryTime)or[ShippingService](/ShippingService)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), Typical properties: minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.In the context of

[ShippingService](/ShippingService), use the[ServicePeriod](/ServicePeriod)format, that contains the same information in a structured form, with cut-off time, business days and duration.[hasMeasurement](/hasMeasurement)

[Certification](/Certification)or[Offer](/Offer)or[Product](/Product)or[SizeSpecification](/SizeSpecification)[height](/height)

[MediaObject](/MediaObject)or[OfferShippingDetails](/OfferShippingDetails)or[Person](/Person)or[Product](/Product)or[ShippingConditions](/ShippingConditions)or[VisualArtwork](/VisualArtwork)[incentiveAmount](/incentiveAmount)

[FinancialIncentive](/FinancialIncentive)[QuantitativeValue](/QuantitativeValue): Use this for incentives based on price (either raw amount or percentage-based). For a raw amount example, "You can claim $2,500 - $7,500 from the total cost of installation" would be represented as the following:```
{
"@type": "QuantitativeValue",
“minValue”: 2500,
“maxValue”: 7500,
"unitCode": "USD"
}
```


[QuantitativeValue](/QuantitativeValue)can also be used for percentage amounts. In such cases, value is used to represent the incentive’s percentage, while maxValue represents a limit (if one exists) to that incentive. The unitCode should be 'P1' and the unitText should be '%', while valueReference should be used for holding the currency type. For example, "You can claim up to 30% of the total cost of installation, up to a maximum of $7,500" would be:```
{
"@type": "QuantitativeValue",
"value": 30,
"unitCode": "P1",
"unitText": "%",
“maxValue”: 7500,
“valueReference”: “USD”
}
```


[UnitPriceSpecification](/UnitPriceSpecification): Use this for incentives that are based on amounts rather than price. For example, a net metering rebate that pays $10/kWh, up to $1,000:```
{
"@type": "UnitPriceSpecification",
"price": 10,
"priceCurrency": "USD",
"referenceQuantity": 1,
"unitCode": "DO3",
"unitText": "kw/h",
"maxPrice": 1000,
"description": "$10 / kwh up to $1000"
}
```


[LoanOrCredit](/LoanOrCredit): Use for incentives that are loan based. For example, a loan of $4,000 - $50,000 with a repayment term of 10 years, interest free would look like:```
{
"@type": "LoanOrCredit",
"loanTerm": {
"@type":"QuantitativeValue",
"value":"10",
"unitCode": "ANN"
},
"amount":[
{
"@type": "QuantitativeValue",
"Name":"fixed interest rate",
"value":"0",
},
],
"amount":[
{
"@type": "MonetaryAmount",
"Name":"min loan amount",
"value":"4000",
"currency":"CAD"
},
{
"@type": "MonetaryAmount",
"Name":"max loan amount",
"value":"50000",
"currency":"CAD"
}
],
}
```


In summary: - Use
[QuantitativeValue](/QuantitativeValue)for absolute/percentage-based incentives applied on the price of a good/service. - Use
[UnitPriceSpecification](/UnitPriceSpecification)for incentives based on a per-unit basis (e.g. net metering). - Use
[LoanOrCredit](/LoanOrCredit)for loans/credits.

[intensity](/intensity)

[ExercisePlan](/ExercisePlan)[interestRate](/interestRate)

[FinancialProduct](/FinancialProduct)[inventoryLevel](/inventoryLevel)

[Demand](/Demand)or[Offer](/Offer)or[SomeProducts](/SomeProducts)[jobDuration](/jobDuration)

[JobPosting](/JobPosting)[leaseLength](/leaseLength)

[Accommodation](/Accommodation)or[Offer](/Offer)or[RealEstateListing](/RealEstateListing)[Accommodation](/Accommodation), either particular to some[Offer](/Offer)or in some cases intrinsic to the property.[loanTerm](/loanTerm)

[LoanOrCredit](/LoanOrCredit)[marginOfError](/marginOfError)

[Observation](/Observation)[marginOfError](/marginOfError)for an[Observation](/Observation).[materialExtent](/materialExtent)

[CreativeWork](/CreativeWork)[membershipPointsEarned](/membershipPointsEarned)

[MemberProgramTier](/MemberProgramTier)or[PriceSpecification](/PriceSpecification)or[ProgramMembership](/ProgramMembership)[mileageFromOdometer](/mileageFromOdometer)

[Vehicle](/Vehicle)Typical unit code(s): KMT for kilometers, SMI for statute miles.

[molecularWeight](/molecularWeight)

[MolecularEntity](/MolecularEntity)[monoisotopicMolecularWeight](/monoisotopicMolecularWeight)

[MolecularEntity](/MolecularEntity)[numAdults](/numAdults)

[LodgingReservation](/LodgingReservation)[numChildren](/numChildren)

[LodgingReservation](/LodgingReservation)[numItems](/numItems)

[ShippingConditions](/ShippingConditions)[numberOfAccommodationUnits](/numberOfAccommodationUnits)

[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan)[ApartmentComplex](/ApartmentComplex), or the number of accommodation units for a specific[FloorPlan](/FloorPlan)(within its specific[ApartmentComplex](/ApartmentComplex)). See also[numberOfAvailableAccommodationUnits](/numberOfAvailableAccommodationUnits).[numberOfAvailableAccommodationUnits](/numberOfAvailableAccommodationUnits)

[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan)[ApartmentComplex](/ApartmentComplex), or the number of accommodation units for a specific[FloorPlan](/FloorPlan)(within its specific[ApartmentComplex](/ApartmentComplex)). See also[numberOfAccommodationUnits](/numberOfAccommodationUnits).[numberOfAxles](/numberOfAxles)

[Vehicle](/Vehicle)Typical unit code(s): C62.

[numberOfBedrooms](/numberOfBedrooms)

[Accommodation](/Accommodation)or[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan)[Accommodation](/Accommodation),[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan).[numberOfDoors](/numberOfDoors)

[Vehicle](/Vehicle)Typical unit code(s): C62.

[numberOfEmployees](/numberOfEmployees)

[BusinessAudience](/BusinessAudience)or[Organization](/Organization)[numberOfForwardGears](/numberOfForwardGears)

[Vehicle](/Vehicle)Typical unit code(s): C62.

[numberOfPlayers](/numberOfPlayers)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[numberOfPreviousOwners](/numberOfPreviousOwners)

[Vehicle](/Vehicle)Typical unit code(s): C62.

[numberOfRooms](/numberOfRooms)

[Accommodation](/Accommodation)or[Apartment](/Apartment)or[FloorPlan](/FloorPlan)or[House](/House)or[LodgingBusiness](/LodgingBusiness)or[SingleFamilyResidence](/SingleFamilyResidence)or[Suite](/Suite)[occupancy](/occupancy)

[Accommodation](/Accommodation)or[Apartment](/Apartment)or[HotelRoom](/HotelRoom)or[SingleFamilyResidence](/SingleFamilyResidence)or[Suite](/Suite)[orderQuantity](/orderQuantity)

[OrderItem](/OrderItem)[partySize](/partySize)

[FoodEstablishmentReservation](/FoodEstablishmentReservation)or[TaxiReservation](/TaxiReservation)[payload](/payload)

[Vehicle](/Vehicle)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of
[weight](/weight)and[payload](/payload) - Note 2: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 3: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 4: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[recipeYield](/recipeYield)

[Recipe](/Recipe)[referenceQuantity](/referenceQuantity)

[UnitPriceSpecification](/UnitPriceSpecification)[repetitions](/repetitions)

[ExercisePlan](/ExercisePlan)[requiredQuantity](/requiredQuantity)

[HowToItem](/HowToItem)[restPeriods](/restPeriods)

[ExercisePlan](/ExercisePlan)[roofLoad](/roofLoad)

[BusOrCoach](/BusOrCoach)or[Car](/Car)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference) - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[seatingCapacity](/seatingCapacity)

[Vehicle](/Vehicle)Typical unit code(s): C62 for persons.

[size](/size)

[CreativeWork](/CreativeWork)or[Product](/Product)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.[speed](/speed)

[Vehicle](/Vehicle)[maxValue](/maxValue)) should be the maximum speed achievable under regular conditions.Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot

*Note 1: Use

[minValue](/minValue)and[maxValue](/maxValue)to indicate the range. Typically, the minimal value is zero. * Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the[valueReference](/valueReference)property.[stupidProperty](/stupidProperty)

[StupidType](/StupidType)or[Vehicle](/Vehicle)[suggestedAge](/suggestedAge)

[PeopleAudience](/PeopleAudience)or[SizeSpecification](/SizeSpecification)[suggestedMeasurement](/suggestedMeasurement)

[PeopleAudience](/PeopleAudience)or[SizeSpecification](/SizeSpecification)[tongueWeight](/tongueWeight)

[Vehicle](/Vehicle)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[torque](/torque)

[EngineSpecification](/EngineSpecification)Typical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch

- Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the
[valueReference](/valueReference)property. - Note 2: You can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[trailerWeight](/trailerWeight)

[Vehicle](/Vehicle)Typical unit code(s): KGM for kilogram, LBR for pound * Note 1: You can indicate additional information in the

[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. * Note 2: You may also link to a[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). * Note 3: Note that you can use[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.[transitTime](/transitTime)

[ShippingConditions](/ShippingConditions)or[ShippingDeliveryTime](/ShippingDeliveryTime)In the context of

[ShippingDeliveryTime](/ShippingDeliveryTime), use the[QuantitativeValue](/QuantitativeValue). Typical properties: minValue, maxValue, unitCode (d for DAY).In the context of

[ShippingConditions](/ShippingConditions), use the[ServicePeriod](/ServicePeriod). It has a duration (as a[QuantitativeValue](/QuantitativeValue)) and also business days and a cut-off time.[valueReference](/valueReference)

[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)[vehicleSeatingCapacity](/vehicleSeatingCapacity)

[Vehicle](/Vehicle)Typical unit code(s): C62 for persons.

[weight](/weight)

[OfferShippingDetails](/OfferShippingDetails)or[Person](/Person)or[Product](/Product)or[ShippingConditions](/ShippingConditions)or[VisualArtwork](/VisualArtwork)[weightTotal](/weightTotal)

[Vehicle](/Vehicle)Typical unit code(s): KGM for kilogram, LBR for pound

- Note 1: You can indicate additional information in the
[name](/name)of the[QuantitativeValue](/QuantitativeValue)node. - Note 2: You may also link to a
[QualitativeValue](/QualitativeValue)node that provides additional information using[valueReference](/valueReference). - Note 3: Note that you can use
[minValue](/minValue)and[maxValue](/maxValue)to indicate ranges.

[wheelbase](/wheelbase)

[Vehicle](/Vehicle)Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet.

[width](/width)

[MediaObject](/MediaObject)or[OfferShippingDetails](/OfferShippingDetails)or[Product](/Product)or[ShippingConditions](/ShippingConditions)or[VisualArtwork](/VisualArtwork)[workload](/workload)

[ExercisePlan](/ExercisePlan)[yearlyRevenue](/yearlyRevenue)

[BusinessAudience](/BusinessAudience)[yearsInOperation](/yearsInOperation)

[BusinessAudience](/BusinessAudience)[yield](/yield)
