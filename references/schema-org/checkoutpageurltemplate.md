---
title: "checkoutPageURLTemplate"
source_url: https://schema.org/checkoutPageURLTemplate
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# checkoutPageURLTemplate

# checkoutPageURLTemplate

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/checkoutPageURLTemplate
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+checkoutPageURLTemplate)

A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/3135](https://github.com/schemaorg/schemaorg/issues/3135)

### Examples

[Example 1](#eg-0475)

Copied

Example notes or example HTML without markup.

An example of an offer with a checkoutPageURLTemplate.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"Product", "sku":"12345", "image":"https://example.com/fnobarizer.jpg", "name":"Advanced Fnobarizer", "brand":{ "@type":"Brand", "name":"Nucleatronics Inc." }, "offers":{ "@type":"Offer", "checkoutPageURLTemplate":"https://www.example.com/checkout?items={VARIANT_ID_1}:{Quantity_1},{VARIANT_ID_2}:{Quantity_2}&discount={DISCOUNT_CODE}&store_id={pickup_store_id}", "priceSpecification":{ "@type":"PriceSpecification", "price":"99.99", "priceCurrency":"USD" }, "acceptedPaymentMethod":"http://purl.org/goodrelations/v1#GoogleCheckout" } } </script>

Structured representation of the JSON-LD example.
