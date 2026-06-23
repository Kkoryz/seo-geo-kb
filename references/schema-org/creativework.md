---
title: "CreativeWork"
source_url: https://schema.org/CreativeWork
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CreativeWork

# CreativeWork

A Schema.org Type

- Canonical URL: https://schema.org/CreativeWork
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CreativeWork)

The most generic kind of creative work, including books, movies, photographs, software programs, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[CreativeWork](/CreativeWork)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)[actionableFeedbackPolicy](/actionableFeedbackPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[NewsMediaOrganization](/NewsMediaOrganization)or other news-related[Organization](/Organization), a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.[appearance](/appearance)

[Claim](/Claim)[Claim](/Claim)in some[CreativeWork](/CreativeWork).[backstory](/backstory)

[Article](/Article)[Article](/Article), typically a[NewsArticle](/NewsArticle), the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.[cheatCode](/cheatCode)

[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)[citation](/citation)

[CreativeWork](/CreativeWork)[correctionsPolicy](/correctionsPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[Organization](/Organization)(e.g.[NewsMediaOrganization](/NewsMediaOrganization)), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.[discusses](/discusses)

[UserComments](/UserComments)[diversityPolicy](/diversityPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[Organization](/Organization)e.g. a[NewsMediaOrganization](/NewsMediaOrganization). For a[NewsMediaOrganization](/NewsMediaOrganization), a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.[documentation](/documentation)

[WebAPI](/WebAPI)[encodesCreativeWork](/encodesCreativeWork)

[MediaObject](/MediaObject)[ethicsPolicy](/ethicsPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[NewsMediaOrganization](/NewsMediaOrganization)regarding journalistic and publishing practices, or of a[Restaurant](/Restaurant), a page describing food source policies. In the case of a[NewsMediaOrganization](/NewsMediaOrganization), an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.[exampleOfWork](/exampleOfWork)

[CreativeWork](/CreativeWork)[firstAppearance](/firstAppearance)

[Claim](/Claim)[Claim](/Claim)in some[CreativeWork](/CreativeWork).[fundedItem](/fundedItem)

[Grant](/Grant)[Grant](/Grant). See also[ownershipFundingInfo](/ownershipFundingInfo).[gameTip](/gameTip)

[VideoGame](/VideoGame)[hasPart](/hasPart)

[CreativeWork](/CreativeWork)[isBasedOn](/isBasedOn)

[CreativeWork](/CreativeWork)[isBasedOnUrl](/isBasedOnUrl)

[CreativeWork](/CreativeWork)[isPartOf](/isPartOf)

[CreativeWork](/CreativeWork)[itemOffered](/itemOffered)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.[license](/license)

[CreativeWork](/CreativeWork)[lyrics](/lyrics)

[MusicComposition](/MusicComposition)[mainEntityOfPage](/mainEntityOfPage)

[Thing](/Thing)[background notes](/docs/datamodel.html#mainEntityBackground)for details.[masthead](/masthead)

[NewsMediaOrganization](/NewsMediaOrganization)[NewsMediaOrganization](/NewsMediaOrganization), a link to the masthead page or a page listing top editorial management.[messageAttachment](/messageAttachment)

[Message](/Message)[missionCoveragePrioritiesPolicy](/missionCoveragePrioritiesPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)[NewsMediaOrganization](/NewsMediaOrganization), a statement on coverage priorities, including any public agenda or stance on issues.[noBylinesPolicy](/noBylinesPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)[NewsMediaOrganization](/NewsMediaOrganization)or other news-related[Organization](/Organization), a statement explaining when authors of articles are not named in bylines.[ownershipFundingInfo](/ownershipFundingInfo)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[Organization](/Organization)(often but not necessarily a[NewsMediaOrganization](/NewsMediaOrganization)), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence. Note that the[funder](/funder)is also available and can be used to make basic funder information machine-readable.[parentItem](/parentItem)

[Answer](/Answer)or[Comment](/Comment)or[Question](/Question)[Article](/Article)or other[CreativeWork](/CreativeWork). See also[comment](/comment)which points from something to a comment about it.[publishingPrinciples](/publishingPrinciples)

[CreativeWork](/CreativeWork)or[Organization](/Organization)or[Person](/Person)[URL](/URL)) a document describing the editorial principles of an[Organization](/Organization)(or individual, e.g. a[Person](/Person)writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a[CreativeWork](/CreativeWork)(e.g.[NewsArticle](/NewsArticle)) the principles are those of the party primarily responsible for the creation of the[CreativeWork](/CreativeWork).While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a

[funder](/funder)) can be expressed using schema.org terminology.[recipeInstructions](/recipeInstructions)

[Recipe](/Recipe)[recordedIn](/recordedIn)

[Event](/Event)[sdLicense](/sdLicense)

[CreativeWork](/CreativeWork)[sharedContent](/sharedContent)

[Comment](/Comment)or[SocialMediaPosting](/SocialMediaPosting)[softwareHelp](/softwareHelp)

[SoftwareApplication](/SoftwareApplication)[step](/step)

[HowTo](/HowTo)[steps](/steps)

[HowTo](/HowTo)or[HowToSection](/HowToSection)[subjectOf](/subjectOf)

[Thing](/Thing)[translationOfWork](/translationOfWork)

[CreativeWork](/CreativeWork)[unnamedSourcesPolicy](/unnamedSourcesPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)or[Organization](/Organization)[Organization](/Organization)(typically a[NewsMediaOrganization](/NewsMediaOrganization)), a statement about policy on use of unnamed sources and the decision process required.[usageInfo](/usageInfo)

[CreativeWork](/CreativeWork)[usageInfo](/usageInfo)property indicates further information about a[CreativeWork](/CreativeWork). This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.

[verificationFactCheckingPolicy](/verificationFactCheckingPolicy)

[NewsMediaOrganization](/NewsMediaOrganization)[NewsMediaOrganization](/NewsMediaOrganization)or other fact-checking[Organization](/Organization).[workExample](/workExample)

[CreativeWork](/CreativeWork)[workFeatured](/workFeatured)

[Event](/Event)[workPerformed](/workPerformed)

[Event](/Event)[workTranslation](/workTranslation)

[CreativeWork](/CreativeWork)#### More specific Types

-
[AmpStory](/AmpStory) -
[ArchiveComponent](/ArchiveComponent) -
[Article](/Article) -
[Atlas](/Atlas) -
[Blog](/Blog) -
[Book](/Book) -
[Certification](/Certification) -
[Chapter](/Chapter) -
[Claim](/Claim) -
[Clip](/Clip) -
[Collection](/Collection) -
[ComicStory](/ComicStory) -
[Comment](/Comment) -
[Conversation](/Conversation) -
[Course](/Course) -
[CreativeWorkSeason](/CreativeWorkSeason) -
[CreativeWorkSeries](/CreativeWorkSeries) -
[Credential](/Credential) -
[DataCatalog](/DataCatalog) -
[Dataset](/Dataset) -
[DefinedTermSet](/DefinedTermSet) -
[Diet](/Diet) -
[DigitalDocument](/DigitalDocument) -
[Drawing](/Drawing) -
[Episode](/Episode) -
[ExercisePlan](/ExercisePlan) -
[Game](/Game) -
[Guide](/Guide) -
[HowTo](/HowTo) -
[HowToDirection](/HowToDirection) -
[HowToSection](/HowToSection) -
[HowToStep](/HowToStep) -
[HowToTip](/HowToTip) -
[HyperToc](/HyperToc) -
[HyperTocEntry](/HyperTocEntry) -
[LearningResource](/LearningResource) -
[Legislation](/Legislation) -
[Manuscript](/Manuscript) -
[Map](/Map) -
[MathSolver](/MathSolver) -
[MediaObject](/MediaObject) -
[MediaReviewItem](/MediaReviewItem) -
[Menu](/Menu) -
[MenuSection](/MenuSection) -
[Message](/Message) -
[Movie](/Movie) -
[MusicComposition](/MusicComposition) -
[MusicPlaylist](/MusicPlaylist) -
[MusicRecording](/MusicRecording) -
[Painting](/Painting) -
[Photograph](/Photograph) -
[Play](/Play) -
[Poster](/Poster) -
[PublicationIssue](/PublicationIssue) -
[PublicationVolume](/PublicationVolume) -
[Quotation](/Quotation) -
[Review](/Review) -
[Sculpture](/Sculpture) -
[SheetMusic](/SheetMusic) -
[ShortStory](/ShortStory) -
[SoftwareApplication](/SoftwareApplication) -
[SoftwareSourceCode](/SoftwareSourceCode) -
[SpecialAnnouncement](/SpecialAnnouncement) -
[Statement](/Statement) -
[TVSeason](/TVSeason) -
[TVSeries](/TVSeries) -
[Thesis](/Thesis) -
[VisualArtwork](/VisualArtwork) -
[WebContent](/WebContent) -
[WebPage](/WebPage) -
[WebPageElement](/WebPageElement) -
[WebSite](/WebSite)

### Acknowledgements

IPTC rNews properties

[rnews.org](http://rnews.org).

### Examples

[Example 1](#eg-0020)

Copied

Example notes or example HTML without markup.

<div> Resistance 3: Fall of Man by Sony Platform: Playstation 3 Rated: Mature <img alt="Fall of Man cover art" src="videogame.jpg" /> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <img itemprop="image" alt="Fall of Man cover art" src="videogame.jpg" /> <span itemprop="name">Resistance 3: Fall of Man</span> by <span itemprop="author">Sony</span>, Platform: Playstation 3 Rated:<span itemprop="contentRating">Mature</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CreativeWork"> <img property="image" alt="Fall of Man cover art" src="videogame.jpg" /> <span property="name">Resistance 3: Fall of Man</span> by <span property="author">Sony</span>, Platform: Playstation 3 Rated:<span property="contentRating">Mature</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CreativeWork", "author": "Sony", "contentRating": "Mature", "image": "videogame.jpg", "name": "Resistance 3: Fall of Man" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0175)

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

[Example 4](#eg-0190)

Copied

Example notes or example HTML without markup.

<div> <span>Julius Caesar at Shakespeare's Globe</span> <span>Wed 01 October 2014 19:30</span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope="" itemtype="https://schema.org/TheaterEvent"> <span itemprop="name">Julius Caesar at Shakespeare's Globe</span> <div itemprop="location" itemscope="" itemtype="https://schema.org/PerformingArtsTheater"> <meta itemprop="name" content="Shakespeare's Globe"/> <link itemprop="sameAs" href="http://www.shakespearesglobe.com/"/> <meta itemprop="address" content="London, UK"/> </div> <div itemprop="offers" itemscope="" itemtype="https://schema.org/Offer"> <link itemprop="url" href="/examples/ticket/0012301230123"/> </div> <span itemprop="startDate" content="2014-10-01T19:30">Wed 01 October 2014 19:30</span> <div itemprop="workPerformed" itemscope="" itemtype="https://schema.org/CreativeWork"> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Julius_Caesar_(play)"/> <link itemprop="sameAs" href="http://worldcat.org/entity/work/id/1807288036"/> <div itemprop="creator" itemscope="" itemtype="https://schema.org/Person"> <meta itemprop="name" content="William Shakespeare"/> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/William_Shakespeare"/> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TheaterEvent"> <span property="name">Julius Caesar at Shakespeare's Globe</span> <div property="location" typeof="PerformingArtsTheater"> <meta property="name" content="Shakespeare's Globe"/> <link property="sameAs" href="http://www.shakespearesglobe.com/"/> <meta property="address" content="London, UK"/> </div> <div property="offers" typeof="Offer"> <link property="url" href="/examples/ticket/0012301230123"/> </div> <span property="startDate" content="2014-10-01T19:30">Wed 01 October 2014 19:30</span> <div property="workPerformed" typeof="CreativeWork"> <link property="sameAs" href="http://en.wikipedia.org/wiki/Julius_Caesar_(play)"/> <link property="sameAs" href="http://worldcat.org/entity/work/id/1807288036"/> <div property="creator" typeof="Person"> <meta property="name" content="William Shakespeare"/> <link property="sameAs" href="http://en.wikipedia.org/wiki/William_Shakespeare"/> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "TheaterEvent", "name": "Julius Caesar at Shakespeare's Globe", "location": { "@type": "PerformingArtsTheater", "name": "Shakespeare's Globe", "sameAs": "http://www.shakespearesglobe.com/", "address": "London, UK" }, "offers": { "@type": "Offer", "url": "/examples/ticket/0012301230123" }, "startDate": "2014-10-01T19:30", "workPerformed": { "@type": "CreativeWork", "name": "Julius Caesar", "sameAs": "http://en.wikipedia.org/wiki/Julius_Caesar_(play)", "sameAs": "http://worldcat.org/entity/work/id/1807288036", "creator": { "@type": "Person", "name": "William Shakespeare", "sameAs": "http://en.wikipedia.org/wiki/William_Shakespeare" } } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0209)

Copied

Example notes or example HTML without markup.

Top 5 covers of Bob Dylan Songs by John Doe 5. If Not for You -- George Harrison 4. The Times They Are A-Changin' -- Tracy Chapman 3. It Ain't Me, Babe -- Johnny Cash and June Carter Cash 2. Don't Think Twice, It's Alright -- Waylon Jennings 1. All Along the Watchtower -- Jimi Hendrix

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/ItemList https://schema.org/CreativeWork"> <h1 itemprop="name">Top 5 covers of Bob Dylan Songs</h1> <div itemprop="author" itemscope itemtype="https://schema.org/Person"> by <span itemprop="name">John Doe</span> </div> <div itemprop="about" itemscope itemtype="https://schema.org/MusicRecording"> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <meta itemprop="name" content="Bob Dylan" /> </div> </div> <link itemprop="itemListOrder" href="https://schema.org/ItemListOrderAscending" /> <meta itemprop="numberOfItems" content="5" /> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <span itemprop="position">5</span> <div itemprop="item" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">If Not For You</span> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">George Harrison</span> </div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <span itemprop="position">4</span> <div itemprop="item" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">The Times They Are A-Changin'</span> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">Tracy Chapman</span> </div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <span itemprop="position">3</span> <div itemprop="item" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">It Ain't Me Babe</span> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">Johnny Cash</span> </div> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">June Carter Cash</span> </div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <span itemprop="position">2</span> <div itemprop="item" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">Don't Think Twice It's Alright</span> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">Waylon Jennings</span> </div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <span itemprop="position">1</span> <div itemprop="item" itemscope itemtype="https://schema.org/MusicRecording"> <span itemprop="name">All Along the Watchtower</span> <div itemprop="byArtist" itemscope itemtype="https://schema.org/MusicGroup"> <span itemprop="name">Jimi Hendrix</span> </div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ItemList CreativeWork"> <h1 property="name"> Top 5 covers of Bob Dylan Songs </h1> <div property="author" typeof="Person"> by <span property="name">John Doe</span> </div> <div property="about" typeof="MusicRecording"> <div property="byArtist" typeof="MusicGroup"> <meta property="name" content="Bob Dylan"> </div> </div> <link property="itemListOrder" href="https://schema.org/ItemListOrderAscending"> <meta property="numberOfItems" content="5"> <div property="itemListElement" typeof="ListItem"> <span property="position">5</span> <div property="item" typeof="MusicRecording"> <span property="name">If Not For You</span> <div property="byArtist" typeof="MusicGroup"> <span property="name">George Harrison</span> </div> </div> </div> <div property="itemListElement" typeof="ListItem"> <span property="position">4</span> <div property="item" typeof="MusicRecording"> <span property="name">The Times They Are A-Changin'</span> <div property="byArtist" typeof="MusicGroup"> <span property="name">Tracy Chapman</span> </div> </div> </div> <div property="itemListElement" typeof="ListItem"> <span property="position">3</span> <div property="item" typeof="MusicRecording"> <span property="name">It Ain't Me Babe</span> <div property="byArtist" typeof="MusicGroup"> <span property="name">Johnny Cash</span> </div> <div property="byArtist" typeof="MusicGroup"> <span property="name">June Carter Cash</span> </div> </div> </div> <div property="itemListElement" typeof="ListItem"> <span property="position">2</span> <div property="item" typeof="MusicRecording"> <span property="name">Don't Think Twice It's Alright</span> <div property="byArtist" typeof="MusicGroup"> <span property="name">Waylon Jennings</span> </div> </div> </div> <div property="itemListElement" typeof="ListItem"> <span property="position">1</span> <div property="item" typeof="MusicRecording"> <span property="name">All Along the Watchtower</span> <div property="byArtist" typeof="MusicGroup"> <span property="name">Jimi Hendrix</span> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["ItemList", "CreativeWork"], "name": "Top 5 covers of Bob Dylan Songs", "author": "John Doe", "about": { "@type": "MusicRecording", "byArtist": { "@type": "MusicGroup", "name": "Bob Dylan" } }, "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 5, "itemListElement": [ { "@type": "ListItem", "position": 5, "item": { "@type": "MusicRecording", "name": "If Not For You", "byArtist": { "@type": "MusicGroup", "name": "George Harrison" } } }, { "@type": "ListItem", "position": 4, "item": { "@type": "MusicRecording", "name": "The Times They Are A-Changin'", "byArtist": { "@type": "MusicGroup", "name": "Tracy Chapman" } } }, { "@type": "ListItem", "position": 3, "item": { "@type": "MusicRecording", "name": "It Ain't Me Babe", "byArtist": [ { "@type": "MusicGroup", "name": "Johnny Cash" }, { "@type": "MusicGroup", "name": "June Carter Cash" } ] } }, { "@type": "ListItem", "position": 2, "item": { "@type": "MusicRecording", "name": "Don't Think Twice It's Alright", "byArtist": { "@type": "MusicGroup", "name": "Waylon Jennings" } } }, { "@type": "ListItem", "position": 1, "item": { "@type": "MusicRecording", "name": "All Along the Watchtower", "byArtist": { "@type": "MusicGroup", "name": "Jimi Hendrix" } } } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0220)

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

[Example 7](#eg-0246)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Thing", "name": "Schema.org Ontology", "subjectOf": { "@type": "Book", "name": "The Complete History of Schema.org" } } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0257)

Copied

Example notes or example HTML without markup.

<div> Name: Assorted collection of items<br/> Extent: 285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> Name: <span itemprop="name">Assorted collection of items</span><br/> Extent: <span itemprop="materialExtent">285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)</span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["CreativeWork","ArchiveComponent"], "name": "Assorted collection of items", "materialExtent": "285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)" } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0258)

Copied

Example notes or example HTML without markup.

<div> Name: Assorted collection of items<br/> Extent: 1 folder containing 5 design drawings<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> Name: <span itemprop="name">Assorted collection of items</span><br/> Extent: <div> <div itemprop="materialExtent" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">1</span> <span itemprop="unitText">folder</span> </div> containing <div itemprop="materialExtent" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">5</span> <span itemprop="unitText">design drawings</span> </div> </div><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["CreativeWork","ArchiveComponent"], "materialExtent": [ { "@type": "QuantitativeValue", "unitText": "folder", "value": "1" }, { "@type": "QuantitativeValue", "unitText": "design drawings", "value": "5" } ] } </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0462)

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

[Example 11](#eg-0465)

Copied

Example notes or example HTML without markup.

Example of Job markup for experience standing in place of formal qualifications.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Software Engineer", "educationRequirements": { "@type": "EducationalOccupationalCredential", "credentialCategory": "bachelor degree" }, "experienceRequirements": { "@type": "OccupationalExperienceRequirements", "monthsOfExperience": "60" }, "experienceInPlaceOfEducation": true } </script>

Structured representation of the JSON-LD example.
