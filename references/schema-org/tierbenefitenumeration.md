---
title: "TierBenefitEnumeration"
source_url: https://schema.org/TierBenefitEnumeration
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# TierBenefitEnumeration

# TierBenefitEnumeration

A Schema.org Enumeration Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/TierBenefitEnumeration
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+TierBenefitEnumeration)

An enumeration of possible benefits as part of a loyalty (members) program.

Instances of

[TierBenefitEnumeration](/TierBenefitEnumeration)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MemberProgramTier](/MemberProgramTier)#### Enumeration members

-
[TierBenefitLoyaltyPoints](/TierBenefitLoyaltyPoints) -
[TierBenefitLoyaltyPrice](/TierBenefitLoyaltyPrice) -
[TierBenefitLoyaltyReturns](/TierBenefitLoyaltyReturns) -
[TierBenefitLoyaltyShipping](/TierBenefitLoyaltyShipping)

#### Source

[https://github.com/schemaorg/schemaorg/issues/3563](https://github.com/schemaorg/schemaorg/issues/3563)

### Examples

[Example 1](#eg-0489)

Copied

Example notes or example HTML without markup.

A member (loyalty) program provided by an OnlineStore. The program has 3 tiers: - The Silver tier is free to join and provides loyalty points to the member. - The Gold tier requires sign-up to a creditcard and has the benefit of member-only pricing and more loyalty points than the silver tier - The Platinum tier has an annual fee of $39.99 and has the benefit of member-only pricing and more loyalty points than the gold tier. Use of the MemberProgram is illustrated by an Offer which has a non-member (regular) price as well as a special member price for the gold and platinum member tiers.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [ { "@context": "https://schema.org", "@type": "OnlineStore", "name": "Example Online Store", "url": "https://www.example.com", "sameAs": [ "https://example.net/profile/example12", "https://example.org/@example34" ], "logo": "https://www.example.com/assets/images/logo.png", "contactPoint": { "contactType": "Customer Service", "email": "support@example.com", "telephone": "+47-99-999-9900" }, "vatID": "FR12345678901", "iso6523Code": "0199:724500PMK2A2M1SQX229", "hasMemberProgram": { "@type": "MemberProgram", "name": "Membership Plus", "description": "For frequent shoppers this is our top-rated loyalty program", "url": "https://www.example.com/membership-plus", "hasTiers": [ { "@type": "MemberProgramTier", "@id": "membership-plus#tier_silver", "name": "silver", "url": "https://www.example.com/membership-plus-silver", "hasTierBenefit": [ "https://schema.org/TierBenefitLoyaltyPoints" ], "membershipPointsEarned": 5 }, { "@type": "MemberProgramTier", "@id": "membership-plus#tier_gold", "name": "gold", "url": "https://www.example.com/membership-plus-gold", "hasTierRequirement": { "@type": "CreditCard", "name":" MyStore Gold Plus" }, "hasTierBenefit": [ "https://schema.org/TierBenefitLoyaltyPrice", "https://schema.org/TierBenefitLoyaltyPoints" ], "membershipPointsEarned": 10 }, { "@type": "MemberProgramTier", "@id": "membership-plus#tier_platinum", "name": "gold", "url": "https://www.example.com/membership-plus-platinum", "hasTierRequirement": { "@type": "UnitPriceSpecification", "price": "39.99", "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": "1", "unitCode": "ANN" } }, "hasTierBenefit": [ "https://schema.org/TierBenefitLoyaltyPrice", "https://schema.org/TierBenefitLoyaltyPoints" ], "membershipPointsEarned": 15 } ] } }, { "@context": "https://schema.org", "@type": "Product", "sku": "44E01-X1100000", "gtin14": "98766051104399", "image": "https://www.example.com/coat_large_lightblue.jpg", "name": "Large light blue coat", "description": "Large wool light blue coat for the winter season", "color": "light blue", "size": "large", "offers": [ { "@type": "Offer", "url": "https://www.example.com/coat?size=large&color=lightblue", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/BackOrder", "shippingDetails": { "@id": "https://www.example.com/shipping#shipping_policy" }, "hasMerchantReturnPolicy": { "@id": "https://www.example.com/returns#return_policy" }, "priceSpecification": [ { "@type": "PriceSpecification", "price": 15, "priceCurrency": "USD" }, { "@type": "PriceSpecification", "validForMemberTier": [ { "@id": "https://www.example.com/membership-plus#tier_gold" }, { "@id": "https://www.example.com/membership-plus#tier_platinum" } ], "price": 9.95, "priceCurrency": "USD" } ] } ] } ] </script>

Structured representation of the JSON-LD example.
