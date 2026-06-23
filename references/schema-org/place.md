---
title: "Place"
source_url: https://schema.org/Place
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Place

# Place

A Schema.org Type

- Canonical URL: https://schema.org/Place
- Equivalent Class: cmns-loc:Location
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Place)

Entities that have a somewhat fixed, physical extension.

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

[URL](/URL)Instances of

[Place](/Place)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BroadcastService](/BroadcastService)[areaServed](/areaServed)

[ContactPoint](/ContactPoint)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[FinancialIncentive](/FinancialIncentive)or[Offer](/Offer)or[Organization](/Organization)or[Service](/Service)[availableAtOrFrom](/availableAtOrFrom)

[Demand](/Demand)or[Offer](/Offer)[birthPlace](/birthPlace)

[Person](/Person)[containedIn](/containedIn)

[Place](/Place)[containedInPlace](/containedInPlace)

[Place](/Place)[containsPlace](/containsPlace)

[Place](/Place)[contentLocation](/contentLocation)

[CreativeWork](/CreativeWork)[course](/course)

[ExerciseAction](/ExerciseAction)[deathPlace](/deathPlace)

[Person](/Person)[displayLocation](/displayLocation)

[CreativeWork](/CreativeWork)or[Product](/Product)[dropoffLocation](/dropoffLocation)

[RentalCarReservation](/RentalCarReservation)[eligibleRegion](/eligibleRegion)

[ActionAccessSpecification](/ActionAccessSpecification)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[Offer](/Offer)See also

[ineligibleRegion](/ineligibleRegion).[exerciseCourse](/exerciseCourse)

[ExerciseAction](/ExerciseAction)[foodEstablishment](/foodEstablishment)

[CookAction](/CookAction)[foundingLocation](/foundingLocation)

[Organization](/Organization)[fromLocation](/fromLocation)

[ExerciseAction](/ExerciseAction)or[MoveAction](/MoveAction)or[TransferAction](/TransferAction)[gameLocation](/gameLocation)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[geoContains](/geoContains)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoCoveredBy](/geoCoveredBy)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoCovers](/geoCovers)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoCrosses](/geoCrosses)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoDisjoint](/geoDisjoint)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)[geoEquals](/geoEquals)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).[geoIntersects](/geoIntersects)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoOverlaps](/geoOverlaps)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[geoTouches](/geoTouches)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)[geoWithin](/geoWithin)

[GeospatialGeometry](/GeospatialGeometry)or[Place](/Place)[DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).[hasPOS](/hasPOS)

[Organization](/Organization)or[Person](/Person)[homeLocation](/homeLocation)

[Person](/Person)[ineligibleRegion](/ineligibleRegion)

[ActionAccessSpecification](/ActionAccessSpecification)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[MediaObject](/MediaObject)or[Offer](/Offer)See also

[eligibleRegion](/eligibleRegion).[itemLocation](/itemLocation)

[ArchiveComponent](/ArchiveComponent)[itinerary](/itinerary)

[Trip](/Trip)[Place](/Place)) that make up a trip. For a trip where destination order is important use[ItemList](/ItemList)to specify that order (see examples).[jobLocation](/jobLocation)

[JobPosting](/JobPosting)[location](/location)

[Action](/Action)or[Event](/Event)or[InteractionCounter](/InteractionCounter)or[Organization](/Organization)[locationCreated](/locationCreated)

[CreativeWork](/CreativeWork)[observationAbout](/observationAbout)

[Observation](/Observation)[observationAbout](/observationAbout)property identifies an entity, often a[Place](/Place), associated with an[Observation](/Observation).[pickupLocation](/pickupLocation)

[RentalCarReservation](/RentalCarReservation)or[TaxiReservation](/TaxiReservation)[regionsAllowed](/regionsAllowed)

[MediaObject](/MediaObject)[ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).[serviceArea](/serviceArea)

[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Service](/Service)[serviceLocation](/serviceLocation)

[ServiceChannel](/ServiceChannel)[spatial](/spatial)

[CreativeWork](/CreativeWork)[locationCreated](/locationCreated),[spatialCoverage](/spatialCoverage),[contentLocation](/contentLocation)) are not known to be appropriate.[spatialCoverage](/spatialCoverage)

[CreativeWork](/CreativeWork)[toLocation](/toLocation)

[ExerciseAction](/ExerciseAction)or[InsertAction](/InsertAction)or[MoveAction](/MoveAction)or[TransferAction](/TransferAction)[tripOrigin](/tripOrigin)

[Trip](/Trip)[workLocation](/workLocation)

[Person](/Person)#### More specific Types

-
[Accommodation](/Accommodation) -
[AdministrativeArea](/AdministrativeArea) -
[CivicStructure](/CivicStructure) -
[DefinedRegion](/DefinedRegion) -
[Landform](/Landform) -
[LandmarksOrHistoricalBuildings](/LandmarksOrHistoricalBuildings) -
[LocalBusiness](/LocalBusiness) -
[Residence](/Residence) -
[TouristAttraction](/TouristAttraction) -
[TouristDestination](/TouristDestination)

### Examples

[Example 1](#eg-0005)

Copied

Example notes or example HTML without markup.

<h1>What is the latitude and longitude of the Empire State Building?</h1> Answer: Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 sec W

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Place"> <h1>What is the latitude and longitude of the <span itemprop="name">Empire State Building</span>?</h1> Answer: <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCoordinates"> Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 dec W <meta itemprop="latitude" content="40.75" /> <meta itemprop="longitude" content="-73.98" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Place"> <h1>What is the latitude and longitude of the <span property="name">Empire State Building</span>?</h1> Answer: <div property="geo" typeof="GeoCoordinates"> Latitude: 40 deg 44 min 54.36 sec N Longitude: 73 deg 59 min 8.5 dec W <meta property="latitude" content="40.75" /> <meta property="longitude" content="-73.98" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Place", "geo": { "@type": "GeoCoordinates", "latitude": "40.75", "longitude": "-73.98" }, "name": "Empire State Building" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0012)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0015)

Copied

Example notes or example HTML without markup.

<h1>Beachwalk Beachwear & Giftware</h1> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach. 3102 Highway 98 Mexico Beach, FL Phone: 850-648-4200

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/LocalBusiness"> <h1><span itemprop="name">Beachwalk Beachwear & Giftware</span></h1> <span itemprop="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">3102 Highway 98</span> <span itemprop="addressLocality">Mexico Beach</span>, <span itemprop="addressRegion">FL</span> </div> Phone: <span itemprop="telephone">850-648-4200</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="LocalBusiness"> <h1><span property="name">Beachwalk Beachwear & Giftware</span></h1> <span property="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress">3102 Highway 98</span> <span property="addressLocality">Mexico Beach</span>, <span property="addressRegion">FL</span> </div> Phone: <span property="telephone">850-648-4200</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "LocalBusiness", "address": { "@type": "PostalAddress", "addressLocality": "Mexico Beach", "addressRegion": "FL", "streetAddress": "3102 Highway 98" }, "description": "A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.", "name": "Beachwalk Beachwear & Giftware", "telephone": "850-648-4200" } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0024)

Copied

Example notes or example HTML without markup.

Springfield Town Hall Hours: Mon-Fri 9am - 5:30pm Sat 9am - 12pm Closed Sun

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CivicStructure"> <span itemprop="name">Springfield Town Hall</span> Hours: <meta itemprop="openingHours" content="Mo-Fr 09:00-17:30">Mon-Fri 9am - 5:30pm <meta itemprop="openingHours" content="Sa 09:00-12:00">Sat 9am - 12pm Closed Sun </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CivicStructure"> <span property="name">Springfield Town Hall</span> Hours: <meta property="openingHours" content="Mo-Fr 09:00-17:30">Mon-Fri 9am - 5:30pm <meta property="openingHours" content="Sa 09:00-12:00">Sat 9am - 12pm Closed Sun </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CivicStructure", "name": "Springfield Town Hall", "openingHours": [ "Mo-Fr 09:00-17:30", "Sa 09:00-12:00" ] } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0171)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-title">CANCELLED - Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> CANCELLED - Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"> <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" property="name"> CANCELLED - Typhoon with Radiation City </div> <meta property="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div property="offers" typeof="Offer"> $<div class="event-price" property="price">13.00</div> <meta property="priceCurrency" content="USD"><a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "eventStatus": "https://schema.org/EventCancelled", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "CANCELLED - Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0172)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Oct 12</div> <div><span>(previously scheduled for Sept 14th)</span></div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-10-12T22:00"> Sat Oct 12 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventRescheduled"><span itemprop="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time"> 10:00 PM </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-10-12T22:00">Sat Oct 12</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <meta property="eventStatus" content="https://schema.org/EventRescheduled"> <span property="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">10:00 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" } ] } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0173)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> SOLD OUT! Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta itemprop="availability" content="https://schema.org/SoldOut"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <meta property="availability" content="https://schema.org/SoldOut"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "SOLD OUT! Typhoon with Radiation City", "offers": { "@type": "Offer", "availability": "https://schema.org/SoldOut", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0174)

Copied

Example notes or example HTML without markup.

JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0201)

Copied

Example notes or example HTML without markup.

An example snippet of JSON-LD describing two B.B. King concerts.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-12T19:30", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "address" : "79 Washington St., Providence, RI" }, "offers" : { "@type" : "Offer", "url" : "https://www.etix.com/ticket/1771656" } }, { "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-13T20:00", "location" : { "@type" : "Place", "name" : "Lynn Auditorium", "address" : "Lynn, MA, 01901" }, "offers" : { "@type" : "Offer", "url" : "http://frontgatetickets.com/venue.php?id=11766" } }] </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.

[Example 11](#eg-0461)

Copied

Example notes or example HTML without markup.

<a href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </a> Thu, 04/21/16 8:00 p.m. <a href="wells-fargo-center.html"> Wells Fargo Center </a> Philadelphia, PA Priced from: $35 1938 tickets left

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Event"> <a itemprop="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span itemprop="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta itemprop="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <a itemprop="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="addressLocality">Philadelphia</span>, <span itemprop="addressRegion">PA</span> </div> </div> <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer"> <meta itemprop="priceCurrency" content="USD" /> Priced from: <span itemprop="lowPrice" content="35">$35</span> <span itemprop="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Event"> <a property="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span property="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta property="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div property="location" typeof="Place"> <a property="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div property="address" typeof="PostalAddress"> <span property="addressLocality">Philadelphia</span>, <span property="addressRegion">PA</span> </div> </div> <div property="offers" typeof="AggregateOffer"> <meta property="priceCurrency" content="USD" /> Priced from: <span property="lowPrice" content="35">$35</span> <span property="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1)", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Philadelphia", "addressRegion": "PA" }, "url": "wells-fargo-center.html" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "35", "offerCount": "1938" }, "startDate": "2016-04-21T20:00", "url": "nba-miami-philidelphia-game3.html" } </script>

Structured representation of the JSON-LD example.
