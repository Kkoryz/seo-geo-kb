---
title: "Person"
source_url: https://schema.org/Person
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2015-01-30
---

# Person

# Person

A Schema.org Type

- Canonical URL: https://schema.org/Person
- Equivalent Class: foaf:Person
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Person)

A person (alive, dead, undead, or fictional).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[additionalName](/additionalName)

[Text](/Text)```
```[address](/address)

[PostalAddress](/PostalAddress)or[Text](/Text)```
```[affiliation](/affiliation)

[Organization](/Organization)```
```[agentInteractionStatistic](/agentInteractionStatistic)

[InteractionCounter](/InteractionCounter)```
```[alumniOf](/alumniOf)

[EducationalOrganization](/EducationalOrganization)or[Organization](/Organization)Inverse property:

[alumni](/alumni)```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[birthDate](/birthDate)

[Date](/Date)```
```[birthPlace](/birthPlace)

[Place](/Place)```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[callSign](/callSign)

[Text](/Text)[callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.```
```[children](/children)

[Person](/Person)```
```[colleague](/colleague)

[Person](/Person)or[URL](/URL)[colleagues](/colleagues).```
```[contactPoint](/contactPoint)

[ContactPoint](/ContactPoint)[contactPoints](/contactPoints).```
```[deathDate](/deathDate)

[Date](/Date)```
```[deathPlace](/deathPlace)

[Place](/Place)```
```[duns](/duns)

[Text](/Text)```
```[email](/email)

[Text](/Text)```
```[familyName](/familyName)

[Text](/Text)```
```[faxNumber](/faxNumber)

[Text](/Text)```
```[follows](/follows)

[Person](/Person)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[gender](/gender)

[GenderType](/GenderType)or[Text](/Text)[Person](/Person), but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who are not a binary gender. The[gender](/gender)property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender[SportsTeam](/SportsTeam)can be indicated with a text value of "Mixed".```
```[givenName](/givenName)

[Text](/Text)```
```[globalLocationNumber](/globalLocationNumber)

[Text](/Text)[Global Location Number](http://www.gs1.org/gln)(GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasCredential](/hasCredential)

[Credential](/Credential)```
```[hasOccupation](/hasOccupation)

[Occupation](/Occupation)```
```[hasOfferCatalog](/hasOfferCatalog)

[OfferCatalog](/OfferCatalog)```
```[hasPOS](/hasPOS)

[Place](/Place)```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[homeLocation](/homeLocation)

[ContactPoint](/ContactPoint)or[Place](/Place)```
```[honorificPrefix](/honorificPrefix)

[Text](/Text)```
```[honorificSuffix](/honorificSuffix)

[Text](/Text)```
```[interactionStatistic](/interactionStatistic)

[InteractionCounter](/InteractionCounter)[interactionCount](/interactionCount).```
```[isicV4](/isicV4)

[Text](/Text)```
```[jobTitle](/jobTitle)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[knows](/knows)

[Person](/Person)```
```[knowsAbout](/knowsAbout)

[Text](/Text)or[Thing](/Thing)or[URL](/URL)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or[JobPosting](/JobPosting)descriptions.```
```[knowsLanguage](/knowsLanguage)

[Language](/Language)or[Text](/Text)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).```
```[lifeEvent](/lifeEvent)

[Event](/Event)```
```[makesOffer](/makesOffer)

[Offer](/Offer)Inverse property:

[offeredBy](/offeredBy)```
```[memberOf](/memberOf)

[MemberProgramTier](/MemberProgramTier)or[Organization](/Organization)or[ProgramMembership](/ProgramMembership)Inverse property:

[member](/member)```
```[naics](/naics)

[Text](/Text)```
```[nationality](/nationality)

[Country](/Country)```
```[netWorth](/netWorth)

[MonetaryAmount](/MonetaryAmount)or[PriceSpecification](/PriceSpecification)```
```[owns](/owns)

[Thing](/Thing)Inverse property:

[owner](/owner)```
```[parent](/parent)

[Person](/Person)[parents](/parents).```
```[performerIn](/performerIn)

[Event](/Event)```
```[pronouns](/pronouns)

[DefinedTerm](/DefinedTerm)or[StructuredValue](/StructuredValue)or[Text](/Text)In English, formulations such as "they/them", "she/her", and "he/him" are commonly used online and can also be used here. We do not intend to enumerate all possible micro-syntaxes in all languages. More structured and well-defined external values for pronouns can be referenced using the

[StructuredValue](/StructuredValue)or[DefinedTerm](/DefinedTerm)values.```
```[publishingPrinciples](/publishingPrinciples)

[CreativeWork](/CreativeWork)or[URL](/URL)[URL](/URL)) a document describing the editorial principles of an[Organization](/Organization)(or individual, e.g. a[Person](/Person)writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a[CreativeWork](/CreativeWork)(e.g.[NewsArticle](/NewsArticle)) the principles are those of the party primarily responsible for the creation of the[CreativeWork](/CreativeWork).While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a

[funder](/funder)) can be expressed using schema.org terminology.```
```[relatedTo](/relatedTo)

[Person](/Person)```
```[seeks](/seeks)

[Demand](/Demand)```
```[sibling](/sibling)

[Person](/Person)[siblings](/siblings).```
```[skills](/skills)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)```
```[spouse](/spouse)

[Person](/Person)```
```[taxID](/taxID)

[Text](/Text)```
```[telephone](/telephone)

[Text](/Text)```
```[vatID](/vatID)

[Text](/Text)[iso6523Code](/iso6523Code)with proper prefix.```
```[weight](/weight)

[Mass](/Mass)or[QuantitativeValue](/QuantitativeValue)```
```[workLocation](/workLocation)

[ContactPoint](/ContactPoint)or[Place](/Place)```
```[worksFor](/worksFor)

[Organization](/Organization)[Thing](/Thing)

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

[Person](/Person)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)[acquiredFrom](/acquiredFrom)

[OwnershipInfo](/OwnershipInfo)[actor](/actor)

[Clip](/Clip)or[CreativeWorkSeason](/CreativeWorkSeason)or[Episode](/Episode)or[Event](/Event)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[PodcastSeries](/PodcastSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)[actors](/actors)

[Clip](/Clip)or[Episode](/Episode)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)[agent](/agent)

[Action](/Action)*John*wrote a book.[alumni](/alumni)

[EducationalOrganization](/EducationalOrganization)or[Organization](/Organization)[artist](/artist)

[ComicIssue](/ComicIssue)or[ComicStory](/ComicStory)or[VisualArtwork](/VisualArtwork)[athlete](/athlete)

[SportsTeam](/SportsTeam)[attendee](/attendee)

[Event](/Event)[attendees](/attendees)

[Event](/Event)[author](/author)

[CreativeWork](/CreativeWork)or[Rating](/Rating)[awayTeam](/awayTeam)

[SportsEvent](/SportsEvent)[bccRecipient](/bccRecipient)

[Message](/Message)[bookingAgent](/bookingAgent)

[Reservation](/Reservation)[borrower](/borrower)

[LendAction](/LendAction)[broker](/broker)

[Invoice](/Invoice)or[Order](/Order)or[Reservation](/Reservation)or[Service](/Service)[buyer](/buyer)

[SellAction](/SellAction)[byArtist](/byArtist)

[MusicAlbum](/MusicAlbum)or[MusicRecording](/MusicRecording)[candidate](/candidate)

[VoteAction](/VoteAction)[ccRecipient](/ccRecipient)

[Message](/Message)[character](/character)

[CreativeWork](/CreativeWork)[children](/children)

[Person](/Person)[claimInterpreter](/claimInterpreter)

[Claim](/Claim)[Claim](/Claim)interpreted from[MediaObject](/MediaObject)content, the[interpretedAsClaim](/interpretedAsClaim)property can be used to indicate a claim contained, implied or refined from the content of a[MediaObject](/MediaObject).[coach](/coach)

[SportsTeam](/SportsTeam)[colleague](/colleague)

[Person](/Person)[colleagues](/colleagues)

[Person](/Person)[colorist](/colorist)

[ComicIssue](/ComicIssue)or[ComicStory](/ComicStory)or[VisualArtwork](/VisualArtwork)[competitor](/competitor)

[SportsEvent](/SportsEvent)[composer](/composer)

[Event](/Event)or[MusicComposition](/MusicComposition)[contributor](/contributor)

[CreativeWork](/CreativeWork)or[Event](/Event)[copyrightHolder](/copyrightHolder)

[CreativeWork](/CreativeWork)[creator](/creator)

[CreativeWork](/CreativeWork)or[UserComments](/UserComments)[creditedTo](/creditedTo)

[MusicRelease](/MusicRelease)[customer](/customer)

[Invoice](/Invoice)or[Order](/Order)[director](/director)

[Clip](/Clip)or[CreativeWorkSeason](/CreativeWorkSeason)or[Episode](/Episode)or[Event](/Event)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)[directors](/directors)

[Clip](/Clip)or[Episode](/Episode)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)[editor](/editor)

[CreativeWork](/CreativeWork)[employee](/employee)

[Organization](/Organization)[employees](/employees)

[Organization](/Organization)[endorsee](/endorsee)

[EndorseAction](/EndorseAction)[endorsers](/endorsers)

[Diet](/Diet)[followee](/followee)

[FollowAction](/FollowAction)[follows](/follows)

[Person](/Person)[founder](/founder)

[Organization](/Organization)[founders](/founders)

[Organization](/Organization)[fundedItem](/fundedItem)

[Grant](/Grant)[Grant](/Grant). See also[ownershipFundingInfo](/ownershipFundingInfo).[funder](/funder)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Grant](/Grant)or[MonetaryGrant](/MonetaryGrant)or[Organization](/Organization)or[Person](/Person)[grantee](/grantee)

[DigitalDocumentPermission](/DigitalDocumentPermission)[hiringOrganization](/hiringOrganization)

[JobPosting](/JobPosting)[homeTeam](/homeTeam)

[SportsEvent](/SportsEvent)[illustrator](/illustrator)

[Book](/Book)[inker](/inker)

[ComicIssue](/ComicIssue)or[ComicStory](/ComicStory)or[VisualArtwork](/VisualArtwork)[instructor](/instructor)

[CourseInstance](/CourseInstance)[CourseInstance](/CourseInstance).[knows](/knows)

[Person](/Person)[landlord](/landlord)

[RentAction](/RentAction)[legalRepresentative](/legalRepresentative)

[Organization](/Organization)[legislationCountersignedBy](/legislationCountersignedBy)

[Legislation](/Legislation)[legislationPassedBy](/legislationPassedBy)

[Legislation](/Legislation)[legislationResponsible](/legislationResponsible)

[Legislation](/Legislation)[lender](/lender)

[BorrowAction](/BorrowAction)[letterer](/letterer)

[ComicIssue](/ComicIssue)or[ComicStory](/ComicStory)or[VisualArtwork](/VisualArtwork)[loser](/loser)

[WinAction](/WinAction)[lyricist](/lyricist)

[MusicComposition](/MusicComposition)[maintainer](/maintainer)

[CreativeWork](/CreativeWork)[Dataset](/Dataset), software package ([SoftwareApplication](/SoftwareApplication)), or other[Project](/Project). A maintainer is a[Person](/Person)or[Organization](/Organization)that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When[maintainer](/maintainer)is applied to a specific version of something e.g. a particular version or packaging of a[Dataset](/Dataset), it is always possible that the upstream source has a different maintainer. The[isBasedOn](/isBasedOn)property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.[member](/member)

[Organization](/Organization)or[ProgramMembership](/ProgramMembership)[members](/members)

[Organization](/Organization)or[ProgramMembership](/ProgramMembership)[merchant](/merchant)

[Order](/Order)[musicBy](/musicBy)

[Clip](/Clip)or[Episode](/Episode)or[Movie](/Movie)or[MovieSeries](/MovieSeries)or[RadioSeries](/RadioSeries)or[TVSeries](/TVSeries)or[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)or[VideoObject](/VideoObject)[musicGroupMember](/musicGroupMember)

[MusicGroup](/MusicGroup)[offeredBy](/offeredBy)

[Offer](/Offer)[opponent](/opponent)

[ExerciseAction](/ExerciseAction)[organizer](/organizer)

[Event](/Event)[owner](/owner)

[Thing](/Thing)[parent](/parent)

[Person](/Person)[parents](/parents)

[Person](/Person)[participant](/participant)

[Action](/Action)*Steve*.[penciler](/penciler)

[ComicIssue](/ComicIssue)or[ComicStory](/ComicStory)or[VisualArtwork](/VisualArtwork)[performer](/performer)

[Event](/Event)[performers](/performers)

[Event](/Event)[producer](/producer)

[CreativeWork](/CreativeWork)[provider](/provider)

[Action](/Action)or[CreativeWork](/CreativeWork)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[FinancialIncentive](/FinancialIncentive)or[Invoice](/Invoice)or[ParcelDelivery](/ParcelDelivery)or[Reservation](/Reservation)or[Service](/Service)or[Trip](/Trip)[publishedBy](/publishedBy)

[PublicationEvent](/PublicationEvent)[publisher](/publisher)

[CreativeWork](/CreativeWork)or[FinancialIncentive](/FinancialIncentive)[readBy](/readBy)

[Audiobook](/Audiobook)[recipient](/recipient)

[AuthorizeAction](/AuthorizeAction)or[CommunicateAction](/CommunicateAction)or[DonateAction](/DonateAction)or[GiveAction](/GiveAction)or[Message](/Message)or[PayAction](/PayAction)or[ReturnAction](/ReturnAction)or[SendAction](/SendAction)or[TipAction](/TipAction)[referee](/referee)

[SportsEvent](/SportsEvent)[relatedTo](/relatedTo)

[Person](/Person)[reviewedBy](/reviewedBy)

[WebPage](/WebPage)[sdPublisher](/sdPublisher)

[CreativeWork](/CreativeWork)[sdPublisher](/sdPublisher)property helps make such practices more explicit.[seller](/seller)

[BuyAction](/BuyAction)or[Demand](/Demand)or[Flight](/Flight)or[Offer](/Offer)or[Order](/Order)[sender](/sender)

[Message](/Message)or[ReceiveAction](/ReceiveAction)[sibling](/sibling)

[Person](/Person)[siblings](/siblings)

[Person](/Person)[spokenByCharacter](/spokenByCharacter)

[Quotation](/Quotation)[sponsor](/sponsor)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Grant](/Grant)or[MedicalStudy](/MedicalStudy)or[Organization](/Organization)or[Person](/Person)[spouse](/spouse)

[Person](/Person)[toRecipient](/toRecipient)

[Message](/Message)[translator](/translator)

[CreativeWork](/CreativeWork)or[Event](/Event)[underName](/underName)

[Reservation](/Reservation)or[Ticket](/Ticket)[vendor](/vendor)

[BuyAction](/BuyAction)[winner](/winner)

[LoseAction](/LoseAction)#### More specific Types

### Acknowledgements

IPTC rNews properties

[rnews.org](http://rnews.org).

### Examples

[Example 1](#eg-0001)

Copied

Example notes or example HTML without markup.

Jane Doe <img src="janedoe.jpg" alt="Photo of Jane Doe"/> Professor 20341 Whitworth Institute Suite 123 405 Whitworth Seattle WA 98052 (425) 123-4567 <a href="mailto:jane-doe@xyz.edu">jane-doe@illinois.edu</a> Jane's home page: <a href="http://www.janedoe.com">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html">Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html">Bob Smith</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jane Doe</span> <img src="janedoe.jpg" itemprop="image" alt="Photo of Jane Doe"/> <span itemprop="jobTitle">Professor</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span itemprop="addressLocality">Seattle</span>, <span itemprop="addressRegion">WA</span> <span itemprop="postalCode">98052</span> </div> <span itemprop="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" itemprop="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" itemprop="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" itemprop="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" itemprop="colleague"> Bob Smith</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">Jane Doe</span> <img src="janedoe.jpg" property="image" alt="Photo of Jane Doe"/> <span property="jobTitle">Professor</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span property="addressLocality">Seattle</span>, <span property="addressRegion">WA</span> <span property="postalCode">98052</span> </div> <span property="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" property="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" property="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" property="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" property="colleague"> Bob Smith</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "address": { "@type": "PostalAddress", "addressLocality": "Seattle", "addressRegion": "WA", "postalCode": "98052", "streetAddress": "20341 Whitworth Institute 405 N. Whitworth", "extendedAddress": "Suite 123" }, "colleague": [ "http://www.xyz.edu/students/alicejones.html", "http://www.xyz.edu/students/bobsmith.html" ], "email": "mailto:jane-doe@xyz.edu", "image": "janedoe.jpg", "jobTitle": "Professor", "name": "Jane Doe", "telephone": "(425) 123-4567", "url": "http://www.janedoe.com" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0189)

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

[Example 3](#eg-0206)

Copied

Example notes or example HTML without markup.

A JSON example of an OrganizationRole, showing information about a 'member' of a 'SportsTeam', including time qualfiers (when he began and ended that role).

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/SportsTeam"> <span itemprop="name">San Francisco 49ers</span> <div itemprop="member" itemscope itemtype="https://schema.org/OrganizationRole"> <div itemprop="member" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Joe Montana</span> </div> <span itemprop="startDate">1979</span> <span itemprop="endDate">1992</span> <span itemprop="roleName">Quarterback</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="SportsTeam"> <span property="name">San Francisco 49ers</span> <div property="member" typeof="OrganizationRole"> <div property="member" typeof="https://schema.org/Person"> <span property="name">Joe Montana</span> </div> <span property="startDate">1979</span> <span property="endDate">1992</span> <span property="roleName">Quarterback</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SportsTeam", "name": "San Francisco 49ers", "member": { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Joe Montana" }, "startDate": "1979", "endDate": "1992", "roleName": "Quarterback" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0212)

Copied

Example notes or example HTML without markup.

George Bush, the 41st President of the United States is the father of George W. Bush, the 43rd President of the United States.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">George Bush</span>, the <span itemprop="disambiguatingDescription">41st President of the United States</span> is the father of <div itemprop="children" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">George W. Bush</span>, the <span itemprop="disambiguatingDescription">43rd President of the United States</span>. </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">George Bush</span>, the <span property="disambiguatingDescription">41st President of the United States</span> is the father of <div property="children" typeof="Person"> <span property="name">George W. Bush</span>, the <span property="disambiguatingDescription">43rd President of the United States</span>. </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "George Bush", "disambiguatingDescription": "41st President of the United States", "children": { "@type": "Person", "name": "George W. Bush", "disambiguatingDescription": "43rd President of the United States" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0249)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Peter Venkman", "hasOccupation": { "@type": "Occupation", "name": "Parapsychologist", "educationRequirements": "PhD in parapsychology" } } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0250)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Albert Einstein", "hasOccupation": [ { "@type": "Role", "hasOccupation": { "@type": "Occupation", "name": "Patent examiner", "occupationalCategory": "23-2099.00" }, "startDate": "1901", "endDate": "1906" }, { "@type": "Occupation", "name": "Professor of Physics", "educationRequirements": "PhD in Physics" } ] } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0276)

Copied

Example notes or example HTML without markup.

<!-- jobTitle utilising DefinedTerm --> <!-- JSONLD only example -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- jobTitle utilising DefinedTerm --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "A. N. Other", "jobTitle": { "@type": "DefinedTerm", "inDefinedTermSet": "https://targetjobs.co.uk/careers-advice/job-descriptions", "termCode": "277133-aid-workerhumanitarian-worker-job-description", "name": "Aid worker/humanitarian worker", "url": "https://targetjobs.co.uk/careers-advice/job-descriptions/277133-aid-workerhumanitarian-worker-job-description" } } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0295)

Copied

Example notes or example HTML without markup.

A media creator with a number of likes and follows.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Jane Doe", "interactionStatistic": [ { "@type": "InteractionCounter", "interactionType": "https://schema.org/LikeAction", "userInteractionCount": 1170 }, { "@type": "InteractionCounter", "interactionType": "https://schema.org/FollowAction", "userInteractionCount": 145098 } ] } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0374)

Copied

Example notes or example HTML without markup.

An example of a credit card bill (invoice). ACME Bank Bill for: January 2015 Visa invoice link: http://www.acmebank.com/invoice.pdf Customer: Jane Doe account ID: xxxx-xxxx-xxxx-1234 payment due: 2015-01-30 minimum payment: $15.00 total due: $200.00 billing period: 2014-12-21 to 2015-01-20 payment due

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Invoice"> <h1 itemprop="description">January 2015 Visa</h1> <a itemprop="url" href="http://acmebank.com/invoice.pdf">Invoice PDF</a> <div itemprop="broker" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <b itemprop="name">ACME Bank</b> </div> <span itemprop="accountId">xxxx-xxxx-xxxx-1234</span> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <time itemprop="paymentDueDate">2015-01-30</time> <div itemprop="minimumPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">15.00</span> <span itemprop="priceCurrency">USD</span> </div> <div itemprop="totalPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">200.00</span> <span itemprop="priceCurrency">USD</span> </div> <meta itemprop="billingPeriod" content="P30D" />starts:2014-12-21 30 days <link itemprop="paymentStatus" href="https://schema.org/PaymentDue" /> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Invoice"> <h1 property="description">January 2015 Visa</h1> <a property="url" href="http://acmebank.com/invoice.pdf">Invoice PDF</a> <div property="broker" typeof="BankOrCreditUnion"> <b property="name">ACME Bank</b> </div> <span property="accountId">xxxx-xxxx-xxxx-1234</span> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <time property="paymentDueDate">2015-01-30T12:00:00</time> <div property="minimumPaymentDue" typeof="PriceSpecification"> <span property="price">15.00</span> <span property="priceCurrency">USD</span> </div> <div property="totalPaymentDue" typeof="PriceSpecification"> <span property="price">200.00</span> <span property="priceCurrency">USD</span> </div> <meta property="billingPeriod" content="P30D" />starts:2014-12-21 30 days <link property="paymentStatus" href="https://schema.org/PaymentDue" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Invoice", "description": "January 2015 Visa bill.", "url": "http://acmebank.com/invoice.pdf", "broker": { "@type": "BankOrCreditUnion", "name": "ACME Bank" }, "accountId": "xxxx-xxxx-xxxx-1234", "customer": { "@type": "Person", "name": "Jane Doe" }, "paymentDueDate": "2015-01-30T12:00:00", "minimumPaymentDue": { "@type": "PriceSpecification", "price": 15.00, "priceCurrency": "USD" }, "totalPaymentDue": { "@type": "PriceSpecification", "price": 200.00, "priceCurrency": "USD" }, "billingPeriod": "P30D", "paymentStatus": "https://schema.org/PaymentDue" } </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0375)

Copied

Example notes or example HTML without markup.

An example of a invoice for a purchase and installation. ACME Home Heating Bill for: New furnace and installation Customer: Jane Doe payment due: 2015-01-30 minimum payment: $0.00 total due: $0.00 payment status: paid order: furnace model ABC123 order: installation labor

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Invoice"> <h1 itemprop="description">New furnace and installation</h1> <div itemprop="broker" itemscope itemtype="https://schema.org/LocalBusiness"> <b itemprop="name">ACME Home Heating</b> </div> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <time itemprop="paymentDueDate">2015-01-30</time> <div itemprop="minimumPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">0.00</span> <span itemprop="priceCurrency">USD</span> </div> <div itemprop="totalPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">0.00</span> <span itemprop="priceCurrency">USD</span> </div> <link itemprop="paymentStatus" href="https://schema.org/PaymentComplete" /> <div itemprop="referencesOrder" itemscope itemtype="https://schema.org/Order"> <span itemprop="description">furnace</span> <time itemprop="orderDate">2014-12-01</time> <span itemprop="orderNumber">123ABC</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">ACME Furnace 3000</span> <meta itemprop="productID" content="ABC123" /> </div> </div> <div itemprop="referencesOrder" itemscope itemtype="https://schema.org/Order"> <span itemprop="description">furnace installation</span> <time itemprop="orderDate">2014-12-02</time> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Service"> <span itemprop="description">furnace installation</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Invoice"> <h1 property="description">New furnace and installation</h1> <div property="broker" typeof="LocalBusiness"> <b property="name">ACME Home Heating</b> </div> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <time property="paymentDueDate">2015-01-30</time> <div property="minimumPaymentDue" typeof="PriceSpecification"> <span property="price">0.00</span> <span property="priceCurrency">USD</span> </div> <div property="totalPaymentDue" typeof="PriceSpecification"> <span property="price">0.00</span> <span property="priceCurrency">USD</span> </div> <meta itemprop="paymentStatus" content="PaymentComplete" /> <div property="referencesOrder" typeof="Order"> <span property="description">furnace</span> <time property="orderDate">2014-12-01</time> <span property="orderNumber">123ABC</span> <div property="orderedItem" typeof="Product"> <span property="name">ACME Furnace 3000</span> <meta property="productID" content="ABC123" /> </div> </div> <div property="referencesOrder" typeof="Order"> <span property="description">furnace installation</span> <time property="orderDate">2014-12-02</time> <div property="orderedItem" typeof="Service"> <span property="description">furnace installation</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Invoice", "broker": { "@type": "LocalBusiness", "name": "ACME Home Heating" }, "accountId": "xxxx-xxxx-xxxx-1234", "customer": { "@type": "Person", "name": "Jane Doe" }, "paymentDueDate": "2015-01-30", "minimumPaymentDue": { "@type": "PriceSpecification", "price": 0.00, "priceCurrency": "USD" }, "totalPaymentDue": { "@type": "PriceSpecification", "price": 0.00, "priceCurrency": "USD" }, "paymentStatus": "https://schema.org/PaymentComplete", "referencesOrder": [ { "@type": "Order", "description": "furnace", "orderDate": "2014-12-01", "orderNumber": "123ABC", "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice", "orderedItem": { "@type": "Product", "name": "ACME Furnace 3000", "productID": "ABC123" } }, { "@type": "Order", "description": "furnace installation", "orderDate": "2014-12-02", "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice", "orderedItem": { "@type": "Service", "description": "furnace installation" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 11](#eg-0376)

Copied

Example notes or example HTML without markup.

An example of an order for multiple items, shipped separately. ACME Supplies Customer: Jane Doe Order: Item abc123: 1 Widget: delivered 2015-03-10 Item def456: 3 Widget accessories: shipped 2015-03-12

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Order"> <div itemprop="seller" itemscope itemtype="https://schema.org/Organization"> <b itemprop="name">ACME Supplies</b> </div> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">abc123</span> <span itemprop="orderQuantity">1</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-10</time> </div> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">def456</span> <span itemprop="orderQuantity">4</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget accessories</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-15</time> <time itemprop="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Order"> <div property="seller" typeof="Organization"> <b property="name">ACME Supplies</b> </div> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">abc123</span> <span property="orderQuantity">1</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-10</time> </div> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">def456</span> <span property="orderQuantity">4</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget accessories</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-15</time> <time property="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Order", "seller": { "@type": "Organization", "name": "ACME Supplies" }, "customer": { "@type": "Person", "name": "Jane Doe" }, "orderedItem": [ { "@type": "OrderItem", "orderItemNumber": "abc123", "orderQuantity": 1, "orderedItem": { "@type": "Product", "name": "Widget" }, "orderItemStatus": "https://schema.org/OrderDelivered", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-10" } }, { "@type": "OrderItem", "orderItemNumber": "def456", "orderQuantity": 3, "orderedItem": { "@type": "Product", "name": "Widget accessories" }, "orderItemStatus": "https://schema.org/OrderInTransit", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-15", "expectedArrivalUntil": "2015-03-18" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 12](#eg-0388)

Copied

Example notes or example HTML without markup.

A MusicComposition Example. The following JSON-LD models the composition A Day in the Life by Lennon and McCartney, regardless of who performs or records the song.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MusicComposition", "@id": "http://musicbrainz.org/work/fd1aa4f2-ba26-3a05-b72d-4392c35a073c", "name": "A Day in the Life", "composer": [ { "@type": "Person", "name": "John Lennon", "@id": "http://musicbrainz.org/artist/4d5447d7-c61c-4120-ba1b-d7f471d385b9" }, { "@type": "Person", "name": "Paul McCartney", "@id": "http://musicbrainz.org/artist/ba550d0e-adac-4864-b88b-407cab5e76af" } ], "iswcCode": "T-010.140.236-1", "publisher": { "@type": "Organization", "name": "Northern Songs, Ltd.", "@id": "http://musicbrainz.org/label/26df054d-78cf-4d83-9bb1-a41816125528" }, "datePublished": "1967", "lyrics": { "@type": "CreativeWork", "inLanguage": "EN", "text": "I read the news today oh boy..." } } </script>

Structured representation of the JSON-LD example.

[Example 13](#eg-0427)

Copied

Example notes or example HTML without markup.

<p>Christopher Froome was sponsored by Sky in the Tour de France.</p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<p itemscope itemprop="Person" itemtype="https://schema.org/Person"> <span itemprop="name">Christopher Froome</span> was sponsored by <span itemprop="sponsor" itemtype="https://schema.org/Organization"> <a itemprop="url" href="http://www.skysports.com/">Sky</a></span> in the Tour de France. </p>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<p vocab="https://schema.org/" typeof="Person"> <span property="name">Christopher Froome</span> was sponsored by <span property="sponsor" typeof="https://schema.org/Organization"> <a property="url" href="http://www.skysports.com/">Sky</a></span> in the Tour de France. </p>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Christopher Froome", "sponsor": { "@type": "Organization", "name": "Sky", "url": "http://www.skysports.com/" } } </script>

Structured representation of the JSON-LD example.

[Example 14](#eg-0428)

Copied

Example notes or example HTML without markup.

<p>Rose Tyler was sponsored by Sarah Jane Smith in the membership process.</p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<p itemscope itemprop="Person" itemtype="https://schema.org/Person"> <span itemprop="name">Rose Tyler</span> was sponsored by <span itemscope itemprop="sponsor" itemtype="https://schema.org/Person"> <span itemprop="name">Sarah Jane Smith</span> </span> in the membership process. </p>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<p vocab="https://schema.org/" typeof="Person"> <span property="name">Rose Tyler</span> was sponsored by <span property="sponsor" typeof="https://schema.org/Person"> <span property="name">Sarah Jane Smith</span> </span> in the membership process. </p>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Rose Tyler", "sponsor": { "@type": "Person", "name": "Sarah Jane Smith" } } </script>

Structured representation of the JSON-LD example.

[Example 15](#eg-0454)

Copied

Example notes or example HTML without markup.

Fairly straightforward painting markup. <div> <h1 lang="fr">La trahison des images </h1> <p> A painting also known as The Treason of Images or The Treachery of Images. </p> <img src="http://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg" /> <div> <p> The painting shows a pipe. Below it, Magritte painted, <q lang="fr">Ceci n'est pas une pipe.</q>, French for "This is not a pipe." </p> <p> His statement is taken to mean that the painting itself is not a pipe. The painting is merely an image of a pipe. Hence, the description, "this is not a pipe." </p> <p> Similarly, the image shown above is neither a pipe nor even a painting, but rather a digital photograph. </p> <p> The painting is sometimes given as an example of meta message conveyed by paralanguage. Compare with Korzybski's <q>The word is not the thing</q> and <q>The map is not the territory</q>. </div> <ul> <li>Artist: <a href="https://www.freebase.com/m/06h88">René Magritte</a></li> <li>Dimensions: 940 mm × 635 mm</li> <li>Materials: oil on canvas</li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/VisualArtwork"> <link itemprop="sameAs" href="http://rdf.freebase.com/rdf/m.0439_q" /> <h1 itemprop="name" lang="fr">La trahison des images </h1> <p> A <span itemprop="artform">painting</span> also known as <span>The Treason of Images</span> or <span itemprop="alternateName">The Treachery of Images</span>. </p> <img itemprop="image" src="http://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg" /> <div itemprop="description"> <p> The painting shows a pipe. Below it, Magritte painted, <q lang="fr">Ceci n'est pas une pipe.</q>, French for "This is not a pipe." </p> <p> His statement is taken to mean that the painting itself is not a pipe. The painting is merely an image of a pipe. Hence, the description, "this is not a pipe." </p> <p> Similarly, the image shown above is neither a pipe nor even a painting, but rather a digital photograph. </p> <p> The painting is sometimes given as an example of meta message conveyed by paralanguage. Compare with Korzybski's <q>The word is not the thing</q> and <q>The map is not the territory</q>. </div> <ul> <li>Artist: <span itemprop="creator" itemscope itemtype="https://schema.org/Person"> <a itemprop="sameAs" href="https://www.freebase.com/m/06h88"> <span itemprop="name">René Magritte</span> </a> </span> </li> <li>Dimensions: <span itemprop="width">940 mm</span> × <span itemprop="height">635 mm</span> </li> <li>Materials: <span itemprop="artMedium">oil</span> on <span itemprop="artworkSurface">canvas</span> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="VisualArtwork"> <link property="sameAs" href="http://rdf.freebase.com/rdf/m.0439_q" /> <h1 property="name" lang="fr">La trahison des images </h1> <p> A <span property="artform">painting</span> also known as <span>The Treason of Images</span> or <span property="alternateName">The Treachery of Images</span>. </p> <img property="image" src="http://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg" /> <div property="description"> <p> The painting shows a pipe. Below it, Magritte painted, <q lang="fr">Ceci n'est pas une pipe.</q>, French for "This is not a pipe." </p> <p> His statement is taken to mean that the painting itself is not a pipe. The painting is merely an image of a pipe. Hence, the description, "this is not a pipe." </p> <p> Similarly, the image shown above is neither a pipe nor even a painting, but rather a digital photograph. </p> <p> The painting is sometimes given as an example of meta message conveyed by paralanguage. Compare with Korzybski's <q>The word is not the thing</q> and <q>The map is not the territory</q>. </div> <ul> <li>Artist: <span property="creator" typeof="Person"> <a property="sameAs" href="https://www.freebase.com/m/06h88"> <span property="name">René Magritte</span> </a> </span> </li> <li>Dimensions: <span property="width">940 mm</span> × <span property="height">635 mm</span> </li> <li>Materials: <span property="artMedium">oil</span> on <span property="artworkSurface">canvas</span> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "VisualArtwork", "name": "La trahison des images", "alternateName": "The Treachery of Images", "image": "http://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg", "description": "The painting shows a pipe. Below it, Magritte...", "creator": [ { "@type": "Person", "name": "René Magritte", "sameAs": "https://www.freebase.com/m/06h88" } ], "width": "940 mm", "height": "635 mm", "artMedium": "oil", "artworkSurface": "canvas" } </script>

Structured representation of the JSON-LD example.
