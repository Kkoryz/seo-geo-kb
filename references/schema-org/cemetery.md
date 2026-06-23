---
title: "Cemetery"
source_url: https://schema.org/Cemetery
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Cemetery

# Cemetery

A Schema.org Type

- Canonical URL: https://schema.org/Cemetery
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Cemetery)

A graveyard.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[openingHours](/openingHours)

[Text](/Text)- Days are specified using the following two-letter combinations:
`Mo`

,`Tu`

,`We`

,`Th`

,`Fr`

,`Sa`

,`Su`

. - Times are specified using 24:00 format. For example, 3pm is specified as
`15:00`

, 10am as`10:00`

. - Here is an example:
`<time itemprop="openingHours" datetime="Tu,Th 16:00-20:00">Tuesdays and Thursdays 4-8pm</time>`

. - If a business is open 7 days a week, then it can be specified as
`<time itemprop="openingHours" datetime="Mo-Su">Monday through Sunday, all day</time>`

.

[Place](/Place)

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

[Map](/Map)or[URL](/URL)[maps](/maps),[map](/map).```
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

[URL](/URL)### Examples

[Example 1](#eg-0438)

Copied

Example notes or example HTML without markup.

Name: Villers–Bretonneux Australian National Memorial Description: The Australian National Memorial, Villers–Bretonneux is the main memorial to Australian military personnel killed on the Western Front during World War I. Address: Fouilloy, FR Geocoordinates: lat 49.8852515, lon 2.5106436 Public Access: yes Is Accessible For Free: yes Tourist Audience: Memorial Tourism from Australia and New Zealand Image: https://commons.wikimedia.org/wiki/File%3AVillers-Bretonneux_m%C3%A9morial_australien_(tour_et_croix)_1.jpg Same As: https://www.wikidata.org/wiki/Q2544355

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemtype="https://schema.org/TouristAttraction" itemscope> <link itemprop="additionalType" href="https://schema.org/Cemetery" /> <meta itemprop="name" content="Villers–Bretonneux Australian National Memorial" /> <meta itemprop="description" content="The Australian National Memorial, Villers–Bretonneux is the main memorial to Australian military personnel killed on the Western Front during World War I." /> <div itemprop="touristType" itemtype="https://schema.org/Audience" itemscope> <meta itemprop="audienceType" content="Memorial Tourism" /> <div itemprop="geographicArea" itemtype="https://schema.org/AdministrativeArea" itemscope> <meta itemprop="name" content="New Zealand" /> </div> <div itemprop="geographicArea" itemtype="https://schema.org/AdministrativeArea" itemscope> <meta itemprop="name" content="Australia" /> </div> </div> <div itemprop="address" itemtype="https://schema.org/PostalAddress" itemscope> <meta itemprop="addressLocality" content="Fouilloy" /> <meta itemprop="addressCountry" content="FR" /> </div> <div itemprop="geo" itemtype="https://schema.org/GeoCoordinates" itemscope> <meta itemprop="latitude" content="49.8852515" /> <meta itemprop="longitude" content="2.5106436" /> </div> <meta itemprop="publicAccess" content="true" /> <meta itemprop="isAccessibleForFree" content="true" /> <link itemprop="sameAs" href="https://www.wikidata.org/wiki/Q2544355" /> <link itemprop="image" href="https://commons.wikimedia.org/wiki/File%3AVillers-Bretonneux_m%C3%A9morial_australien_(tour_et_croix)_1.jpg" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Cemetery TouristAttraction"> <div property="name" content="Villers–Bretonneux Australian National Memorial"></div> <div property="description" content="The Australian National Memorial, Villers–Bretonneux is the main memorial to Australian military personnel killed on the Western Front during World War I."></div> <div property="touristType" typeof="Audience"> <div property="audienceType" content="Memorial Tourism"></div> <div property="geographicArea" typeof="AdministrativeArea"> > <div property="name" content="New Zealand"></div> </div> <div property="geographicArea" typeof="AdministrativeArea"> <div property="name" content="Australia"></div> </div> </div> </div> <div property="address" typeof="PostalAddress"> <div property="addressCountry" content="FR"></div> <div property="addressLocality" content="Fouilloy"></div> </div> <div property="geo" typeof="GeoCoordinates"> <div property="latitude" content="49.8852515"></div> <div property="longitude" content="2.5106436"></div> </div> <div property="publicAccess" datatype="xsd:boolean" content="true"></div> <div property="isAccessibleForFree" datatype="xsd:boolean" content="true"> <link property="sameAs" href="https://www.wikidata.org/wiki/Q2544355"> <link property="image" href="https://commons.wikimedia.org/wiki/File%3AVillers-Bretonneux_m%C3%A9morial_australien_(tour_et_croix)_1.jpg"> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": [ "Cemetery", "TouristAttraction" ], "name": "Villers–Bretonneux Australian National Memorial", "description": "The Australian National Memorial, Villers–Bretonneux is the main memorial to Australian military personnel killed on the Western Front during World War I.", "touristType": { "@type": "Audience", "audienceType" : "Memorial Tourism", "geographicArea": [{ "@type": "AdministrativeArea", "name": "Australia" },{ "@type": "AdministrativeArea", "name": "New Zealand" }] }, "address": { "@type": "PostalAddress", "addressCountry": "FR", "addressLocality":"Fouilloy" }, "geo": { "@type": "GeoCoordinates", "latitude": "49.8852515", "longitude": "2.5106436" }, "publicAccess": true, "isAccessibleForFree": true, "sameAs":"https://www.wikidata.org/wiki/Q2544355", "image":"https://commons.wikimedia.org/wiki/File%3AVillers-Bretonneux_m%C3%A9morial_australien_(tour_et_croix)_1.jpg" } </script>

Structured representation of the JSON-LD example.
