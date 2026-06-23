---
title: "FinancialProduct"
source_url: https://schema.org/FinancialProduct
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# FinancialProduct

# FinancialProduct

A Schema.org Type

- Canonical URL: https://schema.org/FinancialProduct
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+FinancialProduct)

A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[URL](/URL)#### More specific Types

### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

### Examples

[Example 1](#eg-0356)

Copied

Example notes or example HTML without markup.

<body> <h1>Life Insurance</h1> <div> <h3>Term Life Insurance</h3> <p>For most people, the primary reason to purchase life insurance is to help provide for dependents in the case of your death and the resulting loss of income. To determine a coverage amount, estimate what your family members would need after you’re gone to meet immediate, ongoing, and future financial obligations including funeral, rent or mortgage, other every day bills, college, and retirement.</p> <div>Coverage amounts $100,000 - $1,000,000</div> <div>Available through <a href="http://www.icinsure.com/acce/">Life Insurance Central</a></div> </div> <div> <h3>Simplified Term Life</h3> <div>Coverage amounts $50,000 - $250,000</div> <div>Available through <a href="https://www.prudential.com/personal/life-insurance">Prudential Financial</a></div> </div> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body> <h1>Life Insurance</h1> <div itemscope itemtype="https://schema.org/FinancialProduct"> <h3 itemprop="name">Term Life Insurance</h3> <p itemprop="description">For most people, the primary reason to purchase life insurance is to help provide for dependents in the case of your death and the resulting loss of income. To determine a coverage amount, estimate what your family members would need after you’re gone to meet immediate, ongoing, and future financial obligations including funeral, rent or mortgage, other every day bills, college, and retirement.</p> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">Available through <a itemprop="offeredBy" href="http://www.icinsure.com/acce/">Life Insurance Central</a></div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <h1>Life Insurance</h1> <div typeof="FinancialProduct"> <h3 property="name">Term Life Insurance</h3> <p property="description">For most people, the primary reason to purchase life insurance is to help provide for dependents in the case of your death and the resulting loss of income. To determine a coverage amount, estimate what your family members would need after you’re gone to meet immediate, ongoing, and future financial obligations including funeral, rent or mortgage, other every day bills, college, and retirement.</p> <div property="offers" typeof="Offer">Available through <a property="offeredBy" href="http://www.icinsure.com/acce/">Life Insurance Central</a></div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "FinancialProduct", "name": "Term Life Insurance", "description": "For most people, the primary reason to purchase life insurance is to help provide for dependents in the case of your death and the resulting loss of income. To determine a coverage amount, estimate what your family members would need after you’re gone to meet immediate, ongoing, and future financial obligations including funeral, rent or mortgage, other every day bills, college, and retirement.", "offers": { "@type": "Offer", "offeredBy": "http://www.icinsure.com/acce/" } } </script>

Structured representation of the JSON-LD example.
