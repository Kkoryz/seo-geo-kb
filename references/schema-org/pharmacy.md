---
title: "Pharmacy"
source_url: https://schema.org/Pharmacy
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Pharmacy

# Pharmacy

A Schema.org Type

[Thing](/Thing)>

[Organization](/Organization)>

[LocalBusiness](/LocalBusiness)>

[MedicalBusiness](/MedicalBusiness)>

[Pharmacy](/Pharmacy)

[Thing](/Thing)>

[Organization](/Organization)>

[MedicalOrganization](/MedicalOrganization)>

[Pharmacy](/Pharmacy)

[Thing](/Thing)>

[Place](/Place)>

[LocalBusiness](/LocalBusiness)>

[MedicalBusiness](/MedicalBusiness)>

[Pharmacy](/Pharmacy)

- Canonical URL: https://schema.org/Pharmacy
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Pharmacy)

A pharmacy or drugstore.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[currenciesAccepted](/currenciesAccepted)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[floorLevel](/floorLevel)

[Text](/Text)[Accommodation](/Accommodation)in a multi-storey building. Since counting systems[vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.```
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

```
```[paymentAccepted](/paymentAccepted)

[Text](/Text)```
```[priceRange](/priceRange)

[Text](/Text)`$$$`

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

[URL](/URL)[Place](/Place), such as an[Accommodation](/Accommodation)or[ApartmentComplex](/ApartmentComplex)in a real estate setting, as well as other kinds of tours as appropriate.[MedicalOrganization](/MedicalOrganization)

```
```[healthPlanNetworkId](/healthPlanNetworkId)

[Text](/Text)```
```[isAcceptingNewPatients](/isAcceptingNewPatients)

[Boolean](/Boolean)```
```[medicalSpecialty](/medicalSpecialty)

[MedicalSpecialty](/MedicalSpecialty)[Organization](/Organization)

```
```[acceptedPaymentMethod](/acceptedPaymentMethod)

[LoanOrCredit](/LoanOrCredit)or[PaymentMethod](/PaymentMethod)or[Text](/Text)```
```[actionableFeedbackPolicy](/actionableFeedbackPolicy)

[CreativeWork](/CreativeWork)or[URL](/URL)[NewsMediaOrganization](/NewsMediaOrganization)or other news-related[Organization](/Organization), a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.```
```[address](/address)

[PostalAddress](/PostalAddress)or[Text](/Text)```
```[agentInteractionStatistic](/agentInteractionStatistic)

[InteractionCounter](/InteractionCounter)```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[alumni](/alumni)

[Person](/Person)Inverse property:

[alumniOf](/alumniOf)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[companyRegistration](/companyRegistration)

[Certification](/Certification)```
```[contactPoint](/contactPoint)

[ContactPoint](/ContactPoint)[contactPoints](/contactPoints).```
```[correctionsPolicy](/correctionsPolicy)

[CreativeWork](/CreativeWork)or[URL](/URL)[Organization](/Organization)(e.g.[NewsMediaOrganization](/NewsMediaOrganization)), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.```
```[department](/department)

[Organization](/Organization)```
```[dissolutionDate](/dissolutionDate)

[Date](/Date)```
```[diversityPolicy](/diversityPolicy)

[CreativeWork](/CreativeWork)or[URL](/URL)[Organization](/Organization)e.g. a[NewsMediaOrganization](/NewsMediaOrganization). For a[NewsMediaOrganization](/NewsMediaOrganization), a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.```
```[diversityStaffingReport](/diversityStaffingReport)

[Article](/Article)or[URL](/URL)[Organization](/Organization)(often but not necessarily a[NewsMediaOrganization](/NewsMediaOrganization)), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.```
```[duns](/duns)

[Text](/Text)```
```[email](/email)

[Text](/Text)```
```[employee](/employee)

[Person](/Person)[employees](/employees).```
```[ethicsPolicy](/ethicsPolicy)

[CreativeWork](/CreativeWork)or[URL](/URL)[NewsMediaOrganization](/NewsMediaOrganization)regarding journalistic and publishing practices, or of a[Restaurant](/Restaurant), a page describing food source policies. In the case of a[NewsMediaOrganization](/NewsMediaOrganization), an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.```
```[event](/event)

[Event](/Event)[events](/events).```
```[faxNumber](/faxNumber)

[Text](/Text)```
```[founder](/founder)

[Organization](/Organization)or[Person](/Person)[founders](/founders).```
```[foundingDate](/foundingDate)

[Date](/Date)```
```[foundingLocation](/foundingLocation)

[Place](/Place)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[globalLocationNumber](/globalLocationNumber)

[Text](/Text)[Global Location Number](http://www.gs1.org/gln)(GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasCredential](/hasCredential)

[Credential](/Credential)```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMemberProgram](/hasMemberProgram)

[MemberProgram](/MemberProgram)```
```[hasMerchantReturnPolicy](/hasMerchantReturnPolicy)

[MerchantReturnPolicy](/MerchantReturnPolicy)[hasProductReturnPolicy](/hasProductReturnPolicy).```
```[hasOfferCatalog](/hasOfferCatalog)

[OfferCatalog](/OfferCatalog)```
```[hasPOS](/hasPOS)

[Place](/Place)```
```[hasShippingService](/hasShippingService)

[ShippingService](/ShippingService)```
```[interactionStatistic](/interactionStatistic)

[InteractionCounter](/InteractionCounter)[interactionCount](/interactionCount).```
```[isicV4](/isicV4)

[Text](/Text)```
```[iso6523Code](/iso6523Code)

[Text](/Text)[ISO 6523(-1)](https://en.wikipedia.org/wiki/ISO/IEC_6523). The identifier should be in the`XXXX:YYYYYY:ZZZ`

or `XXXX:YYYYYY`

format. Where `XXXX`

is a 4 digit *ICD*(International Code Designator),`YYYYYY`

is an *OID*(Organization Identifier) with all formatting characters (dots, dashes, spaces) removed with a maximal length of 35 characters, and`ZZZ`

is an optional OPI (Organization Part Identifier) with a maximum length of 35 characters. The various components (ICD, OID, OPI) are joined with a colon character (ASCII `0x3a`

). Note that many existing organization identifiers defined as attributes like [leiCode](https://schema.org/leiCode)(`0199`

), [duns](https://schema.org/duns)(`0060`

) or [GLN](https://schema.org/globalLocationNumber)(`0088`

) can be expressed using ISO-6523. If possible, ISO-6523 codes should be preferred to populating [vatID](https://schema.org/vatID)or[taxID](https://schema.org/taxID), as ISO identifiers are less ambiguous.```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[knowsAbout](/knowsAbout)

[Text](/Text)or[Thing](/Thing)or[URL](/URL)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or[JobPosting](/JobPosting)descriptions.```
```[knowsLanguage](/knowsLanguage)

[Language](/Language)or[Text](/Text)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).```
```[legalAddress](/legalAddress)

[PostalAddress](/PostalAddress)```
```[legalName](/legalName)

[Text](/Text)```
```[legalRepresentative](/legalRepresentative)

[Person](/Person)```
```[leiCode](/leiCode)

[Text](/Text)```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[makesOffer](/makesOffer)

[Offer](/Offer)Inverse property:

[offeredBy](/offeredBy)```
```[member](/member)

[Organization](/Organization)or[Person](/Person)[members](/members),[musicGroupMember](/musicGroupMember).Inverse property:

[memberOf](/memberOf)```
```[memberOf](/memberOf)

[MemberProgramTier](/MemberProgramTier)or[Organization](/Organization)or[ProgramMembership](/ProgramMembership)Inverse property:

[member](/member)```
```[naics](/naics)

[Text](/Text)```
```[nonprofitStatus](/nonprofitStatus)

[NonprofitType](/NonprofitType)```
```[numberOfEmployees](/numberOfEmployees)

[QuantitativeValue](/QuantitativeValue)```
```[ownershipFundingInfo](/ownershipFundingInfo)

[AboutPage](/AboutPage)or[CreativeWork](/CreativeWork)or[Text](/Text)or[URL](/URL)[Organization](/Organization)(often but not necessarily a[NewsMediaOrganization](/NewsMediaOrganization)), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence. Note that the[funder](/funder)is also available and can be used to make basic funder information machine-readable.```
```[owns](/owns)

[Thing](/Thing)Inverse property:

[owner](/owner)```
```[parentOrganization](/parentOrganization)

[Organization](/Organization)[subOrganization](/subOrganization)of, if any. Supersedes[branchOf](/branchOf).Inverse property:

[subOrganization](/subOrganization)```
```[publishingPrinciples](/publishingPrinciples)

[CreativeWork](/CreativeWork)or[URL](/URL)[URL](/URL)) a document describing the editorial principles of an[Organization](/Organization)(or individual, e.g. a[Person](/Person)writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a[CreativeWork](/CreativeWork)(e.g.[NewsArticle](/NewsArticle)) the principles are those of the party primarily responsible for the creation of the[CreativeWork](/CreativeWork).While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a

[funder](/funder)) can be expressed using schema.org terminology.```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[seeks](/seeks)

[Demand](/Demand)```
```[skills](/skills)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)```
```[subOrganization](/subOrganization)

[Organization](/Organization)Inverse property:

[parentOrganization](/parentOrganization)```
```[taxID](/taxID)

[Text](/Text)```
```[telephone](/telephone)

[Text](/Text)```
```[unnamedSourcesPolicy](/unnamedSourcesPolicy)

[CreativeWork](/CreativeWork)or[URL](/URL)[Organization](/Organization)(typically a[NewsMediaOrganization](/NewsMediaOrganization)), a statement about policy on use of unnamed sources and the decision process required.```
```[vatID](/vatID)

[Text](/Text)[iso6523Code](/iso6523Code)with proper prefix.[Thing](/Thing)

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

[Example 1](#eg-0194)

Copied

Example notes or example HTML without markup.

<div> <h1>Philippa's Pharmacy</h1> <p>A superb collection of fine pharmaceuticals for your beauty and healthcare convenience, a department of Delia's Drugstore.</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: (800)555-1234</p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Pharmacy"> <h1 itemprop="name">Philippa's Pharmacy</h1> <p itemprop="description">A superb collection of fine pharmaceuticals for your beauty and healthcare convenience, a department of Delia's Drugstore.</p> <p>Open: <span itemprop="openingHours" content="Mo,Tu,We,Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+18005551234">(800)555-1234</span></p> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Pharmacy"> <h1 property="name">Philippa's Pharmacy</h1> <p property="description">A superb collection of fine pharmaceuticals for your beauty and healthcare convenience, a department of Delia's Drugstore.</p> <p>Open: <span property="openingHours" content="Mo,Tu,We,Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+18005551234">(800)555-1234</span></p> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare convenience, a department of Delia's Drugstore.", "openingHours": "Mo,Tu,We,Th 09:00-12:00", "telephone": "+18005551234" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0195)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 800-555-1234</p> </div> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm </span></p> <p>Phone: <span itemprop="telephone" content="+1 8005551234">800-555-1234</span></p> </div> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span property="telephone" content="+1 8005551234">800-555-1234</span></p> </div> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "department": { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0196)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 555-0100-1110</p> </div> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> </div> <!-- another department --> <div> <h2>Larry's Laundromat</h2> <p>Keep your clothes clean while you do your daily shopping!</p> <p>Open: Open weekdays 1pm-5:30pm.</p> <p>Phone: 555-0100-2121</p> <p>A branch of <a href="http://example.com/">Larry's International</a>.</p> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm </span></p> <p>Phone: <span itemprop="telephone" content="+155501001110">555-0100-1110</span></p> </div> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> </div> <!-- another department --> <div itemprop="department" itemscope itemtype="https://schema.org/DryCleaningOrLaundry"> <h2 itemprop="name">Larry's Laundromat</h2> <p itemprop="description">Keep your clothes clean while you do your daily shopping!</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 13:00-17:30">Open weekdays 1pm-5:30pm.</span></p> <p>Phone: <span itemprop="telephone" content="+155501002121">555-0100-2121</span></p> <p>A branch of <span itemprop="parentOrganization" itemscope itemtype="https://schema.org/Corporation"> <a itemprop="url" href="http://example.com/"><span itemprop="name">Larry's International</span></a></span>.</p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span property="telephone" content="+155501001110">555-0100-1110</span></p> </div> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> </div> <div property="department" typeof="DryCleaningOrLaundry"> <h2 property="name">Larry's Laundromat</h2> <p property="description">Keep your clothes clean while you do your daily shopping!</p> <p>Open: <span property="openingHours" content="Mo-Fr 13:00-17:30">Open weekdays 1pm-5:30pm.</span></p> <p>Phone: <span property="telephone" content="+155501002121">555-0100-2121</span></p> <p>A branch of <span property="parentOrganization" typeof="Corporation"> <a property="url" href="http://example.com/"><span property="name">Larry's International</span></a></span>.</p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "department": [ { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111" }, { "@type": "DryCleaningOrLaundry", "name": "Larry's Laundromat", "description": "Keep your clothes clean while you do your daily shopping!", "openingHours": "Mo-Fr 13:00-17:30", "telephone": "+155501002121", "parentOrganization": { "@type": "Corporation", "url": "http://example.com/", "name": "Larry's International" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0197)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 555-0100-1110</p> </div> <address> <span> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals...</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span itemprop="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress"> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm </span></p> <p>Phone: <span property="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address property="address" typeof="PostalAddress"> <span property="streetAddress"> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" }, "department": { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0198)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 555-0100-1110</p> </div> <address> <span>Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals...</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> <address> <span>Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span itemprop="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span property="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address property="address" typeof="PostalAddress"> <span property="streetAddress">Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> <address property="address" typeof="PostalAddress"> <span property="streetAddress">Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" }, "department": { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" } } } </script>

Structured representation of the JSON-LD example.
