---
title: "BroadcastEvent"
source_url: https://schema.org/BroadcastEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2010-05-22
---

# BroadcastEvent

# BroadcastEvent

A Schema.org Type

- Canonical URL: https://schema.org/BroadcastEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BroadcastEvent)

An over the air or online broadcast event.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[broadcastOfEvent](/broadcastOfEvent)

[Event](/Event)```
```[isLiveBroadcast](/isLiveBroadcast)

[Boolean](/Boolean)```
```[subtitleLanguage](/subtitleLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).```
```[videoFormat](/videoFormat)

[Text](/Text)[PublicationEvent](/PublicationEvent)

```
```[publishedBy](/publishedBy)

[Organization](/Organization)or[Person](/Person)```
```[publishedOn](/publishedOn)

[BroadcastService](/BroadcastService)[Event](/Event)

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

[Example 1](#eg-0166)

Copied

Example notes or example HTML without markup.

<div> <a href="http://www.bbc.co.uk/programmes/b006q2x0">Doctor Who</a>, <a href="http://www.bbc.co.uk/programmes/b00rs69w">Series 5</a>, <a href="http://www.bbc.co.uk/programmes/b00sj9sq">The Hungry Earth</a>, episode 8, broadcast on BBC One at 18:15, 22nd of May 2010, available on <a href="http://www.bbc.co.uk/iplayer/b00sj9sq">BBC iPlayer</a> from 19:45 on the 2nd of June until the 9th. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TVSeries"> <a itemprop="url" href="http://www.bbc.co.uk/programmes/b006q2x0"> <span itemprop="name">Doctor Who</span></a>, <div itemprop="containsSeason" itemscope itemtype="https://schema.org/TVSeason"> <a itemprop="url" href="http://www.bbc.co.uk/programmes/b00rs69w"> <span itemprop="name">Series 5</span></a>, <div itemprop="episode" itemscope itemtype="https://schema.org/TVEpisode"> <a itemprop="url" href="http://www.bbc.co.uk/programmes/b00sj9sq"> <span itemprop="name">The Hungry Earth</span></a>, episode <span itemprop="position">8</span>, broadcast on <div itemprop="publication" itemscope itemtype="https://schema.org/BroadcastEvent"> <div itemprop="publishedOn" itemscope itemtype="https://schema.org/BroadcastService"> <a itemprop="url" href="http://www.bbc.co.uk/bbcone"><span itemprop="name">BBC One</span></a> </div> at <span itemprop="startDate" content="2010-05-22T18:15:00+01:00">18:15, 22nd of May 2010</span> </div>, available on <div itemprop="video" itemscope itemtype="https://schema.org/VideoObject"> <a itemprop="url" href="http://www.bbc.co.uk/iplayer/episode/b00sj9sq">BBC iPlayer</a> </div> from <div itemprop="publication" itemscope itemtype="https://schema.org/OnDemandEvent"> <span itemprop="startDate" content="2012-06-02T19:45:00+01:00">19:45 on the 2nd of June</span> until the <span itemprop="endDate" content="2012-06-09T19:44:00+01:00">9th</span>. </div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TVSeries"> <a property="url" href="http://www.bbc.co.uk/programmes/b006q2x0"> <span property="name">Doctor Who</span></a>, <div property="containsSeason" typeof="TVSeason"> <a property="url" href="http://www.bbc.co.uk/programmes/b00rs69w"> <span property="name">Series 5</span></a>, <div property="episode" typeof="TVEpisode"> <a property="url" href="http://www.bbc.co.uk/programmes/b00sj9sq"> <span property="name">The Hungry Earth</span></a>, episode <span property="position">8</span>, broadcast on <div property="publication" typeof="BroadcastEvent"> <div property="publishedOn" typeof="BroadcastService"> <a property="url" href="http://www.bbc.co.uk/bbcone"><span property="name">BBC One</span></a> </div> at <span property="startDate" content="2010-05-22T18:15:00+01:00">18:15, 22nd of May 2010</span> </div>, available on <div property="video" typeof="VideoObject"> <a property="url" href="http://www.bbc.co.uk/iplayer/episode/b00sj9sq">BBC iPlayer</a> </div> from <div property="publication" typeof="OnDemandEvent"> <span property="startDate" content="2012-06-02T19:45:00+01:00">19:45 on the 2nd of June</span> until the <span property="endDate" content="2012-06-09T19:44:00+01:00">9th</span>. </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "TVSeries", "containsSeason": { "@type": "TVSeason", "episode": { "@type": "TVEpisode", "position": "8", "publication": [ { "@type": "BroadcastEvent", "publishedOn": { "@type": "BroadcastService", "url": "http://www.bbc.co.uk/bbcone" }, "startDate": "2010-05-22T18:15:00+01:00" }, { "@type": "OnDemandEvent", "endDate": "2012-06-09T19:44:00+01:00", "startDate": "2012-06-02T19:45:00+01:00" } ], "url": "http://www.bbc.co.uk/programmes/b00sj9sq", "video": { "@type": "VideoObject", "url": "http://www.bbc.co.uk/iplayer/episode/b00sj9sq" } }, "url": "http://www.bbc.co.uk/programmes/b00rs69w" }, "url": "http://www.bbc.co.uk/programmes/b006q2x0" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0167)

Copied

Example notes or example HTML without markup.

<div> <a href="http://www.bbc.co.uk/programmes/b006qykl">In Our Time</a>, <a href="http://www.bbc.co.uk/programmes/b03ggc19">Ordinary Language Philosophy</a>, episode 604, broadcast on BBC Radio 4 at 09:00, 7th of November 2013, available online from 09:45 on the same day. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/RadioSeries"> <a itemprop="url" href="http://www.bbc.co.uk/programmes/b006qykl"> <span itemprop="name">In Our Time</span></a>, <div itemprop="episode" itemscope itemtype="https://schema.org/RadioEpisode"> <a itemprop="url" href="http://www.bbc.co.uk/programmes/b03ggc19"> <span itemprop="name">Ordinary Language Philosophy</span></a>, episode <span itemprop="position">604</span>, broadcast on <div itemprop="publication" itemscope itemtype="https://schema.org/BroadcastEvent"> <div itemprop="publishedOn" itemscope itemtype="https://schema.org/BroadcastService"> <a itemprop="url" href="http://www.bbc.co.uk/radio4"><span itemprop="name">BBC Radio 4</span></a> </div> at <span itemprop="startDate" content="2013-11-07T09:00:00+01:00">09:00, 7th of November 2013</span> </div>, available online from <div itemprop="publication" itemscope itemtype="https://schema.org/OnDemandEvent"> <span itemprop="startDate" content="2013-11-07T09:45:00+01:00">09:45 on the same day</span>. </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="RadioSeries"> <a property="url" href="http://www.bbc.co.uk/programmes/b006qykl"> <span property="name">In Our Time</span></a>, <div property="episode" typeof="RadioEpisode"> <a property="url" href="http://www.bbc.co.uk/programmes/b03ggc19"> <span property="name">Ordinary Language Philosophy</span></a>, episode <span property="position">604</span>, broadcast on <div property="publication" typeof="BroadcastEvent"> <div property="publishedOn" typeof="BroadcastService"> <a property="url" href="http://www.bbc.co.uk/radio4"><span property="name">BBC Radio 4</span></a> </div> at <span property="startDate" content="2013-11-07T09:00:00+01:00">09:00, 7th of November 2013</span> </div>, available online from <div property="publication" typeof="OnDemandEvent"> <span property="startDate" content="2013-11-07T09:45:00+01:00">09:45 on the same day</span>. </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "RadioSeries", "episode": { "@type": "RadioEpisode", "position": "604", "publication": [ { "@type": "BroadcastEvent", "publishedOn": { "@type": "BroadcastService", "url": "http://www.bbc.co.uk/radio4" }, "startDate": "2013-11-07T09:00:00+01:00" }, { "@type": "OnDemandEvent", "startDate": "2013-11-07T09:45:00+01:00" } ], "url": "http://www.bbc.co.uk/programmes/b03ggc19" }, "url": "http://www.bbc.co.uk/programmes/b006qykl" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0444)

Copied

Example notes or example HTML without markup.

WAAY is broadcasting Modern Family at 9:00PM on October 12, 2014 in English with Spanish subtitles available.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastEvent"> <span itemprop="name">Modern Family - S6E8 - Three Turkeys</span> <span itemprop="description">Phil and Luke take over Thanksgiving duties.</span> <link itemprop="isLiveBroadcast" href="https://schema.org/False" /> <span itemprop="videoFormat">HD</span> <span itemprop="inLanguage">en</span> <span itemprop="subtitleLanguage">es</span> <span itemprop="startDate" content="2014-10-12T21:00">starts 10/12/2014 9:00PM</span> <span itemprop="endDate" content="2014-10-12T21:30">ends 10/12/2014 9:30PM</span> <div itemprop="publishedOn" itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WAAY-TV</span> </div> <div itemprop="workPerformed" itemscope itemtype="https://schema.org/TVEpisode"> <span itemprop="name">Modern Family: Three Turkeys</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="BroadcastEvent"> <span property="name">Modern Family - S6E8 - Three Turkeys</span> <span property="description">Phil and Luke take over Thanksgiving duties.</span> <link property="isLiveBroadcast" href="https://schema.org/True" /> <span property="videoFormat">HD</span> <span property="inLanguage">en</span> <span property="subtitleLanguage">es</span> <span property="startDate" content="2014-10-12T21:00">starts 10/12/2014 9:00PM</span> <span property="endDate" content="2014-10-12T21:30">ends 10/12/2014 9:30PM</span> <div property="publishedOn" typeof="BroadcastService"> <span property="name">WAAY-TV</span> </div> <div property="workPerformed" typeof="TVEpisode"> <span property="name">Modern Family: Three Turkeys</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastEvent", "startDate":"2014-10-12T21:00", "endDate":"2014-10-12T21:30", "publishedOn":{ "@type":"BroadcastService", "name": "WAAY-TV" }, "workPerformed":{ "@type":"CreativeWork", "name": "Modern Family: Three Turkeys" }, "inLanguage":"en", "subtitleLanguage":"es", "videoFormat":"HD", "isLiveBroadcast":false, "name":"Modern Family - S6E8 - Three Turkeys", "description":"Phil and Luke take over Thanksgiving duties." } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0445)

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
