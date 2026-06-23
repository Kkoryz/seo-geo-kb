---
title: "TaxiService"
source_url: https://schema.org/TaxiService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# TaxiService

# TaxiService

A Schema.org Type

- Canonical URL: https://schema.org/TaxiService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+TaxiService)

A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.

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

[URL](/URL)| Supersedes |
|---|
```
``` |

### Examples

[Example 1](#eg-0421)

Copied

Example notes or example HTML without markup.

Car for hire driver #123 is within 50 meters of a given location, but is moving.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TaxiService"> <div itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">driver #123</span> <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCircle"> <div itemprop="geoMidpoint" itemscope itemtype="https://schema.org/GeoCoordinates"> <meta itemprop="latitude" content="42.362757" /> <meta itemprop="longitude" content="-71.087109" /> </div> <meta itemprop="geoRadius" content="50" /> </div> </div> </div> <meta itemprop="providerMobility" content="dynamic" /> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TaxiService"> <div property="provider" typeof="LocalBusiness"> <span property="name">driver #123</span> <div property="location" typeof="Place"> <div property="geo" typeof="GeoCircle"> <div property="geoMidpoint" typeof="GeoCoordinates"> <meta property="latitude" content="42.362757" /> <meta property="longitude" content="-71.087109" /> </div> <meta property="geoRadius" content="50" /> </div> </div> </div> <meta property="providerMobility" content="dynamic" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "TaxiService", "provider": { "@type": "LocalBusiness", "name": "driver #123", "location": { "@type": "Place", "geo": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": "42.362757", "longitude": "-71.087109" }, "geoRadius": "50" } } }, "providerMobility": "dynamic" } </script>

Structured representation of the JSON-LD example.
