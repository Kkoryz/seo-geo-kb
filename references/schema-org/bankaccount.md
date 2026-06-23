---
title: "BankAccount"
source_url: https://schema.org/BankAccount
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# BankAccount

# BankAccount

A Schema.org Type

- Canonical URL: https://schema.org/BankAccount
- Equivalent Class: fibo-fbc-pas-fpas:BankAccount
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BankAccount)

A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[accountMinimumInflow](/accountMinimumInflow)

[MonetaryAmount](/MonetaryAmount)```
```[accountOverdraftLimit](/accountOverdraftLimit)

[MonetaryAmount](/MonetaryAmount)```
```[bankAccountType](/bankAccountType)

[Text](/Text)or[URL](/URL)[FinancialProduct](/FinancialProduct)

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

[Example 1](#eg-0352)

Copied

Example notes or example HTML without markup.

<div> <h1>RBS current accounts</h1> <h2>Most popular accounts</h2> <ul> <li><b>Select Account</b><br/> - No monthly account fee<br/> - You need to be aged 18 or over, and UK resident to apply </li> <li><b>Select Silver Account</b><br/> - £10 per month<br/> - You need to be aged 18 or over, and UK resident to apply </li> <li><b>Select Platinum Account</b><br/> - £16 per month<br/> - You need to be aged 18 or over, and UK resident to apply </li> <li><b>Black Account</b>Select Platinum Account</b><br/> - £24 per month<br/> - You need to be aged 18 or over, and UK resident to apply, with either: <ul> <li>£100,000 sole income paid into this account</li> <li>a RBS mortgage of at lease £300,000</li> <li>£100,000 in RBS savings and investments</li> </ul> </li> </ul> <a href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf">Account Terms</a> <div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <h1>RBS current accounts</h1> <h2>Most popular accounts</h2> <ul> <li itemscope itemtype="https://schema.org/BankAccount"><b><span itemprop="name">Select Account</span></b><br/> <span itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <link itemprop="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <span itemprop="offeredBy" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <meta itemprop="name" content="RBS"/> <link itemprop="url" href="http://rbs.co.uk"/> </span> - <span itemprop="description">No monthly account fee<br/>- You need to be aged 18 or over, and UK resident to apply</span> <meta itemprop="price" content="0"/> </span> <link itemprop="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li itemscope itemtype="https://schema.org/BankAccount"><b><span itemprop="name">Select Silver Account</span></b><br/> <span itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <link itemprop="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <meta itemprop="priceCurrency" content="GBP"/> - £<span itemprop="price">10</span> per month<br/> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <meta itemprop="value" content="1"/><meta itemprop="unitCode" content="ANN"/> </span> </span> - <span itemprop="description">You need to be aged 18 or over, and UK resident to apply</span> <span itemprop="offeredBy" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <meta itemprop="name" content="RBS"/> <link itemprop="url" href="http://rbs.co.uk"/> </span> </span> <link itemprop="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li itemscope itemtype="https://schema.org/BankAccount"><b><span itemprop="name">Select Platinum Account</span></b><br/> <span itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <link itemprop="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <meta itemprop="priceCurrency" content="GBP"/> - £<span itemprop="price">16</span> per month<br/> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <meta itemprop="value" content="1"/><meta itemprop="unitCode" content="ANN"/> </span> </span> - <span itemprop="description">You need to be aged 18 or over, and UK resident to apply</span> <span itemprop="offeredBy" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <meta itemprop="name" content="RBS"/> <link itemprop="url" href="http://rbs.co.uk"/> </span> </span> <link itemprop="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li itemscope itemtype="https://schema.org/BankAccount"><b><span itemprop="name">Black Account</span></b><br/> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <link itemprop="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <meta itemprop="priceCurrency" content="GBP"/> - £<span itemprop="price">24</span> per month<br/> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <meta itemprop="value" content="1"/><meta itemprop="unitCode" content="ANN"/> </span> </span> - <div itemprop="description"> You need to be aged 18 or over, and UK resident to apply, with either: <ul> <li>£100,000 sole income paid into this account</li> <li>a RBS mortgage of at lease £300,000</li> <li>£100,000 in RBS savings and investments</li> </ul></div> <span itemprop="offeredBy" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <meta itemprop="name" content="RBS"/> <link itemprop="url" href="http://rbs.co.uk"/> </span> </div> <link itemprop="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> </ul> <a href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf">Account Terms</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/"> <h1>RBS current accounts</h1> <h2>Most popular accounts</h2> <ul> <li typeof="BankAccount"><b><span property="name">Select Account</span></b><br/> <span property="offers" typeof="Offer"> <link property="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> - <span property="description">No monthly account fee<br/>- You need to be aged 18 or over, and UK resident to apply</span> <meta property="price" content="0"/> <span property="offeredBy" typeof="BankOrCreditUnion"> <meta property="name" content="RBS"/> <link property="url" href="http://rbs.co.uk"/> </span> </span> <link property="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li typeof="BankAccount"><b><span property="name">Select Silver Account</span></b><br/> <span property="offers" typeof="Offer"> <link property="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <span property="priceSpecification" typeof="PriceSpecification"> <meta property="priceCurrency" content="GBP"/> - £<span property="price">10</span> per month<br/> <span property="eligibleQuantity" typeof="QuantitativeValue"> <meta property="value" content="1"/><meta property="unitCode" content="ANN"/> </span> </span> - <span property="description">You need to be aged 18 or over, and UK resident to apply</span> <span property="offeredBy" typeof="BankOrCreditUnion"> <meta property="name" content="RBS"/> <link property="url" href="http://rbs.co.uk"/> </span> </span> <link property="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li typeof="BankAccount"><b><span property="name">Select Platinum Account</span></b><br/> <span property="offers" typeof="Offer"> <link property="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <span property="priceSpecification" typeof="PriceSpecification"> <meta property="priceCurrency" content="GBP"/> - £<span property="price">16</span> per month<br/> <span property="eligibleQuantity" typeof="QuantitativeValue"> <meta property="value" content="1"/><meta property="unitCode" content="ANN"/> </span> </span> - <span property="description">You need to be aged 18 or over, and UK resident to apply</span> <span property="offeredBy" typeof="BankOrCreditUnion"> <meta property="name" content="RBS"/> <link property="url" href="http://rbs.co.uk"/> </span> </span> <link property="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> <li typeof="BankAccount"><b><span property="name">Black Account</span></b><br/> <div property="offers" typeof="https://schema.org/Offer"> <link property="eligibleCustomerType" href="http://purl.org/goodrelations/v1#Enduser"/> <div property="priceSpecification" typeof="PriceSpecification"> <meta property="priceCurrency" content="GBP"/> - £<span property="price">24</span> per month<br/> <span property="eligibleQuantity" typeof="QuantitativeValue"> <meta property="value" content="1"/><meta property="unitCode" content="ANN"/> </span> </div> - <div property="description">You need to be aged 18 or over, and UK resident to apply, with either: <ul> <li>£100,000 sole income paid into this account</li> <li>a RBS mortgage of at lease £300,000</li> <li>£100,000 in RBS savings and investments</li> </ul> </div> <span property="offeredBy" typeof="BankOrCreditUnion"> <meta property="name" content="RBS"/> <link property="url" href="http://rbs.co.uk"/> </span> </div> <link property="feesAndCommissionsSpecification" href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf"/> </li> </ul> <a href="http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf">Account Terms</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@graph": [ { "@type": "BankAccount", "name": "Select account", "offers": { "@type": "Offer", "eligibleCustomerType": { "@id":"http://purl.org/goodrelations/v1#Enduser" }, "price": "0", "description": "You need to be aged 18 or over, and UK resident to apply.", "offeredBy": { "@type": "BankOrCreditUnion", "@id": "http://rbs.co.uk", "name": "RBS" } }, "feesAndCommissionsSpecification": "http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf" }, { "@type": "BankAccount", "name": "Select Silver account", "offers": { "@type": "Offer", "eligibleCustomerType": "http://purl.org/goodrelations/v1#Enduser", "priceSpecification": { "@type": "PriceSpecification", "priceCurrency": "GBP", "price": "10", "eligibleQuantity": { "@type": "QuantitativeValue", "value":"1", "unitCode": "ANN" } }, "description": "You need to be aged 18 or over, and UK resident to apply.", "offeredBy": { "@type": "BankOrCreditUnion", "@id": "http://rbs.co.uk", "name": "RBS" } }, "feesAndCommissionsSpecification": "http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf" }, { "@type": "BankAccount", "name": "Select Platinum account", "offers": { "@type": "Offer", "eligibleCustomerType": "http://purl.org/goodrelations/v1#Enduser", "priceSpecification": { "@type": "PriceSpecification", "priceCurrency": "GBP", "price": "16", "eligibleQuantity": { "@type": "QuantitativeValue", "value":"1", "unitCode": "ANN" } }, "description": "You need to be aged 18 or over, and UK resident to apply.", "offeredBy": { "@type": "BankOrCreditUnion", "@id": "http://rbs.co.uk", "name": "RBS" } }, "feesAndCommissionsSpecification": "http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf" }, { "@type": "BankAccount", "name": "Black account", "offers": { "@type": "Offer", "eligibleCustomerType": "http://purl.org/goodrelations/v1#Enduser", "priceSpecification": { "@type": "PriceSpecification", "priceCurrency": "GBP", "price": "24", "eligibleQuantity": { "@type": "QuantitativeValue", "value":"1", "unitCode": "ANN" } }, "description": "You need to be aged 18 or over, and UK resident to apply, with either:<ul><li>£100,000 sole income paid into this account<\/li><li>a RBS mortgage of at lease £300,000<\/li><li>£100,000 in RBS savings and investments<\/li><\/ul>", "offeredBy": { "@type": "BankOrCreditUnion", "@id": "http://rbs.co.uk", "name": "RBS" } }, "feesAndCommissionsSpecification": "http://personal.rbs.co.uk/content/dam/rbs_co_uk/currentaccounts/downloads/Reward/Personal%20and%20Private%20Current%20Account%20Fees%20and%20Interest%20Rates.pdf" } ] }</script>

Structured representation of the JSON-LD example.
