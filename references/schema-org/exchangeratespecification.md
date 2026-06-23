---
title: "ExchangeRateSpecification"
source_url: https://schema.org/ExchangeRateSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ExchangeRateSpecification

# ExchangeRateSpecification

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/ExchangeRateSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ExchangeRateSpecification)

A structured value representing exchange rate.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[currency](/currency)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[currentExchangeRate](/currentExchangeRate)

[UnitPriceSpecification](/UnitPriceSpecification)```
```[exchangeRateSpread](/exchangeRateSpread)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)[Thing](/Thing)

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

#### Source

[https://github.com/schemaorg/schemaorg/issues/1253](https://github.com/schemaorg/schemaorg/issues/1253)

### Examples

[Example 1](#eg-0235)

Copied

Example notes or example HTML without markup.

<body> <h1>Middle exchange rates of foreign currencies – table A</h1> <h2>Table No. 047/A/NBP/2016 of 2016-03-0</h2> <div> <table> <tr> <th>Currency</th> <th>Code</th> <th>Mid-rate </th> </tr> <tr> <td>Euro</td> <td>1 EUR</td> <td>4.3215</td> </tr> <tr> <td>Brazilian Real</td> <td>1 BRL</td> <td>1.0490</td> </tr> </table> </div> </body>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/WebPage"> <h1 itemprop="name">Middle exchange rates of foreign currencies – table A</h1> <div itemprop="mainEntity" itemscope itemtype="https://schema.org/ItemList"> <table> <caption itemprop="name">Table No. 047/A/NBP/2016 of 2016-03-09</caption> <tr> <th>Currency</th> <th>Code</th> <th>Mid-rate </th> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/ExchangeRateSpecification"> <td itemprop="currency" content="EUR">Euro</td> <td>1 EUR</td> <td itemprop="currentExchangeRate" itemscope itemtype="https://schema.org/UnitPriceSpecification"> <span itemprop="price">4.3215</span> <meta itemprop="priceCurrency" content="PLN"/> </td> </tr> <tr itemprop="itemListElement" itemscope itemtype="https://schema.org/ExchangeRateSpecification"> <td itemprop="currency" content="BRL">Brazilian Real</td> <td>1 BRL</td> <td itemprop="currentExchangeRate" itemscope itemtype="https://schema.org/UnitPriceSpecification"> <span itemprop="price">1.0490</span> <meta itemprop="priceCurrency" content="PLN"/> </td> </tr> </table> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> <h1 property="name">Middle exchange rates of foreign currencies – table A</h1> <div property="mainEntity" typeof="ItemList"> <table> <caption property="name">Table No. 047/A/NBP/2016 of 2016-03-09</caption> <tr> <th>Currency</th> <th>Code</th> <th>Mid-rate </th> </tr> <tr property="itemListElement" typeof="ExchangeRateSpecification"> <td property="currency" content="EUR">Euro</td> <td>1 EUR</td> <td property="currentExchangeRate" typeof="UnitPriceSpecification"> <span property="price">4.3215</span> <meta property="priceCurrency" content="PLN"/> </td> </tr> <tr property="itemListElement" typeof="ExchangeRateSpecification"> <td property="currency" content="BRL">Brazilian Real</td> <td>1 BRL</td> <td property="currentExchangeRate" typeof="UnitPriceSpecification"> <span property="price">1.0490</span> <meta property="priceCurrency" content="PLN"/> </td> </tr> </table> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "name": "Middle exchange rates of foreign currencies – table A", "mainEntity": { "@type": "ItemList", "name": "Table No. 047/A/NBP/2016 of 2016-03-09", "itemListElement": [ { "@type": "ExchangeRateSpecification", "currency":"EUR", "currentExchangeRate":{ "@type": "UnitPriceSpecification", "price": "4.3215", "priceCurrency": "PLN" } }, { "@type": "ExchangeRateSpecification", "currency":"BRL", "currentExchangeRate":{ "@type": "UnitPriceSpecification", "price": "1.0490", "priceCurrency": "PLN" } } ] } } </script>

Structured representation of the JSON-LD example.
