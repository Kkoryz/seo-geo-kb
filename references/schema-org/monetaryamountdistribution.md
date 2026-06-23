---
title: "MonetaryAmountDistribution"
source_url: https://schema.org/MonetaryAmountDistribution
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MonetaryAmountDistribution

# MonetaryAmountDistribution

A Schema.org Type

- Canonical URL: https://schema.org/MonetaryAmountDistribution
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MonetaryAmountDistribution)

A statistical distribution of monetary amounts.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[currency](/currency)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".[QuantitativeValueDistribution](/QuantitativeValueDistribution)

```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).```
```[median](/median)

[Number](/Number)```
```[percentile10](/percentile10)

[Number](/Number)```
```[percentile25](/percentile25)

[Number](/Number)```
```[percentile75](/percentile75)

[Number](/Number)```
```[percentile90](/percentile90)

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

[MonetaryAmountDistribution](/MonetaryAmountDistribution)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[JobPosting](/JobPosting)or[Occupation](/Occupation)[salaryUponCompletion](/salaryUponCompletion)

[EducationalOccupationalProgram](/EducationalOccupationalProgram)[trainingSalary](/trainingSalary)

[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[WorkBasedProgram](/WorkBasedProgram)#### Source

[https://github.com/schemaorg/schemaorg/issues/1698](https://github.com/schemaorg/schemaorg/issues/1698)

### Examples

[Example 1](#eg-0252)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Occupation", "name": "Nurse Practioner", "educationRequirements": "Graduate degree in nursing", "occupationalCategory": "29-1171.00", "occupationLocation": { "@type": "Country", "name": "USA", "sameAs": "https://www.wikidata.org/wiki/Q30" }, "qualifications": "Registered nurse licensure in state where practicing", "responsibilities": "Diagnose and treat acute, episodic, or chronic illness, independently or as part of a healthcare team.", "skills": ["Active listening", "Critical thinking", "Social awareness"], "estimatedSalary": { "@type": "MonetaryAmountDistribution", "duration": "1Y", "currency": "USD", "percentile10": 72000, "percentile25": 86000, "median": 109000, "percentile75": 120000, "percentile90": 140000 } } </script>

Structured representation of the JSON-LD example.
