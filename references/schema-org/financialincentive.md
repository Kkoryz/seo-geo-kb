---
title: "FinancialIncentive"
source_url: https://schema.org/FinancialIncentive
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# FinancialIncentive

# FinancialIncentive

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/FinancialIncentive
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+FinancialIncentive)

Represents financial incentives for goods/services offered by an organization (or individual).


Typically contains the


Optionally contains criteria on whether the incentive is limited based on

Typically contains the

[name](/name)of the incentive, the[incentivizedItem](/incentivizedItem), the[incentiveAmount](/incentiveAmount), the[incentiveStatus](/incentiveStatus),[incentiveType](/incentiveType), the[provider](/provider)of the incentive, and[eligibleWithSupplier](/eligibleWithSupplier).Optionally contains criteria on whether the incentive is limited based on

[purchaseType](/purchaseType),[purchasePriceLimit](/purchasePriceLimit),[incomeLimit](/incomeLimit), and the[qualifiedExpense](/qualifiedExpense).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[eligibleWithSupplier](/eligibleWithSupplier)

[Organization](/Organization)```
```[incentiveAmount](/incentiveAmount)

[LoanOrCredit](/LoanOrCredit)or[QuantitativeValue](/QuantitativeValue)or[UnitPriceSpecification](/UnitPriceSpecification)[QuantitativeValue](/QuantitativeValue): Use this for incentives based on price (either raw amount or percentage-based). For a raw amount example, "You can claim $2,500 - $7,500 from the total cost of installation" would be represented as the following:```
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

```
```[incentiveStatus](/incentiveStatus)

[IncentiveStatus](/IncentiveStatus)```
```[incentiveType](/incentiveType)

[IncentiveType](/IncentiveType)```
```[incentivizedItem](/incentivizedItem)

[DefinedTerm](/DefinedTerm)or[Product](/Product)DefinedTermSets are used for product and service categories such as the United Nations Standard Products and Services Code:

```
{
"@type": "DefinedTerm",
"inDefinedTermSet": "https://www.unspsc.org/",
"termCode": "261315XX",
"name": "Photovoltaic module"
}
```


For a specific product or service, use the Product type:```
{
"@type": "Product",
"name": "Kenmore White 17" Microwave",
}
```


For multiple different incentivized items, use multiple [DefinedTerm](/DefinedTerm)or[Product](/Product).```
```[incomeLimit](/incomeLimit)

[MonetaryAmount](/MonetaryAmount)or[Text](/Text)If MonetaryAmount is specified, this should be based on annualized income (e.g. if an incentive is limited to those making <$114,000 annually):

```
{
"@type": "MonetaryAmount",
"maxValue": 114000,
"currency": "USD",
}
```


Use Text for incentives that are limited based on other criteria, for example if an incentive is only available to recipients making 120% of the median poverty income in their area.
```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[publisher](/publisher)

[Organization](/Organization)or[Person](/Person)```
```[purchasePriceLimit](/purchasePriceLimit)

[MonetaryAmount](/MonetaryAmount)```
```[purchaseType](/purchaseType)

[PurchaseType](/PurchaseType)```
```[qualifiedExpense](/qualifiedExpense)

[IncentiveQualifiedExpenseType](/IncentiveQualifiedExpenseType)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)[Thing](/Thing)

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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/3572](https://github.com/schemaorg/schemaorg/issues/3572)

### Examples

[Example 1](#eg-0490)

Copied

Example notes or example HTML without markup.

An example annotation for the US Federal EV Tax Credit implemented as part of the Inflation Reduction Act.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FinancialIncentive", "name": "Clean Vehicle Tax Credit", "url": "https://www.irs.gov/credits-deductions/credits-for-new-clean-vehicles-purchased-in-2023-or-after", "publisher": { "@type": "Organization", "name": "Internal Revenue Service (IRS)" }, "provider": { "@type": "Organization", "name": "US Federal Government" }, "areaServed": { "@type": "Country", "name": "United States" }, "validFrom": "2023-01-01", "validThrough": "2032-12-31", "incentiveType": "TaxCredit", "purchaseType": "NewPurchase", "incentiveAmount": { "@type": "QuantitativeValue", "minValue": "2500", "maxValue": "7500", "unitCode": "USD" }, "incentiveStatus": "Active", "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "25101509", "name": "Electrically powered vehicle" }, "incomeLimit": { "@type": "MonetaryAmount", "maxValue": "114000", "currency": "USD" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0491)

Copied

Example notes or example HTML without markup.

An example annotation for the Australian ACT Sustainable Household Scheme, which offers interest-free loans from 2,000-15,000 AUD using a list of DefinedTerms.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FinancialIncentive", "name": "ACT Sustainable Household Scheme", "url": "https://www.climatechoices.act.gov.au/policy-programs/sustainable-household-scheme", "publisher": { "@type": "Organization", "name": "ACT Government" }, "provider": { "@type": "Organization", "name": "Brighte" }, "areaServed": { "@type": "State", "name": "Australian Capital Territory" }, "validFrom": "2021-05-01", "validThrough": "2026-06-30", "incentiveType": "Loan", "purchaseType": "NewPurchase", "incentiveAmount": { "@type": "LoanOrCredit", "loanTerm": { "@type": "QuantitativeValue", "value": "10", "unitCode": "ANN" }, "annualPercentageRate": [ { "@type": "QuantitativeValue", "name": "fixed interest rates", "minValue": "0", "maxValue": "0" } ], "amount": [ { "@type": "MonetaryAmount", "name": "loan amount", "minValue": "2000", "maxValue": "15000", "currency": "AUD" } ] }, "incentiveStatus": "Active", "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "30141500", "name": "Thermal insulation" }, "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "40101806", "name": "Heat Pumps" }, "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "261315XX", "name": "Photovoltaic module" }, "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "251018XX", "name": "Electric two-wheel vehicle" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0492)

Copied

Example notes or example HTML without markup.

An example annotation for the UK Electric Vehicle chargepoint grant for renters or flat owners, at 75% of the price to a max of $350.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FinancialIncentive", "name": "Electric Vehicle Chargepoint Grant", "url": "https://www.gov.uk/electric-vehicle-chargepoint-grant-household", "publisher": { "@type": "Organization", "name": "UK Government" }, "provider": { "@type": "Organization", "name": "Office for Zero Emission Vehicles (OZEV)" }, "areaServed": { "@type": "Country", "name": "United Kingdom" }, "validFrom": "2020-04-01", "validThrough": "2025-03-31", "incentiveType": "RebateOrSubsidy", "purchaseType": "NewPurchase", "incentiveStatus": "Active", "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "25175000", "name": "Electric vehicle charging systems" }, "incentiveAmount": { "@type": "QuantitativeValue", "value": "75", "unitCode": "P1", "unitText": "%", "maxValue": "350", "valueReference": "GBP" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0493)

Copied

Example notes or example HTML without markup.

An example annotation for the Solar Rebate Program in Banff, CA.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FinancialIncentive", "name": "Solar Rebate Program", "url": "https://www.banff.ca/807/Solar-Incentive-Program", "publisher": { "@type": "Organization", "name": "Town of Banff" }, "provider": { "@type": "Organization", "name": "Town of Banff" }, "areaServed": { "@type": "City", "name": "Banff" }, "validFrom": "2018-01-01", "validThrough": "2024-12-31", "incentiveType": "RebateOrSubsidy", "purchaseType": "NewPurchase", "incentiveAmount": { "@type": "UnitPriceSpecification", "price": "750", "priceCurrency": "USD", "referenceQuantity": "1", "unitCode": "KWT", "unitText": "kW", "maxPrice": "15000" }, "incentiveStatus": "Active", "incentivizedItem": { "@type": "DefinedTerm", "inDefinedTermSet": "https://www.unspsc.org/", "termCode": "261315XX", "name": "Photovoltaic module" } } </script>

Structured representation of the JSON-LD example.
