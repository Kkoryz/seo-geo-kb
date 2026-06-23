---
title: "PhysicalTherapy"
source_url: https://schema.org/PhysicalTherapy
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PhysicalTherapy

| Property | Expected Type | Description |
Properties from
[MedicalTherapy](/MedicalTherapy) |
```
```[contraindication](/contraindication) |
[MedicalContraindication](/MedicalContraindication) or
[Text](/Text) |
A contraindication for this therapy.
|
```
```[duplicateTherapy](/duplicateTherapy) |
[MedicalTherapy](/MedicalTherapy) |
A therapy that duplicates or overlaps this one.
|
```
```[seriousAdverseOutcome](/seriousAdverseOutcome) |
[MedicalEntity](/MedicalEntity) |
A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
|
Properties from
[TherapeuticProcedure](/TherapeuticProcedure) |
```
```[adverseOutcome](/adverseOutcome) |
[MedicalEntity](/MedicalEntity) |
A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
|
```
```[doseSchedule](/doseSchedule) |
[DoseSchedule](/DoseSchedule) |
A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
|
```
```[drug](/drug) |
[Drug](/Drug) |
Specifying a drug or medicine used in a medication procedure.
|
Properties from
[MedicalProcedure](/MedicalProcedure) |
```
```[bodyLocation](/bodyLocation) |
[Text](/Text) |
Location in the body of the anatomical structure.
|
```
```[followup](/followup) |
[Text](/Text) |
Typical or recommended followup care after the procedure is performed.
|
```
```[howPerformed](/howPerformed) |
[Text](/Text) |
How the procedure is performed.
|
```
```[preparation](/preparation) |
[MedicalEntity](/MedicalEntity) or
[Text](/Text) |
Typical preparation that a patient must undergo before having the procedure performed.
|
```
```[procedureType](/procedureType) |
[MedicalProcedureType](/MedicalProcedureType) |
The type of procedure, for example Surgical, Noninvasive, or Percutaneous.
|
```
```[status](/status) |
[EventStatusType](/EventStatusType) or
[MedicalStudyStatus](/MedicalStudyStatus) or
[Text](/Text) |
The status of the study (enumerated).
|
Properties from
[MedicalEntity](/MedicalEntity) |
```
```[code](/code) |
[MedicalCode](/MedicalCode) |
A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
|
```
```[funding](/funding) |
[Grant](/Grant) |
A [Grant](/Grant) that directly or indirectly provide funding or sponsorship for this item. See also [ownershipFundingInfo](/ownershipFundingInfo).
Inverse property:
[fundedItem](/fundedItem)
|
```
```[guideline](/guideline) |
[MedicalGuideline](/MedicalGuideline) |
A medical guideline related to this entity.
|
```
```[legalStatus](/legalStatus) |
[DrugLegalStatus](/DrugLegalStatus) or
[MedicalEnumeration](/MedicalEnumeration) or
[Text](/Text) |
The drug or supplement's legal status, including any controlled substance schedules that apply.
|
```
```[medicineSystem](/medicineSystem) |
[MedicineSystem](/MedicineSystem) |
The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
|
```
```[recognizingAuthority](/recognizingAuthority) |
[Organization](/Organization) |
If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
|
```
```[relevantSpecialty](/relevantSpecialty) |
[MedicalSpecialty](/MedicalSpecialty) |
If applicable, a medical specialty in which this entity is relevant.
|
```
```[study](/study) |
[MedicalStudy](/MedicalStudy) |
A medical study or trial related to this entity.
|
Properties from
[Thing](/Thing) |
```
```[additionalType](/additionalType) |
[Text](/Text) or
[URL](/URL) |
An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the
use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org [style guide](https://schema.org/docs/styleguide.html).
|
```
```[alternateName](/alternateName) |
[Text](/Text) |
An alias for the item.
|
```
```[description](/description) |
[Text](/Text) or
[TextObject](/TextObject) |
A description of the item.
|
```
```[disambiguatingDescription](/disambiguatingDescription) |
[Text](/Text) |
A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
|
```
```[identifier](/identifier) |
[PropertyValue](/PropertyValue) or
[Text](/Text) or
[URL](/URL) |
The identifier property represents any kind of identifier for any kind of [Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
|
```
```[image](/image) |
[ImageObject](/ImageObject) or
[URL](/URL) |
An image of the item. This can be a [URL](/URL) or a fully described [ImageObject](/ImageObject).
|
```
```[mainEntityOfPage](/mainEntityOfPage) |
[CreativeWork](/CreativeWork) or
[URL](/URL) |
Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
Inverse property:
[mainEntity](/mainEntity)
|
```
```[name](/name) |
[Text](/Text) |
The name of the item.
|
```
```[owner](/owner) |
[Organization](/Organization) or
[Person](/Person) |
A person or organization who owns this Thing.
Inverse property:
[owns](/owns)
|
```
```[potentialAction](/potentialAction) |
[Action](/Action) |
Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
|
```
```[sameAs](/sameAs) |
[URL](/URL) |
URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
|
```
```[subjectOf](/subjectOf) |
[CreativeWork](/CreativeWork) or
[Event](/Event) |
A CreativeWork or Event about this Thing.
Inverse property:
[about](/about)
|
```
```[url](/url) |
[URL](/URL) |
URL of the item.
|
