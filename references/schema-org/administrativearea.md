---
title: "AdministrativeArea"
source_url: https://schema.org/AdministrativeArea
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# AdministrativeArea

# AdministrativeArea

A Schema.org Type

- Canonical URL: https://schema.org/AdministrativeArea
- Equivalent Class: cmns-ge:Subdivision
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+AdministrativeArea)

A geographical region, typically under the jurisdiction of a particular government.

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

[AdministrativeArea](/AdministrativeArea)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[DefinedRegion](/DefinedRegion)or[PostalAddress](/PostalAddress)[Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)such as the Province in Italy or Region in Germany.[applicableLocation](/applicableLocation)

[DrugCost](/DrugCost)or[DrugLegalStatus](/DrugLegalStatus)[applicantLocationRequirements](/applicantLocationRequirements)

[JobPosting](/JobPosting)[areaServed](/areaServed)

[ContactPoint](/ContactPoint)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[FinancialIncentive](/FinancialIncentive)or[Offer](/Offer)or[Organization](/Organization)or[Service](/Service)[availableIn](/availableIn)

[DrugStrength](/DrugStrength)[geographicArea](/geographicArea)

[Audience](/Audience)[jurisdiction](/jurisdiction)

[GovernmentService](/GovernmentService)or[Legislation](/Legislation)[legislationJurisdiction](/legislationJurisdiction)

[Legislation](/Legislation)[occupationLocation](/occupationLocation)

[Occupation](/Occupation)[serviceArea](/serviceArea)

[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Service](/Service)[studyLocation](/studyLocation)

[MedicalStudy](/MedicalStudy)[validIn](/validIn)

[Certification](/Certification)or[Credential](/Credential)or[Permit](/Permit)[Permit](/Permit), a[Certification](/Certification), or an[EducationalOccupationalCredential](/EducationalOccupationalCredential).#### More specific Types

### Examples

[Example 1](#eg-0168)

Copied

Example notes or example HTML without markup.

<div> NYC Food Service Establishment Permit, issued by Department of Health and Mental Hygiene. (issued through NYC Food Service Establishment Permit Service; valid in New York for 1 year). </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/GovernmentPermit"> <span itemprop="name">NYC Food Service Establishment Permit</span> <div itemprop="issuedBy" itemscope itemtype="https://schema.org/GovernmentOrganization"> <span itemprop="name">Department of Health and Mental Hygiene"</span> </div> <div itemprop="issuedThrough" itemscope itemtype="https://schema.org/GovernmentService"> <span itemprop="name">NYC Food Service Establishment Permit Service</span> </div> <div itemprop="validIn" itemscope itemtype="https://schema.org/AdministrativeArea"> <span itemprop="name">New York</span> </div> <time itemprop="validFor" datetime="P1Y">1 year</time> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="GovernmentPermit"> <span property="name">NYC Food Service Establishment Permit</span> <div property="issuedBy" typeof="GovernmentOrganization"> <span property="name">Department of Health and Mental Hygiene"</span> </div> <div property="issuedThrough" typeof="GovernmentService"> <span property="name">NYC Food Service Establishment Permit Service</span> </div> <div property="validIn" typeof="AdministrativeArea"> <span property="name">New York</span> </div> <time property="validFor" datetime="P1Y">1 Year</time> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentPermit", "issuedBy": { "@type": "GovernmentOrganization", "name": "Department of Health and Mental Hygiene\"" }, "issuedThrough": { "@type": "GovernmentService", "name": "NYC Food Service Establishment Permit Service" }, "name": "NYC Food Service Establishment Permit", "validFor": "P1Y", "validIn": { "@type": "AdministrativeArea", "name": "New York" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0169)

Copied

Example notes or example HTML without markup.

This example shows a JSON-LD description of services that do not necessarily have a direct human-oriented HTML description. It describes a GovernmentService named "Veterans Affairs Emergency Mental Health", its operator, service area and service details, such as its Veterans Crisis Line (including phone contact line hours of operation, language and other details).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentService", "name": "Veterans Affairs Emergency Mental Health", "serviceType": "Psychiatric Emergency Services", "serviceOperator": { "@type": "GovernmentOrganization", "name": "US Department of Veterans Affairs" }, "areaServed": { "@type": "AdministrativeArea", "name": "Massachusetts" }, "audience": { "@type": "Audience", "name": "Veterans" }, "availableChannel": { "@type": "ServiceChannel", "name": "Urgent Care Clinic", "availableLanguage": { "@type": "Language", "name": "Spanish", "alternateName": "es" }, "serviceLocation": { "@type": "Hospital", "name": "VA Boston -- West Roxbury", "address": { "@type": "PostalAddress", "streetAddress": "1400 VFW Parkway", "addressLocality": "West Roxbury", "addressRegion": "MA", "postalCode": "02132" } } } } </script>

Structured representation of the JSON-LD example.
