---
title: "MeasurementMethodEnum"
source_url: https://schema.org/MeasurementMethodEnum
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MeasurementMethodEnum

# MeasurementMethodEnum

A Schema.org Enumeration Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/MeasurementMethodEnum
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MeasurementMethodEnum)

Enumeration(s) for use with

[measurementMethod](/measurementMethod).Instances of

[MeasurementMethodEnum](/MeasurementMethodEnum)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[DataCatalog](/DataCatalog)or[DataDownload](/DataDownload)or[Dataset](/Dataset)or[Observation](/Observation)or[PropertyValue](/PropertyValue)or[StatisticalVariable](/StatisticalVariable)[measurementTechnique](/measurementTechnique)that can be used for specifying specific methods, in particular via[MeasurementMethodEnum](/MeasurementMethodEnum).[measurementTechnique](/measurementTechnique)

[DataCatalog](/DataCatalog)or[DataDownload](/DataDownload)or[Dataset](/Dataset)or[Observation](/Observation)or[PropertyValue](/PropertyValue)or[StatisticalVariable](/StatisticalVariable)[Observation](/Observation),[StatisticalVariable](/StatisticalVariable)or[Dataset](/Dataset)(or[DataDownload](/DataDownload),[DataCatalog](/DataCatalog)), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using[variableMeasured](/variableMeasured); for[Observation](/Observation), a[StatisticalVariable](/StatisticalVariable)). Often but not necessarily each[variableMeasured](/variableMeasured)will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of[variableMeasured](/variableMeasured)called[measuredProperty](/measuredProperty)is applicable.The

[measurementTechnique](/measurementTechnique)property helps when extra clarification is needed about how a[measuredProperty](/measuredProperty)was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery.For example, if

[variableMeasured](/variableMeasured)is: molecule concentration,[measurementTechnique](/measurementTechnique)could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the[variableMeasured](/variableMeasured)is "depression rating", the[measurementTechnique](/measurementTechnique)could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several

[variableMeasured](/variableMeasured)properties recorded for some given data object, use a[PropertyValue](/PropertyValue)for each[variableMeasured](/variableMeasured)and attach the corresponding[measurementTechnique](/measurementTechnique). The value can also be from an enumeration, organized as a[MeasurementMethodEnum](/MeasurementMethodEnum).#### Enumeration members

#### Source

[https://github.com/schemaorg/schemaorg/issues/2564](https://github.com/schemaorg/schemaorg/issues/2564)
