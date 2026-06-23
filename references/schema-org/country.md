---
title: "Country"
source_url: https://schema.org/Country
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Country

# Country

A Schema.org Type

- Canonical URL: https://schema.org/Country
-
Equivalent Class: lcc-cr:Country

Equivalent Class: unece:Country

Equivalent Class: gs1:Country [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Country)

A country.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[Country](/Country)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[DefinedRegion](/DefinedRegion)or[GeoCoordinates](/GeoCoordinates)or[GeoShape](/GeoShape)or[PostalAddress](/PostalAddress)[ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1)format, for example "US". For backward compatibility, a 3-letter[ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)country code such as "SGP" or a full country name such as "Singapore" can also be used.[applicableCountry](/applicableCountry)

[MerchantReturnPolicy](/MerchantReturnPolicy)[countryOfOrigin](/countryOfOrigin)

[CreativeWork](/CreativeWork)or[Movie](/Movie)or[Product](/Product)or[TVEpisode](/TVEpisode)or[TVSeason](/TVSeason)or[TVSeries](/TVSeries)In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

[nationality](/nationality)

[Person](/Person)[returnPolicyCountry](/returnPolicyCountry)
