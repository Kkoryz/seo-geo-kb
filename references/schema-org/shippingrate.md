---
title: "shippingRate"
source_url: https://schema.org/shippingRate
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# shippingRate

# shippingRate

A Schema.org Property

- Canonical URL: https://schema.org/shippingRate
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+shippingRate)

The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the

[MonetaryAmount](/MonetaryAmount)) are most appropriate.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2506](https://github.com/schemaorg/schemaorg/issues/2506)

[https://github.com/schemaorg/schemaorg/issues/3617](https://github.com/schemaorg/schemaorg/issues/3617)

### Examples

[Example 1](#eg-0392)

Copied

Example notes or example HTML without markup.

Offer shipping details example with nested delivery time(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "OfferShippingDetails", "deliveryTime": { "@type": "ShippingDeliveryTime", "businessDays": { "@type": "OpeningHoursSpecification", "dayOfWeek": [ "https://schema.org/Monday", "https://schema.org/Tuesday", "https://schema.org/Wednesday", "https://schema.org/Thursday", "https://schema.org/Friday" ] }, "cutoffTime": "12:00:15Z", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitCode": "d" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 10, "unitCode": "d" } }, "shippingRate": { "@type": "MonetaryAmount", "value": 4.95, "currency": "USD" } } </script>

Structured representation of the JSON-LD example.
