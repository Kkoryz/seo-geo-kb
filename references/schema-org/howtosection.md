---
title: "HowToSection"
source_url: https://schema.org/HowToSection
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# HowToSection

# HowToSection

A Schema.org Type

[Thing](/Thing)>

[CreativeWork](/CreativeWork)>

[HowToSection](/HowToSection)

[Thing](/Thing)>

[Intangible](/Intangible)>

[ItemList](/ItemList)>

[HowToSection](/HowToSection)

[Thing](/Thing)>

[Intangible](/Intangible)>

[ListItem](/ListItem)>

[HowToSection](/HowToSection)

- Canonical URL: https://schema.org/HowToSection
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+HowToSection)

A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

[CreativeWork](/CreativeWork)

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

[translationOfWork](/translationOfWork)[ItemList](/ItemList)

```
```[aggregateElement](/aggregateElement)

[Thing](/Thing)```
```[itemListElement](/itemListElement)

[ListItem](/ListItem)or[Text](/Text)or[Thing](/Thing)Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.

Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

```
```[itemListOrder](/itemListOrder)

[ItemListOrderType](/ItemListOrderType)or[Text](/Text)```
```[numberOfItems](/numberOfItems)

[Integer](/Integer)[ListItem](/ListItem)

```
```[item](/item)

[Thing](/Thing)```
```[nextItem](/nextItem)

[ListItem](/ListItem)```
```[position](/position)

[Integer](/Integer)or[Text](/Text)```
```[previousItem](/previousItem)

[ListItem](/ListItem)[Thing](/Thing)

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

[HowToSection](/HowToSection)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[HowTo](/HowTo)### Examples

[Example 1](#eg-0371)

Copied

Example notes or example HTML without markup.

<div> <strong><span>Change a Flat Tire</span></strong> <div>About <span>$20</span></div> <div>About <span>30 minutes</span></div> <div>Necessary Items:</div> <div>Spare tire</div> <div>Lug wrench</div> <div>Jack</div> <div>Wheel wedges</div> <div>Flares</div> <div id="steps"> <div>Preparation</div> <div> <div> Turn on your hazard lights and set the flares. </div> <div> You're going to need space and want to be visible.</div> <div> <div> Position your wheel wedges in front of the front tires if a rear tire is flat, or behind the rear tires if a front tire is flat. </div> <div> You don't want the car to move while you're working on it. </div> </div> </div> </div> <div id="steps"> <div>Raise the car</div> <div> <div> <span><img alt="image showing positioning of jack" src="position-jack.jpg" /></span> Position the jack underneath the car, next to the flat tire. </div> </div> <div> <div> <span><img alt="image showing car while still on the ground" src="car-on-ground.jpg" /></span> Raise the jack until the flat tire is just barely off of the ground. <span><img alt="image showing car raised by jack" src="car-raised.jpg" /></span> </div> <div> It doesn't need to be too high. </div> </div> <div> <div> Remove the hubcap and loosen the lug nuts. </div> </div> <div> <div> Remove the flat tire and put the spare tire on the exposed lug bolts. </div> </div> <div> <div> Tighten the lug nuts by hand. </div> <div> Don't use the wrench just yet. </div> </div> </div> <div id="steps"> <div>Finishing up</div> <div> <div> Lower the jack and tighten the lug nuts with the wrench. </div> </div> <div> <div> Replace the hubcap. </div> </div> <div> <div> Put the equipment and the flat tire away. </div> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/HowTo"> <strong><span itemprop="name">Change a Flat Tire</span></strong> <div>About <span itemprop="estimatedCost" itemscope itemtype="https://schema.org/MonetaryAmount"> <meta itemprop="currency" content="USD"/> <meta itemprop="value" content="20"/> </span>$20</div> <div>About <span itemprop="totalTime" content="PT30M">30 minutes</span></div> <div>Necessary Items:</div> <div itemprop="tool">Spare tire</div> <div itemprop="tool" itemscope itemtype="https://schema.org/HowToTool"> <span itemprop="name">Lug wrench</span> <img alt="image of a lug wrench" itemprop="image" src="lug-wrench.jpg"/> </div> <div itemprop="tool">Jack</div> <div itemprop="tool" itemscope itemtype="https://schema.org/HowToTool"> <span itemprop="name">Wheel wedges</span> <img alt="image showing wheel wedges" itemprop="image" src="wheel-wedges.jpg"/> </div> <div itemprop="supply" itemscope itemtype="https://schema.org/HowToSupply"> <span itemprop="name">Flares</span> <img alt="image of flares" itemprop="image" src="flares.jpg"/> </div> <div itemprop="step" itemscope itemtype="https://schema.org/HowToSection"> <div itemprop="name">Preparation</div> <meta itemprop="position" content="1"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="1"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Turn on your hazard lights and set the flares.</div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToTip"> <meta itemprop="position" content="2"/> <div itemprop="text">You're going to need space and want to be visible.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="2"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Position your wheel wedges in front of the front tires if a rear tire is flat, or behind the rear tires if a front tire is flat.</div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToTip"> <meta itemprop="position" content="2"/> <div itemprop="text">You don't want the car to move while you're working on it.</div> </div> </div> </div> <div itemprop="step" itemscope itemtype="https://schema.org/HowToSection"> <div itemprop="name">Raise the car</div> <meta itemprop="position" content="2"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="1"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <img alt="image showing positioning of jack" itemprop="duringMedia" src="position-jack.jpg" /> <div itemprop="text">Position the jack underneath the car, next to the flat tire.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="2"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="beforeMedia" itemscope itemtype="https://schema.org/ImageObject"> <img alt="image showing car while still on the ground" itemprop="contentUrl" src="car-on-ground.jpg" /> </div> <div itemprop="text">Raise the jack until the flat tire is just barely off of the ground.</div> <div itemprop="afterMedia" itemscope itemtype="https://schema.org/ImageObject"> <img alt="image showing car raised by jack" itemprop="contentUrl" src="car-raised.jpg" /> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToTip"> <meta itemprop="position" content="2"/> <div itemprop="text">It doesn't need to be too high.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="3"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Remove the hubcap and loosen the lug nuts.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="4"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Remove the flat tire and put the spare tire on the exposed lug bolts.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="5"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Tighten the lug nuts by hand.</div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToTip"> <meta itemprop="position" content="2"/> <div itemprop="text">Don't use the wrench just yet.</div> </div> </div> </div> <div itemprop="step" itemscope itemtype="https://schema.org/HowToSection"> <div itemprop="name">Finishing up</div> <meta itemprop="position" content="3"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="1"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"> <div itemprop="text">Lower the jack and tighten the lug nuts with the wrench.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="2"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Replace the hubcap.</div> </div> </div> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep"> <meta itemprop="position" content="3"/> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToDirection"> <meta itemprop="position" content="1"/> <div itemprop="text">Put the equipment and the flat tire away.</div> </div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="HowTo"> <strong><span property="name">Change a Flat Tire</span></strong> <div>About <span property="estimatedCost" typeof="MonetaryAmount"> <meta property="currency" content="USD"/> <meta property="value" content="20"/> </span>$20</div> <div>About <span property="totalTime" content="PT30M">30 minutes</span></div> <div>Necessary Items:</div> <div property="tool">Spare tire</div> <div property="tool" typeof="HowToTool"> <span property="name">Lug wrench</span> <img alt="image of a lug wrench" property="image" src="lug-wrench.jpg"/> </div> <div property="tool">Jack</div> <div property="tool" typeof="HowToTool"> <span property="name">Wheel wedges</span> <img alt="image showing wheel wedges" property="image" src="wheel-wedges.jpg"/> </div> <div property="supply" typeof="HowToSupply"> <span property="name">Flares</span> <img alt="image of flares" property="image" src="flares.jpg"/> </div> <div property="step" typeof="HowToSection"> <div property="name">Preparation</div> <meta property="position" content="1"/> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="1"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Turn on your hazard lights and set the flares.</div> </div> <div property="itemListElement" typeof="HowToTip"> <meta property="position" content="2"/> <div property="text">You're going to need space and want to be visible.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="2"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Position your wheel wedges in front of the front tires if a rear tire is flat, or behind the rear tires if a front tire is flat.</div> </div> <div property="itemListElement" typeof="HowToTip"> <meta property="position" content="2"/> <div property="text">You don't want the car to move while you're working on it.</div> </div> </div> </div> <div property="step" typeof="HowToSection"> <div property="name">Raise the car</div> <meta property="position" content="2"/> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="1"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <img alt="image showing positioning of jack" property="duringMedia" src="position-jack.jpg" /> <div property="text">Position the jack underneath the car, next to the flat tire.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="2"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="beforeMedia" typeof="ImageObject"> <img alt="image showing car while still on the ground" property="contentUrl" src="car-on-ground.jpg" /> </div> <div property="text">Raise the jack until the flat tire is just barely off of the ground.</div> <div property="afterMedia" typeof="ImageObject"> <img alt="image showing car raised by jack" property="contentUrl" src="car-raised.jpg" /> </div> </div> <div property="itemListElement" typeof="HowToTip"> <meta property="position" content="2"/> <div property="text">It doesn't need to be too high.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="3"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Remove the hubcap and loosen the lug nuts.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="4"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Remove the flat tire and put the spare tire on the exposed lug bolts.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="5"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Tighten the lug nuts by hand.</div> </div> <div property="itemListElement" typeof="HowToTip"> <meta property="position" content="2"/> <div property="text">Don't use the wrench just yet.</div> </div> </div> </div> <div property="step" typeof="HowToSection"> <div property="name">Finishing up</div> <meta property="position" content="3"/> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="1"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"> <div property="text">Lower the jack and tighten the lug nuts with the wrench.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="2"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Replace the hubcap.</div> </div> </div> <div property="itemListElement" typeof="HowToStep"> <meta property="position" content="3"/> <div property="itemListElement" typeof="HowToDirection"> <meta property="position" content="1"/> <div property="text">Put the equipment and the flat tire away.</div> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "HowTo", "name": "Change a Flat Tire", "estimatedCost": { "@type": "MonetaryAmount", "currency": "USD", "value": "20" }, "totalTime": "PT30M", "tool": [ { "@type": "HowToTool", "name": "Spare tire" }, { "@type": "HowToTool", "name": "Lug wrench", "image": "lug-wrench.jpg" }, { "@type": "HowToTool", "name": "Jack" }, { "@type": "HowToTool", "name": "Wheel wedges", "image": "wheel-wedges.jpg" } ], "supply": { "@type": "HowToSupply", "name": "Flares", "image": "flares.jpg" }, "step": [ { "@type": "HowToSection", "name": "Preparation", "position": "1", "itemListElement": [ { "@type": "HowToStep", "position": "1", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Turn on your hazard lights and set the flares." }, { "@type": "HowToTip", "position": "2", "text": "You're going to need space and want to be visible." } ] }, { "@type": "HowToStep", "position": "2", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Position your wheel wedges in front of the front tires if a rear tire is flat, or behind the rear tires if a front tire is flat" }, { "@type": "HowToTip", "position": "2", "text": "You don't want the car to move while you're working on it." } ] } ] }, { "@type": "HowToSection", "name": "Raise the car", "position": "2", "itemListElement": [ { "@type": "HowToStep", "position": "1", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "duringMedia": "position-jack.jpg", "text": "Position the jack underneath the car, next to the flat tire." } ] }, { "@type": "HowToStep", "position": "2", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "beforeMedia": { "@type": "ImageObject", "contentUrl": "car-on-ground.jpg" }, "afterMedia": { "@type": "ImageObject", "contentUrl": "car-raised.jpg" }, "text": "Raise the jack until the flat tire is just barely off of the ground." }, { "@type": "HowToTip", "position": "2", "text": "It doesn't need to be too high." } ] }, { "@type": "HowToStep", "position": "3", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Remove the hubcap and loosen the lug nuts." } ] }, { "@type": "HowToStep", "position": "4", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Remove the flat tire and put the spare tire on the exposed lug bolts." } ] }, { "@type": "HowToStep", "position": "5", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Tighten the lug nuts by hand." }, { "@type": "HowToTip", "position": "2", "text": "Don't use the wrench just yet." } ] } ] }, { "@type": "HowToSection", "name": "Finishing up", "position": "3", "itemListElement": [ { "@type": "HowToStep", "position": "1", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Lower the jack and tighten the lug nuts with the wrench." } ] }, { "@type": "HowToStep", "position": "2", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Replace the hubcap." } ] }, { "@type": "HowToStep", "position": "3", "itemListElement": [ { "@type": "HowToDirection", "position": "1", "text": "Put the equipment and the flat tire away." } ] } ] } ] } </script>

Structured representation of the JSON-LD example.
