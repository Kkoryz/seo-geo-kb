---
title: "MonetaryAmount"
source_url: https://schema.org/MonetaryAmount
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MonetaryAmount

# MonetaryAmount

A Schema.org Type

- Canonical URL: https://schema.org/MonetaryAmount
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MonetaryAmount)

A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use

[PriceSpecification](/PriceSpecification)Types to describe the price of an Offer, Invoice, etc.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[currency](/currency)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[maxValue](/maxValue)

[Number](/Number)```
```[minValue](/minValue)

[Number](/Number)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[value](/value)

[Boolean](/Boolean)or[Number](/Number)or[StructuredValue](/StructuredValue)or[Text](/Text)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

[Thing](/Thing)

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

[MonetaryAmount](/MonetaryAmount)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BankAccount](/BankAccount)[accountOverdraftLimit](/accountOverdraftLimit)

[BankAccount](/BankAccount)[amount](/amount)

[DatedMoneySpecification](/DatedMoneySpecification)or[InvestmentOrDeposit](/InvestmentOrDeposit)or[LoanOrCredit](/LoanOrCredit)or[MonetaryGrant](/MonetaryGrant)or[MoneyTransfer](/MoneyTransfer)[baseSalary](/baseSalary)

[EmployeeRole](/EmployeeRole)or[JobPosting](/JobPosting)[customerRemorseReturnShippingFeesAmount](/customerRemorseReturnShippingFeesAmount)

[MerchantReturnPolicy](/MerchantReturnPolicy)[customerRemorseReturnFees](/customerRemorseReturnFees)equals[ReturnShippingFees](/ReturnShippingFees).[downPayment](/downPayment)

[RepaymentSpecification](/RepaymentSpecification)[earlyPrepaymentPenalty](/earlyPrepaymentPenalty)

[RepaymentSpecification](/RepaymentSpecification)[estimatedCost](/estimatedCost)

[HowTo](/HowTo)or[HowToSupply](/HowToSupply)[estimatedSalary](/estimatedSalary)

[JobPosting](/JobPosting)or[Occupation](/Occupation)[exchangeRateSpread](/exchangeRateSpread)

[ExchangeRateSpecification](/ExchangeRateSpecification)[floorLimit](/floorLimit)

[PaymentCard](/PaymentCard)[freeShippingThreshold](/freeShippingThreshold)

[ShippingRateSettings](/ShippingRateSettings)[OfferShippingDetails](/OfferShippingDetails)with[shippingSettingsLink](/shippingSettingsLink)matching this[ShippingRateSettings](/ShippingRateSettings).[hasTierRequirement](/hasTierRequirement)

[MemberProgramTier](/MemberProgramTier)[incomeLimit](/incomeLimit)

[FinancialIncentive](/FinancialIncentive)If MonetaryAmount is specified, this should be based on annualized income (e.g. if an incentive is limited to those making <$114,000 annually):

```
{
"@type": "MonetaryAmount",
"maxValue": 114000,
"currency": "USD",
}
```


Use Text for incentives that are limited based on other criteria, for example if an incentive is only available to recipients making 120% of the median poverty income in their area.
[itemDefectReturnShippingFeesAmount](/itemDefectReturnShippingFeesAmount)

[MerchantReturnPolicy](/MerchantReturnPolicy)[itemDefectReturnFees](/itemDefectReturnFees)equals[ReturnShippingFees](/ReturnShippingFees).[loanMortgageMandateAmount](/loanMortgageMandateAmount)

[MortgageLoan](/MortgageLoan)[loanPaymentAmount](/loanPaymentAmount)

[RepaymentSpecification](/RepaymentSpecification)[minimumPaymentDue](/minimumPaymentDue)

[Invoice](/Invoice)[monthlyMinimumRepaymentAmount](/monthlyMinimumRepaymentAmount)

[PaymentCard](/PaymentCard)[netWorth](/netWorth)

[Person](/Person)[orderValue](/orderValue)

[ShippingConditions](/ShippingConditions)[purchasePriceLimit](/purchasePriceLimit)

[FinancialIncentive](/FinancialIncentive)[restockingFee](/restockingFee)

[MerchantReturnPolicy](/MerchantReturnPolicy)or[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)[MonetaryAmount](/MonetaryAmount)to specify a fixed restocking fee for product returns, or use[Number](/Number)to specify a percentage of the product price paid by the customer.[returnShippingFeesAmount](/returnShippingFeesAmount)

[MerchantReturnPolicy](/MerchantReturnPolicy)or[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)[returnFees](/returnFees)equals[ReturnShippingFees](/ReturnShippingFees).[shippingRate](/shippingRate)

[OfferShippingDetails](/OfferShippingDetails)or[ShippingConditions](/ShippingConditions)or[ShippingRateSettings](/ShippingRateSettings)[MonetaryAmount](/MonetaryAmount)) are most appropriate.[totalPaymentDue](/totalPaymentDue)

[Invoice](/Invoice)| Supersedes |
|---|
```
``` |

### Acknowledgements

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

[Example 2](#eg-0351)

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

[Example 3](#eg-0353)

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
