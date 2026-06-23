---
title: "UnitPriceSpecification"
source_url: https://schema.org/UnitPriceSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# UnitPriceSpecification

# UnitPriceSpecification

A Schema.org Type

- Canonical URL: https://schema.org/UnitPriceSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+UnitPriceSpecification)

The price asked for a given offer by the respective organization or person.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[billingDuration](/billingDuration)

[Duration](/Duration)or[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[billingIncrement](/billingIncrement)

[Number](/Number)```
```[billingStart](/billingStart)

[Number](/Number)```
```[priceComponentType](/priceComponentType)

[PriceComponentTypeEnumeration](/PriceComponentTypeEnumeration)```
```[priceType](/priceType)

[PriceTypeEnumeration](/PriceTypeEnumeration)or[Text](/Text)[priceType](/priceType)property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or, a UN/EDIFACT 5387 code, or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.```
```[referenceQuantity](/referenceQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[unitCode](/unitCode)

[Text](/Text)or[URL](/URL)```
```[unitText](/unitText)

[Text](/Text)[unitCode](unitCode).[PriceSpecification](/PriceSpecification)

```
```[eligibleQuantity](/eligibleQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleTransactionVolume](/eligibleTransactionVolume)

[PriceSpecification](/PriceSpecification)```
```[maxPrice](/maxPrice)

[Number](/Number)```
```[membershipPointsEarned](/membershipPointsEarned)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[minPrice](/minPrice)

[Number](/Number)```
```[price](/price)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use the
[priceCurrency](/priceCurrency)property (with standard formats:[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR") instead of including[ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)such as '$' in the value. - Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
- Note that both
[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.

```
```[priceCurrency](/priceCurrency)

[Text](/Text)[PriceSpecification](/PriceSpecification)and its subtypes.Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[valueAddedTaxIncluded](/valueAddedTaxIncluded)

[Boolean](/Boolean)[Thing](/Thing)

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

[UnitPriceSpecification](/UnitPriceSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ExchangeRateSpecification](/ExchangeRateSpecification)[hasTierRequirement](/hasTierRequirement)

[MemberProgramTier](/MemberProgramTier)[incentiveAmount](/incentiveAmount)

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
