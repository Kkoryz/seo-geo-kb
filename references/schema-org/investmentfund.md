---
title: "InvestmentFund"
source_url: https://schema.org/InvestmentFund
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# InvestmentFund

# InvestmentFund

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/InvestmentFund
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+InvestmentFund)

A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[amount](/amount)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)[FinancialProduct](/FinancialProduct)

```
```[annualPercentageRate](/annualPercentageRate)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[feesAndCommissionsSpecification](/feesAndCommissionsSpecification)

[Text](/Text)or[URL](/URL)```
```[interestRate](/interestRate)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)[Service](/Service)

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

[URL](/URL)### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

#### Source

[https://github.com/schemaorg/schemaorg/issues/1253](https://github.com/schemaorg/schemaorg/issues/1253)

### Examples

[Example 1](#eg-0233)

Copied

Example notes or example HTML without markup.

<body> <div> <h1>Guaranteed Interest Fund</h1> <p>This type of secure investment grows your money at a guaranteed rate of interest for a fixed period. It is ideal for investors looking for capital security.</p> <div>Amount to be invested $25,000 to $99,999</div> <div>Guaranteed interest rate 1.25%</div> </div> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body> <div itemscope itemtype="https://schema.org/InvestmentFund"> <h1 itemprop="name">Guaranteed Interest Fund</h1> <p itemprop="description">This type of secure investment grows your money at a guaranteed rate of interest for a fixed period. It is ideal for investors looking for capital security.</p> <div itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount">Amount to be invested <span itemprop="currency" content="USD">$</span><span itemprop="minValue" content="25000">25,000</span> to $<span itemprop="maxValue" content="99000">99,999</span></div> <div>Guaranteed interest rate <span itemprop="interestRate" content="1.25">1.25%</span></div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <div typeof="https://schema.org/InvestmentFund"> <h1 property="name">Guaranteed Interest Fund</h1> <p property="description">This type of secure investment grows your money at a guaranteed rate of interest for a fixed period. It is ideal for investors looking for capital security.</p> <div property="amount" typeof="https://schema.org/MonetaryAmount">Amount to be invested <span property="currency" content="USD">$</span><span property="minValue" content="25000">25,000</span> to $<span property="maxValue" content="99000">99,999</span></div> <div>Guaranteed interest rate <span property="interestRate" content="1.25">1.25%</span></div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "InvestmentFund", "name": "Guaranteed Interest Fund", "description": "This type of secure investment grows your money at a guaranteed rate of interest for a fixed period. It is ideal for investors looking for capital security.", "amount": { "@type": "MonetaryAmount", "currency": "USD", "minValue": "25000", "maxValue": "90000" }, "interestRate": "1.25" } </script>

Structured representation of the JSON-LD example.
