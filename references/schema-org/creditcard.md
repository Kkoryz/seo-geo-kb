---
title: "CreditCard"
source_url: https://schema.org/CreditCard
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CreditCard

# CreditCard

A Schema.org Type

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[LoanOrCredit](/LoanOrCredit)>

[CreditCard](/CreditCard)

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[PaymentCard](/PaymentCard)>

[CreditCard](/CreditCard)

[Thing](/Thing)>

[Intangible](/Intangible)>

[PaymentMethod](/PaymentMethod)>

[PaymentCard](/PaymentCard)>

[CreditCard](/CreditCard)

- Canonical URL: https://schema.org/CreditCard
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CreditCard)

A card payment method of a particular brand or name. Used to mark up a particular payment method and/or the financial product/service that supplies the card account.


Commonly used values:



Commonly used values:

- http://purl.org/goodrelations/v1#AmericanExpress
- http://purl.org/goodrelations/v1#DinersClub
- http://purl.org/goodrelations/v1#Discover
- http://purl.org/goodrelations/v1#JCB
- http://purl.org/goodrelations/v1#MasterCard
- http://purl.org/goodrelations/v1#VISA

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[amount](/amount)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)```
```[currency](/currency)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[gracePeriod](/gracePeriod)

[Duration](/Duration)```
```[loanRepaymentForm](/loanRepaymentForm)

[RepaymentSpecification](/RepaymentSpecification)```
```[loanTerm](/loanTerm)

[QuantitativeValue](/QuantitativeValue)```
```[loanType](/loanType)

[Text](/Text)or[URL](/URL)```
```[recourseLoan](/recourseLoan)

[Boolean](/Boolean)```
```[renegotiableLoan](/renegotiableLoan)

[Boolean](/Boolean)```
```[requiredCollateral](/requiredCollateral)

[Text](/Text)or[Thing](/Thing)[PaymentCard](/PaymentCard)

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

[URL](/URL)Instances of

[CreditCard](/CreditCard)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MemberProgramTier](/MemberProgramTier)### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

### Examples

[Example 1](#eg-0350)

Copied

Example notes or example HTML without markup.

Wells Fargo Secured Visa® Credit Card Requires a minimum $300 security deposit. When you apply, you provide a minimum security deposit of at least $300, or up to $10,000. Annual fee $25 Annual Percentage Rate (APR) Currently, a variable 18.99% APR on purchases. (These APRs do not apply to cash advances.) <a href="https://www.wellsfargo.com/credit-cards/secured/terms/">Full terms and conditions</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreditCard"> <span itemprop="name">Wells Fargo Secured Visa® Credit Card</span> <span itemprop="requiredCollateral">Requires a minimum $300 security deposit.</span> <span itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount">When you apply, you provide a minimum security deposit of at least <span itemprop="currency" content="USD">$</span> <span itemprop="minValue">300</span>, or up to $ <span itemprop="maxValue" content="10000">10,000</span>. </span> <span itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta itemprop="offeredBy" content="Wells Fargo"/> <span itemprop="priceSpecification" itemscope itemtype="https://schema.org/UnitPriceSpecification">Annual fee <span itemprop="priceCurrency" content="USD">$</span> <span itemprop="price">25</span> <span itemprop="referenceQuantity" itemscope itemtype="https://schema.org/QuantitativeValue"> <meta itemprop="value" content="1"/><meta itemprop="unitCode" content="ANN"/> </span> </span> </span> <span>Annual Percentage Rate (APR) Currently, a variable <span itemprop="annualPercentageRate">18.99</span>% APR on purchases. (These APRs do not apply to cash advances.) </span> <a itemprop="feesAndCommissionsSpecification" href="https://www.wellsfargo.com/credit-cards/secured/terms/">Full terms and conditions</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CreditCard"> <span property="name">Wells Fargo Secured Visa® Credit Card</span> <span property="requiredCollateral">Requires a minimum $300 security deposit.</span> <span property="amount" typeof="MonetaryAmount">When you apply, you provide a minimum security deposit of at least <span property="currency" content="USD">$</span> <span property="minValue">300</span>, or up to $ <span property="maxValue" content="10000">10,000</span>. </span> <span property="offers" typeof="Offer"> <meta property="offeredBy" content="Wells Fargo"/> <span property="priceSpecification" typeof="UnitPriceSpecification">Annual fee <span property="priceCurrency" content="USD">$</span> <span property="price">25</span> <span property="referenceQuantity" typeof="QuantitativeValue"> <meta property="value" content="1"/> <meta property="unitCode" content="ANN"/> </span> </span> </span> <span>Annual Percentage Rate (APR) Currently, a variable <span property="annualPercentageRate">18.99</span>% APR on purchases. (These APRs do not apply to cash advances.) </span> <a property="feesAndCommissionsSpecification" href="https://www.wellsfargo.com/credit-cards/secured/terms/">Full terms and conditions</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CreditCard", "name": "Wells Fargo Secured Visa® Credit Card", "requiredCollateral": "Requires a minimum $300 security deposit.", "amount": { "@type": "MonetaryAmount", "minValue": "300", "maxValue": "10000", "currency": "USD" }, "offers": { "@type": "Offer", "offeredBy": { "@type": "BankOrCreditUnion", "name":"Wells Fargo" }, "priceSpecification": { "@type": "UnitPriceSpecification", "price": "25", "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": "1", "unitCode": "ANN" } } }, "annualPercentageRate": "18.99", "feesAndCommissionsSpecification": "https://www.wellsfargo.com/credit-cards/secured/terms/" } </script>

Structured representation of the JSON-LD example.
