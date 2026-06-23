---
title: "MedicalGuideline"
source_url: https://schema.org/MedicalGuideline
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MedicalGuideline

# MedicalGuideline

A Schema.org Type

- Canonical URL: https://schema.org/MedicalGuideline
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MedicalGuideline)

Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.

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

[URL](/URL)Instances of

[MedicalGuideline](/MedicalGuideline)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MedicalEntity](/MedicalEntity)#### More specific Types

### Examples

[Example 1](#eg-0222)

Copied

Example notes or example HTML without markup.

<h1>New guidelines for metformin and diabetes mellitus</h1> <p>Dr. John Smith <br>Medical University <br>2012-03-24</p> <p><b>Abstract:</b> We review clinical evidence related to the use of metformin for treatment of type-2 diabetes mellitus and provide new clinical guideline recommendations.</p> <p><b>MeSH subject headings:</b> Metformin; Diabetes Mellitus, Type 2</p> ... <h3>Guidelines</h3> Recommendation: we recommend monotherapy with metformin as an initial pharmacologic therapy to treat most patients with type 2 diabetes (Grade: strong recommendation; high-quality evidence).

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/MedicalScholarlyArticle"> <link itemprop="audience" href="https://schema.org/Clinician"/> <meta itemprop="publicationType" content="Meta-Analysis"/> <h1><span itemprop="name">New guidelines for metformin and diabetes mellitus</span></h1> <p><span itemprop="author" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Dr. John Smith</span> <br><span itemprop="affiliation">Medical University</span> </span> <br><span itemprop="datePublished">2012-03-24</span></p> <p><b>Abstract:</b> <span itemprop="description">We review clinical evidence related to the use of metformin for treatment of type-2 diabetes mellitus and provide new clinical guideline recommendations.</span></p> <p><b>MeSH subject headings:</b> <span itemprop="about" itemscope itemtype="https://schema.org/Drug"> <span itemprop="name">Metformin</span> <span itemprop="code" itemscope itemtype="https://schema.org/MedicalCode" itemid="http://www.ncbi.nlm.nih.gov/mesh/D02.078.370.141.450"> <!-- Note: use of itemid is not mandatory, but recommended when an external enumeration is available --> <meta itemprop="code" content="D02.078.370.141.450"/> <meta itemprop="codingSystem" content="MeSH"/> </span> </span>; <span itemprop="about" itemscope itemtype="https://schema.org/MedicalCondition"> <span itemprop="name">Diabetes Mellitus, Type 2</span> <span itemprop="code" itemscope itemtype="https://schema.org/MedicalCode" itemid="http://www.ncbi.nlm.nih.gov/mesh/C18.452.394.750.149"> <!-- Note: use of itemid is not mandatory, but recommended when an external enumeration is available --> <meta itemprop="code" content="C18.452.394.750.149"/> <meta itemprop="codingSystem" content="MeSH"/> </span> </span></p> ... <h3>Guidelines</h3> <span itemscope itemtype="https://schema.org/MedicalGuidelineRecommendation"> Recommendation: we recommend monotherapy with <span itemprop="guidelineSubject">metformin</span> as an initial pharmacologic therapy to treat most patients with <span itemprop="guidelineSubject">type 2 diabetes</span> (Grade: <span itemprop="recommendationStrength">strong recommendation</span>; <a itemprop="evidenceLevel" href="https://schema.org/EvidenceLevelA">high-quality evidence</a>). </span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="MedicalScholarlyArticle"> <link property="audience" href="https://schema.org/Clinician"/> <meta property="publicationType" content="Meta-Analysis"/> <h1><span property="name">New guidelines for metformin and diabetes mellitus</span></h1> <p><span property="author" typeof="Person"> <span property="name">Dr. John Smith</span> <br><span property="affiliation">Medical University</span> </span> <br><span property="datePublished">2012-03-24</span></p> <p><b>Abstract:</b> <span property="description">We review clinical evidence related to the use of metformin for treatment of type-2 diabetes mellitus and provide new clinical guideline recommendations.</span></p> <p><b>MeSH subject headings:</b> <span property="about" typeof="Drug"> <span property="name">Metformin</span> <span property="code" typeof="MedicalCode" resource="http://www.ncbi.nlm.nih.gov/mesh/D02.078.370.141.450"> <!-- Note: use of itemid is not mandatory, but recommended when an external enumeration is available --> <meta property="code" content="D02.078.370.141.450"/> <meta property="codingSystem" content="MeSH"/> </span> </span>; <span property="about" typeof="MedicalCondition"> <span property="name">Diabetes Mellitus, Type 2</span> <span property="code" typeof="MedicalCode" resource="http://www.ncbi.nlm.nih.gov/mesh/C18.452.394.750.149"> <!-- Note: use of itemid is not mandatory, but recommended when an external enumeration is available --> <meta property="code" content="C18.452.394.750.149"/> <meta property="codingSystem" content="MeSH"/> </span> </span> </p> ... <h3>Guidelines</h3> <span typeof="MedicalGuidelineRecommendation"> Recommendation: we recommend monotherapy with <span property="guidelineSubject">metformin</span> as an initial pharmacologic therapy to treat most patients with <span property="guidelineSubject">type 2 diabetes</span> (Grade: <span property="recommendationStrength">strong recommendation</span>; <a property="evidenceLevel" href="https://schema.org/EvidenceLevelA">high-quality evidence</a>). </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MedicalScholarlyArticle", "about": [ { "@type": "Drug", "code": { "@id": "http://www.ncbi.nlm.nih.gov/mesh/D02.078.370.141.450", "@type": "MedicalCode", "code": "D02.078.370.141.450", "codingSystem": "MeSH" }, "name": "Metformin" }, { "@type": "MedicalCondition", "name": "Diabetes Mellitus, Type 2" } ], "audience": "https://schema.org/Clinician", "author": { "@type": "Person", "affiliation": "Medical University", "name": "Dr. John Smith" }, "datePublished": "2012-03-24", "description": "We review clinical evidence related to the use of metformin for treatment of type-2 diabetes mellitus and provide new clinical guideline recommendations.", "name": "New guidelines for metformin and diabetes mellitus", "publicationType": "Meta-Analysis" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0224)

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
