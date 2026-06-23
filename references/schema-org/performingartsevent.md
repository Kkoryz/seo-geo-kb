---
title: "PerformingArtsEvent"
source_url: https://schema.org/PerformingArtsEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-04-28
---

# PerformingArtsEvent

# PerformingArtsEvent

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/PerformingArtsEvent
- Equivalent Class: lrmoo:F31_Performance
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PerformingArtsEvent)

Live performance

[Event of the performing arts (music, theatre, dance, acrobatics, spoken word), including performance art and performative sports (e.g. choreographed forms of martial arts, figure skating, competitive ballroom dancing).](http://schema.org/Event)


Note: UseNote: Use

[additionalType](http://schema.org/additionalType)to differentiate between productions / shows (PerformanceWork, EventSeries), tours (EventSeries), and individual performances.| Property | Expected Type | Description |
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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/4468](https://github.com/schemaorg/schemaorg/issues/4468)

### Examples

[Example 1](#eg-4468a)

Copied

Example notes or example HTML without markup.

Gravity and Other Myths - Ten Thousand Hours Tuesday, April 28, 2026 | 7:00 pm Salle Desjardins <img src="https://www.centredesarts.ca/img-activites/gravity-and-the-other-myths-1280x720.webp" /> Circus Eight acrobats and one musician investigate physical skill; how we obtain it, how we perfect it, and how it can transform our lives. Through highlighting the nuance of high level acrobatics, audiences experience a heightened appreciation of the countless hours required to master the skills they are witnessing. Set to a driving, dynamic and intricate musical score using percussion/drums live on-stage, Ten Thousand Hours is a revelry of the distinct physical language that defines GOM and a celebration of the pursuit of mastery. This is a love letter to our bodies and the amazing things they let us do every day. This is an invitation to watch us work. Regular tickets: $48 <a href="https://centredesarts.tuxedobillet.com/main/gravity-and-other-myths-ten-thousand-hours-260428/20260428190000">Purchase</a>

[Example 2](#eg-4468b)

Copied

Example notes or example HTML without markup.

<div> <h1>Rinse</h1> <p> Rinse recreates an origin myth on stage—recounting personal narratives in relation to dance, art, feminism, desire, love, popular culture, and colonial history. </p> <div> <strong>Venue:</strong> Azrieli Studio <div> 1 Elgin Street, Ottawa, ON K1P 5W1, CA </div> </div> <p> <strong>Date and Time:</strong><br> January 22, 2026, 8:00 PM - 9:00 PM </p> <div> <strong>Performer:</strong> Amrita Hepi </div> <div> <strong>Organizer:</strong> NAC Indigenous Theatre </div> <img src="https://naccnaca-eventimages.s3.amazonaws.com/38366/amrita_hero__large.jpg" alt="Rinse"> <div> <strong>Tickets:</strong> 35 $<br> <a href="https://nac-cna.ca/en/event/38366">Buy Tickets</a> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Event"> <h1 itemprop="name">Rinse</h1> <p itemprop="description"> Rinse recreates an origin myth on stage—recounting personal narratives in relation to dance, art, feminism, desire, love, popular culture, and colonial history. </p> <div itemprop="location" itemscope itemtype="https://schema.org/Place" itemid="https://nac-cna.ca/venue/studio#Place"> <strong>Venue:</strong> <span itemprop="name">Azrieli Studio</span> <link itemprop="sameAs" href="http://www.wikidata.org/entity/Q109326244"> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">1 Elgin Street</span>, <span itemprop="addressLocality">Ottawa</span>, <span itemprop="addressRegion">ON</span> <span itemprop="postalCode">K1P 5W1</span>, <span itemprop="addressCountry">CA</span> </div> </div> <p> <strong>Date and Time:</strong><br> <time itemprop="startDate" datetime="2026-01-22T20:00:00-05:00">January 22, 2026, 8:00 PM</time> - <time itemprop="endDate" datetime="2026-01-22T21:00:00-05:00">9:00 PM</time> </p> <div itemprop="performer" itemscope itemtype="https://schema.org/Person"> <strong>Performer:</strong> <span itemprop="name">Amrita Hepi</span> <link itemprop="sameAs" href="http://www.wikidata.org/entity/Q134599760"> </div> <div itemprop="workPerformed" itemscope itemtype="https://schema.org/CreativeWork"> <meta itemprop="name" content="Rinse"> <link itemprop="sameAs" href="http://www.wikidata.org/entity/Q134876960"> </div> <div itemprop="organizer" itemscope itemtype="https://schema.org/Organization"> <strong>Organizer:</strong> <span itemprop="name">NAC Indigenous Theatre</span> <link itemprop="url" href="https://nac-cna.ca/en/indigenoustheatre"> <link itemprop="sameAs" href="http://www.wikidata.org/entity/Q105878246"> </div> <img itemprop="image" src="https://naccnaca-eventimages.s3.amazonaws.com/38366/amrita_hero__large.jpg" alt="Rinse"> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <strong>Tickets:</strong> <span itemprop="price">35</span> <span itemprop="priceCurrency" content="CAD">$</span><br> <link itemprop="url" href="https://nac-cna.ca/en/event/38366"> <meta itemprop="validFrom" content="2025-06-12T10:00:00-05:00"> <a href="https://nac-cna.ca/en/event/38366">Buy Tickets</a> </div> <link itemprop="url" href="https://nac-cna.ca/en/event/38366"> <link itemprop="eventStatus" href="https://schema.org/EventScheduled"> <link itemprop="eventAttendanceMode" href="https://schema.org/OfflineEventAttendanceMode"> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Event"> <h1 property="name">Rinse</h1> <p property="description"> Rinse recreates an origin myth on stage—recounting personal narratives in relation to dance, art, feminism, desire, love, popular culture, and colonial history. </p> <div property="location" typeof="Place" resource="https://nac-cna.ca/venue/studio#Place"> <strong>Venue:</strong> <span property="name">Azrieli Studio</span> <link property="sameAs" href="http://www.wikidata.org/entity/Q109326244"> <div property="address" typeof="PostalAddress"> <span property="streetAddress">1 Elgin Street</span>, <span property="addressLocality">Ottawa</span>, <span property="addressRegion">ON</span> <span property="postalCode">K1P 5W1</span>, <span property="addressCountry">CA</span> </div> </div> <p> <strong>Date and Time:</strong><br> <time property="startDate" content="2026-01-22T20:00:00-05:00">January 22, 2026, 8:00 PM</time> - <time property="endDate" content="2026-01-22T21:00:00-05:00">9:00 PM</time> </p> <div property="performer" typeof="Person"> <strong>Performer:</strong> <span property="name">Amrita Hepi</span> <link property="sameAs" href="http://www.wikidata.org/entity/Q134599760"> </div> <div property="workPerformed" typeof="CreativeWork"> <meta property="name" content="Rinse"> <link property="sameAs" href="http://www.wikidata.org/entity/Q134876960"> </div> <div property="organizer" typeof="Organization"> <strong>Organizer:</strong> <span property="name">NAC Indigenous Theatre</span> <link property="url" href="https://nac-cna.ca/en/indigenoustheatre"> <link property="sameAs" href="http://www.wikidata.org/entity/Q105878246"> </div> <img property="image" src="https://naccnaca-eventimages.s3.amazonaws.com/38366/amrita_hero__large.jpg" alt="Rinse"> <div property="offers" typeof="Offer"> <strong>Tickets:</strong> <span property="price" content="35">35</span> <span property="priceCurrency" content="CAD">$</span><br> <link property="url" href="https://nac-cna.ca/en/event/38366"> <meta property="validFrom" content="2025-06-12T10:00:00-05:00"> <a href="https://nac-cna.ca/en/event/38366">Buy Tickets</a> </div> <link property="url" href="https://nac-cna.ca/en/event/38366"> <link property="eventStatus" href="https://schema.org/EventScheduled"> <link property="eventAttendanceMode" href="https://schema.org/OfflineEventAttendanceMode"> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Event", "startDate": "2026-01-22T20:00:00-05:00", "endDate": "2026-01-22T21:00:00-05:00", "name": "Rinse", "location": { "@type": "Place", "@id": "https://nac-cna.ca/venue/studio#Place", "name": "Azrieli Studio", "sameAs": "http://www.wikidata.org/entity/Q109326244", "address": { "type": "PostalAddress", "streetAddress": "1 Elgin Street", "addressLocality": "Ottawa", "addressRegion": "ON", "postalCode": "K1P 5W1", "addressCountry": "CA" } }, "description": "Rinse recreates an origin myth on stage—recounting personal narratives in relation to dance, art, feminism, desire, love, popular culture, and colonial history.", "url": "https://nac-cna.ca/en/event/38366", "image": "https://naccnaca-eventimages.s3.amazonaws.com/38366/amrita_hero__large.jpg", "organizer": { "@type": "Organization", "name": "NAC Indigenous Theatre", "url": "https://nac-cna.ca/en/indigenoustheatre", "sameAs": "http://www.wikidata.org/entity/Q105878246" }, "performer": { "@type": "Person", "name": "Amrita Hepi", "sameAs": "http://www.wikidata.org/entity/Q134599760" }, "workPerformed": { "@type": "CreativeWork", "name": "Rinse", "sameAs": "http://www.wikidata.org/entity/Q134876960" }, "eventStatus": "https://schema.org/EventScheduled", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "offers": { "@type": "Offer", "url": "https://nac-cna.ca/en/event/38366", "price": "35", "priceCurrency": "CAD", "validFrom": "2025-06-12T10:00:00-05:00" } } </script>

Structured representation of the JSON-LD example.
