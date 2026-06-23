---
title: "HealthPlanCostSharingSpecification"
source_url: https://schema.org/HealthPlanCostSharingSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# HealthPlanCostSharingSpecification

# HealthPlanCostSharingSpecification

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/HealthPlanCostSharingSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+HealthPlanCostSharingSpecification)

A description of costs to the patient under a given network or formulary.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[healthPlanCoinsuranceOption](/healthPlanCoinsuranceOption)

[Text](/Text)```
```[healthPlanCoinsuranceRate](/healthPlanCoinsuranceRate)

[Number](/Number)```
```[healthPlanCopay](/healthPlanCopay)

[PriceSpecification](/PriceSpecification)```
```[healthPlanCopayOption](/healthPlanCopayOption)

[Text](/Text)```
```[healthPlanPharmacyCategory](/healthPlanPharmacyCategory)

[Text](/Text)[Thing](/Thing)

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

[HealthPlanCostSharingSpecification](/HealthPlanCostSharingSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[HealthPlanFormulary](/HealthPlanFormulary)or[HealthPlanNetwork](/HealthPlanNetwork)#### Source

[https://github.com/schemaorg/schemaorg/issues/1062](https://github.com/schemaorg/schemaorg/issues/1062)

### Examples

[Example 1](#eg-0229)

Copied

Example notes or example HTML without markup.

See JSON example. Background, https://docs.google.com/document/d/1LNew5OEon4uir2D5Zzp0AkUPA7c9nO8reJ_M1pOy-3s/edit#

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "http://health-lifesci.schema.org/", "@type": "HealthInsurancePlan", "healthPlanId": "12345XX9876543", "name": "Sample Gold Health Plan", "benefitsSummaryUrl": "http://url/to/summary/benefits/coverage", "healthPlanMarketingUrl": "http://url/to/health/plan/information", "contactPoint": { "@type": "ContactPoint", "email": "email@address.com" }, "healthPlanDrugTier": ["http://healthplan.schema.org/PreferredNetwork", "http://healthplan.schema.org/NonPreferredNetwork"], "includesHealthPlanFormulary": [ { "@type": "HealthPlanFormulary", "healthPlanDrugTier": "http://healthplan.schema.org/DrugTierGeneric", "offersPrescriptionByMail": true, "healthPlanCostSharing": [ { "@type": "HealthPlanCostSharingSpecification", "healthPlanPharmacyCategory": "1-MONTH-IN-RETAIL", "healthPlanCopay": { "@type": "PriceSpecification", "price": 20, "priceCurrency": "USD" }, "healthPlanCopayOption": "http://healthplan.schema.org/HealthPlanCopayAfterDeductable", "healthPlanCoinsuranceRate": 0.1, "healthPlanCoinsuranceOption": "http://healthplan.schema.org/HealthPlanCoinsuranceBeforeDeductable" }, { "@type": "HealthPlanCostSharingSpecification", "healthPlanPharmacyCategory": "1-MONTH-IN-MAIL", "healthPlanCopay": { "@type": "PriceSpecification", "price": 0, "priceCurrency": "USD" }, "healthPlanCopayOption": "http://healthplan.schema.org/HealthPlanCoPayNoCharge", "healthPlanCoinsuranceRate": 0.2, "healthPlanCoinsuranceOption": "http://healthplan.schema.org/HealthPlanCoinsuranceNone" } ] }, { "@type": "HealthPlanFormulary", "healthPlanDrugTier": "http://healthplan.schema.org/DrugTierBrand", "offersPrescriptionByMail": true, "healthPlanCostSharing": [ { "@type": "HealthPlanCostSharingSpecification", "healthPlanPharmacyCategory": "1-MONTH-IN-RETAIL", "healthPlanCopay": { "@type": "PriceSpecification", "price": 15, "priceCurrency": "USD" }, "healthPlanCopayOption": "http://healthplan.schema.org/HealthPlanCopayNone", "healthPlanCoinsuranceRate": 0, "healthPlanCoinsuranceOption": "http://healthplan.schema.org/HealthPlanCoinsuranceNone" }, { "@type": "HealthPlanCostSharingSpecification", "healthPlanPharmacyCategory": "1-MONTH-IN-MAIL", "healthPlanCopay": { "@type": "PriceSpecification", "price": 20, "priceCurrency": "USD" }, "healthPlanCopayOption": "http://healthplan.schema.org/HealthPlanCopayAfterDeductible", "healthPlanCoinsuranceRate": 0.1, "healthPlanCoinsuranceOption": "http://healthplan.schema.org/HealthPlanCoinsuranceBeforeDeductible" } ] } ] } </script>

Structured representation of the JSON-LD example.
