---
title: "Drug"
source_url: https://schema.org/Drug
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Drug

# Drug

A Schema.org Type

- Canonical URL: https://schema.org/Drug
- Equivalent Class: snomed:410942007
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Drug)

A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism. Here the term drug is used interchangeably with the term medicine although clinical knowledge makes a clear difference between them.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[activeIngredient](/activeIngredient)

[Text](/Text)```
```[administrationRoute](/administrationRoute)

[Text](/Text)```
```[alcoholWarning](/alcoholWarning)

[Text](/Text)```
```[availableStrength](/availableStrength)

[DrugStrength](/DrugStrength)```
```[breastfeedingWarning](/breastfeedingWarning)

[Text](/Text)```
```[clinicalPharmacology](/clinicalPharmacology)

[Text](/Text)[clincalPharmacology](/clincalPharmacology).```
```[dosageForm](/dosageForm)

[Text](/Text)```
```[doseSchedule](/doseSchedule)

[DoseSchedule](/DoseSchedule)```
```[drugClass](/drugClass)

[DrugClass](/DrugClass)```
```[drugUnit](/drugUnit)

[Text](/Text)```
```[foodWarning](/foodWarning)

[Text](/Text)```
```[includedInHealthInsurancePlan](/includedInHealthInsurancePlan)

[HealthInsurancePlan](/HealthInsurancePlan)```
```[interactingDrug](/interactingDrug)

[Drug](/Drug)```
```[isAvailableGenerically](/isAvailableGenerically)

[Boolean](/Boolean)```
```[isProprietary](/isProprietary)

[Boolean](/Boolean)```
```[labelDetails](/labelDetails)

[URL](/URL)```
```[legalStatus](/legalStatus)

[DrugLegalStatus](/DrugLegalStatus)or[MedicalEnumeration](/MedicalEnumeration)or[Text](/Text)```
```[maximumIntake](/maximumIntake)

[MaximumDoseSchedule](/MaximumDoseSchedule)```
```[mechanismOfAction](/mechanismOfAction)

[Text](/Text)```
```[nonProprietaryName](/nonProprietaryName)

[Text](/Text)```
```[overdosage](/overdosage)

[Text](/Text)```
```[pregnancyCategory](/pregnancyCategory)

[DrugPregnancyCategory](/DrugPregnancyCategory)```
```[pregnancyWarning](/pregnancyWarning)

[Text](/Text)```
```[prescribingInfo](/prescribingInfo)

[URL](/URL)```
```[prescriptionStatus](/prescriptionStatus)

[DrugPrescriptionStatus](/DrugPrescriptionStatus)or[Text](/Text)```
```[proprietaryName](/proprietaryName)

[Text](/Text)```
```[relatedDrug](/relatedDrug)

[Drug](/Drug)```
```[rxcui](/rxcui)

[Text](/Text)```
```[warning](/warning)

[Text](/Text)or[URL](/URL)[Product](/Product)

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[asin](/asin)

[Text](/Text)or[URL](/URL)[Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.

```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[color](/color)

[Text](/Text)```
```[colorSwatch](/colorSwatch)

[ImageObject](/ImageObject)or[URL](/URL)[Product](/Product). Should match the textual description specified in the[color](/color)property. This can be a URL or a fully described ImageObject.```
```[countryOfAssembly](/countryOfAssembly)

[Text](/Text)```
```[countryOfLastProcessing](/countryOfLastProcessing)

[Text](/Text)[Product](/Product)) was last processed and tested before importation.```
```[countryOfOrigin](/countryOfOrigin)

[Country](/Country)In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

```
```[depth](/depth)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[displayLocation](/displayLocation)

[Place](/Place)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[gtin](/gtin)

[Text](/Text)or[URL](/URL)[GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.A correct

[gtin](/gtin)value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a[valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)and meet the other rules for valid GTINs. See also[GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)and[Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number)for more details. Left-padding of the gtin values is not required or encouraged. The[gtin](/gtin)property generalizes the earlier[gtin8](/gtin8),[gtin12](/gtin12),[gtin13](/gtin13), and[gtin14](/gtin14)properties.The GS1

[digital link specifications](https://www.gs1.org/standards/Digital-Link/)expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the[hasGS1DigitalLink](/hasGS1DigitalLink)attribute.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

```
```[gtin12](/gtin12)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin13](/gtin13)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin14](/gtin14)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin8](/gtin8)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[hasAdultConsideration](/hasAdultConsideration)

[AdultOrientedEnumeration](/AdultOrientedEnumeration)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasEnergyConsumptionDetails](/hasEnergyConsumptionDetails)

[EnergyConsumptionDetails](/EnergyConsumptionDetails)```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMeasurement](/hasMeasurement)

[QuantitativeValue](/QuantitativeValue)```
```[hasMerchantReturnPolicy](/hasMerchantReturnPolicy)

[MerchantReturnPolicy](/MerchantReturnPolicy)[hasProductReturnPolicy](/hasProductReturnPolicy).```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[inProductGroupWithID](/inProductGroupWithID)

[Text](/Text)[productGroupID](/productGroupID)for a[ProductGroup](/ProductGroup)that this product[isVariantOf](/isVariantOf).```
```[isAccessoryOrSparePartFor](/isAccessoryOrSparePartFor)

[Product](/Product)```
```[isConsumableFor](/isConsumableFor)

[Product](/Product)```
```[isFamilyFriendly](/isFamilyFriendly)

[Boolean](/Boolean)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[isVariantOf](/isVariantOf)

[ProductGroup](/ProductGroup)or[ProductModel](/ProductModel)[ProductModel](/ProductModel), this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a[ProductGroup](/ProductGroup), the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with[ProductGroup](/ProductGroup), this property can apply to any[Product](/Product)included in the group.Inverse property:

[hasVariant](/hasVariant)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[manufacturer](/manufacturer)

[Organization](/Organization)```
```[material](/material)

[Product](/Product)or[Text](/Text)or[URL](/URL)```
```[mobileUrl](/mobileUrl)

[Text](/Text)[mobileUrl](/mobileUrl)property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on

[Product](/Product)and[Offer](/Offer), rather than[Thing](/Thing). The general trend in web technology is towards[responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established[url](/url)property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all[url](/url)markup to use[mobileUrl](/mobileUrl)for more mobile-oriented pages. The property is intended for the case when items (primarily[Product](/Product)and[Offer](/Offer)) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.```
```[model](/model)

[ProductModel](/ProductModel)or[Text](/Text)```
```[mpn](/mpn)

[Text](/Text)```
```[negativeNotes](/negativeNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[positiveNotes](/positiveNotes)). For symmetryIn the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find[negativeNotes](/negativeNotes)used in this way. Nevertheless for the sake of symmetry,[negativeNotes](/negativeNotes)can be used on[Product](/Product).The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).

```
```[nsn](/nsn)

[Text](/Text)[NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)(nsn) of a[Product](/Product).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[pattern](/pattern)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[positiveNotes](/positiveNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

```
```[productID](/productID)

[Text](/Text)`meta itemprop="productID" content="isbn:123-456-789"`

.
```
```[productionDate](/productionDate)

[Date](/Date)```
```[purchaseDate](/purchaseDate)

[Date](/Date)```
```[releaseDate](/releaseDate)

[Date](/Date)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[size](/size)

[DefinedTerm](/DefinedTerm)or[QuantitativeValue](/QuantitativeValue)or[SizeSpecification](/SizeSpecification)or[Text](/Text)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.```
```[sku](/sku)

[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[weight](/weight)

[Mass](/Mass)or[QuantitativeValue](/QuantitativeValue)```
```[width](/width)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)[Substance](/Substance)

```
```[activeIngredient](/activeIngredient)

[Text](/Text)```
```[maximumIntake](/maximumIntake)

[MaximumDoseSchedule](/MaximumDoseSchedule)[MedicalEntity](/MedicalEntity)

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

[Drug](/Drug)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MedicalTest](/MedicalTest)[drug](/drug)

[DrugClass](/DrugClass)or[MedicalCondition](/MedicalCondition)or[Patient](/Patient)or[TherapeuticProcedure](/TherapeuticProcedure)[interactingDrug](/interactingDrug)

[Drug](/Drug)[possibleTreatment](/possibleTreatment)

[MedicalCondition](/MedicalCondition)or[MedicalSignOrSymptom](/MedicalSignOrSymptom)[relatedDrug](/relatedDrug)

[Drug](/Drug)[secondaryPrevention](/secondaryPrevention)

[MedicalCondition](/MedicalCondition)### Examples

[Example 1](#eg-0481)

Copied

Example notes or example HTML without markup.

<h1>Denyal Forte 10×5mg</h1> Denyal Forte is a brand of Copium manufactured by Rockwell United in the United States. It is recommended for people suffering of cognitive dissonancy. It is available in the US as a non-prescription drug in the form of of a package of 10 5mg tablets. Common side-effects include hallucinations.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org", "@type": "Drug", "name": "Denyal Forte", "nonProprietaryName": "Copium", "activeIngredient": "Fabula excipiens", "drugUnit": "5mg", "isAvailableGenerically": true, "isProprietary": true, "dosageForm": "tablet", "prescriptionStatus": "https://schema.org/OTC", "warning": "Known side effects include hallucinations", "identifier": { "@type": "PropertyValue", "name": "NDC", "description": "US National Drug Code", "value": "1111100011" }, "gtin": "00311111000118", "brand": { "@type": "Organization", "name": "Rockwell United" }, "recognizingAuthority": { "@type": "Organization", "name": "FDA", "url": "https://www.fda.gov/" } }

Structured representation of the JSON-LD example.
