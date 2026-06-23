---
title: "MedicalGuidelineContraindication"
source_url: https://schema.org/MedicalGuidelineContraindication
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MedicalGuidelineContraindication

# MedicalGuidelineContraindication

A Schema.org Type

- Canonical URL: https://schema.org/MedicalGuidelineContraindication
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MedicalGuidelineContraindication)

A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[evidenceLevel](/evidenceLevel)

[MedicalEvidenceLevel](/MedicalEvidenceLevel)```
```[evidenceOrigin](/evidenceOrigin)

[Text](/Text)```
```[guidelineDate](/guidelineDate)

[Date](/Date)```
```[guidelineSubject](/guidelineSubject)

[MedicalEntity](/MedicalEntity)[MedicalEntity](/MedicalEntity)

```
```[code](/code)

[MedicalCode](/MedicalCode)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[guideline](/guideline)

[MedicalGuideline](/MedicalGuideline)```
```[legalStatus](/legalStatus)

[DrugLegalStatus](/DrugLegalStatus)or[MedicalEnumeration](/MedicalEnumeration)or[Text](/Text)```
```[medicineSystem](/medicineSystem)

[MedicineSystem](/MedicineSystem)```
```[recognizingAuthority](/recognizingAuthority)

[Organization](/Organization)```
```[relevantSpecialty](/relevantSpecialty)

[MedicalSpecialty](/MedicalSpecialty)```
```[study](/study)

[MedicalStudy](/MedicalStudy)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0224)

Copied

Example notes or example HTML without markup.

<h1>Guidelines</h1> <ul> <li>Recommendation: NewvoDrug is indicated for initial treatment of cardiac failure for all adult patients. (Strong recommendation; Class I, based on multiple randomized clinical trials)</li> <li>Contraindication: cardiac failure should never be treated with appendectomy in adults. (Class III, standard of care)</li> </ul>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<h1>Guidelines</h1> <ul> <li>Recommendation: <span itemscope itemtype="https://schema.org/MedicalGuidelineRecommendation"> <span itemprop="guidelineSubject" itemscope itemtype="https://schema.org/Drug"> <span itemprop="name">NewvoDrug</span> </span> is indicated for initial treatment of <span itemprop="guidelineSubject" itemscope itemtype="https://schema.org/MedicalCondition"> <span itemprop="name">cardiac failure</span> </span> for all adult patients. (<span itemprop="recommendationStrength">Strong recommendation</span>; <a itemprop="evidenceLevel" href="https://schema.org/EvidenceLevelA">Class I</a>, based on <span itemprop="evidenceOrigin">multiple randomized clinical trials</span>) </span> </li> <li>Contraindication: <span itemscope itemtype="https://schema.org/MedicalGuidelineContraindication"> <span itemprop="guidelineSubject" itemscope itemtype="https://schema.org/MedicalCondition"> <span itemprop="name">cardiac failure</span></span> should never be treated with <span itemprop="guidelineSubject" itemscope itemtype="https://schema.org/TherapeuticProcedure"> <span itemprop="name">appendectomy</span></span> in adults. (Class III, <link itemprop="evidenceLevel" href="https://schema.org/EvidenceLevelC"/> <span itemprop="evidenceOrigin">standard of care</span>) </span></li> </ul>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<h1>Guidelines</h1> <ul> <li>Recommendation: <span typeof="MedicalGuidelineRecommendation"> <span property="guidelineSubject" typeof="Drug"> <span property="name">NewvoDrug</span> </span> is indicated for initial treatment of <span property="guidelineSubject" typeof="MedicalCondition"> <span property="name">cardiac failure</span> </span> for all adult patients. (<span property="recommendationStrength">Strong recommendation</span>; <a property="evidenceLevel" href="https://schema.org/EvidenceLevelA"> Class I</a>, based on <span property="evidenceOrigin">multiple randomized clinical trials</span>) </span> </li> <li>Contraindication: <span typeof="MedicalGuidelineContraindication"> <span property="guidelineSubject" typeof="MedicalCondition"> <span property="name">cardiac failure</span></span> should never be treated with <span property="guidelineSubject" typeof="TherapeuticProcedure"> <span property="name">appendectomy</span></span> in adults. (Class III, <link property="evidenceLevel" href="https://schema.org/EvidenceLevelC"/> <span property="evidenceOrigin">standard of care</span>) </span></li> </ul>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@type": "MedicalGuidelineRecommendation", "evidenceLevel": "https://schema.org/EvidenceLevelA", "evidenceOrigin": "multiple randomized clinical trials", "recommendationStrength": "Strong recommendation", "guidelineSubject": [ { "@type": "Drug", "name": "NewvoDrug" }, { "@type": "MedicalCondition", "name": "cardiac failure" } ] }, { "@type": "MedicalGuidelineContraindication", "evidenceLevel": "https://schema.org/EvidenceLevelC", "evidenceOrigin": "standard of care", "guidelineSubject": [ { "@type": "MedicalCondition", "name": "cardiac failure" }, { "@type": "TherapeuticProcedure", "name": "appendectomy" } ] } ] } </script>

Structured representation of the JSON-LD example.
