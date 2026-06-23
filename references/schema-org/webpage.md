---
title: "WebPage"
source_url: https://schema.org/WebPage
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# WebPage

# WebPage

A Schema.org Type

- Canonical URL: https://schema.org/WebPage
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+WebPage)

A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as

`breadcrumb`

may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[breadcrumb](/breadcrumb)

[BreadcrumbList](/BreadcrumbList)or[Text](/Text)```
```[lastReviewed](/lastReviewed)

[Date](/Date)```
```[mainContentOfPage](/mainContentOfPage)

[WebPageElement](/WebPageElement)[aspect](/aspect).```
```[primaryImageOfPage](/primaryImageOfPage)

[ImageObject](/ImageObject)```
```[relatedLink](/relatedLink)

[URL](/URL)```
```[reviewedBy](/reviewedBy)

[Organization](/Organization)or[Person](/Person)```
```[significantLink](/significantLink)

[URL](/URL)[significantLinks](/significantLinks).```
```[speakable](/speakable)

[SpeakableSpecification](/SpeakableSpecification)or[URL](/URL)The

*speakable*property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.)

*id-value*URL references - uses*id-value*of an element in the page being annotated. The simplest use of*speakable*has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the

[cssSelector](/cssSelector)property.3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the

[xpath](/xpath)property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type,

[SpeakableSpecification](/SpeakableSpecification)which is defined to be a possible value of the*speakable*property.```
```[specialty](/specialty)

[Specialty](/Specialty)[CreativeWork](/CreativeWork)

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

[WebPage](/WebPage)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)[CreativeWork](/CreativeWork). In the case of[MediaReview](/MediaReview), the items in a[MediaReviewItem](/MediaReviewItem)may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.[originalMediaLink](/originalMediaLink)

[MediaReview](/MediaReview)[MediaObject](/MediaObject)content, e.g. video file.#### More specific Types

-
[AboutPage](/AboutPage) -
[CheckoutPage](/CheckoutPage) -
[CollectionPage](/CollectionPage) -
[ContactPage](/ContactPage) -
[FAQPage](/FAQPage) -
[ItemPage](/ItemPage) -
[MedicalWebPage](/MedicalWebPage) -
[ProfilePage](/ProfilePage) -
[QAPage](/QAPage) -
[RealEstateListing](/RealEstateListing) -
[SearchResultsPage](/SearchResultsPage)

### Examples

[Example 1](#eg-0207)

Copied

Example notes or example HTML without markup.

<body> <h1>Lecture 12: Graphs, networks, incidence matrices</h1> <p>These video lectures of Professor Gilbert Strang teaching 18.06 were recorded in Fall 1999 and do not correspond precisely to the current edition of the textbook.</p> <div> <h4>About <span>MIT OpenCourseWare</span></h4> </div> <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US"><img src="/images/cc_by-nc-sa.png" alt="Creative Commons logo with terms BY-NC-SA." /></a> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope="" itemtype="https://schema.org/WebPage"> <h1 itemprop="name">Lecture 12: Graphs, networks, incidence matrices</h1> <p itemprop="description">These video lectures of Professor Gilbert Strang teaching 18.06 were recorded in Fall 1999 and do not correspond precisely to the current edition of the textbook.</p> <div itemprop="publisher" itemscope="" itemtype="https://schema.org/CollegeOrUniversity"> <h4 class="footer">About <span itemprop="name">MIT OpenCourseWare</span></h4> </div> <a itemprop="license" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US"><img src="/images/cc_by-nc-sa.png" alt="Creative Commons logo with terms BY-NC-SA." /></a> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> <h1 property="name">Lecture 12: Graphs, networks, incidence matrices</h1> <p property="description">These video lectures of Professor Gilbert Strang teaching 18.06 were recorded in Fall 1999 and do not correspond precisely to the current edition of the textbook.</p> <div property="publisher" typeof="CollegeOrUniversity"> <h4 class="footer">About <span property="name">MIT OpenCourseWare</span></h4> </div> <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US"><img src="/images/cc_by-nc-sa.png" alt="Creative Commons logo with terms BY-NC-SA." /></a> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "name": "Lecture 12: Graphs, networks, incidence matrices", "description": "These video lectures of Professor Gilbert Strang teaching 18.06 were recorded in Fall 1999 and do not correspond precisely to the current edition of the textbook.", "publisher": { "@type": "CollegeOrUniversity", "name": "MIT OpenCourseWare" }, "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0462)

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
