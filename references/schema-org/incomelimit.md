---
title: "incomeLimit"
source_url: https://schema.org/incomeLimit
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# incomeLimit

# incomeLimit

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/incomeLimit
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+incomeLimit)

Optional. Income limit for which the incentive is applicable for.


If MonetaryAmount is specified, this should be based on annualized income (e.g. if an incentive is limited to those making <$114,000 annually):



If MonetaryAmount is specified, this should be based on annualized income (e.g. if an incentive is limited to those making <$114,000 annually):

```
{
"@type": "MonetaryAmount",
"maxValue": 114000,
"currency": "USD",
}
```


Use Text for incentives that are limited based on other criteria, for example if an incentive is only available to recipients making 120% of the median poverty income in their area.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/3572](https://github.com/schemaorg/schemaorg/issues/3572)
