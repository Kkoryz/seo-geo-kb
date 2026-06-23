---
title: "measurementTechnique"
source_url: https://schema.org/measurementTechnique
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# measurementTechnique

# measurementTechnique

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/measurementTechnique
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+measurementTechnique)

A technique, method or technology used in an


The


For example, if


If there are several

[Observation](/Observation),[StatisticalVariable](/StatisticalVariable)or[Dataset](/Dataset)(or[DataDownload](/DataDownload),[DataCatalog](/DataCatalog)), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using[variableMeasured](/variableMeasured); for[Observation](/Observation), a[StatisticalVariable](/StatisticalVariable)). Often but not necessarily each[variableMeasured](/variableMeasured)will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of[variableMeasured](/variableMeasured)called[measuredProperty](/measuredProperty)is applicable.The

[measurementTechnique](/measurementTechnique)property helps when extra clarification is needed about how a[measuredProperty](/measuredProperty)was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery.For example, if

[variableMeasured](/variableMeasured)is: molecule concentration,[measurementTechnique](/measurementTechnique)could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the[variableMeasured](/variableMeasured)is "depression rating", the[measurementTechnique](/measurementTechnique)could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several

[variableMeasured](/variableMeasured)properties recorded for some given data object, use a[PropertyValue](/PropertyValue)for each[variableMeasured](/variableMeasured)and attach the corresponding[measurementTechnique](/measurementTechnique). The value can also be from an enumeration, organized as a[MeasurementMethodEnum](/MeasurementMethodEnum).### Values expected to be one of these types


### Used on these types


#### Sub-properties

#### Source

[https://github.com/schemaorg/schemaorg/issues/1425](https://github.com/schemaorg/schemaorg/issues/1425)
