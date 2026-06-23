---
title: "PaymentCard"
source_url: https://schema.org/PaymentCard
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PaymentCard

# PaymentCard

A Schema.org Type

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[PaymentCard](/PaymentCard)

[Thing](/Thing)>

[Intangible](/Intangible)>

[PaymentMethod](/PaymentMethod)>

[PaymentCard](/PaymentCard)

- Canonical URL: https://schema.org/PaymentCard
- Equivalent Class: unece:FinancialCard
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PaymentCard)

A payment method using a credit, debit, store or other card to associate the payment with an account.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[cashBack](/cashBack)

[Boolean](/Boolean)or[Number](/Number)```
```[contactlessPayment](/contactlessPayment)

[Boolean](/Boolean)```
```[floorLimit](/floorLimit)

[MonetaryAmount](/MonetaryAmount)```
```[monthlyMinimumRepaymentAmount](/monthlyMinimumRepaymentAmount)

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

[Text](/Text)or[URL](/URL)[PaymentMethod](/PaymentMethod)

```
```[paymentMethodType](/paymentMethodType)

[PaymentMethodType](/PaymentMethodType)[Thing](/Thing)

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

[Example 1](#eg-0354)

Copied

Example notes or example HTML without markup.

<b>Wells Fargo Platinum Debit Card.</b> Customers with an eligible Wells Fargo Checking account can make everyday purchases using their Platinum debit card worldwide at participating retailers and service providers – including online or by phone. Pay with confidence knowing your Wells Fargo Debit Card comes with many protection features and is a safe way to pay. <a href="https://www.wellsfargo.com/debit-card/#overview">Overview</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/PaymentCard"> <b><span itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <span itemprop="offeredBy" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <span itemprop="name">Wells Fargo</span> </span> <link itemprop="businessFunction" content="http://purl.org/goodrelations/v1#ProvideService" /> </span> <span itemprop="name">Platinum Debit Card.</span></b> <meta itemprop="category" content="Debit Card"/> <p itemprop="description"> Customers with an eligible Wells Fargo Checking account can make everyday purchases using their Platinum debit card worldwide at participating retailers and service providers – including online or by phone. Pay with confidence knowing your Wells Fargo Debit Card comes with many protection features and is a safe way to pay. </p> <a itemprop="feesAndCommissionsSpecification" href="https://www.wellsfargo.com/debit-card/#overview">Overview</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="PaymentCard"> <b><span property="offers" typeof="Offer"> <span property="offeredBy" typeof="https://schema.org/BankOrCreditUnion"> <span property="name">Wells Fargo</span> </span> <link property="businessFunction" content="http://purl.org/goodrelations/v1#ProvideService" /> </span> <span property="name">Platinum Debit Card.</span></b> <meta property="category" content="Debit Card"/> <p property="description"> Customers with an eligible Wells Fargo Checking account can make everyday purchases using their Platinum debit card worldwide at participating retailers and service providers – including online or by phone. Pay with confidence knowing your Wells Fargo Debit Card comes with many protection features and is a safe way to pay. </p> <a property="feesAndCommissionsSpecification" href="https://www.wellsfargo.com/debit-card/#overview">Overview</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "PaymentCard", "name": "Platinum Debit Card", "category": "Debit Card", "offers": { "@type": "Offer", "offeredBy": { "@type": "BankOrCreditUnion", "name":"Wells Fargo" }, "businessFunction": "http://purl.org/goodrelations/v1#ProvideService" }, "description": "Customers with an eligible Wells Fargo Checking account can make everyday purchases using their Platinum debit card worldwide at participating retailers and service providers – including online or by phone. Pay with confidence knowing your Wells Fargo Debit Card comes with many protection features and is a safe way to pay.", "feesAndCommissionsSpecification": "https://www.wellsfargo.com/debit-card/#overview" } </script>

Structured representation of the JSON-LD example.
