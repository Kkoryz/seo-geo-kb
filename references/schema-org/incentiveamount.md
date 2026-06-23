---
title: "incentiveAmount"
source_url: https://schema.org/incentiveAmount
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# incentiveAmount

# incentiveAmount

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/incentiveAmount
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+incentiveAmount)

Describes the amount that can be redeemed from this incentive.











[QuantitativeValue](/QuantitativeValue): Use this for incentives based on price (either raw amount or percentage-based). For a raw amount example, "You can claim $2,500 - $7,500 from the total cost of installation" would be represented as the following:```
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

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/3572](https://github.com/schemaorg/schemaorg/issues/3572)
