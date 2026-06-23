---
title: "Accommodation"
source_url: https://schema.org/Accommodation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Accommodation

# Accommodation

A Schema.org Type

- Canonical URL: https://schema.org/Accommodation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Accommodation)

An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
For more specific types of accommodations not defined in schema.org, one can use


See also the

[additionalType](/additionalType)with external vocabularies.See also the

[dedicated document on the use of schema.org for marking up hotels and other forms of accommodations](/docs/hotels.html).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[accommodationCategory](/accommodationCategory)

[Text](/Text)[Accommodation](/Accommodation), following real estate conventions, e.g. RESO (see[PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and[PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field)fields for suggested values).```
```[accommodationFloorPlan](/accommodationFloorPlan)

[FloorPlan](/FloorPlan)[Accommodation](/Accommodation).```
```[amenityFeature](/amenityFeature)

[LocationFeatureSpecification](/LocationFeatureSpecification)```
```[bed](/bed)

[BedDetails](/BedDetails)or[BedType](/BedType)or[Text](/Text)```
```[floorLevel](/floorLevel)

[Text](/Text)[Accommodation](/Accommodation)in a multi-storey building. Since counting systems[vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.```
```[floorSize](/floorSize)

[QuantitativeValue](/QuantitativeValue)```
```[leaseLength](/leaseLength)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[Accommodation](/Accommodation), either particular to some[Offer](/Offer)or in some cases intrinsic to the property.```
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
```[occupancy](/occupancy)

[QuantitativeValue](/QuantitativeValue)```
```[permittedUsage](/permittedUsage)

[Text](/Text)```
```[petsAllowed](/petsAllowed)

[Boolean](/Boolean)or[Text](/Text)```
```[tourBookingPage](/tourBookingPage)

[URL](/URL)[Place](/Place), such as an[Accommodation](/Accommodation)or[ApartmentComplex](/ApartmentComplex)in a real estate setting, as well as other kinds of tours as appropriate.```
```[yearBuilt](/yearBuilt)

[Number](/Number)[Accommodation](/Accommodation)was constructed. This corresponds to the[YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).[Place](/Place)

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[address](/address)

[PostalAddress](/PostalAddress)or[Text](/Text)```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[amenityFeature](/amenityFeature)

[LocationFeatureSpecification](/LocationFeatureSpecification)```
```[branchCode](/branchCode)

[Text](/Text)For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.

```
```[containedInPlace](/containedInPlace)

[Place](/Place)[containedIn](/containedIn).Inverse property:

[containsPlace](/containsPlace)```
```[containsPlace](/containsPlace)

[Place](/Place)Inverse property:

[containedInPlace](/containedInPlace)```
```[event](/event)

[Event](/Event)[events](/events).```
```[faxNumber](/faxNumber)

[Text](/Text)```
```[geo](/geo)

[GeoCoordinates](/GeoCoordinates)or[GeoShape](/GeoShape)```
```[geoContains](/geoContains)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoCoveredBy](/geoCoveredBy)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoCovers](/geoCovers)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoCrosses](/geoCrosses)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoDisjoint](/geoDisjoint)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)```
```[geoEquals](/geoEquals)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).```
```[geoIntersects](/geoIntersects)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoOverlaps](/geoOverlaps)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[geoTouches](/geoTouches)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)```
```[geoWithin](/geoWithin)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).```
```[globalLocationNumber](/globalLocationNumber)

[Text](/Text)[Global Location Number](http://www.gs1.org/gln)(GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasDriveThroughService](/hasDriveThroughService)

[Boolean](/Boolean)[FoodEstablishment](/FoodEstablishment),[CovidTestingFacility](/CovidTestingFacility)) offers a service that can be used by driving through in a car. In the case of[CovidTestingFacility](/CovidTestingFacility)such facilities could potentially help with social distancing from other potentially-infected users.```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMap](/hasMap)

[Map](/Map)or[URL](/URL)[map](/map),[maps](/maps).```
```[isAccessibleForFree](/isAccessibleForFree)

[Boolean](/Boolean)[free](/free).```
```[isicV4](/isicV4)

[Text](/Text)```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[latitude](/latitude)

[Number](/Number)or[Text](/Text)`37.42242`

([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[longitude](/longitude)

[Number](/Number)or[Text](/Text)`-122.08585`

([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).```
```[maximumAttendeeCapacity](/maximumAttendeeCapacity)

[Integer](/Integer)```
```[openingHoursSpecification](/openingHoursSpecification)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[photo](/photo)

[ImageObject](/ImageObject)or[Photograph](/Photograph)[photos](/photos).```
```[publicAccess](/publicAccess)

[Boolean](/Boolean)[Place](/Place)is open to public visitors. If this property is omitted there is no assumed default boolean value.```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[slogan](/slogan)

[Text](/Text)```
```[smokingAllowed](/smokingAllowed)

[Boolean](/Boolean)```
```[specialOpeningHoursSpecification](/specialOpeningHoursSpecification)

[OpeningHoursSpecification](/OpeningHoursSpecification)Use this to explicitly override general opening hours brought in scope by

[openingHoursSpecification](/openingHoursSpecification)or[openingHours](/openingHours).```
```[telephone](/telephone)

[Text](/Text)```
```[tourBookingPage](/tourBookingPage)

[URL](/URL)[Place](/Place), such as an[Accommodation](/Accommodation)or[ApartmentComplex](/ApartmentComplex)in a real estate setting, as well as other kinds of tours as appropriate.[Thing](/Thing)

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

[Accommodation](/Accommodation)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[FloorPlan](/FloorPlan)#### More specific Types

### Acknowledgements

STI Accommodation Ontology

[http://ontologies.sti-innsbruck.at/acco/ns.html](http://ontologies.sti-innsbruck.at/acco/ns.html)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.

### Examples

[Example 1](#eg-0327)

Copied

Example notes or example HTML without markup.

Apartment example with min and max occupancy limits and floor size of 81 square meters(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Apartment", "name": "227 Lynn Street - Medium apartment", "description": "Great downtown accommodation for family or group of friends.", "numberOfRooms": 3, "occupancy": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 4 }, "floorLevel": "5", "floorSize": { "@type": "QuantitativeValue", "value": 81, "unitCode": "MTK" }, "numberOfBathroomsTotal": 2, "numberOfBedrooms": 2, "petsAllowed": true, "tourBookingPage": "http://example.com", "yearBuilt": 2005, "telephone": "+1-617-312-9783", "address": { "@type": "PostalAddress", "addressCountry": "US", "addressLocality": "West Roxbury", "addressRegion": "MA", "postalCode": "02132", "streetAddress": "227 Lynn Street" }, "latitude": 42.2742, "longitude": -71.1430 } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0422)

Copied

Example notes or example HTML without markup.

Single family residence example with min and max occupancy limits, floor size of 2500 square foots and lease length of 6 months(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SingleFamilyResidence", "name": "1331 St George Street - Family House", "description": "Great opportunity to own this 2500 sqft originally built in 1988 family home with 4 bedroom, 3 bathroom. which was RENOVATED IN 2014:( New Windows, New Bathroom, New Hardwood Floors, Air Condition, New Kitchen, etc.)", "numberOfRooms": 5, "occupancy": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5 }, "floorSize": { "@type": "QuantitativeValue", "value": 2500, "unitCode": "FTK" }, "leaseLength": { "@type": "QuantitativeValue", "value": 6, "unitText": "months" }, "numberOfBathroomsTotal": 3, "numberOfBedrooms": 4, "permittedUsage": "Perfectly suitable for a family with two kids.", "petsAllowed": "Only cats are allowed", "yearBuilt": 1988, "address": { "@type": "PostalAddress", "addressCountry": "CA", "addressLocality": "Vancouver", "addressRegion": "British Columbia", "postalCode": "V5T 1Z7", "streetAddress": "1331 St George Street" }, "telephone": "+1-604-829-6070" } </script>

Structured representation of the JSON-LD example.
