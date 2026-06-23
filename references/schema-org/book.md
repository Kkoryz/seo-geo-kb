---
title: "Book"
source_url: https://schema.org/Book
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Book

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[abridged](/abridged)

[Boolean](/Boolean)```
```[bookEdition](/bookEdition)

[Text](/Text)```
```[bookFormat](/bookFormat)

[BookFormatType](/BookFormatType)```
```[illustrator](/illustrator)

[Person](/Person)```
```[isbn](/isbn)

[Text](/Text)```
```[numberOfPages](/numberOfPages)

[Integer](/Integer)[CreativeWork](/CreativeWork)

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

[URL](/URL)#### More specific Types

### Examples

[Example 1](#eg-0175)

Copied

Example notes or example HTML without markup.

<div> <dl> <dt>Name:</dt> <dd>Holt Physical Science</dd> <dt>Brief Synopsis:</dt> <dd>NIMAC-sourced textbook</dd> <dt>Long Synopsis:</dt> <dd>N/A</dd> <dt>Book Quality:</dt> <dd>Publisher Quality</dd> <dt>Book Size:</dt> <dd>598 Pages</dd> <dt>ISBN-13:</dt> <dd>9780030426599</dd> <dt>Publisher:</dt> <dd >Holt, Rinehart and Winston</dd> <dt>Date of Addition:</dt> <dd>06/08/10</dd> <dt>Copyright Date:</dt> <dd>2007</dd> <dt>Copyrighted By:</dt> <dd>Holt, Rinehart and Winston</dd> <dt>Adult content:</dt> <dd>No</dd> <dt>Language:</dt> <dd>English US</dd> <dt>Essential Images:</dt> <dd>861</dd> <dt>Described Images:</dt> <dd>910</dd> <dt>Categories:</dt> <dd>Educational Materials</dd> <dt>Grade Levels:</dt> <dd>Sixth grade, Seventh grade, Eighth grade</dd> <dt>Submitted By:</dt> <dd>Bookshare Staff</dd> <dt>NIMAC:</dt> <dd>This book is currently only available to public K-12 schools and organizations in the United States for use with students with an IEP, because it was created from files supplied by the NIMAC under these restrictions. Learn more in the NIMAC Support Center.</dd> </dl> <div class="bookReviews"> <h2>Reviews of Holt Physical Science (0 reviews)</h2> <div class="bookReviewScore"> <span>0 - No Rating Yet</span> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<p> This example shows the addition of Accessibility metadata. Although these properties are not a formal enumeration, there is evolving consensus amongst accessibility experts for appropriate values for these properties. This example shows simple text values, as suggested by www.a11ymetadata.org. </p> <div itemscope="" itemtype="https://schema.org/Book"> <meta itemprop="bookFormat" content="EBook"/> <meta itemprop="accessibilityFeature" content="largePrint"/> <meta itemprop="accessibilityFeature" content="highContrastDisplay"/> <meta itemprop="accessibilityFeature" content="displayTransformability"/> <meta itemprop="accessibilityFeature" content="longDescription"/> <meta itemprop="accessibilityFeature" content="alternativeText"/> <meta itemprop="accessibilityControl" content="fullKeyboardControl"/> <meta itemprop="accessibilityControl" content="fullMouseControl"/> <meta itemprop="accessibilityHazard" content="noFlashingHazard"/> <meta itemprop="accessibilityHazard" content="noMotionSimulationHazard"/> <meta itemprop="accessibilityHazard" content="noSoundHazard"/> <meta itemprop="accessibilityAPI" content="ARIA"/> <dl> <dt>Name:</dt> <dd itemprop="name">Holt Physical Science</dd> <dt>Brief Synopsis:</dt> <dd itemprop="description">NIMAC-sourced textbook</dd> <dt>Long Synopsis:</dt> <dd>N/A</dd> <dt>Book Quality:</dt> <dd>Publisher Quality</dd> <dt>Book Size:</dt> <dd><span itemprop="numberOfPages">598</span> Pages</dd> <dt>ISBN-13:</dt> <dd itemprop="isbn">9780030426599</dd> <dt>Publisher:</dt> <dd itemprop="publisher" itemtype="https://schema.org/Organization" itemscope=""><span itemprop="name">Holt, Rinehart and Winston</span></dd> <dt>Date of Addition:</dt> <dd>06/08/10</dd> <dt>Copyright Date:</dt> <dd itemprop="copyrightYear">2007</dd> <dt>Copyrighted By:</dt> <dd itemprop="copyrightHolder" itemtype="https://schema.org/Organization" itemscope=""><span itemprop="name">Holt, Rinehart and Winston</span></dd> <dt>Adult content:</dt> <dd><meta itemprop="isFamilyFriendly" content="true"/>No</dd> <dt>Language:</dt> <dd><meta itemprop="inLanguage" content="en-US"/>English US</dd> <dt>Essential Images:</dt> <dd>861</dd> <dt>Described Images:</dt> <dd>910</dd> <dt>Categories:</dt> <dd><span itemprop="genre">Educational Materials</span></dd> <dt>Grade Levels:</dt> <dd>Sixth grade, Seventh grade, Eighth grade</dd> <dt>Submitted By:</dt> <dd>Bookshare Staff</dd> <dt>NIMAC:</dt> <dd>This book is currently only available to public K-12 schools and organizations in the United States for use with students with an IEP, because it was created from files supplied by the NIMAC under these restrictions. Learn more in the NIMAC Support Center.</dd> </dl> <div class="bookReviews" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <h2>Reviews of Holt Physical Science (<span itemprop="reviewCount">0</span> reviews)</h2> <div class="bookReviewScore"> <span><span itemprop="ratingValue">0</span> - No Rating Yet</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<p> This example shows the addition of Accessibility metadata. Although these properties are not a formal enumeration, there is evolving consensus amongst accessibility experts for appropriate values for these properties. This example shows simple text values, as suggested by www.a11ymetadata.org. </p> <div vocab="https://schema.org/" typeof="Book"> <meta property="bookFormat" content="EBook"/> <meta property="accessibilityFeature" content="largePrint"/> <meta property="accessibilityFeature" content="highContrastDisplay"/> <meta property="accessibilityFeature" content="displayTransformability"/> <meta property="accessibilityFeature" content="longDescription"/> <meta property="accessibilityFeature" content="alternativeText"/> <meta property="accessibilityControl" content="fullKeyboardControl"/> <meta property="accessibilityControl" content="fullMouseControl"/> <meta property="accessibilityHazard" content="noFlashingHazard"/> <meta property="accessibilityHazard" content="noMotionSimulationHazard"/> <meta property="accessibilityHazard" content="noSoundHazard"/> <meta property="accessibilityAPI" content="ARIA"/> <dl> <dt>Name:</dt> <dd property="name">Holt Physical Science</dd> <dt>Brief Synopsis:</dt> <dd property="description">NIMAC-sourced textbook</dd> <dt>Long Synopsis:</dt> <dd>N/A</dd> <dt>Book Quality:</dt> <dd>Publisher Quality</dd> <dt>Book Size:</dt> <dd><span property="numberOfPages">598</span> Pages</dd> <dt>ISBN-13:</dt> <dd property="isbn">9780030426599</dd> <dt>Publisher:</dt> <dd property="publisher" typeof="Organization"><span property="name">Holt, Rinehart and Winston</span></dd> <dt>Date of Addition:</dt> <dd>06/08/10</dd> <dt>Copyright Date:</dt> <dd property="copyrightYear">2007</dd> <dt>Copyrighted By:</dt> <dd property="copyrightHolder" typeof="Organization"><span property="name">Holt, Rinehart and Winston</span></dd> <dt>Adult content:</dt> <dd><meta property="isFamilyFriendly" content="true"/>No</dd> <dt>Language:</dt> <dd><meta property="inLanguage" content="en-US"/>English US</dd> <dt>Essential Images:</dt> <dd>861</dd> <dt>Described Images:</dt> <dd>910</dd> <dt>Categories:</dt> <dd><span property="genre">Educational Materials</span></dd> <dt>Grade Levels:</dt> <dd>Sixth grade, Seventh grade, Eighth grade</dd> <dt>Submitted By:</dt> <dd>Bookshare Staff</dd> <dt>NIMAC:</dt> <dd>This book is currently only available to public K-12 schools and organizations in the United States for use with students with an IEP, because it was created from files supplied by the NIMAC under these restrictions. Learn more in the NIMAC Support Center.</dd> </dl> <div class="bookReviews" property="aggregateRating" typeof="AggregateRating"> <h2>Reviews of Holt Physical Science (<span property="reviewCount">0</span> reviews)</h2> <div class="bookReviewScore"> <span><span property="ratingValue">0</span> - No Rating Yet</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Book", "accessibilityAPI": "ARIA", "accessibilityControl": [ "fullKeyboardControl", "fullMouseControl" ], "accessibilityFeature": [ "largePrint", "highContrastDisplay", "displayTransformability", "longDescription", "alternativeText" ], "accessibilityHazard": [ "noFlashingHazard", "noMotionSimulationHazard", "noSoundHazard" ], "aggregateRating": { "@type": "AggregateRating", "reviewCount": "0" }, "bookFormat": "EBook", "copyrightHolder": { "@type": "Organization", "name": "Holt, Rinehart and Winston" }, "copyrightYear": "2007", "description": "NIMAC-sourced textbook", "genre": "Educational Materials", "inLanguage": "en-US", "isFamilyFriendly": "true", "isbn": "9780030426599", "name": "Holt Physical Science", "numberOfPages": "598", "publisher": { "@type": "Organization", "name": "Holt, Rinehart and Winston" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0220)

Copied

Example notes or example HTML without markup.

A CreativeWork and its translation. <div> <div> <h1>Rouge et le noir</h1> <div>Author: Stendhal</div> <div>Language: French</div> <div>Has Translation: Red and Black : A New Translation, Backgrounds and Sources, Criticism</div> </div> <div> <h1>Red and Black : A New Translation, Backgrounds and Sources, Criticism</h1> <div>Author: Stendhal</div> <div>Language: English</div> <div>Subject: Psychological fiction, French</div> <div>Translation of: Rouge et le noir</div> <div>Translator: Robert Martin Adams</div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemscope itemtype="https://schema.org/Book" itemid="http://worldcat.org/entity/work/id/2292573321"> <h1><span itemprop="name">Rouge et le noir</span></h1> <div>Author: <span itemprop="author" itemscope itemtype="https://schema.org/Person" itemid="http://viaf.org/viaf/17823">Stendhal</span></div> <div>Language: <meta itemprop="inLanguage" content="fr" />French</div> <div>Has Translation: <span itemprop="workTranslation" itemscope itemtype="https://schema.org/CreativeWork" itemid="http://worldcat.org/entity/work/id/460647">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></div> </div> <div itemscope itemtype="https://schema.org/Book" itemid="http://worldcat.org/entity/work/id/460647"> <h1><span itemprop="name">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></h1> <div>Author: <span itemprop="author" itemscope itemtype="https://schema.org/Person" itemid="http://viaf.org/viaf/17823">Stendhal</span></div> <div>Language: <meta itemprop="inLanguage" content="en" />English</div> <div>Subject: <span itemprop="about">Psychological fiction, French</span></div> <div>Translation of: <span itemprop="translationOfWork" itemscope itemtype="https://schema.org/CreativeWork" itemid="http://worldcat.org/entity/work/id/2292573321">Rouge et le noir</span></div> <div>Translator: <span itemprop="translator" itemscope itemtype="https://schema.org/Person" itemid="http://viaf.org/viaf/8453420">Robert Martin Adams</span></div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/"> <div typeof="Book" resource="http://worldcat.org/entity/work/id/2292573321"> <h1><span property="name">Rouge et le noir</span></h1> <div>Author: <span property="author" typeof="Person" resource="http://viaf.org/viaf/17823">Stendhal</span></div> <div>Language: <span property="inLanguage" content="fr">French</span></div> <div>Has Translation: <span property="workTranslation" typeof="CreativeWork" resource="http://worldcat.org/entity/work/id/460647">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></div> </div> <div typeof="Book" resource="http://worldcat.org/entity/work/id/460647"> <h1><span property="name">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></h1> <div>Author: <span property="author" typeof="Person" resource="http://viaf.org/viaf/17823">Stendhal</span></div> <div>Language: <span property="inLanguage" content="en">English</span></div> <div>Subject: <span property="about">Psychological fiction, French</span></div> <div>Translation of: <span property="translationOfWork" typeof="CreativeWork" resource="http://worldcat.org/entity/work/id/2292573321">Rouge et le noir</span></div> <div>Translator: <span property="translator" typeof="Person" resource="http://viaf.org/viaf/8453420">Robert Martin Adams</span></div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@graph": [ { "@id": "http://worldcat.org/entity/work/id/2292573321", "@type": "Book", "author": { "@id": "http://viaf.org/viaf/17823" }, "inLanguage": "fr", "name": "Rouge et le noir", "workTranslation": { "@type": "Book", "@id": "http://worldcat.org/entity/work/id/460647" } }, { "@id": "http://worldcat.org/entity/work/id/460647", "@type": "Book", "about": "Psychological fiction, French", "author": { "@id": "http://viaf.org/viaf/17823" }, "inLanguage": "en", "name": "Red and Black : A New Translation, Backgrounds and Sources, Criticism", "translationOfWork": { "@id": "http://worldcat.org/entity/work/id/2292573321" }, "translator": { "@id": "http://viaf.org/viaf/8453420" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0393)

Copied

Example notes or example HTML without markup.

<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div> <h3>Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td>Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr> <th>Copy </th> <td>Available <div>Barcode: <span>CONC91000937</span></div> <div>Call number: <span>780 R2</span></div> <div>Library: <span>Anytown City Library</span></div> </td> </tr> <table> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div itemscope itemtype="https://schema.org/Book" itemid="#record"> <link itemprop="additionalType" href="https://schema.org/Product"/> <h3 itemprop="name">Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td itemprop="author">Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr itemscope itemtype="https://schema.org/Offer"> <th>Copy </th> <td>Available <link itemprop="availability" href="https://schema.org/InStock"> <div>Barcode: <span itemprop="serialNumber">CONC91000937</span></div> <div>Call number: <span itemprop="sku">780 R2</span></div> <div>Library: <span itemprop="offeredBy" itemscope itemtype="https://schema.org/Library" itemid="http://library.anytown.gov.uk" >Anytown City Library</span></div> <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut"> <link itemprop="itemOffered" href="#record"> </td> </tr> </table> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div vocab="https://schema.org/" resource="#record" typeof="Book Product"> <h3 property="name"> Le concerto </h3> <div> Bibliographic Details <table> <tr> <th> Main Author: </th> <td property="author"> Ferchault, Guy </td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table vocab="https://schema.org/"> <!-- Example of a copy available for loan --> <tr typeof="Offer"> <th> Copy </th> <td> Available <div> Barcode: <span property="serialNumber">CONC91000937</span> </div> <div> Call number: <span property="sku">780 R2</span> </div> <div> Library: <span property="offeredBy" typeof="Library" resource="http://library.anytown.gov.uk">Anytown City Library</span> </div> </td> </tr> </table> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@id": "#record", "@type": "Book", "additionalType": "Product", "name": "Le concerto", "author": "Ferchault, Guy", "offers":{ "@type": "Offer", "availability": "https://schema.org/InStock", "serialNumber": "CONC91000937", "sku": "780 R2", "offeredBy": { "@type": "Library", "@id": "http://library.anytown.gov.uk", "name": "Anytown City Library" }, "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "itemOffered": "#record" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0395)

Copied

Example notes or example HTML without markup.

<!-- A Library Example with Holdings --> <body> <h1>In search of Haydn [videorecording] / Phil Grabsky Films.com & Seventh Art Productions in association with Sky Art HD ; filmed, written and directed by Phil Grabsky.</h1> <h2>Record details</h2> <ul> <li><strong>Publisher:</strong>[Brighton, UK] :Seventh Art Productions,[2011]</li> </ul> <table> <tr><td>Subject:</td> <td>Haydn, Joseph, 1732-1809.<br>Composers > Austria > Biography.<br></td> </tr> <tr><td>Genre:</td> <td>Documentary films.<br></td> </tr> </table> <table> <tr><th>Location</th><th>Call Number / Copy Notes</th><th>Barcode</th><th>Shelving Location</th><th>Status</th><th>Due Date</th></tr> <tr> <td><a href="/eg/opac/library/MRC">Music Resource Centre</a></td> <td>ML 410 H4 I5 2011</td> <td>30007008812793</td> <td>Circulation</td> <td> </td> </tr> </table> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype='https://schema.org/Movie'> <link itemprop="url" href="#schemarecord"/> <link itemprop="additionalType" href="https://schema.org/Product"/> <h1 itemprop="name">In search of Haydn [videorecording] / Phil Grabsky Films.com & Seventh Art Productions in association with Sky Art HD ; filmed, written and directed by Phil Grabsky.</h1> <h2>Record details</h2> <ul> <li><div itemprop="publisher" itemscope itemtype="https://schema.org/Organization"><strong>Publisher:</strong> <span ><span itemprop="location">[Brighton, UK] :</span> <span itemprop="name">Seventh Art Productions,</span></span> </div> <span itemprop="datePublished" content="2011-01-01">[2011]</span></li> </ul> <table> <tr><td>Subject:</td> <td><span itemprop="about">Haydn, Joseph, 1732-1809.<br></span><span itemprop="about">Composers > Austria > Biography.<br></span></td> </tr> <tr><td>Genre:</td> <td><span itemprop="about">Documentary films.<br></span></td> </tr> </table> <table> <tr><th>Location</th><th>Call Number / Copy Notes</th><th>Barcode</th><th>Shelving Location</th><th>Status</th></tr> <tr itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <td><a itemprop="offeredBy" itemscope itemtype="https://schema.org/Library" href="/eg/opac/library/MRC"><span itemprop="name">Music Resource Centre</span></a></td> <td><span itemprop="sku">ML 410 H4 I5 2011</span></td> <td itemprop="serialNumber">30007008812793</td> <td itemprop="availableAtOrFrom">Circulation</td> <td> <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut"> <meta itemprop="price" content="0.00"> <link itemprop="availability" href="https://schema.org/InStock"> </td> </tr> </table> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org" typeof='Movie Product' resource="#schemarecord"> <h1 property="name">In search of Haydn [videorecording] / Phil Grabsky Films.com & Seventh Art Productions in association with Sky Art HD ; filmed, written and directed by Phil Grabsky.</h1> <h2>Record details</h2> <ul> <li><strong>Publisher:</strong> <span property="publisher" typeof="Organization"><span property="location">[Brighton, UK] :</span> <span property="name">Seventh Art Productions,</span></span> <span property="datePublished" content="2011-01-01">[2011]</span></li> </ul> <table> <tr><td>Subject:</td> <td><span property="about">Haydn, Joseph, 1732-1809.<br></span><span property="about">Composers > Austria > Biography.<br></span></td> </tr> <tr><td>Genre:</td> <td><span property="about">Documentary films.<br></span></td> </tr> </table> <table> <tr><th>Location</th><th>Call Number / Copy Notes</th><th>Barcode</th><th>Shelving Location</th><th>Status</th><th>Due Date</th></tr> <tr property="offers" typeof="Offer"> <td><a property="offeredBy" typeof="Library" href="/eg/opac/library/MRC"><span property="name">Music Resource Centre</span></a></td> <td><span property="sku">ML 410 H4 I5 2011</span></td> <td property="serialNumber">30007008812793</td> <td property="availableAtOrFrom">Circulation</td> <td> <link property="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut"> <meta property="price" content="0.00"> <link property="availability" href="https://schema.org/InStock"> </td> </tr> </table> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@graph": [ { "@id": "https://laurentian.concat.ca/eg/opac/library/MRC", "@type": "Library", "name": "Music Resource Centre" }, { "@id": "https://laurentian.concat.ca/eg/opac/record/2845929#schemarecord", "@type": ["Movie","Product"], "about": [ "Composers > Austria > Biography.", "Haydn, Joseph, 1732-1809.", "Documentary films." ], "datePublished": "2011-01-01", "name": "In search of Haydn [videorecording] / Phil Grabsky Films.com & Seventh Art Productions in association with Sky Art HD ; filmed, written and directed by Phil Grabsky.", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "availableAtOrFrom": "Circulation", "price": "0.00", "seller": { "@id": "https://laurentian.concat.ca/eg/opac/library/MRC" }, "serialNumber": "30007008812793", "sku": "ML 410 H4 I5 2011" }, "publisher": { "@type": "Organization", "location": "[Brighton, UK] :", "name": "Seventh Art Productions," } } ] } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0400)

Copied

Example notes or example HTML without markup.

<!-- A trilogy of books with numbered volumes. --> <div> <p> The <strong>Lord of the Rings</strong> is an English-language fictional trilogy by J. R. R. Tolkien (1892-1973). </p> <p> The books in the trilogy are: </p> <ul> <li>Vol. 1: The Fellowship of the Ring</li> <li>Vol. 2: The Two Towers</li> <li>Vol. 3: The Return of the King</li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- A trilogy of books with numbered volumes. --> <div> <p itemscope itemtype="https://schema.org/Book" itemid="#trilogy"> <link itemprop="about" href="http://id.worldcat.org/fast/1020337"> The <strong itemprop="name">Lord of the Rings</strong> is an <meta itemprop="inLanguage" content="en"/>English-language <span itemprop="genre">fictional</span> trilogy by <span itemprop="author" itemscope itemtype="https://schema.org/Person" itemid="#author"> <link itemprop="sameAs" href="http://viaf.org/viaf/95218067"> <meta itemprop="name" content="Tolkien, J. R. R. (John Ronald Reuel)"/>J. R. R. Tolkien (<span itemprop="birthDate">1892</span>-<span itemprop="deathDate">1973</span>). </span> <link itemprop="hasPart" href="#book1"> <link itemprop="hasPart" href="#book2"> <link itemprop="hasPart" href="#book3"> </p> <p> The books in the trilogy are: </p> <ul> <li itemscope itemtype="https://schema.org/Book https://schema.org/PublicationVolume" itemid="#book1"> Vol. <span itemprop="volumeNumber">1</span>: <link itemprop="about" href="http://id.worldcat.org/fast/1020337"> <link itemprop="isPartOf" href="#trilogy"> <link itemprop="author" href="#author"> <meta itemprop="inLanguage" content="en"> <span itemprop="name">The Fellowship of the Ring</span> </li> <li itemscope itemtype="https://schema.org/Book https://schema.org/PublicationVolume" itemid="#book2"> Vol. <span itemprop="volumeNumber">2</span>: <link itemprop="about" href="http://id.worldcat.org/fast/1020337"> <link itemprop="isPartOf" href="#trilogy"> <link itemprop="author" href="#author"> <meta itemprop="inLanguage" content="en"> <span itemprop="name">The Two Towers</span> </li> <li itemscope itemtype="https://schema.org/Book https://schema.org/PublicationVolume" itemid="#book3"> Vol. <span itemprop="volumeNumber">3</span>: <link itemprop="about" href="http://id.worldcat.org/fast/1020337"> <link itemprop="isPartOf" href="#trilogy"> <link itemprop="author" href="#author"> <meta itemprop="inLanguage" content="en"> <span itemprop="name">The Return of the King</span> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- A trilogy of books with numbered volumes. --> <div vocab="https://schema.org/"> <p typeof="Book" resource="#trilogy"> <link property="about" href="http://id.worldcat.org/fast/1020337"> The <strong property="name">Lord of the Rings</strong> is an <span property="inLanguage" content="en">English-language</span> <span property="genre">fictional</span> trilogy by <span property="author" typeof="Person" resource="#author"> <link property="sameAs" href="http://viaf.org/viaf/95218067"> <span property="name" content="Tolkien, J. R. R. (John Ronald Reuel)">J. R. R. Tolkien</span> (<span property="birthDate">1892</span>-<span property="deathDate">1973</span>). </span> <link property="hasPart" href="#book1"> <link property="hasPart" href="#book2"> <link property="hasPart" href="#book3"> </p> <p> The books in the trilogy are: </p> <ul> <li typeof="Book PublicationVolume" resource="#book1"> Vol. <span property="volumeNumber">1</span>: <link property="about" href="http://id.worldcat.org/fast/1020337"> <link property="isPartOf" href="#trilogy"> <link property="author" href="#author"> <meta property="inLanguage" content="en"> <span property="name">The Fellowship of the Ring</span> </li> <li typeof="Book PublicationVolume" resource="#book2"> Vol. <span property="volumeNumber">2</span>: <link property="about" href="http://id.worldcat.org/fast/1020337"> <link property="isPartOf" href="#trilogy"> <link property="author" href="#author"> <meta property="inLanguage" content="en"> <span property="name">The Two Towers</span> </li> <li typeof="Book PublicationVolume" resource="#book3"> Vol. <span property="volumeNumber">3</span>: <link property="about" href="http://id.worldcat.org/fast/1020337"> <link property="isPartOf" href="#trilogy"> <link property="author" href="#author"> <meta property="inLanguage" content="en"> <span property="name">The Return of the King</span> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@id": "#author", "@type": "Person", "birthDate": "1892", "deathDate": "1973", "name": "Tolkien, J. R. R. (John Ronald Reuel)", "sameAs": "http://viaf.org/viaf/95218067" }, { "@id": "#trilogy", "@type": "Book", "about": "http://id.worldcat.org/fast/1020337", "hasPart": [ { "@id": "#book3", "@type": [ "Book", "PublicationVolume" ], "name": "The Return of the King", "about": "http://id.worldcat.org/fast/1020337", "isPartOf": "#trilogy", "inLanguage": "en", "volumeNumber": "3", "author": "#author" }, { "@id": "#book2", "@type": [ "Book", "PublicationVolume" ], "name": "The Two Towers", "about": "http://id.worldcat.org/fast/1020337", "isPartOf": "#trilogy", "inLanguage": "en", "volumeNumber": "2", "author": "#author" }, { "@id": "#book1", "@type": [ "Book", "PublicationVolume" ], "name": "The Fellowship of the Ring", "about": "http://id.worldcat.org/fast/1020337", "isPartOf": "#trilogy", "inLanguage": "en", "volumeNumber": "1", "author": "#author" } ], "name": "Lord of the Rings", "inLanguage": "en", "genre": "fictional", "author": "#author" } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0462)

Copied

Example notes or example HTML without markup.

<a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> <img src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> The Catcher in the Rye - Mass Market Paperback by <a href="/author/jd_salinger.html">J.D. Salinger</a> 4 stars - 3077 reviews Price: $6.99 In Stock Product details 224 pages Publisher: Little, Brown, and Company - May 1, 1991 Language: English ISBN-10: 0316769487 Reviews: 5 stars - <b>"A masterpiece of literature" </b> by John Doe. Written on May 4, 2006 I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood. 4 stars - <b>"love it LOLOL111!" </b> by Bob Smith, Written on June 15, 2006 Catcher in the Rye is a fun book. It's a good book to read.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/WebPage"> ... <div itemprop="breadcrumb"> <a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> </div> <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Book"> <img itemprop="image" src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> <span itemprop="name">The Catcher in the Rye</span> - <link itemprop="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback by <a itemprop="author" href="/author/jd_salinger.html">J.D. Salinger</a> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">4</span> stars - <span itemprop="reviewCount">3077</span> reviews </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> Price: $<span itemprop="price">6.99</span> <meta itemprop="priceCurrency" content="USD" /> <link itemprop="availability" href="https://schema.org/InStock">In Stock </div> Product details <span itemprop="numberOfPages">224</span> pages Publisher: <span itemprop="publisher">Little, Brown, and Company</span> - <meta itemprop="datePublished" content="1991-05-01">May 1, 1991 Language: <span itemprop="inLanguage">English</span> ISBN-10: <span itemprop="isbn">0316769487</span> Reviews: <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="reviewRating">5</span> stars - <b>"<span itemprop="name">A masterpiece of literature</span>"</b> by <span itemprop="author">John Doe</span>, Written on <meta itemprop="datePublished" content="2006-05-04">May 4, 2006 <span itemprop="reviewBody">I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.</span> </div> <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="reviewRating">4</span> stars - <b>"<span itemprop="name">A good read.</span>" </b> by <span itemprop="author">Bob Smith</span>, Written on <meta itemprop="datePublished" content="2006-06-15">June 15, 2006 <span itemprop="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span> </div> </div> ... </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> ... <div property="breadcrumb"> <a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> </div> <div property="mainEntity" typeof="Book"> <img property="image" src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> <span property="name">The Catcher in the Rye</span> - <link property="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback by <a property="author" href="/author/jd_salinger.html">J.D. Salinger</a> <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">4</span> stars - <span property="reviewCount">3077</span> reviews </div> <div property="offers" typeof="Offer"> Price: $<span property="price">6.99</span> <meta property="priceCurrency" content="USD" /> <link property="availability" href="https://schema.org/InStock">In Stock </div> Product details <span property="numberOfPages">224</span> pages Publisher: <span property="publisher">Little, Brown, and Company</span> - <meta property="datePublished" content="1991-05-01">May 1, 1991 Language: <span property="inLanguage">English</span> ISBN-10: <span property="isbn">0316769487</span> Reviews: <div property="review" typeof="Review"> <span property="reviewRating">5</span> stars - <b>"<span property="name">A masterpiece of literature</span>"</b> by <span property="author">John Doe</span>, Written on <meta property="datePublished" content="2006-05-04">May 4, 2006 <span property="reviewBody">I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.</span> </div> <div property="review" typeof="Review"> <span property="reviewRating">4</span> stars - <b>"<span property="name">A good read.</span>" </b> by <span property="author">Bob Smith</span>, Written on <meta property="datePublished" content="2006-06-15">June 15, 2006 <span property="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span> </div> </div> ... </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "breadcrumb": "Books > Literature & Fiction > Classics", "mainEntity":{ "@type": "Book", "author": "/author/jd_salinger.html", "bookFormat": "https://schema.org/Paperback", "datePublished": "1991-05-01", "image": "catcher-in-the-rye-book-cover.jpg", "inLanguage": "English", "isbn": "0316769487", "name": "The Catcher in the Rye", "numberOfPages": "224", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "6.99", "priceCurrency": "USD" }, "publisher": "Little, Brown, and Company", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4", "reviewCount": "3077" }, "review": [ { "@type": "Review", "author": "John Doe", "datePublished": "2006-05-04", "name": "A masterpiece of literature", "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.", "reviewRating": { "@type": "Rating", "ratingValue": "5" } }, { "@type": "Review", "author": "Bob Smith", "datePublished": "2006-06-15", "name": "A good read.", "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.", "reviewRating": "4" } ] } } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-3697)

Copied

Example notes or example HTML without markup.

<ruby>源氏物語<rp>(</rp>Genji Monogatari<rp>)</rp></ruby> NDC: 913

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Book", "name": [{ "@lang": "en", "@value": "Genji Monogatari" },{ "@lang": "ja", "@value": "源氏物語" }], "genre": { "@type": "DefinedTerm", "name": "Monogatari", "termCode": "913", "inDefinedTermSet": { "@type": "DefinedTermSet", "name": "Nippon Decimal Classification", "alternateName": "NDC", "url": "https://www.asahi-net.or.jp/~ax2s-kmtn/ref/ndc10/e_ndc.html" } } } </script>

Structured representation of the JSON-LD example.
