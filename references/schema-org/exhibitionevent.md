---
title: "ExhibitionEvent"
source_url: https://schema.org/ExhibitionEvent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ExhibitionEvent

# ExhibitionEvent

A Schema.org Type

- Canonical URL: https://schema.org/ExhibitionEvent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ExhibitionEvent)

Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...

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

[Example 1](#eg-0349)

Copied

Example notes or example HTML without markup.

<div> <h2><a href="http://www.vam.ac.uk/whatson/event/5150/shoes-pleasure-and-pain-696789408/"> Shoes: Pleasure and Pain</a></h2> <p><time datetime="2015-06-13">Sat 13 June 2015</time>–<time datetime="2016-01-31">Sun 31 January 2016</time></p> <p>Explore the transformative power of footwear from around the world as we present over 200 pairs of the most extreme shoes from the last 2000 years.</p> <a href="http://www.vam.ac.uk/whatson/event/5150/date/20151007/">Book tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope="" itemtype="https://schema.org/ExhibitionEvent"> <meta itemprop="location" content="Victoria and Albert Museum"> <meta itemprop="inLanguage" content="en"> <h2><a itemprop="url" href="http://www.vam.ac.uk/whatson/event/5150/shoes-pleasure-and-pain-696789408/"> <span itemprop="name">Shoes: Pleasure and Pain</span> </a></h2> <p><time itemprop="startDate" datetime="2015-06-13">Sat 13 June 2015</time>–<time itemprop="endDate" datetime="2016-01-31">Sun 31 January 2016</time></p> <p itemprop="description">Explore the transformative power of footwear from around the world as we present over 200 pairs of the most extreme shoes from the last 2000 years.</p> <a itemprop="offers" href="http://www.vam.ac.uk/whatson/event/5150/date/20151007/">Book tickets</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ExhibitionEvent"> <meta property="location" content="Victoria and Albert Museum"> <meta property="inLanguage" content="en"> <h2><a property="url" href="http://www.vam.ac.uk/whatson/event/5150/shoes-pleasure-and-pain-696789408/"> <span property="name">Shoes: Pleasure and Pain</span> </a></h2> <p><time property="startDate" datetime="2015-06-13">Sat 13 June 2015</time>–<time property="endDate" datetime="2016-01-31">Sun 31 January 2016</time></p> <p property="description">Explore the transformative power of footwear from around the world as we present over 200 pairs of the most extreme shoes from the last 2000 years.</p> <a property="offers" href="http://www.vam.ac.uk/whatson/event/5150/date/20151007/">Book tickets</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ExhibitionEvent", "location": "Victoria and Albert Museum", "url": "http://www.vam.ac.uk/whatson/event/5150/shoes-pleasure-and-pain-696789408/", "name": "Shoes: Pleasure and Pain", "startDate": "2015-06-13", "endDate": "2016-01-31", "description": "Explore the transformative power of footwear from around the world as we present over 200 pairs of the most extreme shoes from the last 2000 years.", "offers": [ {"@type": "Offer", "@id": "http://www.vam.ac.uk/whatson/event/5150/date/20151007/" } ] } </script>

Structured representation of the JSON-LD example.
