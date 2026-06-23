---
title: "SportsTeam"
source_url: https://schema.org/SportsTeam
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SportsTeam

# SportsTeam

A Schema.org Type

- Canonical URL: https://schema.org/SportsTeam
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SportsTeam)

Organization: Sports team.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[athlete](/athlete)

[Person](/Person)```
```[coach](/coach)

[Person](/Person)```
```[gender](/gender)

[GenderType](/GenderType)or[Text](/Text)[Person](/Person), but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who are not a binary gender. The[gender](/gender)property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender[SportsTeam](/SportsTeam)can be indicated with a text value of "Mixed".[SportsOrganization](/SportsOrganization)

```
```[sport](/sport)

[Text](/Text)or[URL](/URL)[Organization](/Organization)

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

[Organization](/Organization)or[Person](/Person)[musicGroupMember](/musicGroupMember),[members](/members).Inverse property:

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

[SportsTeam](/SportsTeam)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[SportsEvent](/SportsEvent)[competitor](/competitor)

[SportsEvent](/SportsEvent)[homeTeam](/homeTeam)

[SportsEvent](/SportsEvent)[sportsTeam](/sportsTeam)

[ExerciseAction](/ExerciseAction)### Examples

[Example 1](#eg-0206)

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

[Example 2](#eg-0430)

Copied

Example notes or example HTML without markup.

Seattle Seahawks American Football Team (NFC West) Head Coach: Pete Carroll Notable Players: Russell Wilson, Marshawn Lynch

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SportsTeam", "name": "Seattle Seahawks", "sport": "American Football", "memberOf": [ { "@type": "SportsOrganization", "name": "National Football League" },{ "@type": "SportsOrganization", "name": "National Football Conference" },{ "@type": "SportsOrganization", "name": "NFC West Division" } ], "coach": { "@type": "Person", "name": "Pete Carroll" }, "athlete": [ { "@type": "Person", "name": "Russell Wilson" },{ "@type": "Person", "name": "Marshawn Lynch" } ] } </script>

Structured representation of the JSON-LD example.
