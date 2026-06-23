---
title: "MusicEvent"
source_url: https://schema.org/MusicEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MusicEvent

# MusicEvent

A Schema.org Type

- Canonical URL: https://schema.org/MusicEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MusicEvent)

Event type: Music event.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[about](/about)

[Thing](/Thing)Inverse property:

[subjectOf](/subjectOf)```
```[actor](/actor)

[PerformingGroup](/PerformingGroup)or[Person](/Person)[actors](/actors).```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[attendee](/attendee)

[Organization](/Organization)or[Person](/Person)[attendees](/attendees).```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[composer](/composer)

[Organization](/Organization)or[Person](/Person)```
```[contributor](/contributor)

[Organization](/Organization)or[Person](/Person)```
```[director](/director)

[Person](/Person)[directors](/directors).```
```[doorTime](/doorTime)

[DateTime](/DateTime)or[Time](/Time)```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[eventAttendanceMode](/eventAttendanceMode)

[EventAttendanceModeEnumeration](/EventAttendanceModeEnumeration)```
```[eventSchedule](/eventSchedule)

[Schedule](/Schedule)[Event](/Event)with a[Schedule](/Schedule). There are circumstances where it is preferable to share a schedule for a series of repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An[Event](/Event)that is associated with a[Schedule](/Schedule)using this property should not have[startDate](/startDate)or[endDate](/endDate)properties. These are instead defined within the associated[Schedule](/Schedule), this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months or seasons.```
```[eventStatus](/eventStatus)

[EventStatusType](/EventStatusType)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[hasParticipationOffer](/hasParticipationOffer)

[Offer](/Offer)```
```[hasSponsorshipOffer](/hasSponsorshipOffer)

[Offer](/Offer)```
```[inLanguage](/inLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage). Supersedes[language](/language).```
```[isAccessibleForFree](/isAccessibleForFree)

[Boolean](/Boolean)[free](/free).```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[maximumAttendeeCapacity](/maximumAttendeeCapacity)

[Integer](/Integer)```
```[maximumPhysicalAttendeeCapacity](/maximumPhysicalAttendeeCapacity)

[Integer](/Integer)[Event](/Event)whose[eventAttendanceMode](/eventAttendanceMode)is[OfflineEventAttendanceMode](/OfflineEventAttendanceMode)(or the offline aspects, in the case of a[MixedEventAttendanceMode](/MixedEventAttendanceMode)).```
```[maximumVirtualAttendeeCapacity](/maximumVirtualAttendeeCapacity)

[Integer](/Integer)[Event](/Event)whose[eventAttendanceMode](/eventAttendanceMode)is[OnlineEventAttendanceMode](/OnlineEventAttendanceMode)(or the online aspects, in the case of a[MixedEventAttendanceMode](/MixedEventAttendanceMode)).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[organizer](/organizer)

[Organization](/Organization)or[Person](/Person)```
```[performer](/performer)

[Organization](/Organization)or[Person](/Person)[performers](/performers).```
```[previousStartDate](/previousStartDate)

[Date](/Date)or[DateTime](/DateTime)```
```[recordedIn](/recordedIn)

[CreativeWork](/CreativeWork)Inverse property:

[recordedAt](/recordedAt)```
```[remainingAttendeeCapacity](/remainingAttendeeCapacity)

[Integer](/Integer)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[subEvent](/subEvent)

[Event](/Event)[subEvents](/subEvents).Inverse property:

[superEvent](/superEvent)```
```[superEvent](/superEvent)

[Event](/Event)Inverse property:

[subEvent](/subEvent)```
```[translator](/translator)

[Organization](/Organization)or[Person](/Person)```
```[typicalAgeRange](/typicalAgeRange)

[Text](/Text)```
```[workFeatured](/workFeatured)

[CreativeWork](/CreativeWork)```
```[workPerformed](/workPerformed)

[CreativeWork](/CreativeWork)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0189)

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

[Example 2](#eg-0201)

Copied

Example notes or example HTML without markup.

An example snippet of JSON-LD describing two B.B. King concerts.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-12T19:30", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "address" : "79 Washington St., Providence, RI" }, "offers" : { "@type" : "Offer", "url" : "https://www.etix.com/ticket/1771656" } }, { "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-13T20:00", "location" : { "@type" : "Place", "name" : "Lynn Auditorium", "address" : "Lynn, MA, 01901" }, "offers" : { "@type" : "Offer", "url" : "http://frontgatetickets.com/venue.php?id=11766" } }] </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.
