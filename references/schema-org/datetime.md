---
title: "DateTime"
source_url: https://schema.org/DateTime
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DateTime

# DateTime

A Schema.org Data Type

- Canonical URL: https://schema.org/DateTime
- Equivalent Class: cmns-dt:DateTime
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DateTime)

A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).

Instances of

[DateTime](/DateTime)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Trip](/Trip)[auditDate](/auditDate)

[Certification](/Certification)[gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate).[availabilityEnds](/availabilityEnds)

[ActionAccessSpecification](/ActionAccessSpecification)or[Demand](/Demand)or[Offer](/Offer)[availabilityStarts](/availabilityStarts)

[ActionAccessSpecification](/ActionAccessSpecification)or[Demand](/Demand)or[Offer](/Offer)[availableFrom](/availableFrom)

[DeliveryEvent](/DeliveryEvent)[availableThrough](/availableThrough)

[DeliveryEvent](/DeliveryEvent)[bookingTime](/bookingTime)

[Reservation](/Reservation)[checkinTime](/checkinTime)

[LodgingBusiness](/LodgingBusiness)or[LodgingReservation](/LodgingReservation)[checkoutTime](/checkoutTime)

[LodgingBusiness](/LodgingBusiness)or[LodgingReservation](/LodgingReservation)[commentTime](/commentTime)

[UserComments](/UserComments)[contentReferenceTime](/contentReferenceTime)

[CreativeWork](/CreativeWork)[coverageEndTime](/coverageEndTime)

[LiveBlogPosting](/LiveBlogPosting)[coverageStartTime](/coverageStartTime)

[LiveBlogPosting](/LiveBlogPosting)[cvdCollectionDate](/cvdCollectionDate)

[CDCPMDRecord](/CDCPMDRecord)[datasetTimeInterval](/datasetTimeInterval)

[Dataset](/Dataset)[dateCreated](/dateCreated)

[CreativeWork](/CreativeWork)or[DataFeedItem](/DataFeedItem)[dateDeleted](/dateDeleted)

[DataFeedItem](/DataFeedItem)[dateIssued](/dateIssued)

[Ticket](/Ticket)[dateModified](/dateModified)

[CreativeWork](/CreativeWork)or[DataFeedItem](/DataFeedItem)[datePosted](/datePosted)

[CDCPMDRecord](/CDCPMDRecord)or[JobPosting](/JobPosting)or[RealEstateListing](/RealEstateListing)or[SpecialAnnouncement](/SpecialAnnouncement)[datePublished](/datePublished)

[Certification](/Certification)or[CreativeWork](/CreativeWork)[CreativeWork](/CreativeWork)was broadcast or a[Certification](/Certification)was issued.[dateRead](/dateRead)

[Message](/Message)[dateReceived](/dateReceived)

[Message](/Message)[dateSent](/dateSent)

[Message](/Message)[departureTime](/departureTime)

[Trip](/Trip)[doorTime](/doorTime)

[Event](/Event)[dropoffTime](/dropoffTime)

[RentalCarReservation](/RentalCarReservation)[endDate](/endDate)

[CreativeWorkSeason](/CreativeWorkSeason)or[CreativeWorkSeries](/CreativeWorkSeries)or[DatedMoneySpecification](/DatedMoneySpecification)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[Event](/Event)or[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)or[Role](/Role)or[Schedule](/Schedule)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).[endTime](/endTime)

[Action](/Action)or[FoodEstablishmentReservation](/FoodEstablishmentReservation)or[InteractionCounter](/InteractionCounter)or[MediaObject](/MediaObject)or[Schedule](/Schedule)*December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

[exceptDate](/exceptDate)

[Schedule](/Schedule)[Date](/Date)or[DateTime](/DateTime)during which a scheduled[Event](/Event)will not take place. The property allows exceptions to a[Schedule](/Schedule)to be specified. If an exception is specified as a[DateTime](/DateTime)then only the event that would have started at that specific date and time should be excluded from the schedule. If an exception is specified as a[Date](/Date)then any event that is scheduled for that 24 hour period should be excluded from the schedule. This allows a whole day to be excluded from the schedule without having to itemise every scheduled event.[expectedArrivalFrom](/expectedArrivalFrom)

[ParcelDelivery](/ParcelDelivery)[expectedArrivalUntil](/expectedArrivalUntil)

[ParcelDelivery](/ParcelDelivery)[expires](/expires)

[Certification](/Certification)or[CreativeWork](/CreativeWork)[VideoObject](/VideoObject)or[NewsArticle](/NewsArticle)whose availability or relevance is time-limited, a[ClaimReview](/ClaimReview)fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a[Certification](/Certification)the validity has expired.[merchantReturnDays](/merchantReturnDays)

[MerchantReturnPolicy](/MerchantReturnPolicy)or[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)[returnPolicyCategory](/returnPolicyCategory)property is specified as[MerchantReturnFiniteReturnWindow](/MerchantReturnFiniteReturnWindow).[modifiedTime](/modifiedTime)

[Reservation](/Reservation)[observationDate](/observationDate)

[Observation](/Observation)[Observation](/Observation).[orderDate](/orderDate)

[Order](/Order)[ownedFrom](/ownedFrom)

[OwnershipInfo](/OwnershipInfo)[ownedThrough](/ownedThrough)

[OwnershipInfo](/OwnershipInfo)[paymentDue](/paymentDue)

[Invoice](/Invoice)or[Order](/Order)[paymentDueDate](/paymentDueDate)

[Invoice](/Invoice)or[Order](/Order)[pickupTime](/pickupTime)

[RentalCarReservation](/RentalCarReservation)or[TaxiReservation](/TaxiReservation)[previousStartDate](/previousStartDate)

[Event](/Event)[scheduledTime](/scheduledTime)

[PlanAction](/PlanAction)[startDate](/startDate)

[CreativeWorkSeason](/CreativeWorkSeason)or[CreativeWorkSeries](/CreativeWorkSeries)or[DatedMoneySpecification](/DatedMoneySpecification)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[Event](/Event)or[MerchantReturnPolicySeasonalOverride](/MerchantReturnPolicySeasonalOverride)or[Role](/Role)or[Schedule](/Schedule)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).[startTime](/startTime)

[Action](/Action)or[FoodEstablishmentReservation](/FoodEstablishmentReservation)or[InteractionCounter](/InteractionCounter)or[MediaObject](/MediaObject)or[Schedule](/Schedule)*January*to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

[temporal](/temporal)

[CreativeWork](/CreativeWork)[temporalCoverage](/temporalCoverage),[dateCreated](/dateCreated),[dateModified](/dateModified),[datePublished](/datePublished)) are not known to be appropriate.[temporalCoverage](/temporalCoverage)

[CreativeWork](/CreativeWork)[ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL. Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated.

[timestamp](/timestamp)

[InstantaneousEvent](/InstantaneousEvent)[uploadDate](/uploadDate)

[MediaObject](/MediaObject)[validFrom](/validFrom)

[Certification](/Certification)or[Demand](/Demand)or[FinancialIncentive](/FinancialIncentive)or[LocationFeatureSpecification](/LocationFeatureSpecification)or[MonetaryAmount](/MonetaryAmount)or[Offer](/Offer)or[OpeningHoursSpecification](/OpeningHoursSpecification)or[Permit](/Permit)or[PriceSpecification](/PriceSpecification)[validThrough](/validThrough)

[Demand](/Demand)or[FinancialIncentive](/FinancialIncentive)or[JobPosting](/JobPosting)or[LocationFeatureSpecification](/LocationFeatureSpecification)or[MonetaryAmount](/MonetaryAmount)or[Offer](/Offer)or[OpeningHoursSpecification](/OpeningHoursSpecification)or[PriceSpecification](/PriceSpecification)[webCheckinTime](/webCheckinTime)
