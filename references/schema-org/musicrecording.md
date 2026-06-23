---
title: "MusicRecording"
source_url: https://schema.org/MusicRecording
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MusicRecording

# MusicRecording

A Schema.org Type

- Canonical URL: https://schema.org/MusicRecording
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MusicRecording)

A music recording (track), usually a single song.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[byArtist](/byArtist)

[MusicGroup](/MusicGroup)or[Person](/Person)```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).```
```[inAlbum](/inAlbum)

[MusicAlbum](/MusicAlbum)```
```[inPlaylist](/inPlaylist)

[MusicPlaylist](/MusicPlaylist)```
```[isrcCode](/isrcCode)

[Text](/Text)```
```[recordingOf](/recordingOf)

[MusicComposition](/MusicComposition)Inverse property:

[recordedAs](/recordedAs)[CreativeWork](/CreativeWork)

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

[MusicRecording](/MusicRecording)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)[recordedAs](/recordedAs)

[MusicComposition](/MusicComposition)[track](/track)

[MusicGroup](/MusicGroup)or[MusicPlaylist](/MusicPlaylist)[tracks](/tracks)

[MusicGroup](/MusicGroup)or[MusicPlaylist](/MusicPlaylist)### Examples

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

[Example 2](#eg-0390)

Copied

Example notes or example HTML without markup.

An example of some of the tracks on the Beatles White Album.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicRecording", "@id": "http://musicbrainz.org/recording/3566e453-8f10-4a45-ac85-2c72eb183ca1", "name": "Back in the U.S.S.R.", "producer": { "@type": "Person", "name": "George Martin" }, "duration": "PT2M43S", "recordingOf": { "@type": "MusicComposition", "name": "Back in the U.S.S.R", "iswcCode": "T-010.140.236-1" } } </script>

Structured representation of the JSON-LD example.
