---
title: "RepaymentSpecification"
source_url: https://schema.org/RepaymentSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# RepaymentSpecification

# RepaymentSpecification

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/RepaymentSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+RepaymentSpecification)

A structured value representing repayment.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[downPayment](/downPayment)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)```
```[earlyPrepaymentPenalty](/earlyPrepaymentPenalty)

[MonetaryAmount](/MonetaryAmount)```
```[loanPaymentAmount](/loanPaymentAmount)

[MonetaryAmount](/MonetaryAmount)```
```[loanPaymentFrequency](/loanPaymentFrequency)

[Number](/Number)```
```[numberOfLoanPayments](/numberOfLoanPayments)

[Number](/Number)[Thing](/Thing)

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

[RepaymentSpecification](/RepaymentSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[LoanOrCredit](/LoanOrCredit)### Acknowledgements

Financial Industry Business Ontology project

[http://www.fibo.org/schema](http://www.fibo.org/schema)for details), in support of the W3C Financial Industry Business Ontology Community Group (

[http://www.fibo.org/community](http://www.fibo.org/community)). Many class and property definitions are inspired by or based on

[http://www.fibo.org](http://www.fibo.org).

#### Source

[https://github.com/schemaorg/schemaorg/issues/1253](https://github.com/schemaorg/schemaorg/issues/1253)

### Examples

[Example 1](#eg-0234)

Copied

Example notes or example HTML without markup.

<div> <h1>Agency 30 Year Fixed</h1> <p>Experience easier budgeting with predictable monthly payments. Relax knowing you’ll never have to worry about rising interest rates for the life of your loan.</p> </div> <table> <caption>Rates are based on a loan amount of $200,000 and 20% down payment.</caption> <tr> <td>Interest rate</td> <td>3.625%</td> </tr> <tr> <td>APR</td> <td>3.8047%</td> </tr> <tr> <td>Estimated payment</td> <td>$912.11</td> </tr> <tr> <td>Months</td> <td>360</td> </tr> </table>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/MortgageLoan"> <h1 itemprop="name">Agency 30 Year Fixed</h1> <div itemprop="loanTerm" itemscope itemtype="https://schema.org/QuantitativeValue"> <meta itemprop="value" content="30"/> <meta itemprop="unitCode" content="ANN"/> </div> <p itemprop="description">Experience easier budgeting with predictable monthly payments. Relax knowing you’ll never have to worry about rising interest rates for the life of your loan.</p> <div itemprop="loanRepaymentForm" itemscope itemtype="https://schema.org/RepaymentSpecification" itemref="estPay payNum"> <meta itemprop="downPayment" content="20"/> <meta itemprop="loanPaymentFrequency" content="1"/> <span>Estimated payment</span> <div id="estPay" itemprop="loanPaymentAmount" itemscope itemtype="https://schema.org/MonetaryAmount"> <span itemprop="currency" content="USD">$</span><span itemprop="value">912.11</span></div> <span>Months</span> <div id="payNum" itemprop="numberOfLoanPayments">360</div> </div> <table> <caption id="amount" itemprop="amount" itemscope itemtype="https://schema.org/MonetaryAmount">Rates are based on a loan amount of <span itemprop="currency" content="USD">$</span><span itemprop="value" content="200000">200,000</span> and 20% down payment.</caption> <tr> <td>Interest rate</td> <td><span id="intRate" itemprop="interestRate">3.625</span>%</td> </tr> <tr> <td>APR</td> <td><span id="apr" itemprop="annualPercentageRate">3.8047</span>%</td> </tr> </table> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="MortgageLoan"> <h1 property="name">Agency 30 Year Fixed</h1> <div property="loanTerm" typeof="QuantitativeValue"> <meta property="value" content="30"/> <meta property="unitCode" content="ANN"/> </div> <p property="description">Experience easier budgeting with predictable monthly payments. Relax knowing you’ll never have to worry about rising interest rates for the life of your loan.</p> <div property="loanRepaymentForm" typeof="RepaymentSpecification" itemref="estPay payNum"> <meta property="downPayment" content="20"/> <meta property="loanPaymentFrequency" content="1"/> <span>Estimated payment</span> <div id="estPay" property="loanPaymentAmount" typeof="MonetaryAmount"> <span property="currency" content="USD">$</span><span property="value">912.11</span></div> <span>Months</span> <div id="payNum" property="numberOfLoanPayments">360</div> </div> <table> <caption id="amount" property="amount" typeof="MonetaryAmount">Rates are based on a loan amount of <span property="currency" content="USD">$</span><span property="value" content="200000">200,000</span> and 20% down payment.</caption> <tr> <td>Interest rate</td> <td><span id="intRate" property="interestRate">3.625</span>%</td> </tr> <tr> <td>APR</td> <td><span id="apr" property="annualPercentageRate">3.8047</span>%</td> </tr> </table> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MortgageLoan", "name": "Agency 30 Year Fixed", "description": "Experience easier budgeting with predictable monthly payments. Relax knowing you’ll never have to worry about rising interest rates for the life of your loan.", "amount": { "@type": "MonetaryAmount", "value": "200000", "currency": "USD" }, "loanTerm": { "@type": "QuantitativeValue", "value": "30", "unitCode": "ANN" }, "interestRate": "3.625", "annualPercentageRate": "3.8047", "loanRepaymentForm": { "@type": "RepaymentSpecification", "loanPaymentAmount": { "@type": "MonetaryAmount", "value": "909.3", "currency": "USD" }, "downPayment": "20", "numberOfLoanPayments": "360", "loanPaymentFrequency": "1" } } </script>

Structured representation of the JSON-LD example.
