---
title: "DepositAccount"
source_url: https://schema.org/DepositAccount
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DepositAccount

# DepositAccount

A Schema.org Type

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[BankAccount](/BankAccount)>

[DepositAccount](/DepositAccount)

[Thing](/Thing)>

[Intangible](/Intangible)>

[Service](/Service)>

[FinancialProduct](/FinancialProduct)>

[InvestmentOrDeposit](/InvestmentOrDeposit)>

[DepositAccount](/DepositAccount)

- Canonical URL: https://schema.org/DepositAccount
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DepositAccount)

A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.

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

[Text](/Text)or[URL](/URL)[InvestmentOrDeposit](/InvestmentOrDeposit)

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

### Examples

[Example 1](#eg-0353)

Copied

Example notes or example HTML without markup.

<body> <h1>Easy access accounts Comparison - Ordered by interest rate (AER)</h1> <div> <table> <tr> <th>Bank</th><th>Account</th><th>Interest Rate</th><th>Min/Max Opening Amount</th><th>Access</th> </tr> <tr> <td><a href="https://www.rcibank.co.uk">RCI Bank</a></td> <td>Freedom Savings Account</td> <td>1.65% Variable</td> <td>£100 to £1,000,000</td> <td>Internet, Post, Telephone</td> </tr> <tr> <td><a href="https://sbiukonlinesavings.com/">State Bank of India</a></td> <td>Online Instant Access Savings Issue 4</td> <td>1.25% Variable</td> <td>£500 to £1,000,000</td> <td>Internet, In Branch</td> </tr> <tr> <td><a href="http://www.aldermore.co.uk/">Aldermore</a></td> <td>Easy Access Issue 9</td> <td>1.25% Variable</td> <td>£1,000 to £1,000,000</td> <td>Internet, Post, Telephone</td> </tr> </table> </div> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/WebPage"> <h1 itemprop="name">Easy access accounts Comparison - Ordered by interest rate (AER)</h1> <div itemprop="mainEntity" itemscope itemtype="https://schema.org/ItemList"> <meta itemprop="name" content="Easy access accounts Comparison List"/> <table> <tr> <th>Bank</th><th>Account</th><th>Interest Rate</th><th>Min/Max Opening Amount</th><th>Access</th> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/DepositAccount"> <td><a itemprop="provider" href="https://www.rcibank.co.uk">RCI Bank</a></td> <td itemprop="name">Freedom Savings Account</td> <td itemprop="interestRate" itemscope itemtype="https://schema.org/QuantitativeValue"><span itemprop="value">1.65</span>% <span itemprop="valueReference">Variable</span></td> <td itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount"><meta itemprop="currency" content="GBP"/>£<span itemprop="minValue" content="100">100</span> to £<span itemprop="maxValue" content="1000000">1,000,000</span></td> <td><span itemprop="availableChannel">Internet</span>, <span itemprop="availableChannel">Post</span>, <span itemprop="availableChannel">Telephone</span></td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/DepositAccount"> <td><a itemprop="provider" href="https://sbiukonlinesavings.com/">State Bank of India</a></td> <td itemprop="name">Online Instant Access Savings Issue 4</td> <td itemprop="interestRate" itemscope itemtype="https://schema.org/QuantitativeValue"><span itemprop="value">1.25</span>% <span itemprop="valueReference">Variable</span></td> <td itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount"><meta itemprop="currency" content="GBP"/>£<span itemprop="minValue" content="500">500</span> to £<span itemprop="maxValue" content="1000000">1,000,000</span></td> <td><span itemprop="availableChannel">Internet</span>, <span itemprop="availableChannel">In Branch</span></td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/DepositAccount"> <td><a itemprop="provider" href="http://www.aldermore.co.uk/">Aldermore</a></td> <td itemprop="name">Easy Access Issue 9</td> <td itemprop="interestRate" itemscope itemtype="https://schema.org/QuantitativeValue"><span itemprop="value">1.25</span>% <span itemprop="valueReference">Variable</span></td> <td itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount"><meta itemprop="currency" content="GBP"/>£<span itemprop="minValue" content="1000">1,000</span> to £<span itemprop="maxValue" content="1000000">1,000,000</span></td> <td><span itemprop="availableChannel">Internet</span>, <span itemprop="availableChannel">Post</span>, <span itemprop="availableChannel">Telephone</span></td> </tr> </table> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> <h1 property="name">Easy access accounts Comparison - Ordered by interest rate (AER)</h1> <div property="mainEntity" typeof="ItemList"> <meta property="name" content="Easy access accounts Comparison List"/> <table> <tr> <th>Bank</th><th>Account</th><th>Interest Rate</th><th>Min/Max Opening Amount</th><th>Access</th> </tr> <tr property="itemListElement" typeof="DepositAccount"> <td><a property="provider" href="https://www.rcibank.co.uk">RCI Bank</a></td> <td property="name">Freedom Savings Account</td> <td property="interestRate" typeof="QuantitativeValue"><span property="value">1.65</span>% <span property="valueReference">Variable</span></td> <td property="amount" typeof="MonetaryAmount"><meta property="currency" content="GBP"/>£<span property="minValue" content="100">100</span> to £<span property="maxValue" content="1000000">1,000,000</span></td> <td><span property="availableChannel">Internet</span>, <span property="availableChannel">Post</span>, <span property="availableChannel">Telephone</span></td> </tr> <tr property="itemListElement" typeof="DepositAccount"> <td><a property="provider" href="https://sbiukonlinesavings.com/">State Bank of India</a></td> <td property="name">Online Instant Access Savings Issue 4</td> <td property="interestRate" typeof="QuantitativeValue"><span property="value">1.25</span>% <span property="valueReference">Variable</span></td> <td property="amount" typeof="MonetaryAmount"><meta property="currency" content="GBP"/>£<span property="minValue" content="500">500</span> to £<span property="maxValue" content="1000000">1,000,000</span></td> <td><span property="availableChannel">Internet</span>, <span property="availableChannel">In Branch</span></td> </tr> <tr property="itemListElement" typeof="DepositAccount"> <td><a property="provider" href="http://www.aldermore.co.uk/">Aldermore</a></td> <td property="name">Easy Access Issue 9</td> <td property="interestRate" typeof="QuantitativeValue"><span property="value">1.25</span>% <span property="valueReference">Variable</span></td> <td property="amount" typeof="MonetaryAmount"><meta property="currency" content="GBP"/>£<span property="minValue" content="1000">1,000</span> to £<span property="maxValue" content="1000000">1,000,000</span></td> <td><span property="availableChannel">Internet</span>, <span property="availableChannel">Post</span>, <span property="availableChannel">Telephone</span></td> </tr> </table> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "name": "Easy access accounts Comparison - Ordered by interest rate (AER)", "mainEntity": { "@type": "ItemList", "name": "Easy access accounts Comparison List", "itemListElement": [ { "@type": "DepositAccount", "provider": { "@id": "https://www.rcibank.co.uk", "name": "RCI Bank" }, "name": "Freedom Savings Account", "interestRate": { "@type": "QuantitativeValue", "value": "1.65", "valueReference": "Variable" }, "amount": { "@type": "MonetaryAmount", "currency": "GBP", "minValue": "100", "maxValue": "1000000" }, "availableChannel": ["Internet","Post","Telephone"] }, { "@type": "DepositAccount", "provider": { "@id": "https://sbiukonlinesavings.com/", "name": "State Bank of India" }, "name": "Online Instant Access Savings Issue 4", "interestRate": { "@type": "QuantitativeValue", "value": "1.25", "valueReference": "Variable" }, "amount": { "@type": "MonetaryAmount", "currency": "GBP", "minValue": "500", "maxValue": "1000000" }, "availableChannel": ["Internet","In Branch"] }, { "@type": "DepositAccount", "provider": { "@id": "http://www.aldermore.co.uk/", "name": "Aldermore" }, "name": "Easy Access Issue 9", "interestRate": { "@type": "QuantitativeValue", "value": "1.65", "valueReference": "Variable" }, "amount": { "@type": "MonetaryAmount", "currency": "GBP", "minValue": "1000", "maxValue": "1000000" }, "availableChannel": ["Internet","Post","Telephone"] } ] } } </script>

Structured representation of the JSON-LD example.
