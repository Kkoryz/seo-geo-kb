---
title: "StatisticalVariable"
source_url: https://schema.org/StatisticalVariable
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# StatisticalVariable

# StatisticalVariable

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/StatisticalVariable
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+StatisticalVariable)

[StatisticalVariable](/StatisticalVariable)represents any type of statistical metric that can be measured at a place and time. The usage pattern for

[StatisticalVariable](/StatisticalVariable)is typically expressed using

[Observation](/Observation)with an explicit

[populationType](/populationType), which is a type, typically drawn from Schema.org. Each

[StatisticalVariable](/StatisticalVariable)is marked as a

[ConstraintNode](/ConstraintNode), meaning that some properties (those listed using

[constraintProperty](/constraintProperty)) serve in this setting solely to define the statistical variable rather than literally describe a specific person, place or thing. For example, a

[StatisticalVariable](/StatisticalVariable)Median

*Height*Person_Female representing the median height of women, could be written as follows: the population type is

[Person](/Person); the measuredProperty

[height](/height); the

[statType](/statType)

[median](/median); the

[gender](/gender)

[Female](/Female). It is important to note that there are many kinds of scientific quantitative observation which are not fully, perfectly or unambiguously described following this pattern, or with solely Schema.org terminology. The approach taken here is designed to allow partial, incremental or minimal description of

[StatisticalVariable](/StatisticalVariable)s, and the use of detailed sets of entity and property IDs from external repositories. The

[measurementMethod](/measurementMethod),

[unitCode](/unitCode)and

[unitText](/unitText)properties can also be used to clarify the specific nature and notation of an observed measurement.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
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
```[populationType](/populationType)

[Class](/Class)[StatisticalPopulation](/StatisticalPopulation)or all cases within the scope of a[StatisticalVariable](/StatisticalVariable).```
```[statType](/statType)

[Property](/Property)or[Text](/Text)or[URL](/URL)[StatisticalVariable](/StatisticalVariable), e.g. mean, count etc. The value of statType is a property, either from within Schema.org (e.g.[median](/median),[marginOfError](/marginOfError),[maxValue](/maxValue),[minValue](/minValue)) or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.[ConstraintNode](/ConstraintNode)

```
```[constraintProperty](/constraintProperty)

[Property](/Property)or[URL](/URL)[StatisticalVariable](/StatisticalVariable). The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.```
```[numConstraints](/numConstraints)

[Integer](/Integer)[ConstraintNode](/ConstraintNode)such as[StatisticalVariable](/StatisticalVariable). This helps applications understand if they have access to a sufficiently complete description of a[StatisticalVariable](/StatisticalVariable)or other construct that is defined using properties on template-style nodes.[Thing](/Thing)

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

[StatisticalVariable](/StatisticalVariable)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Observation](/Observation)or[StatisticalVariable](/StatisticalVariable)[variableMeasured](/variableMeasured)

[Dataset](/Dataset)or[Observation](/Observation)[StatisticalVariable](/StatisticalVariable).#### Source

[https://github.com/schemaorg/schemaorg/issues/2564](https://github.com/schemaorg/schemaorg/issues/2564)

### Examples

[Example 1](#eg-0480)

Copied

Example notes or example HTML without markup.

As an example, the statement "According to the US Census ACS 5 Year Estimates, the median age of women in San Antonio, Texas in 2014 was 34.4 years." can be represented in JSON-LD.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@graph": [ { "@type": "StatisticalVariable", "@id": "Median_Height_Person_Female", "name": "Median height of women", "description": "The median height of the female population.", "populationType": { "@id": "schema:Person" }, "measuredProperty": { "@id": "schema:height" }, "statType": { "@id": "schema:median" } }, { "@type": "Observation", "@id": "Observation_Median_Age_Person_Female_SanAntonio_TX_2014", "name": "Median height of women in San Antonio, Texas in 2014", "description": "An Observation of the StatisticalVariable Median_Height_Person_Female in location: San Antonio, Texas, for time period: 2014", "variableMeasured": { "@id": "Median_Height_Person_Female" }, "observationAbout": { "@id": "https://www.wikidata.org/entity/Q975" }, "observationDate": "2014", "value": 160, "unitCode": "CMT" } ] } </script>

Structured representation of the JSON-LD example.
