---
title: "SpecialAnnouncement"
source_url: https://schema.org/SpecialAnnouncement
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SpecialAnnouncement

# SpecialAnnouncement

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/SpecialAnnouncement
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SpecialAnnouncement)

A SpecialAnnouncement combines a simple date-stamped textual information update
with contextualized Web links and other structured data. It represents an information update made by a
locally-oriented organization, for example schools, pharmacies, healthcare providers, community groups, police,
local government.


For work in progress guidelines on Coronavirus-related markup see


The motivating scenario for SpecialAnnouncement is the


While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like


Several kinds of information can be provided:


We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and "url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20_coronavirus_pandemic" or "https://www.wikidata.org/wiki/Q81068910".


For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property's value. For an inline description, use a


We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info,


Many


The


The basic content of

For work in progress guidelines on Coronavirus-related markup see

[this doc](https://docs.google.com/document/d/14ikaGCKxo50rRM7nvKSlbUpjyIk2WMQd3IkB1lItlrM/edit#).The motivating scenario for SpecialAnnouncement is the

[Coronavirus pandemic](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic), and the initial vocabulary is oriented to this urgent situation. Schema.org expect to improve the markup iteratively as it is deployed and as feedback emerges from use. In addition to our usual[Github entry](https://github.com/schemaorg/schemaorg/issues/2490), feedback comments can also be provided in[this document](https://docs.google.com/document/d/1fpdFFxk8s87CWwACs53SGkYv3aafSxz_DTtOQxMrBJQ/edit#).While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like

[CAP](https://en.wikipedia.org/wiki/Common_Alerting_Protocol), although there may be overlaps. The intent is to cover the kinds of everyday practical information being posted to existing websites during an emergency situation.Several kinds of information can be provided:

We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and "url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20_coronavirus_pandemic" or "https://www.wikidata.org/wiki/Q81068910".

For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property's value. For an inline description, use a

[WebContent](/WebContent)type, and provide the url as a property of that, alongside at least a simple "[text](/text)" summary of the page. It is unlikely that a single SpecialAnnouncement will need all of the possible properties simultaneously.We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info,

[openingHours](/openingHours),[Event](/Event),[FAQPage](/FAQPage)etc. By linking to those pages from a[SpecialAnnouncement](/SpecialAnnouncement)you can help make it clearer that the events are related to the situation (e.g. Coronavirus) indicated by the[category](/category)property of the[SpecialAnnouncement](/SpecialAnnouncement).Many

[SpecialAnnouncement](/SpecialAnnouncement)s will relate to particular regions and to identifiable local organizations. Use[spatialCoverage](/spatialCoverage)for the region, and[announcementLocation](/announcementLocation)to indicate specific[LocalBusiness](/LocalBusiness)es and[CivicStructure](/CivicStructure)s. If the announcement affects both a particular region and a specific location (for example, a library closure that serves an entire region), use both[spatialCoverage](/spatialCoverage)and[announcementLocation](/announcementLocation).The

[about](/about)property can be used to indicate entities that are the focus of the announcement. We now recommend using[about](/about)only for representing non-location entities (e.g. a[Course](/Course)or a[RadioStation](/RadioStation)). For places, use[announcementLocation](/announcementLocation)and[spatialCoverage](/spatialCoverage). Consumers of this markup should be aware that the initial design encouraged the use of[about](/about)for locations too.The basic content of

[SpecialAnnouncement](/SpecialAnnouncement)is similar to that of an[RSS](https://en.wikipedia.org/wiki/RSS)or[Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard))feed. For publishers without such feeds, basic feed-like information can be shared by posting[SpecialAnnouncement](/SpecialAnnouncement)updates in a page, e.g. using JSON-LD. For sites with Atom/RSS functionality, you can point to a feed with the[webFeed](/webFeed)property. This can be a simple URL, or an inline[DataFeed](/DataFeed)object, with[encodingFormat](/encodingFormat)providing media type information, e.g. "application/rss+xml" or "application/atom+xml".| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[announcementLocation](/announcementLocation)

[CivicStructure](/CivicStructure)or[LocalBusiness](/LocalBusiness)[CivicStructure](/CivicStructure)or[LocalBusiness](/LocalBusiness)associated with the SpecialAnnouncement. For example, a specific testing facility or business with special opening hours. For a larger geographic region like a quarantine of an entire region, use[spatialCoverage](/spatialCoverage).```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[datePosted](/datePosted)

[Date](/Date)or[DateTime](/DateTime)```
```[diseasePreventionInfo](/diseasePreventionInfo)

[URL](/URL)or[WebContent](/WebContent)```
```[diseaseSpreadStatistics](/diseaseSpreadStatistics)

[Dataset](/Dataset)or[Observation](/Observation)or[URL](/URL)or[WebContent](/WebContent)[WebContent](/WebContent), or described directly as a[Dataset](/Dataset), or the specific[Observation](/Observation)s in the dataset. When a[WebContent](/WebContent)URL is provided, the page indicated might also contain more such markup.```
```[gettingTestedInfo](/gettingTestedInfo)

[URL](/URL)or[WebContent](/WebContent)[MedicalCondition](/MedicalCondition)), e.g. in the context of a pandemic.```
```[governmentBenefitsInfo](/governmentBenefitsInfo)

[GovernmentService](/GovernmentService)```
```[newsUpdatesAndGuidelines](/newsUpdatesAndGuidelines)

[URL](/URL)or[WebContent](/WebContent)[SpecialAnnouncement](/SpecialAnnouncement)markup on a site.```
```[publicTransportClosuresInfo](/publicTransportClosuresInfo)

[URL](/URL)or[WebContent](/WebContent)```
```[quarantineGuidelines](/quarantineGuidelines)

[URL](/URL)or[WebContent](/WebContent)```
```[schoolClosuresInfo](/schoolClosuresInfo)

[URL](/URL)or[WebContent](/WebContent)```
```[travelBans](/travelBans)

[URL](/URL)or[WebContent](/WebContent)```
```[webFeed](/webFeed)

[DataFeed](/DataFeed)or[URL](/URL)[CreativeWork](/CreativeWork)

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

[https://github.com/schemaorg/schemaorg/issues/2490](https://github.com/schemaorg/schemaorg/issues/2490)

### Examples

[Example 1](#eg-0297)

Copied

Example notes or example HTML without markup.

An announcement e.g. from a drive-through testing centre such as http://med.stanford.edu/news/all-news/2020/03/stanford-offers-drive-through-coronavirus-test.html

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "Stanford announce COVID-19 testing facility", "text": "Stanford Health Care’s same-day primary care program is offering drive-through testing, by appointment, for SARS-CoV-2, the coronavirus that causes COVID-19.", "datePosted": "2020-03-16", "url": "http://med.stanford.edu/news/all-news/2020/03/stanford-offers-drive-through-coronavirus-test.html", "category": "https://www.wikidata.org/wiki/Q81068910", "announcementLocation" : { "@type": "CovidTestingFacility", "name": "Stanford Health Care", "url": "https://stanfordhealthcare.org/" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0298)

Copied

Example notes or example HTML without markup.

An announcement showing school closure information.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "School Closure information for Eastergate School", "text": "School closure information has been published.", "datePosted": "2020-03-17", "expires": "2020-03-24", "category": "https://www.wikidata.org/wiki/Q81068910", "schoolClosuresInfo": "http://example.org/schools/school/eastergate-cofe-primary-school/closures", "webFeed": { "@type": "DataFeed", "@url": "http://example.org/schools/school/eastergate-cofe-primary-school/closures", "encodingFormat": "application/rss+atom" }, "announcementLocation" : { "@type": "School", "name": "Eastergate School", "url": "http://example.org/schools/school/eastergate-cofe-primary-school/", "location": "..." } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0299)

Copied

Example notes or example HTML without markup.

An announcement of shelter-in-place for a number of administrative areas.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "Shelter-in-place for 6 California counties", "text": "Shelter-in-place for 6 California counties", "datePosted": "2020-03-17", "category": "https://www.wikidata.org/wiki/Q81068910", "quarantineGuidelines": "http://example.org/california/shelter-in-place/", "spatialCoverage": [ { "@type": "AdministrativeArea", "name": "San Francisco County, CA" }, { "@type": "AdministrativeArea", "name": "Marin County, CA" }, { "@type": "AdministrativeArea", "name": "Santa Clara County, CA" }, { "@type": "AdministrativeArea", "name": "Santa Cruz County, CA" }, { "@type": "AdministrativeArea", "name": "Santa Clara County, CA" }, { "@type": "AdministrativeArea", "name": "San Mateo County, CA" }, { "@type": "AdministrativeArea", "name": "Santa Clara County, CA" }, { "@type": "AdministrativeArea", "name": "Contra Costa County, CA" }, { "@type": "AdministrativeArea", "name": "Alameda County, CA" }, { "@type": "City", "name": "Fresno, CA" } ] } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0300)

Copied

Example notes or example HTML without markup.

An announcement of where to pick up free lunches for school children in Boston.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "SpecialAnnouncement", "category": "https://www.wikidata.org/wiki/Q81068910", "name": "Breakfast and lunch for school children", "text": "The city of Boston will provide free breakfast and lunch meals will be provided for school age children attending Boston schools.", "datePosted": "2020-03-17", "newsUpdatesAndGuidelines": "https://www.bostonpublicschools.org/Page/8098", "spatialCoverage": { "@type": "City", "name": "Boston, MA" }, "announcementLocation": [ { "@type": "School", "name": "Charlestown High School", "address": { "@type": "PostalAddress", "streetAddress": "240 Medford Street", "addressLocality": "Charlestown", "addressRegion": "Massachusetts" } }, { "@type": "School", "name": "East Boston High School", "address": { "@type": "PostalAddress", "streetAddress": "86 White Street", "addressLocality": "Charlestown", "addressRegion": "Massachusetts" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0301)

Copied

Example notes or example HTML without markup.

Government benefits coverage for SpecialAnnouncement pertaining to the covid-19 situation.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "New Paycheck Protection Program for small business", "text": "Example Administration announces a new loan that helps small businesses keep their workforce employed during the Coronavirus (COVID-19) crisis.", "datePosted": "2020-03-30T08:00", "expires": "2020-04-24T23:59", "category": "https://www.wikidata.org/wiki/Q81068910", "spatialCoverage": { "type": "Country", "name": "US" }, "governmentBenefitsInfo": { "@type": "GovernmentService", "name": "Paycheck Protection Program", "url": "https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program-ppp", "provider": { "@type": "GovernmentOrganization", "name": "US Small Business Administration" }, "serviceType": "https://schema.org/BusinessSupport", "audience": { "@type": "Audience", "name": "Small businesses" } } } </script>

Structured representation of the JSON-LD example.
