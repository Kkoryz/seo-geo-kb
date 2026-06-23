---
title: "ResearchProject"
source_url: https://schema.org/ResearchProject
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ResearchProject

# ResearchProject

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ResearchProject
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ResearchProject)

A Research project.

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

[URL](/URL)#### Source

[https://schema.org/docs/collab/FundInfoCollab](https://schema.org/docs/collab/FundInfoCollab)

[https://github.com/schemaorg/schemaorg/issues/383](https://github.com/schemaorg/schemaorg/issues/383)

### Examples

[Example 1](#eg-0469)

Copied

Example notes or example HTML without markup.

A scientific dataset.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Turner, Caroline B.", "givenName": "Caroline B.", "familyName": "Turner", "funding": { "@type": "Grant", "identifier": "1448821", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0471)

Copied

Example notes or example HTML without markup.

A scientific dataset.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Turner, Caroline B.", "givenName": "Caroline B.", "familyName": "Turner", "funding": { "@type": "Grant", "identifier": "1448821", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0479)

Copied

Example notes or example HTML without markup.

An example of an online repository that hosts scientific research data (JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.See https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/DataRepository.md for a complete guide. <script type="application/ld+json"> { "@context": { "@vocab": "https://schema.org/" }, "@type": [ "Service", "ResearchProject" ], "legalName": "Sample Data Repository Office", "name": "SDRO", "url": "https://www.sample-data-repository.org", "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.", "sameAs": [ "http://www.re3data.org/repository/r3d1000000xx", "https://twitter.com/SDRO", "https://www.linkedin.com/company/123456789/" ], "category": [ "Biological Oceanography", "Chemical Oceanography" ], "provider": [ { "@type": "ResearchProject", "name": "SDRO Technical Office", "description": "We provide all the infrastructure for the SDRO" }, { "@type": "ResearchProject", "name": "SDRO Science Support Office", "description": "We provide all the science support functionality for the SDRO" } ], "logo": { "@type": "ImageObject", "url": "https://www.sample-data-repository.org/images/logo.jpg" }, "contactPoint": { "@type": "ContactPoint", "name": "Support", "email": "info@bco-dmo.org", "url": "https://www.sample-data-repository.org/about-us", "contactType": "customer support" }, "foundingDate": "2006-09-01", "address": { "@type": "PostalAddress", "streetAddress": "123 Main St.", "addressLocality": "Anytown", "addressRegion": "ST", "postalCode": "12345", "addressCountry": "USA" }, "parentOrganization": { "@type": "Organization", "@id": "http://www.someinstitute.edu", "legalName": "Some Institute", "name": "SI", "url": "http://www.someinstitute.edu", "address": { "@type": "PostalAddress", "streetAddress": "234 Main St.", "addressLocality": "Anytown", "addressRegion": "ST", "postalCode": "12345", "addressCountry": "USA" } }, "identifier": { "@type": "PropertyValue", "name": "Re3data DOI: 10.17616/R37P4C", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.17616/R37P4C", "url": "https://doi.org/10.17616/R37P4C" }, "funder": { "@type": "Organization", "@id": "https://doi.org/10.13039/100000141", "legalName": "Division of Ocean Sciences", "alternateName": "OCE", "url": "https://www.nsf.gov/div/index.jsp?div=OCE", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000141", "url": "https://doi.org/10.13039/100000141" }, "parentOrganization": { "@type": "Organization", "@id": "http://doi.org/10.13039/100000085", "legalName": "Directorate for Geosciences", "alternateName": "NSF-GEO", "url": "http://www.nsf.gov", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000085", "url": "https://doi.org/10.13039/100000085" }, "parentOrganization": { "@type": "Organization", "@id": "http://dx.doi.org/10.13039/100000001", "legalName": "National Science Foundation", "alternateName": "NSF", "url": "http://www.nsf.gov", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000001", "url": "https://doi.org/10.13039/100000001" } } } }, "availableChannel": [ { "@type": "ServiceChannel", "serviceUrl": "https://www.sample-data-repository.org/search", "providesService": { "@type": "Service", "name": "SDRO Website Search", "description": "Search for webpages, datasets, authors, funding awards, instrumentation and measurements", "potentialAction": { "@type": "SearchAction", "target": "https://www.sample-data-repository.org/search?keywords={query_string}" } } } ], "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Sample Data Repository Resource Catalog", "itemListElement": [ { "@type": "DataCatalog", "@id": "https://www.sample-data-repository.org/collection/biological-data", "name": "Biological Data", "audience": { "@type": "Audience", "audienceType": "public", "name": "General Public" } }, { "@type": "DataCatalog", "@id": "https://www.sample-data-repository.org/collection/geological-data", "name": "Geological Data", "audience": { "@type": "Audience", "audienceType": "public", "name": "General Public" } } ] } } </script>

Structured representation of the JSON-LD example.
