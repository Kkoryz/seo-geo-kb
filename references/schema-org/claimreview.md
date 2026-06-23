---
title: "ClaimReview"
source_url: https://schema.org/ClaimReview
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ClaimReview

# ClaimReview

A Schema.org Type

- Canonical URL: https://schema.org/ClaimReview
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ClaimReview)

A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[claimReviewed](/claimReviewed)

[Text](/Text)[Review](/Review)

```
```[associatedClaimReview](/associatedClaimReview)

[Review](/Review)[ClaimReview](/ClaimReview), related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case[relatedMediaReview](/relatedMediaReview)would commonly be used on a[ClaimReview](/ClaimReview), while[associatedClaimReview](/associatedClaimReview)would be used on[MediaReview](/MediaReview).```
```[associatedMediaReview](/associatedMediaReview)

[Review](/Review)[MediaReview](/MediaReview), related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case[relatedMediaReview](/relatedMediaReview)would commonly be used on a[ClaimReview](/ClaimReview), while[associatedClaimReview](/associatedClaimReview)would be used on[MediaReview](/MediaReview).```
```[associatedReview](/associatedReview)

[Review](/Review)[Review](/Review).```
```[itemReviewed](/itemReviewed)

[Thing](/Thing)```
```[negativeNotes](/negativeNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[positiveNotes](/positiveNotes)). For symmetryIn the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find[negativeNotes](/negativeNotes)used in this way. Nevertheless for the sake of symmetry,[negativeNotes](/negativeNotes)can be used on[Product](/Product).The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).

```
```[positiveNotes](/positiveNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

```
```[reviewAspect](/reviewAspect)

[StructuredValue](/StructuredValue)or[Text](/Text)```
```[reviewBody](/reviewBody)

[Text](/Text)```
```[reviewRating](/reviewRating)

[Rating](/Rating)`reviewRating`

applies to rating given by the review. The [aggregateRating](/aggregateRating)property applies to the review itself, as a creative work.[CreativeWork](/CreativeWork)

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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/1061](https://github.com/schemaorg/schemaorg/issues/1061)

### Examples

[Example 1](#eg-0324)

Copied

Example notes or example HTML without markup.

This would be part of a page such as http://www.politifact.com/texas/statements/2014/jul/23/rick-perry/rick-perry-claim-about-3000-homicides-illegal-immi/ Simple example based on material from that page. Earlier examples included Review and ClaimReview types while the latter design was under discussion, but this is not strictly needed now. <p> An example paragraph reviewing a claim expressed in another document. <dl> <dt>Date published:</dt> <dd>2014-07-23</dd> <dt>Review url:</dt> <dd>http://www.politifact.com/texas/statements/2014/jul/23/rick-perry/rick-perry-claim-about-3000-homicides-illegal-immi/</dd> <dt>Review by:</dt> <dd><a href="http://www.politifact.com/">Politifact</a> <img src="http://static.politifact.com/mediapage/jpgs/politifact-logo-big.jpg" alt="Politifact" /> </dd> </dl> <h3>Claim reviewed:</h3> <blockquote> More than 3,000 homicides were committed by 'illegal aliens' over the past six years. </blockquote> <div>Rating: 1 (best score: 6), "True".</div> <img src="http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif" alt="Politifact Pants on Fire rating logo" /> <h4>Item reviewed:</h4> <ul> <li>Claim author's name: Rich Perry. Job title: "Former Governor of Texas".</li> <li>Claim original document: "The St. Petersburg Times interview" (2014-07-17)</li> </ul> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Gov._Perry_CPAC_February_2015.jpg/440px-Gov._Perry_CPAC_February_2015.jpg" alt="photo of R.Perry."/> </p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope="" itemtype="https://schema.org/ClaimReview"> An example paragraph reviewing a claim expressed in another document. <dl> <dt>Date published:</dt> <dd itemprop="datePublished">2014-07-23</dd> <dt>Review url:</dt> <dd itemprop="url">http://www.politifact.com/texas/statements/2014/jul/23/rick-perry/rick-perry-claim-about-3000-homicides-illegal-immi/</dd> <dt>Review by:</dt> <dd> <span itemprop="author" itemscope="" itemtype="https://schema.org/Organization"> <span itemprop="name"><a itemprop="url" href="http://www.politifact.com/">Politifact</a></span> <img itemprop="image" src="http://static.politifact.com/mediapage/jpgs/politifact-logo-big.jpg" alt="Politifact" /> <link itemprop="sameAs" href="http://twitter.com/politifact"/> </span> </dd> </dl> <h3>Claim reviewed:</h3> <blockquote itemprop="claimReviewed"> More than 3,000 homicides were committed by 'illegal aliens' over the past six years. </blockquote> <span itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating"> Rating: <span itemprop="ratingValue">1</span> (best score: <span itemprop="bestRating">6</span>), "<span itemprop="alternateName">True</span>". <img itemprop="image" src="http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif" alt="Politifact Pants on Fire rating logo" /> </span> <h4>Item reviewed:</h4> <div itemprop="itemReviewed" itemscope="" itemtype="https://schema.org/CreativeWork"> <ul> <li itemprop="author" itemscope="" itemtype="https://schema.org/Person">Claim author's name: <span itemprop="name">Rich Perry</span>. Job title: "<span itemprop="jobTitle">Former Governor of Texas</span>". <link itemprop="sameAs" href="https://en.wikipedia.org/wiki/Rick_Perry"/> <a itemprop="sameAs" href="https://rickperry.org/">rickperry.org</a> <img itemprop="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Gov._Perry_CPAC_February_2015.jpg/440px-Gov._Perry_CPAC_February_2015.jpg" alt="photo of R.Perry."/> </li> <li>Claim original document: "<span itemprop="name">The St. Petersburg Times interview</span>" (<span itemprop="datePublished">2014-07-17</span>)</li> </ul> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ClaimReview", "datePublished": "2014-07-23", "url": "http://www.politifact.com/texas/statements/2014/jul/23/rick-perry/rick-perry-claim-about-3000-homicides-illegal-immi/", "author": { "@type": "Organization", "url": "http://www.politifact.com/", "image": "http://static.politifact.com/mediapage/jpgs/politifact-logo-big.jpg", "sameAs": "https://twitter.com/politifact" }, "claimReviewed": "More than 3,000 homicides were committed by \"illegal aliens\" over the past six years.", "reviewRating": { "@type": "Rating", "ratingValue": 1, "bestRating": 6, "image": "http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif", "alternateName": "True" }, "itemReviewed": { "@type": "CreativeWork", "author": { "@type": "Person", "name": "Rich Perry", "jobTitle": "Former Governor of Texas", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Gov._Perry_CPAC_February_2015.jpg/440px-Gov._Perry_CPAC_February_2015.jpg", "sameAs": [ "https://en.wikipedia.org/wiki/Rick_Perry", "https://rickperry.org/" ] }, "datePublished": "2014-07-17", "name": "The St. Petersburg Times interview [...]" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0325)

Copied

Example notes or example HTML without markup.

An extended ClaimReview example for fact-check of a TV Clip (JSON-LD only). The content is Dan's review of Obama's claim about Iran, where the item reviewed is a Clip, which is part of a larger VideoObject.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ClaimReview", "datePublished": "2017-07-06", "url": "http://danbri.org/2017/TODO", "author": { "@type": "Person", "url": "http://danbri.org/", "sameAs": "https://twitter.com/danbri" }, "claimReviewed": "In the middle of the Cold War, the United States played a role in the overthrow of a democratically-elected Iranian government.", "reviewBody": "This claim is true. The UK also played a role.", "itemReviewed": { "@type": "Clip", "startOffset": "350", "endOffset": "370", "isPartOf": { "@type": "VideoObject", "url": "https://www.youtube.com/watch?v=B_889oBKkNU", "name": "Clip from President Obama Speech to Muslim World in Cairo", "transcript": "http://www.nytimes.com/2009/06/04/us/politics/04obama.text.html" }, "author": { "@type": "Person", "name": "Barack Obama", "jobTitle": "44th President of the United States of America", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg", "sameAs": [ "https://twitter.com/barackobama", "https://www.wikidata.org/wiki/Q76" ] }, "datePublished": "2009-06-04", "name": "President Obama Speech to Muslim World in Cairo" } } </script>

Structured representation of the JSON-LD example.
