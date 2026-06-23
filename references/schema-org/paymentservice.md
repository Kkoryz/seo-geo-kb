---
title: "PaymentService"
source_url: https://schema.org/PaymentService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PaymentService

# PaymentService

A Schema.org Type

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[PaymentService](/PaymentService)

[Thing](/Thing)>

[Intangible](/Intangible)>

[PaymentMethod](/PaymentMethod)>

[PaymentService](/PaymentService)

- Canonical URL: https://schema.org/PaymentService
- Equivalent Class: fibo-pay-ps-ps:PaymentService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PaymentService)

A Service to transfer funds from a person or organization to a beneficiary person or organization.

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

[URL](/URL)### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

### Examples

[Example 1](#eg-0355)

Copied

Example notes or example HTML without markup.

<h1>Payment Fees</h1> <h2>Selling is $0.15 - $0.50 per sale.</h2> <div> <div> <p>That's a small price to pay for accepting all forms of payments from over million customers worldwide. There are no hidden fees. You don't have to pay anything until you get paid for selling something. Our rates are some of the most competitive in the industry – keeping you in business and your customers happy.</p> </div> <div> <table> <tr> <th>Sales within the US</th> <td>$0.30 per transaction</td> </tr> <tr> <th>Discounted rate for eligible nonprofits</th> <td>$0.25 per transaction</td> </tr> <tr> <th>International sales</th> <td>$0.50 per transaction</td> </tr> <tr> <th>Card reader</th> <td>$0.15 for manually entered transactions</td> </tr> </table> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/WebPage"> <h1 itemprop="name">Payment Fees</h1> <h2>Selling is $0.15 - $0.50 per sale.</h2> <div> <div itemprop="mainEntity" itemscope itemtype="https://schema.org/ItemList"> <meta itemprop="name" content="Payment List"/> <table> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/PaymentService"> <th itemprop="name">Sales within the US</th> <td itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price">0.30</span> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="unitText">per transaction</span> </span> </span> </td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/PaymentService"> <th itemprop="name">Discounted rate for eligible nonprofits</th> <td itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price">0.25</span> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="unitText">per transaction</span> </span> </span> </td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/PaymentService"> <th itemprop="name">International sales</th> <td itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price">0.50</span> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="unitText">per transaction</span> </span> </span> </td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/PaymentService"> <th itemprop="name">Card reader</th> <td itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price">0.15</span> <span itemprop="eligibleQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="unitText">per transaction</span> </span> </span> </td> </tr> </table> </div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> <h1 property="name">Payment Fees</h1> <h2>Selling is $0.15 - $0.50 per sale.</h2> <div> <div property="mainEntity" typeof="ItemList"> <meta property="name" content="Payment List"/> <table> <tr property="itemListElement" typeof="PaymentService"> <th property="name">Sales within the US</th> <td property="offers" typeof="Offer"> <span property="priceSpecification" typeof="PriceSpecification"> <span property="priceCurrency" content="USD">$</span><span property="price">0.30</span> </span> </td> </tr> <tr property="itemListElement" typeof="PaymentService"> <th property="name">Discounted rate for eligible nonprofits</th> <td property="offers" typeof="Offer"> <span property="priceSpecification" typeof="PriceSpecification"> <span property="priceCurrency" content="USD">$</span><span property="price">0.25</span> <span property="eligibleQuantity" typeof="QuantitativeValue"> <span property="unitText">per transaction</span> </span> </span> </td> </tr> <tr property="itemListElement" typeof="PaymentService"> <th property="name">International sales</th> <td property="offers" typeof="Offer"> <span property="priceSpecification" typeof="PriceSpecification"> <span property="priceCurrency" content="USD">$</span><span property="price">0.50</span> <span property="eligibleQuantity" typeof="QuantitativeValue"> <span property="unitText">per transaction</span> </span> </span> </td> </tr> <tr property="itemListElement" typeof="PaymentService"> <th property="name">Card reader</th> <td property="offers" typeof="Offer"> <span property="priceSpecification" typeof="PriceSpecification"> <span property="priceCurrency" content="USD">$</span><span property="price">0.15</span> <span property="eligibleQuantity" typeof="QuantitativeValue"> <span property="unitText">per transaction</span> </span> </span> </td> </tr> </table> </div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "name": "Payment Fees", "mainEntity": { "@type": "ItemList", "name": "Payment List", "itemListElement": [ { "@type": "PaymentService", "name": "Sales within the US", "offers": { "@type": "Offer", "priceSpecification": { "@type": "PriceSpecification", "eligibleQuantity":{ "@type": "QuantitativeValue", "unitText": "per transaction" }, "priceCurrency": "USD", "price": "0.30" } } }, { "@type": "PaymentService", "name": "Discounted rate for eligible nonprofits", "offers": { "@type": "Offer", "priceSpecification": { "@type": "PriceSpecification", "eligibleQuantity":{ "@type": "QuantitativeValue", "unitText": "per transaction" }, "priceCurrency": "USD", "price": "0.30" } } }, { "@type": "PaymentService", "name": "International sales", "offers": { "@type": "Offer", "priceSpecification": { "@type": "PriceSpecification", "eligibleQuantity":{ "@type": "QuantitativeValue", "unitText": "per transaction" }, "priceCurrency": "USD", "price": "0.30" } } }, { "@type": "PaymentService", "name": "Card reader", "offers": { "@type": "Offer", "priceSpecification": { "@type": "PriceSpecification", "eligibleQuantity":{ "@type": "QuantitativeValue", "unitText": "per transaction" }, "priceCurrency": "USD", "price": "0.30" } } } ] } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-3537)

Copied

Example notes or example HTML without markup.

Possible Payment: Cash On Delivery, SplashPay 🌊, SEPA bank transfer and prepayment in all Splash stores 🌊.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "OnlineStore", "name": "Example Online Store", "acceptedPaymentMethod": [ { "@type": "PaymentMethod", "paymentMethodType": "https://schema.org/COD", "name": "Cash on Delivery" }, { "@type": "PaymentService", "name": "SplashPay", "description": "Pay using the SplashPay app." }, { "@type": "PaymentMethod", "paymentMethodType": "https://schema.org/ByBankTransferInAdvance", "name": "SEPA bank transfer", "description": "Bank transfer within the Single Euro Payments Area (SEPA)." }, { "@type": "PaymentService", "paymentMethodType": "https://schema.org/InStorePrepay", "provider": { "@type": "Organization", "name": "Splash Store", "description": "Pay your online purchases conveniently in any Splash Store." } } ] } </script>

Structured representation of the JSON-LD example.
