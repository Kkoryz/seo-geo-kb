---
title: "Article"
source_url: https://schema.org/Article
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2016-03-21
---

# Article

# Article

A Schema.org Type

- Canonical URL: https://schema.org/Article
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Article)

An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.


See also

See also

[blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[articleBody](/articleBody)

[Text](/Text)```
```[articleSection](/articleSection)

[Text](/Text)```
```[backstory](/backstory)

[CreativeWork](/CreativeWork)or[Text](/Text)[Article](/Article), typically a[NewsArticle](/NewsArticle), the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.```
```[pageEnd](/pageEnd)

[Integer](/Integer)or[Text](/Text)```
```[pageStart](/pageStart)

[Integer](/Integer)or[Text](/Text)```
```[pagination](/pagination)

[Text](/Text)```
```[speakable](/speakable)

[SpeakableSpecification](/SpeakableSpecification)or[URL](/URL)The

*speakable*property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.)

*id-value*URL references - uses*id-value*of an element in the page being annotated. The simplest use of*speakable*has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the

[cssSelector](/cssSelector)property.3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the

[xpath](/xpath)property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type,

[SpeakableSpecification](/SpeakableSpecification)which is defined to be a possible value of the*speakable*property.```
```[wordCount](/wordCount)

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

[URL](/URL)Instances of

[Article](/Article)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[Organization](/Organization)(often but not necessarily a[NewsMediaOrganization](/NewsMediaOrganization)), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.#### More specific Types

-
[AdvertiserContentArticle](/AdvertiserContentArticle) -
[NewsArticle](/NewsArticle) -
[Report](/Report) -
[SatiricalArticle](/SatiricalArticle) -
[ScholarlyArticle](/ScholarlyArticle) -
[SocialMediaPosting](/SocialMediaPosting) -
[TechArticle](/TechArticle)

### Acknowledgements

IPTC rNews properties

[rnews.org](http://rnews.org).

### Examples

[Example 1](#eg-0023)

Copied

Example notes or example HTML without markup.

How to Tie a Reef Knot by John Doe This article has been tweeted 1203 times and contains 78 user comments.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Article"> <span itemprop="name">How to Tie a Reef Knot</span> by <span itemprop="author">John Doe</span> This article has been tweeted 1203 times and contains 78 user comments. <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <div itemprop="interactionService" itemscope itemid="http://www.twitter.com" itemtype="https://schema.org/WebSite"> <meta itemprop="name" content="Twitter" /> </div> <meta itemprop="interactionType" content="https://schema.org/ShareAction"/> <meta itemprop="userInteractionCount" content="1203" /> </div> <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <meta itemprop="interactionType" content="https://schema.org/CommentAction"/> <meta itemprop="userInteractionCount" content="78" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Article"> <span property="name">How to Tie a Reef Knot</span> by <span property="author">John Doe</span> This article has been tweeted 1203 times and contains 78 user comments. <div property="interactionStatistic" typeof="InteractionCounter"> <div property="interactionService" typeof="WebSite"> <meta property="url" content="http://www.twitter.com"/> <meta property="name" content="Twitter" /> </div> <meta property="interactionType" content="https://schema.org/ShareAction"/> <meta property="userInteractionCount" content="1203" /> </div> <div property="interactionStatistic" typeof="InteractionCounter"> <meta property="interactionType" content="https://schema.org/CommentAction"/> <meta property="userInteractionCount" content="78" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Article", "author": "John Doe", "interactionStatistic": [ { "@type": "InteractionCounter", "interactionService": { "@type": "WebSite", "name": "Twitter", "url": "http://www.twitter.com" }, "interactionType": "https://schema.org/ShareAction", "userInteractionCount": "1203" }, { "@type": "InteractionCounter", "interactionType": "https://schema.org/CommentAction", "userInteractionCount": "78" } ], "name": "How to Tie a Reef Knot" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0228)

Copied

Example notes or example HTML without markup.

A JSON example for an Article about a particular event.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Article", "name": "Apple announces iPhone SE", "description": "New iPhone announced at 11:30 in California.", "about": { "@type": "Event", "name": "Apple's March 21 Announcements" }, "contentReferenceTime": "2016-03-21T11:30:00-07:00" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0398)

Copied

Example notes or example HTML without markup.

<!-- A list of the issues for a single volume of a given periodical. --> <div> <h1>The Lancet</h1> <p>Volume 376, July 2010-December 2010</p> <p>Published by Elsevier <ul> <li>ISSN 0140-6736</li> </ul> <h3>Issues:</h3> <ul> <li>No. 9734 Jul 3, 2010 p 1-68</li> <li>No. 9735 Jul 10, 2010 p 69-140</li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- A list of the issues for a single volume of a given periodical. --> <div itemscope itemtype="https://schema.org/Periodical"> <h1 itemprop="name">The Lancet</h1> <p>Volume 376, July 2010-December 2010</p> <p>Published by <span itemprop="publisher">Elsevier</span> <ul> <li>ISSN <span itemprop="issn">0140-6736</span></li> </ul> <h3>Issues:</h3> <div itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationVolume" itemid="#vol376"> <meta itemprop="volumeNumber" content="376"> <ul> <li itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#iss9734">No. <span itemprop="issueNumber">9734</span> <time datetime="2010-07-03" itemprop="datePublished">Jul 3, 2010</time> p <span itemprop="pageStart">1</span>-<span itemprop="pageEnd">68</span> </li> <li itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#iss9735">No. <span itemprop="issueNumber">9735</span> <time datetime="2010-07-03" itemprop="datePublished">Jul 10, 2010</time> p <span itemprop="pageStart">69</span>-<span itemprop="pageEnd">140</span> </li> </ul> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- A list of the issues for a single volume of a given periodical. --> <div vocab="https://schema.org/" typeof="Periodical"> <h1 property="name">The Lancet</h1> <p>Volume 376, July 2010-December 2010</p> <p>Published by <span property="publisher">Elsevier</span> <ul> <li>ISSN <span property="issn">0140-6736</span></li> </ul> <h3>Issues:</h3> <div property="hasPart" typeof="PublicationVolume" resource="#vol376"> <meta property="volumeNumber" content="376"> <ul> <li property="hasPart" typeof="PublicationIssue" resource="#issue9734">No. <span property="issueNumber">9734</span> <time datetime="2010-07-03" property="datePublished">Jul 3, 2010</time> p <span property="pageStart">1</span>-<span property="pageEnd">68</span> </li> <li property="hasPart" typeof="PublicationIssue" resource="#issue9735">No. <span property="issueNumber">9735</span> <time datetime="2010-07-03" property="datePublished">Jul 10, 2010</time> p <span property="pageStart">69</span>-<span property="pageEnd">140</span> </li> </ul> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Periodical", "issn": "0140-6736", "hasPart": { "@id": "vol376", "@type": "PublicationVolume", "volumeNumber": "376", "hasPart": [ { "@id": "issue9735", "@type": "PublicationIssue", "datePublished": "2010-07-03", "pageEnd": "140", "pageStart": "69", "issueNumber": "9735" }, { "@id": "issue9734", "@type": "PublicationIssue", "datePublished": "2010-07-03", "pageEnd": "68", "pageStart": "1", "issueNumber": "9734" } ] }, "name": "The Lancet", "publisher": "Elsevier" } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0399)

Copied

Example notes or example HTML without markup.

<!-- An article, fully linked to the issue, volume, and periodical in which it was published --> <div> <strong>Title:</strong> Be Careful What You Wish For: FRBR, Some Lacunae, A Review<br /> <strong>Author:</strong> Smiraglia, Richard P.<br /> <strong>Subjects:</strong> Catalog ; Works <br /> <strong>Is Part Of:</strong> <div>Cataloging &amp; Classification Quarterly, 2012, Vol. 50 (5),</div> <div>p.360-368 [Peer Reviewed Journal]<br /> <strong>Description:</strong> The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge—the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model. </div> <strong>Publisher:</strong> Taylor &amp; Francis Group<br /> <strong>Source:</strong> Routledge, Taylor &amp; Francis Group<br /> <strong>ISSN</strong> 0163-9374 ;<br /> <strong>E-ISSN</strong> 1544-4554;<br /> <strong>DOI:</strong> <a href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- An article, fully linked to the issue, volume, and periodical in which it was published --> <div itemscope itemtype="https://schema.org/ScholarlyArticle"> <strong>Title:</strong> <span itemprop="name">Be Careful What You Wish For: FRBR, Some Lacunae, A Review</span><br /> <strong>Author:</strong> <span itemprop="author">Smiraglia, Richard P.</span><br /> <strong>Subjects:</strong> <span itemprop="about">Catalog</span> ; <span itemprop="about">Works</span> <br /> <strong>Is Part Of:</strong> <div itemprop="isPartOf" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#issue"> <span itemscope itemtype="https://schema.org/Periodical" itemid="#periodical"> <span itemprop="name">Cataloging &amp; Classification Quarterly</span>, </span> <span itemprop="datePublished">2012</span>, Vol.<span itemprop="isPartOf" itemscope itemtype="https://schema.org/PublicationVolume"><link itemprop="isPartOf" href="#periodical" /><span itemprop="volumeNumber">50</span></span>(<span itemprop="issueNumber">5</span>), </div> <div> p.<span itemprop="pageStart">360</span>-<span itemprop="pageEnd">368</span> [Peer Reviewed Journal]<br /> <strong>Description:</strong> <span itemprop="description">The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge—the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.</span> </div> <span itemscope itemtype="https://schema.org/Periodical" itemid="#periodical"> <strong>Publisher:</strong> <span itemprop="publisher">Taylor &amp; Francis Group</span><br /> <strong>Source:</strong> Routledge, Taylor &amp; Francis Group<br /> <strong>ISSN</strong> <span itemprop="issn">0163-9374</span> ;<br /> <strong>E-ISSN</strong> <span itemprop="issn">1544-4554</span> ;<br /> </span> <strong>DOI:</strong> <a itemprop="sameAs" href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- An article, fully linked to the issue, volume, and periodical in which it was published --> <div vocab="https://schema.org/" typeof="ScholarlyArticle" resource="#article"> <strong>Title:</strong> <span property="name">Be Careful What You Wish For: FRBR, Some Lacunae, A Review</span><br /> <strong>Author:</strong> <span property="author">Smiraglia, Richard P.</span><br /> <strong>Subjects:</strong> <span property="about">Catalog</span> ; <span property="about">Works</span> <br /> <strong>Is Part Of:</strong> <div property="isPartOf" typeof="PublicationIssue" resource="#issue"> <span typeof="Periodical" resource="#periodical"> <span property="name">Cataloging &amp; Classification Quarterly</span>, </span> <span property="datePublished">2012</span>, Vol.<span property="isPartOf" typeof="PublicationVolume" resource="#periodical"><span property="volumeNumber">50</span></span>(<span property="issueNumber">5</span>), </div> <div> p.<span property="pageStart">360</span>-<span property="pageEnd">368</span> [Peer Reviewed Journal]<br /> <strong>Description:</strong> <span property="description">The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge—the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.</span> </div> <span resource="#periodical"> <strong>Publisher:</strong> <span property="publisher">Taylor &amp; Francis Group</span><br /> <strong>Source:</strong> Routledge, Taylor &amp; Francis Group<br /> <strong>ISSN</strong> <span property="issn">0163-9374</span> ;<br /> <strong>E-ISSN</strong> <span property="issn">1544-4554</span> ;<br /> </span> <strong>DOI:</strong> <a property="sameAs" href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@id": "#issue", "@type": "PublicationIssue", "issueNumber": "5", "datePublished": "2012", "isPartOf": { "@id": "#periodical", "@type": [ "PublicationVolume", "Periodical" ], "name": "Cataloging & Classification Quarterly", "issn": [ "1544-4554", "0163-9374" ], "volumeNumber": "50", "publisher": "Taylor & Francis Group" } }, { "@type": "ScholarlyArticle", "isPartOf": "#issue", "description": "The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge--the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.", "sameAs": "https://doi.org/10.1080/01639374.2012.682254", "about": [ "Works", "Catalog" ], "pageEnd": "368", "pageStart": "360", "name": "Be Careful What You Wish For: FRBR, Some Lacunae, A Review", "author": "Smiraglia, Richard P." } ] } </script>

Structured representation of the JSON-LD example.
