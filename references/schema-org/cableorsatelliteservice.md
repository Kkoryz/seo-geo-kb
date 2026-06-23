---
title: "CableOrSatelliteService"
source_url: https://schema.org/CableOrSatelliteService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CableOrSatelliteService

# CableOrSatelliteService

A Schema.org Type

- Canonical URL: https://schema.org/CableOrSatelliteService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CableOrSatelliteService)

A service which provides access to media programming like TV or radio. Access may be via cable or satellite.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[CableOrSatelliteService](/CableOrSatelliteService)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BroadcastChannel](/BroadcastChannel)### Examples

[Example 1](#eg-0443)

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
