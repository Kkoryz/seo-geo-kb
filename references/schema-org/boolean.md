---
title: "Boolean"
source_url: https://schema.org/Boolean
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Boolean

# Boolean

A Schema.org Data Type

- Canonical URL: https://schema.org/Boolean
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Boolean)

Boolean: True or False.

Instances of

[Boolean](/Boolean)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Book](/Book)[acceptsReservations](/acceptsReservations)

[FoodEstablishment](/FoodEstablishment)`Yes`

or `No`

.
[cashBack](/cashBack)

[PaymentCard](/PaymentCard)[contactlessPayment](/contactlessPayment)

[PaymentCard](/PaymentCard)[directApply](/directApply)

[JobPosting](/JobPosting)[url](/url)that is associated with a[JobPosting](/JobPosting)enables direct application for the job, via the posting website. A job posting is considered to have directApply of[True](/True)if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of[False](/False)is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.[doesNotShip](/doesNotShip)

[OfferShippingDetails](/OfferShippingDetails)or[ShippingConditions](/ShippingConditions)or[ShippingRateSettings](/ShippingRateSettings)[shippingDestination](/shippingDestination)is not available.[domiciledMortgage](/domiciledMortgage)

[MortgageLoan](/MortgageLoan)[experienceInPlaceOfEducation](/experienceInPlaceOfEducation)

[JobPosting](/JobPosting)[JobPosting](/JobPosting)will accept experience (as indicated by[OccupationalExperienceRequirements](/OccupationalExperienceRequirements)) in place of its formal educational qualifications (as indicated by[educationRequirements](/educationRequirements)). If true, indicates that satisfying one of these requirements is sufficient.[free](/free)

[PublicationEvent](/PublicationEvent)[hasDriveThroughService](/hasDriveThroughService)

[Place](/Place)[FoodEstablishment](/FoodEstablishment),[CovidTestingFacility](/CovidTestingFacility)) offers a service that can be used by driving through in a car. In the case of[CovidTestingFacility](/CovidTestingFacility)such facilities could potentially help with social distancing from other potentially-infected users.[healthPlanCostSharing](/healthPlanCostSharing)

[HealthPlanFormulary](/HealthPlanFormulary)or[HealthPlanNetwork](/HealthPlanNetwork)[inStoreReturnsOffered](/inStoreReturnsOffered)

[MerchantReturnPolicy](/MerchantReturnPolicy)[returnMethod](/returnMethod)property.)[isAcceptingNewPatients](/isAcceptingNewPatients)

[MedicalOrganization](/MedicalOrganization)[isAccessibleForFree](/isAccessibleForFree)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Place](/Place)[isAvailableGenerically](/isAvailableGenerically)

[Drug](/Drug)[isFamilyFriendly](/isFamilyFriendly)

[CreativeWork](/CreativeWork)or[Offer](/Offer)or[Product](/Product)[isGift](/isGift)

[Order](/Order)[isLiveBroadcast](/isLiveBroadcast)

[BroadcastEvent](/BroadcastEvent)[isProprietary](/isProprietary)

[DietarySupplement](/DietarySupplement)or[Drug](/Drug)[isResizable](/isResizable)

[3DModel](/3DModel)[isUnlabelledFallback](/isUnlabelledFallback)

[DeliveryTimeSettings](/DeliveryTimeSettings)or[ShippingRateSettings](/ShippingRateSettings)[DeliveryTimeSettings](/DeliveryTimeSettings)or[ShippingRateSettings](/ShippingRateSettings)are intended to apply to all[OfferShippingDetails](/OfferShippingDetails)published by the same merchant, when referenced by a[shippingSettingsLink](/shippingSettingsLink)in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for[DeliveryTimeSettings](/DeliveryTimeSettings)) or shippingLabel (for[ShippingRateSettings](/ShippingRateSettings)), since this property is for use with unlabelled settings.[jobImmediateStart](/jobImmediateStart)

[JobPosting](/JobPosting)[multipleValues](/multipleValues)

[PropertyValueSpecification](/PropertyValueSpecification)[offersPrescriptionByMail](/offersPrescriptionByMail)

[HealthPlanFormulary](/HealthPlanFormulary)[petsAllowed](/petsAllowed)

[Accommodation](/Accommodation)or[ApartmentComplex](/ApartmentComplex)or[FloorPlan](/FloorPlan)or[LodgingBusiness](/LodgingBusiness)[publicAccess](/publicAccess)

[Place](/Place)[Place](/Place)is open to public visitors. If this property is omitted there is no assumed default boolean value.[readonlyValue](/readonlyValue)

[PropertyValueSpecification](/PropertyValueSpecification)[recourseLoan](/recourseLoan)

[LoanOrCredit](/LoanOrCredit)[renegotiableLoan](/renegotiableLoan)

[LoanOrCredit](/LoanOrCredit)[representativeOfPage](/representativeOfPage)

[ImageObject](/ImageObject)[requiresSubscription](/requiresSubscription)

[ActionAccessSpecification](/ActionAccessSpecification)or[MediaObject](/MediaObject)`true`

or `false`

(note that an earlier version had 'yes', 'no').
[smokingAllowed](/smokingAllowed)

[Place](/Place)[value](/value)

[MonetaryAmount](/MonetaryAmount)or[PropertyValue](/PropertyValue)or[QuantitativeValue](/QuantitativeValue)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

[valueAddedTaxIncluded](/valueAddedTaxIncluded)

[PriceSpecification](/PriceSpecification)[valueRequired](/valueRequired)
