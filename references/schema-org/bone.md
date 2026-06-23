---
title: "Bone"
source_url: https://schema.org/Bone
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Bone

| Property | Expected Type | Description |
Properties from
[AnatomicalStructure](/AnatomicalStructure) |
```
```[associatedPathophysiology](/associatedPathophysiology) |
[Text](/Text) |
If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
|
```
```[bodyLocation](/bodyLocation) |
[Text](/Text) |
Location in the body of the anatomical structure.
|
```
```[connectedTo](/connectedTo) |
[AnatomicalStructure](/AnatomicalStructure) |
Other anatomical structures to which this structure is connected.
|
```
```[diagram](/diagram) |
[ImageObject](/ImageObject) |
An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.
|
```
```[partOfSystem](/partOfSystem) |
[AnatomicalSystem](/AnatomicalSystem) |
The anatomical or organ system that this structure is part of.
|
```
```[relatedCondition](/relatedCondition) |
[MedicalCondition](/MedicalCondition) |
A medical condition associated with this anatomy.
|
```
```[relatedTherapy](/relatedTherapy) |
[MedicalTherapy](/MedicalTherapy) |
A medical therapy related to this anatomy.
|
```
```[subStructure](/subStructure) |
[AnatomicalStructure](/AnatomicalStructure) |
Component (sub-)structure(s) that comprise this anatomical structure.
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
