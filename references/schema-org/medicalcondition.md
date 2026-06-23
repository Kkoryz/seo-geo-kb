---
title: "MedicalCondition"
source_url: https://schema.org/MedicalCondition
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MedicalCondition

# MedicalCondition

A Schema.org Type

- Canonical URL: https://schema.org/MedicalCondition
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MedicalCondition)

Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[associatedAnatomy](/associatedAnatomy)

[AnatomicalStructure](/AnatomicalStructure)or[AnatomicalSystem](/AnatomicalSystem)or[SuperficialAnatomy](/SuperficialAnatomy)```
```[cause](/cause)

[MedicalCause](/MedicalCause)Inverse property:

[causeOf](/causeOf)```
```[differentialDiagnosis](/differentialDiagnosis)

[DDxElement](/DDxElement)```
```[drug](/drug)

[Drug](/Drug)```
```[epidemiology](/epidemiology)

[Text](/Text)```
```[expectedPrognosis](/expectedPrognosis)

[Text](/Text)```
```[naturalProgression](/naturalProgression)

[Text](/Text)```
```[pathophysiology](/pathophysiology)

[Text](/Text)```
```[possibleComplication](/possibleComplication)

[Text](/Text)```
```[possibleTreatment](/possibleTreatment)

[Drug](/Drug)or[DrugClass](/DrugClass)or[LifestyleModification](/LifestyleModification)or[MedicalTherapy](/MedicalTherapy)```
```[primaryPrevention](/primaryPrevention)

[MedicalTherapy](/MedicalTherapy)```
```[riskFactor](/riskFactor)

[MedicalRiskFactor](/MedicalRiskFactor)```
```[secondaryPrevention](/secondaryPrevention)

[Drug](/Drug)or[DrugClass](/DrugClass)or[LifestyleModification](/LifestyleModification)or[MedicalTherapy](/MedicalTherapy)```
```[signOrSymptom](/signOrSymptom)

[MedicalSignOrSymptom](/MedicalSignOrSymptom)```
```[stage](/stage)

[MedicalConditionStage](/MedicalConditionStage)```
```[status](/status)

[EventStatusType](/EventStatusType)or[MedicalStudyStatus](/MedicalStudyStatus)or[Text](/Text)```
```[typicalTest](/typicalTest)

[MedicalTest](/MedicalTest)[MedicalEntity](/MedicalEntity)

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

[MedicalCondition](/MedicalCondition)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BioChemEntity](/BioChemEntity)[diagnosis](/diagnosis)

[DDxElement](/DDxElement)or[Patient](/Patient)[healthCondition](/healthCondition)

[MedicalStudy](/MedicalStudy)or[Patient](/Patient)or[PeopleAudience](/PeopleAudience)[relatedCondition](/relatedCondition)

[AnatomicalStructure](/AnatomicalStructure)or[AnatomicalSystem](/AnatomicalSystem)or[SuperficialAnatomy](/SuperficialAnatomy)[usedToDiagnose](/usedToDiagnose)

[MedicalTest](/MedicalTest)#### More specific Types

### Examples

[Example 1](#eg-0223)

Copied

Example notes or example HTML without markup.

<h1>Stable angina (angina pectoris)</h1> Stable angina is a medical condition that affects the heart. The most common causes are atherosclerosis and spasms of the epicardial artery. Typical symptoms include: <ul> <li>chest discomfort</li> <li>feeling of tightness, heaviness, or pain in the chest</li> </ul> Both stable angina and a heart attack result in chest pain, but a heart attack will have chest pain lasting at least 10 minutes at rest, repeated episodes of chest pain at rest lasting 5 or more minutes, or an accelerating pattern of chest discomfort (episodes that are more frequent, severe, longer in duration, and precipitated by minimal exertion). <br> Risk factors for stable angina include: <ul> <li>Age</li> <li>Gender</li> <li>Systolic blood pressure</li> <li>Smoking</li> <li>Total cholesterol and/or cholesterol:HDL ratio</li> <li>Coronary artery disease</li> </ul> The initial treatment for stable angina is usually drug therapy with aspirin, beta blockers, ACE inhibitors, and/or nitroglycerine. Future episodes of stable angina can sometimes be prevented by stopping smoking, weight management, and increased physical activity.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/MedicalCondition"> <h1><span itemprop="name">Stable angina</span> (<span itemprop="alternateName">angina pectoris</span>)</h1> <span itemprop="code" itemscope itemtype="https://schema.org/MedicalCode"> <meta itemprop="code" content="413"/> <meta itemprop="codingSystem" content="ICD-9"/> </span> Stable angina is a medical condition that affects the <span itemprop="associatedAnatomy" itemscope itemtype="https://schema.org/AnatomicalStructure"> <span itemprop="name">heart</span> </span>. The most common causes are <span itemprop="cause" itemscope itemtype="https://schema.org/MedicalCause"> <span itemprop="name">atherosclerosis</span> </span> and <span itemprop="cause" itemscope itemtype="https://schema.org/MedicalCause"> <span itemprop="name">spasms of the epicardial artery</span> </span>. Typical symptoms include: <ul> <li><span itemprop="signOrSymptom" itemscope itemtype="https://schema.org/MedicalSymptom"> <span itemprop="name">chest discomfort</span> </span> </li> <li><span itemprop="signOrSymptom" itemscope itemtype="https://schema.org/MedicalSymptom"> <span itemprop="name">feeling of tightness, heaviness, or pain in the chest</span> </span> </li> </ul> Both stable angina and a <span itemprop="differentialDiagnosis" itemscope itemtype="https://schema.org/DDxElement"> <span itemprop="diagnosis" itemscope itemtype="https://schema.org/MedicalCondition"> <span itemprop="name">heart attack</span> </span> result in chest pain, but a heart attack will have <span itemprop="distinguishingSign" itemscope itemtype="https://schema.org/MedicalSymptom"> <span itemprop="name">chest pain lasting at least 10 minutes at rest</span> </span>, <span itemprop="distinguishingSign" itemscope itemtype="https://schema.org/MedicalSymptom"> <span itemprop="name">repeated episodes of chest pain at rest lasting 5 or more minutes </span> </span>, or <span itemprop="distinguishingSign" itemscope itemtype="https://schema.org/MedicalSymptom"> <span itemprop="name">an accelerating pattern of chest discomfort (episodes that are more frequent, severe, longer in duration, and precipitated by minimal exertion) </span> </span> </span>. <br> Risk factors for stable angina include: <ul> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Age</span> </span></li> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Gender</span> </span></li> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Systolic blood pressure</span> </span></li> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Smoking</span> </span></li> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Total cholesterol and/or cholesterol:HDL ratio</span> </span></li> <li><span itemprop="riskFactor" itemscope itemtype="https://schema.org/MedicalRiskFactor"> <span itemprop="name">Coronary artery disease</span> </span></li> </ul> The initial treatment for stable angina is usually drug therapy with <span itemprop="possibleTreatment" itemscope itemtype="https://schema.org/Drug"> <span itemprop="name">aspirin</span> </span>, <span itemprop="possibleTreatment" itemscope itemtype="https://schema.org/DrugClass"> <span itemprop="name">beta blockers</span> </span>, <span itemprop="possibleTreatment" itemscope itemtype="https://schema.org/DrugClass"> <span itemprop="name">ACE inhibitors</span> </span>, and/or <span itemprop="possibleTreatment" itemscope itemtype="https://schema.org/Drug"> <span itemprop="name">nitroglycerine</span> </span>, Future episodes of stable angina can sometimes be prevented by <span itemprop="secondaryPrevention" itemscope itemtype="https://schema.org/LifestyleModification"> <span itemprop="name">stopping smoking</span> </span>, <span itemprop="secondaryPrevention" itemscope itemtype="https://schema.org/LifestyleModification"> <span itemprop="name">weight management</span> </span>, and <span itemprop="secondaryPrevention" itemscope itemtype="https://schema.org/LifestyleModification"> <span itemprop="name">increased physical activity</span> </span>. </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="MedicalCondition"> <h1><span property="name">Stable angina</span> (<span property="alternateName">angina pectoris</span>)</h1> <span property="code" typeof="MedicalCode"> <meta property="code" content="413"/> <meta property="codingSystem" content="ICD-9"/> </span> Stable angina is a medical condition that affects the <span property="associatedAnatomy" typeof="AnatomicalStructure"> <span property="name">heart</span> </span>. The most common causes are <span property="cause" typeof="MedicalCause"> <span property="name">atherosclerosis</span> </span> and <span property="cause" typeof="MedicalCause"> <span property="name">spasms of the epicardial artery</span> </span>. Typical symptoms include: <ul> <li><span property="signOrSymptom" typeof="MedicalSymptom"> <span property="name">chest discomfort</span> </span> </li> <li><span property="signOrSymptom" typeof="MedicalSymptom"> <span property="name">feeling of tightness, heaviness, or pain in the chest</span> </span> </li> </ul> Both stable angina and a <span property="differentialDiagnosis" typeof="DDxElement"> <span property="diagnosis" typeof="MedicalCondition"> <span property="name">heart attack</span> </span> result in chest pain, but a heart attack will have <span property="distinguishingSign" typeof="MedicalSymptom"> <span property="name">chest pain lasting at least 10 minutes at rest</span> </span>, <span property="distinguishingSign" typeof="MedicalSymptom"> <span property="name">repeated episodes of chest pain at rest lasting 5 or more minutes </span> </span>, or <span property="distinguishingSign" typeof="MedicalSymptom"> <span property="name">an accelerating pattern of chest discomfort (episodes that are more frequent, severe, longer in duration, and precipitated by minimal exertion) </span> </span> </span>. <br> Risk factors for stable angina include: <ul> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Age</span> </span></li> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Gender</span> </span></li> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Systolic blood pressure</span> </span></li> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Smoking</span> </span></li> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Total cholesterol and/or cholesterol:HDL ratio</span> </span></li> <li><span property="riskFactor" typeof="MedicalRiskFactor"> <span property="name">Coronary artery disease</span> </span></li> </ul> The initial treatment for stable angina is usually drug therapy with <span property="possibleTreatment" typeof="Drug"> <span property="name">aspirin</span> </span>, <span property="possibleTreatment" typeof="DrugClass"> <span property="name">beta blockers</span> </span>, <span property="possibleTreatment" typeof="DrugClass"> <span property="name">ACE inhibitors</span> </span>, and/or <span property="possibleTreatment" typeof="Drug"> <span property="name">nitroglycerine</span> </span>, Future episodes of stable angina can sometimes be prevented by <span property="secondaryPrevention" typeof="LifestyleModification"> <span property="name">stopping smoking</span> </span>, <span property="secondaryPrevention" typeof="LifestyleModification"> <span property="name">weight management</span> </span>, and <span property="secondaryPrevention" typeof="LifestyleModification"> <span property="name">increased physical activity</span> </span>. </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MedicalCondition", "alternateName": "angina pectoris", "associatedAnatomy": { "@type": "AnatomicalStructure", "name": "heart" }, "cause": [ { "@type": "MedicalCause", "name": "atherosclerosis" }, { "@type": "MedicalCause", "name": "spasms of the epicardial artery" } ], "code": { "@type": "MedicalCode", "code": "413", "codingSystem": "ICD-9" }, "differentialDiagnosis": { "@type": "DDxElement", "diagnosis": { "@type": "MedicalCondition", "name": "heart attack" }, "distinguishingSign": [ { "@type": "MedicalSymptom", "name": "chest pain lasting at least 10 minutes at rest" }, { "@type": "MedicalSymptom", "name": "repeated episodes of chest pain at rest lasting 5 or more minutes" }, { "@type": "MedicalSymptom", "name": "an accelerating pattern of chest discomfort (episodes that are more frequent, severe, longer in duration, and precipitated by minimal exertion)" } ] }, "name": "Stable angina", "possibleTreatment": [ { "@type": "Drug", "name": "aspirin" }, { "@type": "DrugClass", "name": "beta blockers" }, { "@type": "DrugClass", "name": "ACE inhibitors" }, { "@type": "Drug", "name": "nitroglycerine" } ], "riskFactor": [ { "@type": "MedicalRiskFactor", "name": "Age" }, { "@type": "MedicalRiskFactor", "name": "Gender" }, { "@type": "MedicalRiskFactor", "name": "Systolic blood pressure" }, { "@type": "MedicalRiskFactor", "name": "Smoking" }, { "@type": "MedicalRiskFactor", "name": "Total cholesterol and/or cholesterol:HDL ratio" }, { "@type": "MedicalRiskFactor", "name": "Coronary artery disease" } ], "secondaryPrevention": [ { "@type": "LifestyleModification", "name": "stopping smoking" }, { "@type": "LifestyleModification", "name": "weight management" }, { "@type": "LifestyleModification", "name": "increased physical activity" } ], "signOrSymptom": [ { "@type": "MedicalSymptom", "name": "chest discomfort" }, { "@type": "MedicalSymptom", "name": "feeling of tightness, heaviness, or pain in the chest" } ] } </script>

Structured representation of the JSON-LD example.
