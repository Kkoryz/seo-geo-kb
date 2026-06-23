---
title: "SportsEvent"
source_url: https://schema.org/SportsEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SportsEvent

# SportsEvent

A Schema.org Type

- Canonical URL: https://schema.org/SportsEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SportsEvent)

Event type: Sports event.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[awayTeam](/awayTeam)

[Person](/Person)or[SportsTeam](/SportsTeam)```
```[competitor](/competitor)

[Person](/Person)or[SportsTeam](/SportsTeam)```
```[homeTeam](/homeTeam)

[Person](/Person)or[SportsTeam](/SportsTeam)```
```[referee](/referee)

[Person](/Person)```
```[sport](/sport)

[Text](/Text)or[URL](/URL)[Event](/Event)

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

[URL](/URL)Instances of

[SportsEvent](/SportsEvent)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ExerciseAction](/ExerciseAction)### Examples

[Example 1](#eg-0191)

Copied

Example notes or example HTML without markup.

World Series Event in JSON.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SportsEvent", "name": "2013 World Series", "subEvent": { "@type": "SportsEvent", "@id": "http://mlb.com/ws2013g1", "name": "2013 World Series - Game 1" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0445)

Copied

Example notes or example HTML without markup.

A broadcast of the FIFA Women's World Cup 2015 final.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastEvent"> <span itemprop="name">FIFA Women's World Cup Final</span> <span itemprop="description">US vs. Japan</span> <link itemprop="isLiveBroadcast" href="https://schema.org/True" /> <span itemprop="videoFormat">HD</span> <span itemprop="startDate" content="2015-07-05T15:30-07:00">starts 07/05/2015 3:30PM</span> <div itemprop="broadcastOfEvent" itemscope itemtype="https://schema.org/SportsEvent"> <span itemprop="name">FIFA Women's World Cup Final 2015</span> <div itemprop="competitor" itemscope itemtype="https://schema.org/SportsTeam"> <meta itemprop="name" content="United States" /> </div> <div itemprop="competitor" itemscope itemtype="https://schema.org/SportsTeam"> <meta itemprop="name" content="Japan" /> </div> <meta itemprop="startDate" content="2015-07-05T16:00-07:00" /> <div itemprop="location" itemscope itemtype="https://schema.org/City"> Played in <span itemprop="name">Vancouver</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastEvent"> <span property="name">FIFA Women's World Cup Final</span> <span property="description">US vs. Japan</span> <link property="isLiveBroadcast" href="https://schema.org/True" /> <span property="videoFormat">HD</span> <span property="startDate" content="2015-07-05T15:30-07:00">starts 07/05/2015 3:30PM</span> <div property="broadcastOfEvent" typeof="SportsEvent"> <span property="name">FIFA Women's World Cup Final 2015</span> <div property="competitor" typeof="SportsTeam"> <meta property="name" content="United States" /> </div> <div property="competitor" typeof="SportsTeam"> <meta property="name" content="Japan" /> </div> <meta property="startDate" content="2015-07-05T16:00-07:00" /> <div property="location" typeof="City"> Played in <span property="name">Vancouver</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastEvent", "name": "FIFA Women's World Cup Final", "description": "US vs. Japan", "isLiveBroadcast": true, "videoFormat": "HD", "startDate": "2015-07-05T15:30-07:00", "broadcastOfEvent": { "@type": "SportsEvent", "name": "FIFA Women's World Cup Final 2015", "competitor": [ { "@type": "SportsTeam", "name": "United States" }, { "@type": "SportsTeam", "name": "Japan" } ], "startDate": "2015-07-05T16:00-07:00", "location": { "@type": "City", "name": "Vancouver" } } } </script>

Structured representation of the JSON-LD example.
