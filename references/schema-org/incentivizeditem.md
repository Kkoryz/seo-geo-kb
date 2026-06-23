---
title: "incentivizedItem"
source_url: https://schema.org/incentivizedItem
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# incentivizedItem

# incentivizedItem

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/incentivizedItem
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+incentivizedItem)

The type or specific product(s) and/or service(s) being incentivized.


DefinedTermSets are used for product and service categories such as the United Nations Standard Products and Services Code:





DefinedTermSets are used for product and service categories such as the United Nations Standard Products and Services Code:

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


For multiple different incentivized items, use multiple [DefinedTerm](/DefinedTerm)or[Product](/Product).### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/3572](https://github.com/schemaorg/schemaorg/issues/3572)
