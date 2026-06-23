---
title: "LoanOrCredit"
source_url: https://schema.org/LoanOrCredit
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# LoanOrCredit

# LoanOrCredit

A Schema.org Type

- Canonical URL: https://schema.org/LoanOrCredit
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+LoanOrCredit)

A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

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

[Text](/Text)or[Thing](/Thing)[FinancialProduct](/FinancialProduct)

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

[URL](/URL)Instances of

[LoanOrCredit](/LoanOrCredit)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Demand](/Demand)or[Offer](/Offer)or[Organization](/Organization)[incentiveAmount](/incentiveAmount)

[FinancialIncentive](/FinancialIncentive)[QuantitativeValue](/QuantitativeValue): Use this for incentives based on price (either raw amount or percentage-based). For a raw amount example, "You can claim $2,500 - $7,500 from the total cost of installation" would be represented as the following:```
{
"@type": "QuantitativeValue",
“minValue”: 2500,
“maxValue”: 7500,
"unitCode": "USD"
}
```


[QuantitativeValue](/QuantitativeValue)can also be used for percentage amounts. In such cases, value is used to represent the incentive’s percentage, while maxValue represents a limit (if one exists) to that incentive. The unitCode should be 'P1' and the unitText should be '%', while valueReference should be used for holding the currency type. For example, "You can claim up to 30% of the total cost of installation, up to a maximum of $7,500" would be:```
{
"@type": "QuantitativeValue",
"value": 30,
"unitCode": "P1",
"unitText": "%",
“maxValue”: 7500,
“valueReference”: “USD”
}
```


[UnitPriceSpecification](/UnitPriceSpecification): Use this for incentives that are based on amounts rather than price. For example, a net metering rebate that pays $10/kWh, up to $1,000:```
{
"@type": "UnitPriceSpecification",
"price": 10,
"priceCurrency": "USD",
"referenceQuantity": 1,
"unitCode": "DO3",
"unitText": "kw/h",
"maxPrice": 1000,
"description": "$10 / kwh up to $1000"
}
```


[LoanOrCredit](/LoanOrCredit): Use for incentives that are loan based. For example, a loan of $4,000 - $50,000 with a repayment term of 10 years, interest free would look like:```
{
"@type": "LoanOrCredit",
"loanTerm": {
"@type":"QuantitativeValue",
"value":"10",
"unitCode": "ANN"
},
"amount":[
{
"@type": "QuantitativeValue",
"Name":"fixed interest rate",
"value":"0",
},
],
"amount":[
{
"@type": "MonetaryAmount",
"Name":"min loan amount",
"value":"4000",
"currency":"CAD"
},
{
"@type": "MonetaryAmount",
"Name":"max loan amount",
"value":"50000",
"currency":"CAD"
}
],
}
```


In summary: - Use
[QuantitativeValue](/QuantitativeValue)for absolute/percentage-based incentives applied on the price of a good/service. - Use
[UnitPriceSpecification](/UnitPriceSpecification)for incentives based on a per-unit basis (e.g. net metering). - Use
[LoanOrCredit](/LoanOrCredit)for loans/credits.

#### More specific Types

### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

### Examples

[Example 1](#eg-0351)

Copied

Example notes or example HTML without markup.

<div> Wells Fargo GraduateSM Student Loan You'll have up to 15 years to repay the loan. Competitive Annual Percentage Rate (APR) Variable interest rates range from 3.22% APR (with discount) to 8.74% APR (without discount). Fixed interest rates range from 6.36% APR (with discount) to 10.61% APR (without discount). The lifetime limit for this loan combined with all other education-related debt is $180,000 for law and business, and $120,000 for other fields of study. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Wells Fargo GraduateSM Student Loan --> <div itemscope itemtype="https://schema.org/LoanOrCredit"> <span itemprop="name">Wells Fargo GraduateSM Student Loan</span> You'll have up to <div itemprop="loanTerm" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value" content="15">15</span> <span itemprop="unitCode" content="ANN">years</span> </div> to repay the loan. Competitive Annual Percentage Rate (APR) <div itemprop="annualPercentageRate" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="name">Variable interest rates</span> range from <span itemprop="minValue" content="3.22">3.22%</span> APR (with discount) to <span itemprop="maxValue" content="8.74">8.74%</span> APR (without discount). </div> <div itemprop="annualPercentageRate" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="name">Fixed interest rates</span> range from <span itemprop="minValue" content="6.36">6.36%</span> APR (with discount) to <span itemprop="maxValue" content="10.61">10.61%</span> APR (without discount). </div> The lifetime limit for this loan combined with all other education-related debt is <div itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount"> <span itemprop="currency" content="USD">$</span> <span itemprop="value" content="180000">180,000</span> <span itemprop="name">for law and business</span>, </div> and <div itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount"> <span itemprop="currency" content="USD">$</span> <span itemprop="value" content="120000">120,000</span> <span itemprop="name">for other fields of study</span>. </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- Wells Fargo GraduateSM Student Loan --> <div vocab="https://schema.org/" typeof="LoanOrCredit"> <span property="name">Wells Fargo GraduateSM Student Loan</span> You'll have up to <div property="loanTerm" typeof="QuantitativeValue"> <span property="value" content="15">15</span> <span property="unitCode" content="ANN">years</span> </div> to repay the loan. Competitive Annual Percentage Rate (APR) <div property="annualPercentageRate" typeof="QuantitativeValue"> <span property="name">Variable interest rates</span> range from <span property="minValue" content="3.22">3.22%</span> APR (with discount) to <span property="maxValue" content="8.74">8.74%</span> APR (without discount). </div> <div property="annualPercentageRate" typeof="QuantitativeValue"> <span property="name">Fixed interest rates</span> range from <span property="minValue" content="6.36">6.36%</span> APR (with discount) to <span property="maxValue" content="10.61">10.61%</span> APR (without discount). </div> The lifetime limit for this loan combined with all other education-related debt is <div property="amount" typeof="MonetaryAmount"> <span property="currency" content="USD">$</span> <span property="value" content="180000">180,000</span> <span property="name">for law and business</span>, </div> and <div property="amount" typeof="MonetaryAmount"> <span property="currency" content="USD">$</span> <span property="value" content="120000">120,000</span> <span property="name">for other fields of study</span>. </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- Wells Fargo GraduateSM Student Loan --> <script type="application/ld+json"> { "@context":"https://schema.org", "@type":"LoanOrCredit", "name":"Wells Fargo GraduateSM Student Loan", "loanTerm":{ "@type":"QuantitativeValue", "value":"15", "unitCode": "ANN" }, "annualPercentageRate":[ { "@type":"QuantitativeValue", "name": "variable interest rates", "minValue":"3.22", "maxValue":"8.74" }, { "@type":"QuantitativeValue", "name": "fixed interest rates", "minValue":"6.36", "maxValue":"10.61" } ], "amount":[ { "@type": "MonetaryAmount", "name":"debt for law and business", "value":"180000", "currency":"USD" }, { "@type": "MonetaryAmount", "name":"debt for other fields of study than law and business", "value":"120000", "currency":"USD" } ] } </script>

Structured representation of the JSON-LD example.
