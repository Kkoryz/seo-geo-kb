---
title: "FloorPlan"
source_url: https://schema.org/FloorPlan
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# FloorPlan

# FloorPlan

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/FloorPlan
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+FloorPlan)

A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some

[ApartmentComplex](/ApartmentComplex)has an[accommodationFloorPlan](/accommodationFloorPlan)which is a[FloorPlan](/FloorPlan). A FloorPlan is always in the context of a particular place, either a larger[ApartmentComplex](/ApartmentComplex)or a single[Apartment](/Apartment). The visual/spatial aspects of a floor plan (i.e. room layout,[see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using[image](/image).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[amenityFeature](/amenityFeature)

[LocationFeatureSpecification](/LocationFeatureSpecification)```
```[floorSize](/floorSize)

[QuantitativeValue](/QuantitativeValue)```
```[isPlanForApartment](/isPlanForApartment)

[Accommodation](/Accommodation)```
```[layoutImage](/layoutImage)

[ImageObject](/ImageObject)or[URL](/URL)```
```[numberOfAccommodationUnits](/numberOfAccommodationUnits)

[QuantitativeValue](/QuantitativeValue)[ApartmentComplex](/ApartmentComplex), or the number of accommodation units for a specific[FloorPlan](/FloorPlan)(within its specific[ApartmentComplex](/ApartmentComplex)). See also[numberOfAvailableAccommodationUnits](/numberOfAvailableAccommodationUnits).```
```[numberOfAvailableAccommodationUnits](/numberOfAvailableAccommodationUnits)

[QuantitativeValue](/QuantitativeValue)[ApartmentComplex](/ApartmentComplex), or the number of accommodation units for a specific[FloorPlan](/FloorPlan)(within its specific[ApartmentComplex](/ApartmentComplex)). See also[numberOfAccommodationUnits](/numberOfAccommodationUnits).```
```[numberOfBathroomsTotal](/numberOfBathroomsTotal)

[Integer](/Integer)[Accommodation](/Accommodation), following real estate conventions as[documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also[numberOfRooms](/numberOfRooms).```
```[numberOfBedrooms](/numberOfBedrooms)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)[Accommodation](/Accommodation),[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan).```
```[numberOfFullBathrooms](/numberOfFullBathrooms)

[Number](/Number)[Accommodation](/Accommodation). This corresponds to the[BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).```
```[numberOfPartialBathrooms](/numberOfPartialBathrooms)

[Number](/Number)[Accommodation](/Accommodation). This corresponds to the[BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).```
```[numberOfRooms](/numberOfRooms)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[petsAllowed](/petsAllowed)

[Boolean](/Boolean)or[Text](/Text)[Thing](/Thing)

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

[FloorPlan](/FloorPlan)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Accommodation](/Accommodation)or[Residence](/Residence)[Accommodation](/Accommodation).#### Source

[https://github.com/schemaorg/schemaorg/issues/2373](https://github.com/schemaorg/schemaorg/issues/2373)
