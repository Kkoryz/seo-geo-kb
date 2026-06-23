---
title: "TouristDestination"
source_url: https://schema.org/TouristDestination
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# TouristDestination

# TouristDestination

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/TouristDestination
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+TouristDestination)

A tourist destination. In principle any

[Place](/Place)can be a[TouristDestination](/TouristDestination)from a[City](/City), Region or[Country](/Country)to an[AmusementPark](/AmusementPark)or[Hotel](/Hotel). This Type can be used on its own to describe a general[TouristDestination](/TouristDestination), or be used as an[additionalType](/additionalType)to add tourist relevant properties to any other[Place](/Place). A[TouristDestination](/TouristDestination)is defined as a[Place](/Place)that contains, or is colocated with, one or more[TouristAttraction](/TouristAttraction)s, often linked by a similar theme or interest to a particular[touristType](/touristType). The[UNWTO](http://www2.unwto.org/)defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip. (See examples below.)| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[includesAttraction](/includesAttraction)

[TouristAttraction](/TouristAttraction)```
```[touristType](/touristType)

[Audience](/Audience)or[Text](/Text)[Place](/Place)

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

[URL](/URL)### Acknowledgements

Future Internet Lab, Institute of Informatics and Telematics

Tourism Structured Web Data Community Group

[Tourism Structured Web Data Community Group](https://www.w3.org/community/tourismdata).

#### Source

[https://github.com/schemaorg/schemaorg/issues/1810](https://github.com/schemaorg/schemaorg/issues/1810)

### Examples

[Example 1](#eg-0262)

Copied

Example notes or example HTML without markup.

<div class="tourist-destination-wrapper"> <h1> Ribera del Duero Wine Route </h1> <div> <p> Ribera del Duero is on the northern plateau of Spain and covers parts of the provinces of Burgos, Segovia, Soria and Valladolid. The course of the River Duero marks the landscape here, dotting it with gentle hills, valleys and moorland, where vines are mixed with cereal crops. </p> <p> The wines from Ribera del Duero are the gateway to extensive and varied examples of its heritage; a sign of the cultural, historical and artistic wealth of the region. </p> <p> The Ribera del Duero wine route offers visitors charming villages where they can find monuments, castles, towers, cloisters, squares with special columns, cloistered convents, monasteries, churches, museums and palaces. Buildings from the Romanesque, Gothic and medieval periods will fill visitors’ memories with spectacular moments and unforgettable instants. </p> </div> <a href="http://www.rutadelvinoriberadelduero.es/en"> Official Website </a> <div> Tourist Audience: Wine tourism, Cultural tourism </div> <div> Geocoordinates: lat 41.67022, lon -3.6900 </div> <div class="event-wrapper"> <h2> Event: European Wine Tourism Week </h2> <div> The six Castile and León's wine routes jointly promote their enoturistic wealth. </div> <div> Location: Arlanza Wine Route, Bierzo Wine Route, Cigales Wine Route, Sierra de Francia Wine Route, Rueda Wine Route, Ribera del Duero Wine Route. </div> <div> Start Date: November 6, 2017 </div> <div> End Date: November 11, 2017 </div> <a href="http://www.rutadelvinoriberadelduero.es/es/agenda/semana-europea-del-enoturismo-2017"> Event Website </a> </div> <div class="includes-attraction-wrapper"> <div> <h2>Bodegas Protos</h2> <a href="http://www.bodegasprotos.com">Website</a> <a href="https://commons.wikimedia.org/wiki/File%3AFoto_Bodega_Rogers2.jpg">Picture</a> </div> <div> <h2>Bodega Alejandro F. Tinto Pesquera</h2> <a href="http://www.grupopesquera.com">Website</a> <a href="https://commons.wikimedia.org/wiki/File%3ARibera_Del_Duero_Pesquera.JPG">Picture</a> </div> <div> <h2>Peñafiel</h2> <a href="https://commons.wikimedia.org/wiki/File:Castillo_pe%C3%B1afiel_desde_plaza_coso_valladolid.jpg">Peñafiel</a> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemtype="https://schema.org/TouristDestination" itemscope> <meta itemprop="name" content="Ribera del Duero Wine Route" /> <meta itemprop="description" content="Ribera del Duero is on the northern plateau of Spain and covers parts of the provinces of Burgos, Segovia, Soria and Valladolid. The course of the River Duero marks the landscape here, dotting it with gentle hills, valleys and moorland, where vines are mixed with cereal crops. The wines from Ribera del Duero are the gateway to extensive and varied examples of its heritage; a sign of the cultural, historical and artistic wealth of the region. The Ribera del Duero wine route offers visitors charming villages where they can find monuments, castles, towers, cloisters, squares with special columns, cloistered convents, monasteries, churches, museums and palaces. Buildings from the Romanesque, Gothic and medieval periods will fill visitors’ memories with spectacular moments and unforgettable instants." /> <link itemprop="url" href="http://www.rutadelvinoriberadelduero.es/en" /> <div itemprop="touristType" itemtype="https://schema.org/Audience" itemscope> <meta itemprop="audienceType" content="Wine tourism" /> <meta itemprop="audienceType" content="Cultural tourism" /> </div> <div itemprop="geo" itemtype="https://schema.org/GeoCoordinates" itemscope> <meta itemprop="latitude" content="41.67022" /> <meta itemprop="longitude" content="-3.6900" /> </div> <div itemprop="event" itemtype="https://schema.org/Event" itemscope> <meta itemprop="name" content="European Wine Tourism Week" /> <meta itemprop="description" content="The six Castile and León's wine routes jointly promote their enoturistic wealth." /> <link itemprop="url" href="http://www.rutadelvinoriberadelduero.es/es/agenda/semana-europea-del-enoturismo-2017" /> <meta itemprop="startDate" content="2017-11-06" /> <meta itemprop="endDate" content="2017-11-12" /> <meta itemprop="location" content="Sierra de Francia Wine Route" /> <meta itemprop="location" content="Cigales Wine Route" /> <meta itemprop="location" content="Arlanza Wine Route" /> <meta itemprop="location" content="Rueda Wine Route" /> <meta itemprop="location" content="Ribera del Duero Wine Route" /> <meta itemprop="location" content="Bierzo Wine Route" /> </div> <div itemprop="includesAttraction" itemtype="https://schema.org/TouristAttraction" itemscope> <link itemprop="additionalType" href="https://schema.org/City" /> <meta itemprop="name" content="Peñafiel" /> <link itemprop="image" href="https://commons.wikimedia.org/wiki/File:Castillo_pe%C3%B1afiel_desde_plaza_coso_valladolid.jpg" /> </div> <div itemprop="includesAttraction" itemtype="https://schema.org/TouristAttraction" itemscope> <link itemprop="additionalType" href="https://schema.org/Winery" /> <meta itemprop="name" content="Bodegas Protos" /> <link itemprop="sameAs" href="http://www.bodegasprotos.com/" /> <link itemprop="image" href="https://commons.wikimedia.org/wiki/File%3AFoto_Bodega_Rogers2.jpg" /> </div> <div itemprop="includesAttraction" itemtype="https://schema.org/Winery" itemscope> <link itemprop="additionalType" href="https://schema.org/TouristAttraction" /> <meta itemprop="name" content="Bodega Alejandro F. Tinto Pesquera" /> <link itemprop="sameAs" href="http://www.grupopesquera.com/" /> <link itemprop="image" href="https://commons.wikimedia.org/wiki/File%3ARibera_Del_Duero_Pesquera.JPG" /> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div> <div vocab="https://schema.org/" typeof="TouristDestination"> <div property="name" content="Ribera del Duero Wine Route"></div> <div property="description" content="Ribera del Duero is on the northern plateau of Spain and covers parts of the provinces of Burgos, Segovia, Soria and Valladolid. The course of the River Duero marks the landscape here, dotting it with gentle hills, valleys and moorland, where vines are mixed with cereal crops. The wines from Ribera del Duero are the gateway to extensive and varied examples of its heritage; a sign of the cultural, historical and artistic wealth of the region. The Ribera del Duero wine route offers visitors charming villages where they can find monuments, castles, towers, cloisters, squares with special columns, cloistered convents, monasteries, churches, museums and palaces. Buildings from the Romanesque, Gothic and medieval periods will fill visitors’ memories with spectacular moments and unforgettable instants."></div> <div rel="url" resource="http://www.rutadelvinoriberadelduero.es/en"></div> <div rel="touristType"> <div typeof="Audience"> <div property="audienceType" content="Cultural tourism"></div> <div property="audienceType" content="Wine tourism"></div> </div> </div> <div rel="geo"> <div typeof="GeoCoordinates"> <div property="longitude" content="-3.6900"></div> <div property="latitude" content="41.67022"></div> </div> </div> <div rel="event"> <div typeof="Event"> <div property="startDate" datatype="Date" content="2017-11-06"></div> <div property="endDate" datatype="Date" content="2017-11-12"></div> <div property="location" content="Bierzo Wine Route"></div> <div property="location" content="Rueda Wine Route"></div> <div property="location" content="Ribera del Duero Wine Route"></div> <div property="name" content="European Wine Tourism Week"></div> <div property="location" content="Arlanza Wine Route"></div> <div rel="url" resource="http://www.rutadelvinoriberadelduero.es/es/agenda/semana-europea-del-enoturismo-2017"></div> <div property="location" content="Cigales Wine Route"></div> <div property="location" content="Sierra de Francia Wine Route"></div> <div property="description" content="The six Castile and León's wine routes jointly promote their enoturistic wealth."></div> </div> </div> <div rel="includesAttraction"> <div typeof="TouristAttraction"> <div property="name" content="Peñafiel"></div> <div rel="image" resource="https://commons.wikimedia.org/wiki/File:Castillo_pe%C3%B1afiel_desde_plaza_coso_valladolid.jpg"></div> <div rel="rdf:type" resource="https://schema.org/City"></div> </div> </div> <div rel="includesAttraction"> <div typeof="TouristAttraction"> <div property="name" content="Bodega Alejandro F. Tinto Pesquera"></div> <div rel="rdf:type" resource="https://schema.org/Winery"></div> <div rel="image" resource="https://commons.wikimedia.org/wiki/File%3ARibera_Del_Duero_Pesquera.JPG"></div> <div rel="sameAs" resource="http://www.grupopesquera.com/"></div> </div> </div> <div rel="includesAttraction"> <div typeof="TouristAttraction"> <div property="name" content="Bodegas Protos"></div> <div rel="sameAs" resource="http://www.bodegasprotos.com/"></div> <div rel="image" resource="https://commons.wikimedia.org/wiki/File%3AFoto_Bodega_Rogers2.jpg"></div> <div rel="rdf:type" resource="https://schema.org/Winery"></div> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org", "@type": "TouristDestination", "name": "Ribera del Duero Wine Route", "description": "Ribera del Duero is on the northern plateau of Spain and covers parts of the provinces of Burgos, Segovia, Soria and Valladolid. The course of the River Duero marks the landscape here, dotting it with gentle hills, valleys and moorland, where vines are mixed with cereal crops.\nThe wines from Ribera del Duero are the gateway to extensive and varied examples of its heritage; a sign of the cultural, historical and artistic wealth of the region.\nThe Ribera del Duero wine route offers visitors charming villages where they can find monuments, castles, towers, cloisters, squares with special columns, cloistered convents, monasteries, churches, museums and palaces. Buildings from the Romanesque, Gothic and medieval periods will fill visitors’ memories with spectacular moments and unforgettable instants.", "url": "http://www.rutadelvinoriberadelduero.es/en", "touristType": { "@type": "Audience", "audienceType": [ "Wine tourism", "Cultural tourism" ] }, "geo": { "@type": "GeoCoordinates", "latitude": "41.67022", "longitude": "-3.6900" }, "event": { "@type": "Event", "name": "European Wine Tourism Week", "description": "The six Castile and León's wine routes jointly promote their enoturistic wealth.", "location": [ "Arlanza Wine Route", "Bierzo Wine Route", "Cigales Wine Route", "Sierra de Francia Wine Route", "Rueda Wine Route", "Ribera del Duero Wine Route" ], "startDate": "2017-11-06", "endDate": "2017-11-12", "url": "http://www.rutadelvinoriberadelduero.es/es/agenda/semana-europea-del-enoturismo-2017" }, "includesAttraction": [ { "@type": [ "Winery", "TouristAttraction" ], "name": "Bodegas Protos", "sameAs": "http://www.bodegasprotos.com", "image": "https://commons.wikimedia.org/wiki/File%3AFoto_Bodega_Rogers2.jpg" }, { "@type": [ "Winery", "TouristAttraction" ], "name": "Bodega Alejandro F. Tinto Pesquera", "sameAs": "http://www.grupopesquera.com", "image": "https://commons.wikimedia.org/wiki/File%3ARibera_Del_Duero_Pesquera.JPG" }, { "@type": [ "City", "TouristAttraction" ], "name": "Peñafiel", "image": "https://commons.wikimedia.org/wiki/File:Castillo_pe%C3%B1afiel_desde_plaza_coso_valladolid.jpg" } ] }

Structured representation of the JSON-LD example.
