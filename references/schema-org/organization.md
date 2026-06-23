---
title: "Organization"
source_url: https://schema.org/Organization
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Organization

# Organization

A Schema.org Type

- Canonical URL: https://schema.org/Organization
-
Equivalent Class: gs1:Organization

Equivalent Class: fibo-fnd-org-org:Organization [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Organization)

An organization such as a school, NGO, corporation, club, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[Organization](/Organization)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[OwnershipInfo](/OwnershipInfo)[affiliation](/affiliation)

[Person](/Person)[agent](/agent)

[Action](/Action)*John*wrote a book.[alumniOf](/alumniOf)

[Person](/Person)[attendee](/attendee)

[Event](/Event)[attendees](/attendees)

[Event](/Event)[authenticator](/authenticator)

[MediaSubscription](/MediaSubscription)[author](/author)

[CreativeWork](/CreativeWork)or[Rating](/Rating)[bccRecipient](/bccRecipient)

[Message](/Message)[bookingAgent](/bookingAgent)

[Reservation](/Reservation)[branchOf](/branchOf)

[LocalBusiness](/LocalBusiness)[branch](/branch).[brand](/brand)

[Organization](/Organization)or[Person](/Person)or[Product](/Product)or[Service](/Service)[broadcastAffiliateOf](/broadcastAffiliateOf)

[BroadcastService](/BroadcastService)[broadcaster](/broadcaster)

[BroadcastService](/BroadcastService)[broker](/broker)

[Invoice](/Invoice)or[Order](/Order)or[Reservation](/Reservation)or[Service](/Service)[buyer](/buyer)

[SellAction](/SellAction)[carrier](/carrier)

[Flight](/Flight)or[ParcelDelivery](/ParcelDelivery)[ccRecipient](/ccRecipient)

[Message](/Message)[claimInterpreter](/claimInterpreter)

[Claim](/Claim)[Claim](/Claim)interpreted from[MediaObject](/MediaObject)content, the[interpretedAsClaim](/interpretedAsClaim)property can be used to indicate a claim contained, implied or refined from the content of a[MediaObject](/MediaObject).[composer](/composer)

[Event](/Event)or[MusicComposition](/MusicComposition)[contributor](/contributor)

[CreativeWork](/CreativeWork)or[Event](/Event)[copyrightHolder](/copyrightHolder)

[CreativeWork](/CreativeWork)[creator](/creator)

[CreativeWork](/CreativeWork)or[UserComments](/UserComments)[creditedTo](/creditedTo)

[MusicRelease](/MusicRelease)[customer](/customer)

[Invoice](/Invoice)or[Order](/Order)[department](/department)

[Organization](/Organization)[eligibleWithSupplier](/eligibleWithSupplier)

[FinancialIncentive](/FinancialIncentive)[employmentUnit](/employmentUnit)

[JobPosting](/JobPosting)[endorsee](/endorsee)

[EndorseAction](/EndorseAction)[endorsers](/endorsers)

[Diet](/Diet)[followee](/followee)

[FollowAction](/FollowAction)[founder](/founder)

[Organization](/Organization)[fundedItem](/fundedItem)

[Grant](/Grant)[Grant](/Grant). See also[ownershipFundingInfo](/ownershipFundingInfo).[funder](/funder)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Grant](/Grant)or[MonetaryGrant](/MonetaryGrant)or[Organization](/Organization)or[Person](/Person)[grantee](/grantee)

[DigitalDocumentPermission](/DigitalDocumentPermission)[hiringOrganization](/hiringOrganization)

[JobPosting](/JobPosting)[hostingOrganization](/hostingOrganization)

[MemberProgram](/MemberProgram)or[ProgramMembership](/ProgramMembership)[issuedBy](/issuedBy)

[Certification](/Certification)or[Permit](/Permit)or[Ticket](/Ticket)[Permit](/Permit),[Ticket](/Ticket), or[Certification](/Certification).[landlord](/landlord)

[RentAction](/RentAction)[legislationCountersignedBy](/legislationCountersignedBy)

[Legislation](/Legislation)[legislationPassedBy](/legislationPassedBy)

[Legislation](/Legislation)[legislationResponsible](/legislationResponsible)

[Legislation](/Legislation)[lender](/lender)

[BorrowAction](/BorrowAction)[maintainer](/maintainer)

[CreativeWork](/CreativeWork)[Dataset](/Dataset), software package ([SoftwareApplication](/SoftwareApplication)), or other[Project](/Project). A maintainer is a[Person](/Person)or[Organization](/Organization)that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When[maintainer](/maintainer)is applied to a specific version of something e.g. a particular version or packaging of a[Dataset](/Dataset), it is always possible that the upstream source has a different maintainer. The[isBasedOn](/isBasedOn)property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.[manufacturer](/manufacturer)

[Product](/Product)[member](/member)

[Organization](/Organization)or[ProgramMembership](/ProgramMembership)[memberOf](/memberOf)

[Organization](/Organization)or[Person](/Person)[members](/members)

[Organization](/Organization)or[ProgramMembership](/ProgramMembership)[merchant](/merchant)

[Order](/Order)[offeredBy](/offeredBy)

[Offer](/Offer)[organizer](/organizer)

[Event](/Event)[owner](/owner)

[Thing](/Thing)[parentOrganization](/parentOrganization)

[Organization](/Organization)[subOrganization](/subOrganization)of, if any.[participant](/participant)

[Action](/Action)*Steve*.[performer](/performer)

[Event](/Event)[performers](/performers)

[Event](/Event)[producer](/producer)

[CreativeWork](/CreativeWork)[productionCompany](/productionCompany)

[CreativeWorkSeason](/CreativeWorkSeason)or[Episode](/Episode)or[MediaObject](/MediaObject)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGameSeries](/VideoGameSeries)[provider](/provider)

[Action](/Action)or[CreativeWork](/CreativeWork)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[FinancialIncentive](/FinancialIncentive)or[Invoice](/Invoice)or[ParcelDelivery](/ParcelDelivery)or[Reservation](/Reservation)or[Service](/Service)or[Trip](/Trip)[publishedBy](/publishedBy)

[PublicationEvent](/PublicationEvent)[publisher](/publisher)

[CreativeWork](/CreativeWork)or[FinancialIncentive](/FinancialIncentive)[publisherImprint](/publisherImprint)

[CreativeWork](/CreativeWork)[recipient](/recipient)

[AuthorizeAction](/AuthorizeAction)or[CommunicateAction](/CommunicateAction)or[DonateAction](/DonateAction)or[GiveAction](/GiveAction)or[Message](/Message)or[PayAction](/PayAction)or[ReturnAction](/ReturnAction)or[SendAction](/SendAction)or[TipAction](/TipAction)[recognizedBy](/recognizedBy)

[Credential](/Credential)[recognizingAuthority](/recognizingAuthority)

[MedicalEntity](/MedicalEntity)[recordLabel](/recordLabel)

[MusicRelease](/MusicRelease)[reviewedBy](/reviewedBy)

[WebPage](/WebPage)[sdPublisher](/sdPublisher)

[CreativeWork](/CreativeWork)[sdPublisher](/sdPublisher)property helps make such practices more explicit.[seller](/seller)

[BuyAction](/BuyAction)or[Demand](/Demand)or[Flight](/Flight)or[Offer](/Offer)or[Order](/Order)[sender](/sender)

[Message](/Message)or[ReceiveAction](/ReceiveAction)[serviceOperator](/serviceOperator)

[GovernmentService](/GovernmentService)[sourceOrganization](/sourceOrganization)

[CreativeWork](/CreativeWork)[spokenByCharacter](/spokenByCharacter)

[Quotation](/Quotation)[sponsor](/sponsor)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Grant](/Grant)or[MedicalStudy](/MedicalStudy)or[Organization](/Organization)or[Person](/Person)[subOrganization](/subOrganization)

[Organization](/Organization)[toRecipient](/toRecipient)

[Message](/Message)[translator](/translator)

[CreativeWork](/CreativeWork)or[Event](/Event)[underName](/underName)

[Reservation](/Reservation)or[Ticket](/Ticket)[vendor](/vendor)

[BuyAction](/BuyAction)[worksFor](/worksFor)

[Person](/Person)#### More specific Types

-
[Airline](/Airline) -
[Consortium](/Consortium) -
[Cooperative](/Cooperative) -
[Corporation](/Corporation) -
[EducationalOrganization](/EducationalOrganization) -
[FundingScheme](/FundingScheme) -
[GovernmentOrganization](/GovernmentOrganization) -
[LibrarySystem](/LibrarySystem) -
[LocalBusiness](/LocalBusiness) -
[MedicalOrganization](/MedicalOrganization) -
[NGO](/NGO) -
[NewsMediaOrganization](/NewsMediaOrganization) -
[OnlineBusiness](/OnlineBusiness) -
[PerformingGroup](/PerformingGroup) -
[PoliticalParty](/PoliticalParty) -
[Project](/Project) -
[ResearchOrganization](/ResearchOrganization) -
[SearchRescueOrganization](/SearchRescueOrganization) -
[SportsOrganization](/SportsOrganization) -
[WorkersUnion](/WorkersUnion)

### Examples

[Example 1](#eg-0007)

Copied

Example notes or example HTML without markup.

Google.Org Contact Details: Main address: 38 avenue de l'Opéra, F-75002 Paris, France Tel: ( 33 1) 42 68 53 00, Fax: ( 33 1) 42 68 53 01 E-mail: secretariat (at) google.org URL: <a href="http://www.google.org">www.google.org</a> SIRET Code: 443 061 841 00039 VAT Number: FR64443061841 Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: Member 1, Member 2 History:

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">Google.org (GOOG)</span> Contact Details: <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> Main address: <span itemprop="streetAddress">38 avenue de l'Opéra</span> <span itemprop="postalCode">F-75002</span> <span itemprop="addressLocality">Paris, France</span> , </div> Tel:<span itemprop="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span itemprop="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span itemprop="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jack Dan</span> </span>, <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">John Smith</span> </span>, History: </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Organization"> <span property="name">Google.org (GOOG)</span> Contact Details: <div property="address" typeof="PostalAddress"> Main address: <span property="streetAddress">38 avenue de l'Opera</span> <span property="postalCode">F-75002</span> <span property="addressLocality">Paris, France</span> , </div> Tel:<span property="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span property="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span property="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span property="alumni" typeof="Person"> <span property="name">Jack Dan</span> </span>, <span property="alumni" typeof="Person"> <span property="name">John Smith</span> </span> History: </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Organization", "address": { "@type": "PostalAddress", "addressLocality": "Paris, France", "postalCode": "F-75002", "streetAddress": "38 avenue de l'Opéra" }, "email": "secretariat@example.com", "faxNumber": "+33142685301", "iso6523Code": [ "0009:44306184100039", "9957:FR64443061841" ], "member": [ { "@type": "Organization" }, { "@type": "Organization" } ], "alumni": [ { "@type": "Person", "name": "Jack Dan" }, { "@type": "Person", "name": "John Smith" } ], "name": "Google.org (GOOG)", "telephone": "+33 1 42 68 53 00" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0199)

Copied

Example notes or example HTML without markup.

Example specifying one customer service phone number.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Organization", "url" : "http://www.your-company-site.com", "contactPoint" : [ { "@type" : "ContactPoint", "telephone" : "+1-401-555-1212", "contactType" : "customer service" } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0200)

Copied

Example notes or example HTML without markup.

A fuller example that illustrates multiple contact numbers for a company, including US toll-free numbers, a hearing-impaired number, and several contact categories.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Organization", "url" : "http://www.t-mobile.com", "contactPoint" : [ { "@type" : "ContactPoint", "telephone" : "+1-877-746-0909", "contactType" : "customer service", "contactOption" : "TollFree", "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-505-998-3793", "contactType" : "customer service" } , { "@type" : "ContactPoint", "telephone" : "+1-877-296-1018", "contactType" : "customer service", "contactOption" : ["HearingImpairedSupported","TollFree"] , "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "technical support", "contactOption" : "TollFree", "areaServed" : ["US","CA"], "availableLanguage" : ["English","French"] } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "bill payment", "contactOption" : "TollFree", "areaServed" : ["US","CA"] } ] } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0206)

Copied

Example notes or example HTML without markup.

A JSON example of an OrganizationRole, showing information about a 'member' of a 'SportsTeam', including time qualfiers (when he began and ended that role).

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/SportsTeam"> <span itemprop="name">San Francisco 49ers</span> <div itemprop="member" itemscope itemtype="https://schema.org/OrganizationRole"> <div itemprop="member" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Joe Montana</span> </div> <span itemprop="startDate">1979</span> <span itemprop="endDate">1992</span> <span itemprop="roleName">Quarterback</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="SportsTeam"> <span property="name">San Francisco 49ers</span> <div property="member" typeof="OrganizationRole"> <div property="member" typeof="https://schema.org/Person"> <span property="name">Joe Montana</span> </div> <span property="startDate">1979</span> <span property="endDate">1992</span> <span property="roleName">Quarterback</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SportsTeam", "name": "San Francisco 49ers", "member": { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Joe Montana" }, "startDate": "1979", "endDate": "1992", "roleName": "Quarterback" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0296)

Copied

Example notes or example HTML without markup.

An organization with a number of likes and follows.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Organization", "name": "ACME", "interactionStatistic": [ { "@type": "InteractionCounter", "interactionType": "https://schema.org/LikeAction", "userInteractionCount": 1170 }, { "@type": "InteractionCounter", "interactionType": "https://schema.org/FollowAction", "userInteractionCount": 145098 } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0376)

Copied

Example notes or example HTML without markup.

An example of an order for multiple items, shipped separately. ACME Supplies Customer: Jane Doe Order: Item abc123: 1 Widget: delivered 2015-03-10 Item def456: 3 Widget accessories: shipped 2015-03-12

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Order"> <div itemprop="seller" itemscope itemtype="https://schema.org/Organization"> <b itemprop="name">ACME Supplies</b> </div> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">abc123</span> <span itemprop="orderQuantity">1</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-10</time> </div> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">def456</span> <span itemprop="orderQuantity">4</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget accessories</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-15</time> <time itemprop="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Order"> <div property="seller" typeof="Organization"> <b property="name">ACME Supplies</b> </div> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">abc123</span> <span property="orderQuantity">1</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-10</time> </div> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">def456</span> <span property="orderQuantity">4</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget accessories</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-15</time> <time property="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Order", "seller": { "@type": "Organization", "name": "ACME Supplies" }, "customer": { "@type": "Person", "name": "Jane Doe" }, "orderedItem": [ { "@type": "OrderItem", "orderItemNumber": "abc123", "orderQuantity": 1, "orderedItem": { "@type": "Product", "name": "Widget" }, "orderItemStatus": "https://schema.org/OrderDelivered", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-10" } }, { "@type": "OrderItem", "orderItemNumber": "def456", "orderQuantity": 3, "orderedItem": { "@type": "Product", "name": "Widget accessories" }, "orderItemStatus": "https://schema.org/OrderInTransit", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-15", "expectedArrivalUntil": "2015-03-18" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0388)

Copied

Example notes or example HTML without markup.

A MusicComposition Example. The following JSON-LD models the composition A Day in the Life by Lennon and McCartney, regardless of who performs or records the song.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicComposition", "@id": "http://musicbrainz.org/work/fd1aa4f2-ba26-3a05-b72d-4392c35a073c", "name": "A Day in the Life", "composer": [ { "@type": "Person", "name": "John Lennon", "@id": "http://musicbrainz.org/artist/4d5447d7-c61c-4120-ba1b-d7f471d385b9" }, { "@type": "Person", "name": "Paul McCartney", "@id": "http://musicbrainz.org/artist/ba550d0e-adac-4864-b88b-407cab5e76af" } ], "iswcCode": "T-010.140.236-1", "publisher": { "@type": "Organization", "name": "Northern Songs, Ltd.", "@id": "http://musicbrainz.org/label/26df054d-78cf-4d83-9bb1-a41816125528" }, "datePublished": "1967", "lyrics": { "@type": "CreativeWork", "inLanguage": "EN", "text": "I read the news today oh boy..." } } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0429)

Copied

Example notes or example HTML without markup.

<p> <a href="http://npr.org">National Public Radio</a> has a sponsor: <a href="http://www.example.com/GloboCorp">GloboCorp</a>. </p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<p itemscope itemprop="organization" itemtype="https://schema.org/Organization"> <a href="http://npr.org" itemprop="url"> <span itemprop="name">National Public Radio</span></a> has a sponsor: <span itemprop="sponsor" itemscope itemtype="https://schema.org/Organization"> <a itemprop="url" href="http://www.example.com/GloboCorp"> <span itemprop="name">GloboCorp</span></a> </span>. </p>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<p vocab="https://schema.org/" typeof="Organization"> <a href="http://npr.org" property="url"> <span property="name">National Public Radio</span></a> has a sponsor, <span property="sponsor" typeof="https://schema.org/Organization"> <a property="url" href="http://www.example.com/GloboCorp"> <span property="name">GloboCorp</span></a> </span>. </p>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Organization", "name": "National Public Radio", "url": "http://npr.org", "sponsor": { "@type": "Organization", "name": "GloboCorp", "url": "http://www.example.com/" } } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0442)

Copied

Example notes or example HTML without markup.

WAAY is an affiliate of the ABC network and broadcasts in SD.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WAAY-TV</span> <span itemprop="broadcastDisplayName">ABC</span> <span itemprop="videoFormat">SD</span> <span itemprop="broadcastTimezone" content="-8:00">PST</span> <div itemprop="broadcastAffiliateOf" itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">ABC</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="BroadcastService"> <span property="name">WAAY-TV</span> <span property="broadcastDisplayName">ABC</span> <span property="videoFormat">SD</span> <span property="broadcastTimezone" content="-8:00">PST</span> <div property="broadcastAffiliateOf" typeof="Organization"> <span property="name">ABC</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name":"WAAY-TV", "broadcastDisplayName":"ABC", "videoFormat":"SD", "broadcastTimezone": "-8:00", "broadcastAffiliateOf":{ "@type":"Organization", "name":"ABC" } } </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0443)

Copied

Example notes or example HTML without markup.

WAAY is channel 7 on Comcast cable.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TelevisionChannel"> <span itemprop="name">WAAY 7</span> <span itemprop="broadcastChannelId">7</span> <span itemprop="broadcastServiceTier">Premium</span> <div itemprop="inBroadcastLineup" itemscope itemtype="https://schema.org/CableOrSatelliteService"> <span itemprop="name">Comcast</span> </div> <div itemprop="providesBroadcastService" itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WAAY-TV</span> <span itemprop="broadcastDisplayName">ABC</span> <div itemprop="broadcastAffiliateOf" itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">ABC</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="TelevisionChannel"> <span property="name">WAAY 7</span> <span property="broadcastChannelId">7</span> <span property="broadcastServiceTier">Premium</span> <div property="inBroadcastLineup" typeof="CableOrSatelliteService"> <span property="name">Comcast</span> </div> <div property="providesBroadcastService" typeof="BroadcastService"> <span property="name">WAAY-TV</span> <span property="broadcastDisplayName">ABC</span> <div property="broadcastAffiliateOf" typeof="Organization"> <span property="name">ABC</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"TelevisionChannel", "name": "WAAY 7", "broadcastChannelId":"7", "broadcastServiceTier":"Premium", "inBroadcastLineup":{ "@type":"CableOrSatelliteService", "name": "Comcast" }, "providesBroadcastService":{ "@type":"BroadcastService", "name": "WAAY-TV", "broadcastDisplayName": "ABC", "broadcastAffiliateOf":{ "@type":"Organization", "name":"ABC" } } } </script>

Structured representation of the JSON-LD example.

[Example 11](#eg-3617b)

Copied

Example notes or example HTML without markup.

Organization with free shipping worldwide for members (in the V2 Shipping format) and paid shipping for non-members.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Organization", "name": "Example Inc.", "hasShippingService": [ { "@type": "ShippingService", "name": "Members Free Shipping", "description": "Free shipping worldwide for Gold and Platinum members.", "validForMemberTier": [ { "@id": "https://www.example.com/membership-plus#tier_gold" }, { "@id": "https://www.example.com/membership-plus#tier_platinum" } ], "shippingConditions": { "@type": "ShippingConditions", "shippingRate": "0" } }, { "@type": "ShippingService", "name": "Standard Shipping", "description": "Flat-fee worldwide shipping.", "shippingConditions": { "@type": "ShippingConditions", "shippingRate": { "@type": "MonetaryAmount", "value": "9.99", "currency": "USD" } } } ] } </script>

Structured representation of the JSON-LD example.

[Example 12](#eg-4505)

Copied

Example notes or example HTML without markup.

<strong>Château Snotty 2020</strong> The snottiest red wine on the market. <ul> <li>Organic red wine, made in France</li> <li>2020 Vintage, a very interesting year</li> <li>75 cl bottle</li> <li>Cru du Pichet d'Or</li> <li>Best before 2026</li> <li>Contains Sulfite</li> <li>Please recycle the glass bottle</li> </ul>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": { "@vocab": "https://schema.org/", "gs1": "https://ref.gs1.org/voc/", "unece": "https://vocabulary.uncefact.org/" }, "@graph": [ { "@type": [ "https://schema.org/DefinedRegion", "https://schema.org/PostalAddress" ], "@id": "http://example.com/lechateausnottyaddress", "addressCountry": "FR", "addressLocality": "L'Introuvable", "addressRegion": "Charentes" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottynetmass", "name": "Net mass", "unitCode": "KGM", "unitText": "kg.", "value": 0.75, "gs1:unitCode": "KGM", "gs1:value": 0.75, "unece:MeasureTypeValue": 75, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#AAA" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottygrossmass", "name": "Gross mass", "unitCode": "KGM", "unitText": "kg.", "value": 1, "gs1:unitCode": "KGM", "gs1:value": 1, "unece:MeasureTypeValue": 1, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#ACN" }, { "@type": [ "Organization", "gs1:Organization", "unece:TradeParty" ], "@id": "http://example.com/lechateausnotty", "name": "Domaine du Château Snotty", "address": { "@id": "http://example.com/lechateausnottyaddress" }, "unece:allianceName": "Les Châteaux obscurs de Charente" }, { "@type": [ "Organization", "gs1:Organization" ], "@id": "http://example.com/oenologuesatteres", "name": "Association des Œnologues attérés" }, { "@type": [ "Certification", "unece:TradeProductCertification" ], "@id": "http://example.com/certifiedpretentiouswine", "name": "Certified Pretentious Wine", "certificationIdentification": "pichetdor", "issuedBy": { "@id": "http://example.com/oenologuesatteres" }, "certificationRating": { "@type": "Rating", "ratingValue": "Pichet d'Or" } }, { "@type": [ "Product", "unece:TradeProduct", "gs1:Beverage" ], "name": "Château Snotty 2020", "description": [ { "@value": "The snottiest red wine on the market.", "@language": "en" }, { "@value": "Le vin le plus prétentieux du marché.", "@language": "fr" } ], "url": "https://www.example.com/chateau-snotty", "image": "https://www.example.com/chateau-snotty.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "priceValidUntil": "2026-01-01", "price": "999.00", "priceCurrency": "EUR", "seller": { "@id": "http://example.com/lechateausnotty" }, "hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "EU", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted" }, "shippingDetails": { "@type": "OfferShippingDetails", "shippingDestination": { "@type": "DefinedRegion", "name": "Europe", "addressCountry": "EU" }, "shippingRate": { "@type": "MonetaryAmount", "name": "Free", "value": 0, "currency": "EUR" }, "deliveryTime": { "@type": "ShippingDeliveryTime", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitText": "Days", "unitCode": "DAY" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5, "unitText": "Days", "unitCode": "DAY" } }, "hasShippingService": { "@type": "ShippingService", "name": "Postal Service", "fulfillmentType": "https://schema.org/FulfillmentTypeDelivery", "shippingConditions": { "@type": "ShippingConditions", "shippingOrigin": { "@id": "http://example.com/lechateausnottyaddress" }, "orderValue": { "@type": "MonetaryAmount", "value": 100.0, "currency": "EUR" } } } } }, "manufacturer": { "@id": "http://example.com/lechateausnotty" }, "weight": [{ "@id": "http://example.com/lechateausnottynetmass" }, { "@id": "http://example.com/lechateausnottygrossmass" }], "productionDate": "2020-10-01", "hasCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "aggregateRating": { "@type": "AggregateRating", "ratingCount": 33, "ratingValue": 4.7, "bestRating": 5, "worstRating": 1 }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1 }, "reviewBody": { "@value": "Oncques n'a jamais vu de vin plus prétentieux", "@language": "fr" }, "author": { "@type": "Person", "name": "Jean d'Eau" } }, "gs1:bestBeforeDate": "2027-01-01", "gs1:AdditiveDetails": { "@type": "gs1:AdditiveDetails", "gs1:additiveName": "Sulfite", "gs1:additiveLevelOfContainment": "gs1:LevelOfContainmentCode-CONTAINS" }, "gs1:netWeight": { "@id": "http://example.com/lechateausnottynetmass" }, "gs1:beverageVintage": "2020", "gs1:gpcCategoryCode": "10000276", "gs1:percentageOfAlcoholByVolume": 4.0, "gs1:vintner": "Domaine du Château Snotty", "gs1:alcoholicBeverageSubregion": "FR-16", "gs1:sweetnessLevelOfAlcoholicBeverage": "gs1:SweetnessLevelOfAlcoholicBeverageCode-DRY", "gs1:growingMethod": "gs1:GrowingMethodCode-ORGANIC", "gs1:packagingMarkedLabelAccreditation": "gs1:PackagingMarkedLabelAccreditationCode-EU_ECO_LABEL", "gs1:consumerSalesCondition": "gs1:ConsumerSalesConditionsCode-RESTRICTED_TO_SELL_16", "gs1:seller": { "@id": "http://example.com/lechateausnotty" }, "unece:specifiedMarking": { "@type": "unece:Marking", "unece:packagingMarkingTypeCode": [ "unece:PackagingMarkingCodeList#32", "unece:PackagingMarkingCodeList#9" ] }, "unece:fromDeliveryLifeSpanMeasure": { "@type": "unece:SupplyChainPackaging", "unece:DurationUnitMeasureCode": "unece:DurationUnitMeasureCode#MON", "unece:DurationUnitMeasureTypeValue": 6 }, "unece:recyclableIndicator": true, "unece:applicableTradeProductCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "unece:manufacturerParty": { "@id": "http://example.com/lechateausnotty" }, "unece:netWeightMeasure": { "@id": "http://example.com/lechateausnottynetmass" }, "unece:grossWeightMeasure": { "@id": "http://example.com/lechateausnottygrossmass" } } ] } </script>

Structured representation of the JSON-LD example.
