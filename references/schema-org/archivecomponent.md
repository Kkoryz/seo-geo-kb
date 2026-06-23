---
title: "ArchiveComponent"
source_url: https://schema.org/ArchiveComponent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ArchiveComponent

# ArchiveComponent

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ArchiveComponent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ArchiveComponent)

An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[holdingArchive](/holdingArchive)

[ArchiveOrganization](/ArchiveOrganization)[ArchiveOrganization](/ArchiveOrganization)that holds, keeps or maintains the[ArchiveComponent](/ArchiveComponent).Inverse property:

[archiveHeld](/archiveHeld)```
```[itemLocation](/itemLocation)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)[CreativeWork](/CreativeWork)

```
```[about](/about)

[Thing](/Thing)Inverse property:

[subjectOf](/subjectOf)```
```[abstract](/abstract)

[Text](/Text)[CreativeWork](/CreativeWork).```
```[accessMode](/accessMode)

[Text](/Text)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).```
```[accessModeSufficient](/accessModeSufficient)

[ItemList](/ItemList)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).```
```[accessibilityAPI](/accessibilityAPI)

[Text](/Text)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).```
```[accessibilityControl](/accessibilityControl)

[Text](/Text)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).```
```[accessibilityFeature](/accessibilityFeature)

[Text](/Text)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).```
```[accessibilityHazard](/accessibilityHazard)

[Text](/Text)[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).```
```[accessibilitySummary](/accessibilitySummary)

[Text](/Text)```
```[accountablePerson](/accountablePerson)

[Person](/Person)```
```[acquireLicensePage](/acquireLicensePage)

[CreativeWork](/CreativeWork)or[URL](/URL)```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[alternativeHeadline](/alternativeHeadline)

[Text](/Text)```
```[archivedAt](/archivedAt)

[URL](/URL)or[WebPage](/WebPage)[CreativeWork](/CreativeWork). In the case of[MediaReview](/MediaReview), the items in a[MediaReviewItem](/MediaReviewItem)may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.```
```[assesses](/assesses)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[associatedMedia](/associatedMedia)

[MediaObject](/MediaObject)```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[audio](/audio)

[AudioObject](/AudioObject)or[Clip](/Clip)or[MusicRecording](/MusicRecording)```
```[author](/author)

[Organization](/Organization)or[Person](/Person)```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[character](/character)

[Person](/Person)```
```[citation](/citation)

[CreativeWork](/CreativeWork)or[Text](/Text)```
```[comment](/comment)

[Comment](/Comment)```
```[commentCount](/commentCount)

[Integer](/Integer)```
```[conditionsOfAccess](/conditionsOfAccess)

[Text](/Text)[ArchiveComponent](/ArchiveComponent)held by an[ArchiveOrganization](/ArchiveOrganization). This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ".

```
```[contentLocation](/contentLocation)

[Place](/Place)```
```[contentRating](/contentRating)

[Rating](/Rating)or[Text](/Text)```
```[contentReferenceTime](/contentReferenceTime)

[DateTime](/DateTime)```
```[contributor](/contributor)

[Organization](/Organization)or[Person](/Person)```
```[copyrightHolder](/copyrightHolder)

[Organization](/Organization)or[Person](/Person)```
```[copyrightNotice](/copyrightNotice)

[Text](/Text)```
```[copyrightYear](/copyrightYear)

[Number](/Number)```
```[correction](/correction)

[CorrectionComment](/CorrectionComment)or[Text](/Text)or[URL](/URL)[CreativeWork](/CreativeWork), either via a[CorrectionComment](/CorrectionComment), textually or in another document.```
```[countryOfOrigin](/countryOfOrigin)

[Country](/Country)In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

```
```[creativeWorkStatus](/creativeWorkStatus)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[creator](/creator)

[Organization](/Organization)or[Person](/Person)```
```[creditText](/creditText)

[Text](/Text)```
```[dateCreated](/dateCreated)

[Date](/Date)or[DateTime](/DateTime)```
```[dateModified](/dateModified)

[Date](/Date)or[DateTime](/DateTime)```
```[datePublished](/datePublished)

[Date](/Date)or[DateTime](/DateTime)[CreativeWork](/CreativeWork)was broadcast or a[Certification](/Certification)was issued.```
```[digitalSourceType](/digitalSourceType)

[IPTCDigitalSourceEnumeration](/IPTCDigitalSourceEnumeration)[CreativeWork](/CreativeWork).```
```[discussionUrl](/discussionUrl)

[URL](/URL)```
```[displayLocation](/displayLocation)

[Place](/Place)```
```[editEIDR](/editEIDR)

[Text](/Text)or[URL](/URL)[EIDR](https://eidr.org/)(Entertainment Identifier Registry)[identifier](/identifier)representing a specific edit / edition for a work of film or television.For example, the motion picture known as "Ghostbusters" whose

[titleEIDR](/titleEIDR)is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".Since schema.org types like

[Movie](/Movie)and[TVEpisode](/TVEpisode)can be used for both works and their multiple expressions, it is possible to use[titleEIDR](/titleEIDR)alone (for a general description), or alongside[editEIDR](/editEIDR)for a more edit-specific description.```
```[editor](/editor)

[Person](/Person)```
```[educationalAlignment](/educationalAlignment)

[AlignmentObject](/AlignmentObject)This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource

[teaches](/teaches)or[assesses](/assesses)a competency.```
```[educationalLevel](/educationalLevel)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[educationalUse](/educationalUse)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[encoding](/encoding)

[MediaObject](/MediaObject)[encodings](/encodings).Inverse property:

[encodesCreativeWork](/encodesCreativeWork)```
```[encodingFormat](/encodingFormat)

[Text](/Text)or[URL](/URL)[IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)and[MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.In cases where a

[CreativeWork](/CreativeWork)has several media type representations,[encoding](/encoding)can be used to indicate each[MediaObject](/MediaObject)alongside particular[encodingFormat](/encodingFormat)information.Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry. Supersedes

[fileFormat](/fileFormat).```
```[exampleOfWork](/exampleOfWork)

[CreativeWork](/CreativeWork)Inverse property:

[workExample](/workExample)```
```[expires](/expires)

[Date](/Date)or[DateTime](/DateTime)[VideoObject](/VideoObject)or[NewsArticle](/NewsArticle)whose availability or relevance is time-limited, a[ClaimReview](/ClaimReview)fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a[Certification](/Certification)the validity has expired.```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[genre](/genre)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[hasPart](/hasPart)

[CreativeWork](/CreativeWork)Inverse property:

[isPartOf](/isPartOf)```
```[headline](/headline)

[Text](/Text)```
```[inLanguage](/inLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage). Supersedes[language](/language).```
```[interactionStatistic](/interactionStatistic)

[InteractionCounter](/InteractionCounter)[interactionCount](/interactionCount).```
```[interactivityType](/interactivityType)

[Text](/Text)```
```[interpretedAsClaim](/interpretedAsClaim)

[Claim](/Claim)[MediaObject](/MediaObject)or other[CreativeWork](/CreativeWork). The interpreting party can be indicated using[claimInterpreter](/claimInterpreter).```
```[isAccessibleForFree](/isAccessibleForFree)

[Boolean](/Boolean)[free](/free).```
```[isBasedOn](/isBasedOn)

[CreativeWork](/CreativeWork)or[Product](/Product)or[URL](/URL)[isBasedOnUrl](/isBasedOnUrl).```
```[isFamilyFriendly](/isFamilyFriendly)

[Boolean](/Boolean)```
```[isPartOf](/isPartOf)

[CreativeWork](/CreativeWork)or[URL](/URL)Inverse property:

[hasPart](/hasPart)```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[learningResourceType](/learningResourceType)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[license](/license)

[CreativeWork](/CreativeWork)or[URL](/URL)```
```[locationCreated](/locationCreated)

[Place](/Place)```
```[mainEntity](/mainEntity)

[Thing](/Thing)Inverse property:

[mainEntityOfPage](/mainEntityOfPage)```
```[maintainer](/maintainer)

[Organization](/Organization)or[Person](/Person)[Dataset](/Dataset), software package ([SoftwareApplication](/SoftwareApplication)), or other[Project](/Project). A maintainer is a[Person](/Person)or[Organization](/Organization)that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When[maintainer](/maintainer)is applied to a specific version of something e.g. a particular version or packaging of a[Dataset](/Dataset), it is always possible that the upstream source has a different maintainer. The[isBasedOn](/isBasedOn)property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.```
```[material](/material)

[Product](/Product)or[Text](/Text)or[URL](/URL)```
```[materialExtent](/materialExtent)

[QuantitativeValue](/QuantitativeValue)or[Text](/Text)```
```[mentions](/mentions)

[Thing](/Thing)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[pattern](/pattern)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[position](/position)

[Integer](/Integer)or[Text](/Text)```
```[producer](/producer)

[Organization](/Organization)or[Person](/Person)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[publication](/publication)

[PublicationEvent](/PublicationEvent)```
```[publisher](/publisher)

[Organization](/Organization)or[Person](/Person)```
```[publisherImprint](/publisherImprint)

[Organization](/Organization)```
```[publishingPrinciples](/publishingPrinciples)

[CreativeWork](/CreativeWork)or[URL](/URL)[URL](/URL)) a document describing the editorial principles of an[Organization](/Organization)(or individual, e.g. a[Person](/Person)writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a[CreativeWork](/CreativeWork)(e.g.[NewsArticle](/NewsArticle)) the principles are those of the party primarily responsible for the creation of the[CreativeWork](/CreativeWork).While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a

[funder](/funder)) can be expressed using schema.org terminology.```
```[recordedAt](/recordedAt)

[Event](/Event)Inverse property:

[recordedIn](/recordedIn)```
```[releasedEvent](/releasedEvent)

[PublicationEvent](/PublicationEvent)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[schemaVersion](/schemaVersion)

[Text](/Text)or[URL](/URL)`10.0`

as a simple string, or more explicitly via URL, `https://schema.org/docs/releases.html#v10.0`

. There may be situations in which other schemas might usefully be referenced this way, e.g. `http://dublincore.org/specifications/dublin-core/dces/1999-07-02/`

but this has not been carefully explored in the community.
```
```[sdDatePublished](/sdDatePublished)

[Date](/Date)[sdPublisher](/sdPublisher).```
```[sdLicense](/sdLicense)

[CreativeWork](/CreativeWork)or[URL](/URL)```
```[sdPublisher](/sdPublisher)

[Organization](/Organization)or[Person](/Person)[sdPublisher](/sdPublisher)property helps make such practices more explicit.```
```[size](/size)

[DefinedTerm](/DefinedTerm)or[QuantitativeValue](/QuantitativeValue)or[SizeSpecification](/SizeSpecification)or[Text](/Text)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.```
```[sourceOrganization](/sourceOrganization)

[Organization](/Organization)```
```[spatial](/spatial)

[Place](/Place)[locationCreated](/locationCreated),[spatialCoverage](/spatialCoverage),[contentLocation](/contentLocation)) are not known to be appropriate.```
```[spatialCoverage](/spatialCoverage)

[Place](/Place)```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)```
```[teaches](/teaches)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[temporal](/temporal)

[DateTime](/DateTime)or[Text](/Text)[temporalCoverage](/temporalCoverage),[dateCreated](/dateCreated),[dateModified](/dateModified),[datePublished](/datePublished)) are not known to be appropriate.```
```[temporalCoverage](/temporalCoverage)

[DateTime](/DateTime)or[Text](/Text)or[URL](/URL)[ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL. Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated. Supersedes

[datasetTimeInterval](/datasetTimeInterval).```
```[text](/text)

[Text](/Text)```
```[thumbnail](/thumbnail)

[ImageObject](/ImageObject)```
```[thumbnailUrl](/thumbnailUrl)

[URL](/URL)```
```[timeRequired](/timeRequired)

[Duration](/Duration)```
```[translationOfWork](/translationOfWork)

[CreativeWork](/CreativeWork)Inverse property:

[workTranslation](/workTranslation)```
```[translator](/translator)

[Organization](/Organization)or[Person](/Person)```
```[typicalAgeRange](/typicalAgeRange)

[Text](/Text)```
```[usageInfo](/usageInfo)

[CreativeWork](/CreativeWork)or[URL](/URL)[usageInfo](/usageInfo)property indicates further information about a[CreativeWork](/CreativeWork). This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.

```
```[version](/version)

[Number](/Number)or[Text](/Text)```
```[video](/video)

[Clip](/Clip)or[VideoObject](/VideoObject)```
```[wordCount](/wordCount)

[Integer](/Integer)```
```[workExample](/workExample)

[CreativeWork](/CreativeWork)Inverse property:

[exampleOfWork](/exampleOfWork)```
```[workTranslation](/workTranslation)

[CreativeWork](/CreativeWork)Inverse property:

[translationOfWork](/translationOfWork)[Thing](/Thing)

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

[ArchiveComponent](/ArchiveComponent)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ArchiveOrganization](/ArchiveOrganization)[fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an[ArchiveOrganization](/ArchiveOrganization).#### Source

[https://github.com/schemaorg/schemaorg/issues/1758](https://github.com/schemaorg/schemaorg/issues/1758)

### Examples

[Example 1](#eg-0255)

Copied

Example notes or example HTML without markup.

<div> <h1>Ronnie Barker Collection</h1> <span class="label">Material held at</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Reference</span> <span class="val">GB 71 THM/407/8<span><br/> <span class="label">Dates of Creation</span> <span class="val">1929-2005</span><br/> <span class="label">Name of Creator</span> <span class="val">Ronnie Barker</span><br/> <span class="label">Language of Material</span> <span class="val">English</span><br/> <span class="label">Direct Link</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">https://archiveshub.jisc.ac.uk/data/gb71-thm/407</a></span><br/> <span class="label">Description</span> <span class="val">The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.</span><br/> <span class="label">Conditions Governing Access</span> <span class="val">This archive collection is available for consultation in the V&A Blythe House Archive and Library Study Room by appointment only. Full details of access arrangements may be found here: http://www.vam.ac.uk/content/articles/a/archives/. Access to some of the material may be restricted. These are noted in the catalogue where relevant.</span><br/> <span class="label">Contains</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Collection"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> <h1 itemprop="name">Ronnie Barker Collection</h1> <span class="label">Material held at</span> <span class="val"><a itemprop="holdingArchive" href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Reference</span> <span class="val" itemprop="identifier">GB 71 THM/407/8</span><br/> <span class="label">Dates of Creation</span> <span class="val" itemprop="temporalCoverage">1929-2005</span><br/> <span class="label">Name of Creator</span> <span class="val" itemprop="creator">Ronnie Barker</span><br/> <span class="label">Language of Material</span> <span class="val" itemprop="inLanguage" content="EN">English</span><br/> <span class="label">Direct Link</span> <span class="val"><a itemprop="url" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">https://archiveshub.jisc.ac.uk/data/gb71-thm/407</a></span><br/> <span class="label">Description</span> <span class="val" itemprop="description">The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.</span><br/> <span class="label">Contains</span> <span class="val"><a itemprop="hasPart" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- A collection of items held in an archive --> <script type="application/ld+json"> { "@context": "https://schema.org", "@id": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407", "@type": ["Collection","ArchiveComponent"], "identifier": "GB 71 THM/407/8", "name": "Ronnie Barker Collection", "about": ["Comedy","Ronnie Barker"], "creator": { "@type": "Person", "name": "Ronnie Barker", "sameAs": "http://viaf.org/viaf/2676198" }, "description": "The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.", "inLanguage": "EN", "temporalCoverage": "1929-2005", "itemLocation": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "holdingArchive": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "hasPart": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0256)

Copied

Example notes or example HTML without markup.

<div> <h1>Sound Recording of Lines from My Grandafther's Forehead (Radio)</h1> <span class="label">Material held at</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance </a></span> <span class="label">Reference</span> <span class="val">GB 71 THM/407/8/3</span><br/> <span class="label">In Collection</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> <span class="label">Dates of Creation</span> <span class="val">1971</span><br/> <span class="label">Direct Link</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3">https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3</a></span><br/> <span class="label">Subject</span> <span class="val">Comedy</span><br/> <span class="label">Language of Material</span> <span class="val">English</span><br/> <span class="label">Description</span> <span class="val">Sound recording of the first radio broadcast of Lines from My Grandfather's Forehead by Ronnie Barker and others. Duration: max 90 mins.</span><br/> <span class="label">Conditions Governing Access</span> <span class="val">Please check with the Theatre and Performance enquiry team regarding access arrangements before making an appointment to listen to this item.</span><br/> <span class="label">Physical Characteristics</span> <span class="val">Audio Cassette</span><br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/AudioObject"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> <h1 itemprop="name">Sound Recording of Lines from My Grandafther's Forehead (Radio)</h1> <span class="val"><a property="holdingArchive" href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance</a></span> <span class="val" itemprop="holdingArchive">V&A Theatre and Performance Collections</span><br/> <span class="label">Reference</span> <span class="val" itemprop="identifier">GB 71 THM/407/8/3</span><br/> <span class="label">In Collection</span> <span class="val"><a itemprop="isPartOf" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> <span class="label">Dates of Creation</span> <span class="val" itemprop="dateCreated">1971</span><br/> <span class="label">Direct Link</span> <span class="val"><a itemprop="url" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3">https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3</a></span><br/> <span class="label">Subject</span> <span class="val" itemprop="about">Comedy</span><br/> <span class="label">Language of Material</span> <span class="val" itemprop="inLanguage" content="EN">English</span><br/> <span class="label">Description</span> <span class="val" itemprop="description">Sound recording of the first radio broadcast of Lines from My Grandfather's Forehead by Ronnie Barker and others. Duration: max 90 mins.</span><br/> <span class="label">Conditions Governing Access</span> <span class="val">Please check with the Theatre and Performance enquiry team regarding access arrangements before making an appointment to listen to this item.</span><br/> <span class="label">Physical Characteristics</span> <span class="val" itemprop="playerType">Audio Cassette</span><br/> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ArchiveComponent AudioObject"> <h1 property="name">Sound Recording of Lines from My Grandafther's Forehead (Radio)</h1> <span class="val"><a property="holdingArchive" href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance</a></span><br/> <span class="val" property="holdingArchive">V&A Theatre and Performance Collections</span><br/> <span class="label">Reference</span> <span class="val" property="identifier">GB 71 THM/407/8/3</span><br/> <span class="label">In Collection</span> <span class="val"><a property="isPartOf" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> <span class="label">Dates of Creation</span> <span class="val" property="dateCreated">1971</span><br/> <span class="label">Direct Link</span> <span class="val"><a property="url" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3">https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3</a></span><br/> <span class="label">Subject</span> <span class="val" property="about">Comedy</span><br/> <span class="label">Language of Material</span> <span class="val" property="inLanguage" content="EN">English</span><br/> <span class="label">Description</span> <span class="val" property="description">Sound recording of the first radio broadcast of Lines from My Grandfather's Forehead by Ronnie Barker and others. Duration: max 90 mins.</span><br/> <span class="label">Conditions Governing Access</span> <span class="label">Physical Characteristics</span> <span class="val" property="playerType">Audio Cassette</span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- A sound recording held in an archive --> <script type="application/ld+json"> { "@context": "https://schema.org", "@id": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8/3", "@type": ["AudioObject","ArchiveComponent"], "identifier": "GB 71 THM/407/8/3", "name": "Sound Recording of Lines from My Grandafther's Forehead (Radio)", "about": "Comedy", "description": "Sound recording of the first radio broadcast of Lines from My Grandfather's Forehead by Ronnie Barker and others. Duration: max 90 mins.", "inLanguage": "EN", "dateCreated": "1971", "duration": "PT90M", "playerType": "Audio Cassette", "itemLocation": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "isPartOf": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0274)

Copied

Example notes or example HTML without markup.

<!-- ArchiveComponent with restricted access -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- ArchiveComponent with restricted access --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": ["CreativeWork","ArchiveComponent"], "url": "https://purl.stanford.edu/bp158wj7223", "name": "Margaret Mitchell letter to Herschel Bricknell, 1936 August 22", "conditionsOfAccess": "Online content is available for access via the Special Collections Reading Room.", "holdingArchive": { "@type": "ArchiveOrganization", "name": "Stanford Digital Repository", "url": "https://purl.stanford.edu/" } } </script>

Structured representation of the JSON-LD example.
