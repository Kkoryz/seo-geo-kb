---
title: "Observation"
source_url: https://schema.org/Observation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Observation

# Observation

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

[Thing](/Thing)>

[Intangible](/Intangible)>

[Observation](/Observation)

[Thing](/Thing)>

[Intangible](/Intangible)>

[StructuredValue](/StructuredValue)>

[QuantitativeValue](/QuantitativeValue)>

[Observation](/Observation)

- Canonical URL: https://schema.org/Observation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Observation)

Instances of the class


Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and


In the context of a quantitative knowledge graph, typical properties could include

[Observation](/Observation)are used to specify observations about an entity at a particular time. The principal properties of an[Observation](/Observation)are[observationAbout](/observationAbout),[measuredProperty](/measuredProperty),[statType](/statType), [[value] and[observationDate](/observationDate)and[measuredProperty](/measuredProperty). Some but not all Observations represent a[QuantitativeValue](/QuantitativeValue). Quantitative observations can be about a[StatisticalVariable](/StatisticalVariable), which is an abstract specification about which we can make observations that are grounded at a particular location and time.Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and

[value](/value))In the context of a quantitative knowledge graph, typical properties could include

[measuredProperty](/measuredProperty),[observationAbout](/observationAbout),[observationDate](/observationDate),[value](/value),[unitCode](/unitCode),[unitText](/unitText),[measurementMethod](/measurementMethod).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[marginOfError](/marginOfError)

[QuantitativeValue](/QuantitativeValue)[marginOfError](/marginOfError)for an[Observation](/Observation).```
```[measuredProperty](/measuredProperty)

[Property](/Property)[Observation](/Observation), typically via its[StatisticalVariable](/StatisticalVariable). There are various kinds of applicable[Property](/Property): a schema.org property, a property from other RDF-compatible systems, e.g. W3C RDF Data Cube, Data Commons, Wikidata, or schema.org extensions such as[GS1's](https://www.gs1.org/voc/?show=properties).```
```[measurementDenominator](/measurementDenominator)

[StatisticalVariable](/StatisticalVariable)```
```[measurementMethod](/measurementMethod)

[DefinedTerm](/DefinedTerm)or[MeasurementMethodEnum](/MeasurementMethodEnum)or[Text](/Text)or[URL](/URL)[measurementTechnique](/measurementTechnique)that can be used for specifying specific methods, in particular via[MeasurementMethodEnum](/MeasurementMethodEnum).```
```[measurementQualifier](/measurementQualifier)

[Enumeration](/Enumeration)```
```[measurementTechnique](/measurementTechnique)

[DefinedTerm](/DefinedTerm)or[MeasurementMethodEnum](/MeasurementMethodEnum)or[Text](/Text)or[URL](/URL)[Observation](/Observation),[StatisticalVariable](/StatisticalVariable)or[Dataset](/Dataset)(or[DataDownload](/DataDownload),[DataCatalog](/DataCatalog)), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using[variableMeasured](/variableMeasured); for[Observation](/Observation), a[StatisticalVariable](/StatisticalVariable)). Often but not necessarily each[variableMeasured](/variableMeasured)will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of[variableMeasured](/variableMeasured)called[measuredProperty](/measuredProperty)is applicable.The

[measurementTechnique](/measurementTechnique)property helps when extra clarification is needed about how a[measuredProperty](/measuredProperty)was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery.For example, if

[variableMeasured](/variableMeasured)is: molecule concentration,[measurementTechnique](/measurementTechnique)could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the[variableMeasured](/variableMeasured)is "depression rating", the[measurementTechnique](/measurementTechnique)could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several

[variableMeasured](/variableMeasured)properties recorded for some given data object, use a[PropertyValue](/PropertyValue)for each[variableMeasured](/variableMeasured)and attach the corresponding[measurementTechnique](/measurementTechnique). The value can also be from an enumeration, organized as a[MeasurementMethodEnum](/MeasurementMethodEnum).```
```[observationAbout](/observationAbout)

[Place](/Place)or[Thing](/Thing)[observationAbout](/observationAbout)property identifies an entity, often a[Place](/Place), associated with an[Observation](/Observation).```
```[observationDate](/observationDate)

[Date](/Date)or[DateTime](/DateTime)[Observation](/Observation).```
```[observationPeriod](/observationPeriod)

[Text](/Text)`P[0-9]*[Y|M|D|h|m|s]`

. For example, P1Y is Period 1 Year, P3M is Period 3 Months, P3h is Period 3 hours.
```
```[variableMeasured](/variableMeasured)

[Property](/Property)or[PropertyValue](/PropertyValue)or[StatisticalVariable](/StatisticalVariable)or[Text](/Text)[StatisticalVariable](/StatisticalVariable).[QuantitativeValue](/QuantitativeValue)

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[maxValue](/maxValue)

[Number](/Number)```
```[minValue](/minValue)

[Number](/Number)```
```[unitCode](/unitCode)

[Text](/Text)or[URL](/URL)```
```[unitText](/unitText)

[Text](/Text)[unitCode](unitCode).```
```[value](/value)

[Boolean](/Boolean)or[Number](/Number)or[StructuredValue](/StructuredValue)or[Text](/Text)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[valueReference](/valueReference)

[DefinedTerm](/DefinedTerm)or[Enumeration](/Enumeration)or[MeasurementTypeEnumeration](/MeasurementTypeEnumeration)or[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)or[StructuredValue](/StructuredValue)or[Text](/Text)[Thing](/Thing)

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

[Observation](/Observation)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[SpecialAnnouncement](/SpecialAnnouncement)[WebContent](/WebContent), or described directly as a[Dataset](/Dataset), or the specific[Observation](/Observation)s in the dataset. When a[WebContent](/WebContent)URL is provided, the page indicated might also contain more such markup.#### Source

[https://github.com/schemaorg/schemaorg/issues/2291](https://github.com/schemaorg/schemaorg/issues/2291)

### Examples

[Example 1](#eg-0480)

Copied

Example notes or example HTML without markup.

As an example, the statement "According to the US Census ACS 5 Year Estimates, the median age of women in San Antonio, Texas in 2014 was 34.4 years." can be represented in JSON-LD.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@graph": [ { "@type": "StatisticalVariable", "@id": "Median_Height_Person_Female", "name": "Median height of women", "description": "The median height of the female population.", "populationType": { "@id": "schema:Person" }, "measuredProperty": { "@id": "schema:height" }, "statType": { "@id": "schema:median" } }, { "@type": "Observation", "@id": "Observation_Median_Age_Person_Female_SanAntonio_TX_2014", "name": "Median height of women in San Antonio, Texas in 2014", "description": "An Observation of the StatisticalVariable Median_Height_Person_Female in location: San Antonio, Texas, for time period: 2014", "variableMeasured": { "@id": "Median_Height_Person_Female" }, "observationAbout": { "@id": "https://www.wikidata.org/entity/Q975" }, "observationDate": "2014", "value": 160, "unitCode": "CMT" } ] } </script>

Structured representation of the JSON-LD example.
