---
title: "BroadcastService"
source_url: https://schema.org/BroadcastService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2010-05-22
---

# BroadcastService

# BroadcastService

A Schema.org Type

- Canonical URL: https://schema.org/BroadcastService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BroadcastService)

A delivery service through which content is provided via broadcast over the air or online.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[broadcastAffiliateOf](/broadcastAffiliateOf)

[Organization](/Organization)```
```[broadcastDisplayName](/broadcastDisplayName)

[Text](/Text)```
```[broadcastFrequency](/broadcastFrequency)

[BroadcastFrequencySpecification](/BroadcastFrequencySpecification)or[Text](/Text)```
```[broadcastTimezone](/broadcastTimezone)

[Text](/Text)[ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)for which the service bases its broadcasts.```
```[broadcaster](/broadcaster)

[Organization](/Organization)```
```[callSign](/callSign)

[Text](/Text)[callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.```
```[hasBroadcastChannel](/hasBroadcastChannel)

[BroadcastChannel](/BroadcastChannel)Inverse property:

[providesBroadcastService](/providesBroadcastService)```
```[inLanguage](/inLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage). Supersedes[language](/language).```
```[parentService](/parentService)

[BroadcastService](/BroadcastService)```
```[videoFormat](/videoFormat)

[Text](/Text)[Service](/Service)

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[availableChannel](/availableChannel)

[ServiceChannel](/ServiceChannel)```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasOfferCatalog](/hasOfferCatalog)

[OfferCatalog](/OfferCatalog)```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[providerMobility](/providerMobility)

[Text](/Text)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[serviceOutput](/serviceOutput)

[Thing](/Thing)[produces](/produces).```
```[serviceType](/serviceType)

[GovernmentBenefitsType](/GovernmentBenefitsType)or[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[termsOfService](/termsOfService)

[Text](/Text)or[URL](/URL)[Thing](/Thing)

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

[BroadcastService](/BroadcastService)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BroadcastService](/BroadcastService)[providesBroadcastService](/providesBroadcastService)

[BroadcastChannel](/BroadcastChannel)[publishedOn](/publishedOn)

[PublicationEvent](/PublicationEvent)#### More specific Types

### Examples

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

[Example 3](#eg-0319)

Copied

Example notes or example HTML without markup.

A radio station on 107.9 FM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WXKS-FM</span> <span itemprop="broadcastDisplayName">Kiss 108</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="107.9" /> <meta itemprop="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WXKS-FM</span> <span property="broadcastDisplayName">Kiss 108</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="107.9" /> <meta property="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WXKS-FM", "broadcastDisplayName": "Kiss 108", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 107.9, "broadcastSignalModulation": "FM" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0320)

Copied

Example notes or example HTML without markup.

A radio station on 1030 AM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WBZ-AM</span> <span itemprop="broadcastDisplayName">WBZ NewsRadio</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="1030" /> <meta itemprop="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WBZ-AM</span> <span property="broadcastDisplayName">WBZ NewsRadio</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="1030" /> <meta property="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WBZ-AM", "broadcastDisplayName": "WBZ NewsRadio", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 1030, "broadcastSignalModulation": "AM" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0442)

Copied

Example notes or example HTML without markup.

WAAY is an affiliate of the ABC network and broadcasts in SD.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WAAY-TV</span> <span itemprop="broadcastDisplayName">ABC</span> <span itemprop="videoFormat">SD</span> <span itemprop="broadcastTimezone" content="-8:00">PST</span> <div itemprop="broadcastAffiliateOf" itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">ABC</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="BroadcastService"> <span property="name">WAAY-TV</span> <span property="broadcastDisplayName">ABC</span> <span property="videoFormat">SD</span> <span property="broadcastTimezone" content="-8:00">PST</span> <div property="broadcastAffiliateOf" typeof="Organization"> <span property="name">ABC</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name":"WAAY-TV", "broadcastDisplayName":"ABC", "videoFormat":"SD", "broadcastTimezone": "-8:00", "broadcastAffiliateOf":{ "@type":"Organization", "name":"ABC" } } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0443)

Copied

Example notes or example HTML without markup.

WAAY is channel 7 on Comcast cable.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TelevisionChannel"> <span itemprop="name">WAAY 7</span> <span itemprop="broadcastChannelId">7</span> <span itemprop="broadcastServiceTier">Premium</span> <div itemprop="inBroadcastLineup" itemscope itemtype="https://schema.org/CableOrSatelliteService"> <span itemprop="name">Comcast</span> </div> <div itemprop="providesBroadcastService" itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WAAY-TV</span> <span itemprop="broadcastDisplayName">ABC</span> <div itemprop="broadcastAffiliateOf" itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">ABC</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="TelevisionChannel"> <span property="name">WAAY 7</span> <span property="broadcastChannelId">7</span> <span property="broadcastServiceTier">Premium</span> <div property="inBroadcastLineup" typeof="CableOrSatelliteService"> <span property="name">Comcast</span> </div> <div property="providesBroadcastService" typeof="BroadcastService"> <span property="name">WAAY-TV</span> <span property="broadcastDisplayName">ABC</span> <div property="broadcastAffiliateOf" typeof="Organization"> <span property="name">ABC</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"TelevisionChannel", "name": "WAAY 7", "broadcastChannelId":"7", "broadcastServiceTier":"Premium", "inBroadcastLineup":{ "@type":"CableOrSatelliteService", "name": "Comcast" }, "providesBroadcastService":{ "@type":"BroadcastService", "name": "WAAY-TV", "broadcastDisplayName": "ABC", "broadcastAffiliateOf":{ "@type":"Organization", "name":"ABC" } } } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0444)

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
