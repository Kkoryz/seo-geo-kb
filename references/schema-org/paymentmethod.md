---
title: "PaymentMethod"
source_url: https://schema.org/PaymentMethod
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PaymentMethod

# PaymentMethod

A Schema.org Type

- Canonical URL: https://schema.org/PaymentMethod
-
Equivalent Class: fibo-fbc-pas-fpas:PaymentMechanism

Equivalent Class: unece:PaymentMeans [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PaymentMethod)

A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction. The following legacy values should be accepted:



- http://purl.org/goodrelations/v1#ByBankTransferInAdvance
- http://purl.org/goodrelations/v1#ByInvoice
- http://purl.org/goodrelations/v1#Cash
- http://purl.org/goodrelations/v1#CheckInAdvance
- http://purl.org/goodrelations/v1#COD
- http://purl.org/goodrelations/v1#DirectDebit
- http://purl.org/goodrelations/v1#GoogleCheckout
- http://purl.org/goodrelations/v1#PayPal
- http://purl.org/goodrelations/v1#PaySwarm

[UNCE payment means](https://vocabulary.uncefact.org/PaymentMeans)are recommended or for newer annotations.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[paymentMethodType](/paymentMethodType)

[PaymentMethodType](/PaymentMethodType)[Thing](/Thing)

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

[PaymentMethod](/PaymentMethod)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Demand](/Demand)or[Offer](/Offer)or[Organization](/Organization)[appliesToPaymentMethod](/appliesToPaymentMethod)

[PaymentChargeSpecification](/PaymentChargeSpecification)[paymentMethod](/paymentMethod)

[Invoice](/Invoice)or[Order](/Order)#### More specific Types

#### Source

[https://github.com/schemaorg/schemaorg/issues/3537](https://github.com/schemaorg/schemaorg/issues/3537)

### Examples

[Example 1](#eg-3537)

Copied

Example notes or example HTML without markup.

Possible Payment: Cash On Delivery, SplashPay 🌊, SEPA bank transfer and prepayment in all Splash stores 🌊.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "OnlineStore", "name": "Example Online Store", "acceptedPaymentMethod": [ { "@type": "PaymentMethod", "paymentMethodType": "https://schema.org/COD", "name": "Cash on Delivery" }, { "@type": "PaymentService", "name": "SplashPay", "description": "Pay using the SplashPay app." }, { "@type": "PaymentMethod", "paymentMethodType": "https://schema.org/ByBankTransferInAdvance", "name": "SEPA bank transfer", "description": "Bank transfer within the Single Euro Payments Area (SEPA)." }, { "@type": "PaymentService", "paymentMethodType": "https://schema.org/InStorePrepay", "provider": { "@type": "Organization", "name": "Splash Store", "description": "Pay your online purchases conveniently in any Splash Store." } } ] } </script>

Structured representation of the JSON-LD example.
