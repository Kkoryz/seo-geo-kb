---
title: "isVariantOf"
source_url: https://schema.org/isVariantOf
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# isVariantOf

# isVariantOf

A Schema.org Property

- Canonical URL: https://schema.org/isVariantOf
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+isVariantOf)

Indicates the kind of product that this is a variant of. In the case of

[ProductModel](/ProductModel), this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a[ProductGroup](/ProductGroup), the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with[ProductGroup](/ProductGroup), this property can apply to any[Product](/Product)included in the group.**Subproperty of:**

- skos:broader
- cmns-cls:exemplifies

Inverse-property:
[hasVariant](/hasVariant)

### Values expected to be one of these types


### Used on these types


### Acknowledgements

GoodRelations Vocabulary Terms

[uses](https://blog.schema.org/2012/11/08/good-relations-and-schema-org/)terminology from the GoodRelations Vocabulary for E-Commerce, created by Martin Hepp. GoodRelations is a data model for sharing e-commerce data on the Web. More information about GoodRelations can be found at

[http://purl.org/goodrelations/](http://purl.org/goodrelations/).
