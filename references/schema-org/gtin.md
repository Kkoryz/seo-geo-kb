---
title: "gtin"
source_url: https://schema.org/gtin
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# gtin

# gtin

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/gtin
-
Equivalent Property: gs1:gtin

Equivalent Property: unece:gTINId [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+gtin)

A Global Trade Item Number (


A correct


The GS1


Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

[GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.A correct

[gtin](/gtin)value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a[valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)and meet the other rules for valid GTINs. See also[GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)and[Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number)for more details. Left-padding of the gtin values is not required or encouraged. The[gtin](/gtin)property generalizes the earlier[gtin8](/gtin8),[gtin12](/gtin12),[gtin13](/gtin13), and[gtin14](/gtin14)properties.The GS1

[digital link specifications](https://www.gs1.org/standards/Digital-Link/)expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the[hasGS1DigitalLink](/hasGS1DigitalLink)attribute.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

#### Sub-properties

#### Source

[https://github.com/schemaorg/schemaorg/issues/2288](https://github.com/schemaorg/schemaorg/issues/2288)
