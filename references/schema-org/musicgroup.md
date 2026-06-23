---
title: "MusicGroup"
source_url: https://schema.org/MusicGroup
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MusicGroup

# MusicGroup

A Schema.org Type

- Canonical URL: https://schema.org/MusicGroup
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MusicGroup)

A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[album](/album)

[MusicAlbum](/MusicAlbum)[albums](/albums).```
```[genre](/genre)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[track](/track)

[ItemList](/ItemList)or[MusicRecording](/MusicRecording)[tracks](/tracks).[Organization](/Organization)

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

[URL](/URL)Instances of

[MusicGroup](/MusicGroup)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MusicAlbum](/MusicAlbum)or[MusicRecording](/MusicRecording)[musicBy](/musicBy)

[Clip](/Clip)or[Episode](/Episode)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)### Examples

[Example 1](#eg-0009)

Copied

Example notes or example HTML without markup.

<h1>Foo Fighters</h1> <h2>Video: Interview with the Foo Fighters</h2> <object ...> <param ...> <embed type="application/x-shockwave-flash" ...> </object> Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope. <h2>Songs</h2> Rope Length: 4:05 - 14300 plays <a href="foo-fighters-rope-play.html">Play</a> <a href="foo-fighters-rope-buy.html">Buy</a> From album: <a href="foo-fighters-wasting-light.html">Wasting Light</a> Everlong Length: 6:33 - 11700 plays <a href="foo-fighters-everlong-play.html">Play</a> <a href="foo-fighters-everlong-buy.html">Buy</a> From album: <a href="foo-fighters-color-and-shape.html">The Color And The Shape</a> <h2>Upcoming shows</h2> <a href="foo-fighters-may20-fedexforum">FedExForum</a> Memphis, TN, US May 20 <a href="ticketworlds.com/foofighters/may20-2011">Buy tickets</a> <a href="foo-fighters-may23-midamericacenter">Mid America Center</a> Council Bluffs, IA, US May 23 <a href="ticketworlds.com/foofighters/may23-2011">Buy tickets</a> <h2><a href="foo-fighters-photos">28 Photos</a></h2> <a href="foofighters-1.jpg"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb1.jpg" /></a> <a href="foofighters-2.jpg"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb2.jpg" /></a> <a href="foofighters-3.jpg"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb3.jpg" /></a> <h2>Comments:</h2> Excited about seeing them in concert next week. -Lawrence , Jan 23 I dig their latest single. -Mary, Jan 19 Showing 1-2 of 18 comments. <a href="foofighters-comments">More</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/MusicGroup"> <h1 itemprop="name"> Foo Fighters </h1> <div itemprop="subjectOf" itemscope itemtype="https://schema.org/VideoObject"> <h2> Video: <span itemprop="name">Interview with the Foo Fighters</span> </h2> <meta itemprop="duration" content="PT1M33S"> <meta itemprop="thumbnail" content="foo-fighters-interview-thumb.jpg"><object> <param> <embed type="application/x-shockwave-flash"> </object> <span itemprop="description">Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope.</span> <h3> Comments: </h3>Excited about seeing them in concert next week. -Lawrence , Jan 23 I dig their latest single. -Mary, Jan 19 <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <meta itemprop="interactionType" content="https://schema.org/CommentAction"> <meta itemprop="userInteractionCount" content="18"> </div>Showing 1-2 of 18 comments. <a href="foofighters-comments">More</a> </div> <h2> Songs </h2> <div itemprop="track" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">Rope</span> <link itemprop="url" href="foo-fighters-rope.html">Length: <meta itemprop="duration" content="PT4M5S">4:05 - 14300 plays <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <meta itemprop="interactionType" content="https://schema.org/ListenAction"> <meta itemprop="userInteractionCount" content="14300"> </div><a href="foo-fighters-rope-play.html" itemprop="audio">Play</a> <a href="foo-fighters-rope-buy.html" itemprop="offers">Buy</a> From album: <a href="foo-fighters-wasting-light.html" itemprop="inAlbum">Wasting Light</a> </div> <div itemprop="track" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">Everlong</span> <link itemprop="url" href="foo-fighters-everlong.html">Length: <meta itemprop="duration" content="PT6M33S">6:33 - 11700 plays <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <meta itemprop="interactionType" content="https://schema.org/ListenAction"> <meta itemprop="userInteractionCount" content="11700"> </div><a href="foo-fighters-everlong-play.html" itemprop="audio">Play</a> <a href="foo-fighters-everlong-buy.html" itemprop="offers">Buy</a> From album: <a href="foo-fighters-color-and-shape.html" itemprop="inAlbum">The Color And The Shape</a> </div> <h2> Upcoming shows </h2> <div itemprop="event" itemscope itemtype="https://schema.org/Event"> <a href="foo-fighters-may20-fedexforum" itemprop="url"><span itemprop="name">FedExForum</span></a> <span itemprop="location">Memphis, TN, US</span> <meta itemprop="startDate" content="2011-05-20">May 20 <a href="ticketmaster.com/foofighters/may20-2011" itemprop="offers">Buy tickets</a> </div> <div itemprop="event" itemscope itemtype="https://schema.org/Event"> <a href="foo-fighters-may23-midamericacenter" itemprop="url"><span itemprop="name">Mid America Center</span></a> <span itemprop="location">Council Bluffs, IA, US</span> <meta itemprop="startDate" content="2011-05-23">May 23 <a href="ticketmaster.com/foofighters/may23-2011" itemprop="offers">Buy tickets</a> </div> <h2> <a href="foo-fighters-photos">28 Photos</a> </h2><a href="foofighters-1.jpg" itemprop="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb1.jpg"></a> <a href="foofighters-2.jpg" itemprop="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb2.jpg"></a> <a href="foofighters-3.jpg" itemprop="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb3.jpg"></a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="MusicGroup"> <h1 property="name"> Foo Fighters </h1> <div property="subjectOf" typeof="VideoObject"> <h2> Video: <span property="name">Interview with the Foo Fighters</span> </h2> <meta property="duration" content="PT1M33S"> <meta property="thumbnail" content="foo-fighters-interview-thumb.jpg"><object> <param> <embed type="application/x-shockwave-flash"> </object> <span property="description">Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope.</span> <h3> Comments: </h3>Excited about seeing them in concert next week. -Lawrence , Jan 23 I dig their latest single. -Mary, Jan 19 <div property="interactionStatistic" typeof="https://schema.org/InteractionCounter"> <meta property="interactionType" content="https://schema.org/CommentAction"> <meta property="userInteractionCount" content="18"> </div>Showing 1-2 of 18 comments. <a href="foofighters-comments">More</a> </div> <h2> Songs </h2> <div property="track" typeof="MusicRecording"> <span property="name">Rope</span> <link property="url" href="foo-fighters-rope.html">Length: <meta property="duration" content="PT4M5S">4:05 - 14300 plays <div property="interactionStatistic" typeof="https://schema.org/InteractionCounter"> <meta property="interactionType" content="https://schema.org/ListenAction"> <meta property="userInteractionCount" content="14300"> </div><a href="foo-fighters-rope-play.html" property="audio">Play</a> <a href="foo-fighters-rope-buy.html" property="offers">Buy</a> From album: <a href="foo-fighters-wasting-light.html" property="inAlbum">Wasting Light</a> </div> <div property="track" typeof="MusicRecording"> <span property="name">Everlong</span> <link property="url" href="foo-fighters-everlong.html">Length: <meta property="duration" content="PT6M33S">6:33 - 11700 plays <div property="interactionStatistic" typeof="https://schema.org/InteractionCounter"> <meta property="interactionType" content="https://schema.org/ListenAction"> <meta property="userInteractionCount" content="11700"> </div><a href="foo-fighters-everlong-play.html" property="audio">Play</a> <a href="foo-fighters-everlong-buy.html" property="offers">Buy</a> From album: <a href="foo-fighters-color-and-shape.html" property="inAlbum">The Color And The Shape</a> </div> <h2> Upcoming shows </h2> <div property="event" typeof="Event"> <a href="foo-fighters-may20-fedexforum" property="url"><span property="name">FedExForum</span></a> <span property="location">Memphis, TN, US</span> <meta property="startDate" content="2011-05-20">May 20 <a href="ticketmaster.com/foofighters/may20-2011" property="offers">Buy tickets</a> </div> <div property="event" typeof="Event"> <a href="foo-fighters-may23-midamericacenter" property="url"><span property="name">Mid America Center</span></a> <span property="location">Council Bluffs, IA, US</span> <meta property="startDate" content="2011-05-23">May 23 <a href="ticketmaster.com/foofighters/may23-2011" property="offers">Buy tickets</a> </div> <h2> <a href="foo-fighters-photos">28 Photos</a> </h2><a href="foofighters-1.jpg" property="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb1.jpg"></a> <a href="foofighters-2.jpg" property="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb2.jpg"></a> <a href="foofighters-3.jpg" property="image"><img alt="Thumbnail and linked photo of Foo Fighters band" src="foofighters-thumb3.jpg"></a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicGroup", "event": [ { "@type": "Event", "location": "Memphis, TN, US", "offers": "ticketmaster.com/foofighters/may20-2011", "startDate": "2011-05-20", "url": "foo-fighters-may20-fedexforum" }, { "@type": "Event", "location": "Council Bluffs, IA, US", "offers": "ticketmaster.com/foofighters/may23-2011", "startDate": "2011-05-23", "url": "foo-fighters-may23-midamericacenter" } ], "image": [ "foofighters-1.jpg", "foofighters-2.jpg", "foofighters-3.jpg" ], "name": "Foo Fighters", "track": [ { "@type": "MusicRecording", "audio": "foo-fighters-rope-play.html", "duration": "PT4M5S", "inAlbum": "foo-fighters-wasting-light.html", "interactionStatistic": { "@type": "InteractionCounter", "interactionType": "https://schema.org/ListenAction", "userInteractionCount": "14300" }, "name": "Rope", "offers": "foo-fighters-rope-buy.html", "url": "foo-fighters-rope.html" }, { "@type": "MusicRecording", "audio": "foo-fighters-everlong-play.html", "duration": "PT6M33S", "inAlbum": "foo-fighters-color-and-shape.html", "name": "Everlong", "interactionStatistic": { "@type": "InteractionCounter", "interactionType": "https://schema.org/ListenAction", "userInteractionCount": "11700" }, "offers": "foo-fighters-everlong-buy.html", "url": "foo-fighters-everlong.html" } ], "subjectOf": { "@type": "VideoObject", "description": "Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope.", "duration": "PT1M33S", "name": "Interview with the Foo Fighters", "thumbnail": "foo-fighters-interview-thumb.jpg", "interactionStatistic": { "@type": "InteractionCounter", "interactionType": "https://schema.org/CommentAction", "userInteractionCount": "18" } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0174)

Copied

Example notes or example HTML without markup.

JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0189)

Copied

Example notes or example HTML without markup.

<div> <h2>Shostakovich Leningrad</h2> <div> <div>May<span>23</span></div> <div>8:00 PM</div> <div> <strong>Britten, Shostakovich</strong> </div> </div> <div> <p>Jaap van Zweden conducts two World War II-era pieces showcasing the glorious sound of the CSO.</p> </div> <div> <h3>Program</h3> <ul> <li> <link href="http://en.wikipedia.org/wiki/Peter_Grimes" /> <span><strong>Britten</strong> Four Sea Interludes and Passacaglia from <em>Peter Grimes</em></span> </li> <li> <link href="http://en.wikipedia.org/wiki/Symphony_No._7_(Shostakovich)" /> <span><strong>Shostakovich</strong> Symphony No. 7 <em>(Leningrad)</em></span> </li> </ul> </div> <div> <h3>Performers</h3> <div> <img src="/examples/cso_c_logo_s.jpg" alt="Chicago Symphony Orchestra" /> <link href="http://cso.org/" /> <link href="http://en.wikipedia.org/wiki/Chicago_Symphony_Orchestra" /> <div> <a href="examples/Performer?id=4434">Chicago Symphony Orchestra</a> </div> </div> <div> <link href="http://www.jaapvanzweden.com/" /> <img src="/examples/jvanzweden_s.jpg" alt="Jaap van Zweden"/> <div> <a href="/examples/Performer.aspx?id=11324">Jaap van Zweden</a> </div> <div>conductor</div> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope="" itemtype="https://schema.org/MusicEvent"> <div itemprop="location" itemscope="" itemtype="https://schema.org/MusicVenue"> <meta itemprop="name" content="Chicago Symphony Center"/> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Symphony_Center"/> <meta itemprop="address" content="220 S. Michigan Ave, Chicago, Illinois, USA"/> </div> <div itemprop="offers" itemscope="" itemtype="https://schema.org/Offer"> <link itemprop="url" href="/examples/ticket/12341234" /> <meta itemprop="price" content="40"/> <meta itemprop="priceCurrency" content="USD" /> <link itemprop="availability" href="https://schema.org/InStock"/> </div> <h2 itemprop="name">Shostakovich Leningrad</h2> <div> <div itemprop="startDate" content="2014-05-23T20:00">May<span>23</span></div> <div>8:00 PM</div> <div> <strong>Britten, Shostakovich</strong> </div> </div> <div> <p>Jaap van Zweden conducts two World War II-era pieces showcasing the glorious sound of the CSO.</p> </div> <div> <h3>Program</h3> <ul> <li itemprop="workPerformed" itemscope="" itemtype="https://schema.org/CreativeWork"> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Peter_Grimes" /> <span itemprop="name"><strong>Britten</strong> Four Sea Interludes and Passacaglia from <em itemprop="name">Peter Grimes</em></span> </li> <li itemprop="workPerformed" itemscope="" itemtype="https://schema.org/CreativeWork"> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Symphony_No._7_(Shostakovich)" /> <span itemprop="name"><strong>Shostakovich</strong> Symphony No. 7 <em>(Leningrad)</em></span> </li> </ul> </div> <div> <h3>Performers</h3> <div itemprop="performer" itemscope="" itemtype="https://schema.org/MusicGroup"> <img src="/examples/cso_c_logo_s.jpg" alt="Chicago Symphony Orchestra" /> <link itemprop="sameAs" href="http://cso.org/" /> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Chicago_Symphony_Orchestra" /> <div> <a href="examples/Performer?id=4434"><span itemprop="name">Chicago Symphony Orchestra</span></a> </div> </div> <div itemprop="performer" itemscope="" itemtype="https://schema.org/Person"> <link itemprop="sameAs" href="http://www.jaapvanzweden.com/" /> <img itemprop="image" src="/examples/jvanzweden_s.jpg" alt="Jaap van Zweden"/> <div> <a href="/examples/Performer.aspx?id=11324"><span itemprop="name">Jaap van Zweden</span></a> </div> <div>conductor</div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="MusicEvent"> <div property="location" typeof="MusicVenue"> <meta property="name" content="Chicago Symphony Center"/> <link property="sameAs" href="http://en.wikipedia.org/wiki/Symphony_Center"/> <meta property="address" content="220 S. Michigan Ave, Chicago, Illinois, USA"/> </div> <div property="offers" typeof="Offer"> <link property="url" href="/examples/ticket/12341234"/> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="40"/>40.00 <link property="availability" href="https://schema.org/InStock"/> </div> <h2 property="name">Shostakovich Leningrad</h2> <div> <div property="startDate" content="2014-05-23T20:00">May<span>23</span></div> <div>8:00 PM</div> <div> <strong>Britten, Shostakovich</strong> </div> </div> <div> <p>Jaap van Zweden conducts two World War II-era pieces showcasing the glorious sound of the CSO.</p> </div> <div> <h3>Program</h3> <ul> <li property="workPerformed" typeof="CreativeWork"> <link href="http://en.wikipedia.org/wiki/Peter_Grimes" property="sameAs"/> <span property="name"><strong>Britten</strong> Four Sea Interludes and Passacaglia from <em property="name">Peter Grimes</em></span> </li> <li property="workPerformed" typeof="CreativeWork"> <link href="http://en.wikipedia.org/wiki/Symphony_No._7_(Shostakovich)" property="sameAs"/> <span property="name"><strong>Shostakovich</strong> Symphony No. 7 <em>(Leningrad)</em></span> </li> </ul> </div> <div> <h3>Performers</h3> <div property="performer" typeof="MusicGroup"> <img src="/examples/cso_c_logo_s.jpg" alt="Chicago Symphony Orchestra"/> <link href="http://cso.org/" property="sameAs"/> <link href="http://en.wikipedia.org/wiki/Chicago_Symphony_Orchestra" property="sameAs"/> <span property="name"><a href="examples/Performer?id=4434">Chicago Symphony Orchestra</a></span> </div> <div property="performer" typeof="Person"> <link href="http://www.jaapvanzweden.com/" property="sameAs"/> <img src="/examples/jvanzweden_s.jpg" alt="Jaap van Zweden" property="image"/> <span property="name"><a href="/examples/Performer.aspx?id=11324">Jaap van Zweden</a></span> <div>conductor</div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicEvent", "location": { "@type": "MusicVenue", "name": "Chicago Symphony Center", "address": "220 S. Michigan Ave, Chicago, Illinois, USA" }, "name": "Shostakovich Leningrad", "offers": { "@type": "Offer", "url": "/examples/ticket/12341234", "price": "40", "priceCurrency": "USD", "availability": "https://schema.org/InStock" }, "performer": [ { "@type": "MusicGroup", "name": "Chicago Symphony Orchestra", "sameAs": [ "http://cso.org/", "http://en.wikipedia.org/wiki/Chicago_Symphony_Orchestra" ] }, { "@type": "Person", "image": "/examples/jvanzweden_s.jpg", "name": "Jaap van Zweden", "sameAs": "http://www.jaapvanzweden.com/" } ], "startDate": "2014-05-23T20:00", "workPerformed": [ { "@type": "CreativeWork", "name": "Britten Four Sea Interludes and Passacaglia from Peter Grimes", "sameAs": "http://en.wikipedia.org/wiki/Peter_Grimes" }, { "@type": "CreativeWork", "name": "Shostakovich Symphony No. 7 (Leningrad)", "sameAs": "http://en.wikipedia.org/wiki/Symphony_No._7_(Shostakovich)" } ] } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0387)

Copied

Example notes or example HTML without markup.

An example of possible JSON-LD for Let It Be by the Beatles.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicAlbum", "@id": "http://musicbrainz.org/release-group/bff544a7-56e0-3ed6-9e0f-3b676cca9111", "name": "Let It Be", "sameAs": [ "http://en.wikipedia.org/wiki/Let_It_Be", "http://www.wikidata.org/wiki/Q199585" ], "image": "http://coverartarchive.org/release-group/bff544a7-56e0-3ed6-9e0f-3b676cca9111/front.jpg", "albumProductionType": "https://schema.org/StudioAlbum", "albumReleaseType": "https://schema.org/AlbumRelease", "genre": "rock", "byArtist": { "@type": "MusicGroup", "name": "The Beatles", "@id": "http://musicbrainz.org/artist/b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d" }, "albumRelease": { "@type": "MusicRelease", "name": "Let It Be", "@id": "http://musicbrainz.org/release/8d5347a5-9ecb-44be-a213-860aaaf5d0b8" }, "track": { "@type": "ItemList", "numberOfItems": 12, "itemListElement": [ { "@type": "ListItem", "position": 1, "item": { "@type": "MusicRecording", "name": "Two Of Us" } }, { "@type": "ListItem", "position": 2, "item": { "@type": "MusicRecording", "name": "Dig a Pony" } }, { "@type": "ListItem", "position": 3, "item": { "@type": "MusicRecording", "name": "Across the Universe" } } ] } } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0389)

Copied

Example notes or example HTML without markup.

MusicGroup Example. Sample JSON-LD for the Beatles as described by MusicBrainz.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicGroup", "@id": "http://musicbrainz.org/artist/b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d", "name": "Beatles", "sameAs": "http://www.thebeatles.com", "foundingLocation": { "@type": "City", "name": "Liverpool" }, "foundingDate": "1957", "dissolutionDate": "1970", "genre": "Rock", "album": { "@type": "MusicAlbum", "name": "The Beatles", "alternateName": "The White Album", "@id": "http://musicbrainz.org/release-group/055be730-dcad-31bf-b550-45ba9c202aa3", "datePublished": "1968" }, "member": [ { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "John Lennon" }, "startDate": "1957", "endDate": "1970", "roleName": ["guitar", "lead vocals"] }, { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Paul McCartney" }, "startDate": "1957", "endDate": "1970", "roleName": ["bass guitar", "lead vocals"] }, { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "George Harrison" }, "startDate": "1958", "endDate": "1970", "roleName": ["guitar", "lead vocals"] }, { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Ringo Starr" }, "startDate": "1962", "endDate": "1970", "roleName": "drums" } ] } </script>

Structured representation of the JSON-LD example.
