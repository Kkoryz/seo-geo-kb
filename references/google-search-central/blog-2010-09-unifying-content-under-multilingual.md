---
title: "Unifying content under multilingual templates | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/09/unifying-content-under-multilingual
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-09-09
---

# Unifying content under multilingual templates | Google Search Central Blog | Google for Developers

Thursday, September 09, 2010

If you have a global site containing pages where the:

- template (that is, side navigation, footer) is machine-translated into various languages,
- main content remains unchanged, creating largely duplicate pages,

and sometimes search results direct users to the wrong language, we'd like to help you better target your international/multilingual audience through:

<link rel=”alternate” hreflang="a-different-language" href="https://url-of-the-different-language-page" />

As you know, when
[ rel="canonical"](/search/blog/2009/02/specify-your-canonical) or a

[is properly implemented, we become more precise in clustering information from duplicate URLs, such as consolidating their linking properties. Now, when](/search/docs/crawling-indexing/301-redirects)

`301`

response code`rel="alternate" hreflang="x"`

is included in conjunction with
`rel="canonical"`

or `301`

redirects, not only will our indexing and linking
properties be more accurate, but we can better serve users the URL of their preferred language.
## Sample configuration that's prime for ` rel="alternate" hreflang="x"`


How does this all work? Imagine that you're the proud owner of example.com, a site called "The
Network" where you allow users to create their very own profile. Let's say Javier Lopez, a Spanish
speaker, makes his page at `https://es.example.com/javier-lopez`

:

Because you're trying to target a multilingual audience, once Javier hits "Publish," his profile becomes immediately available in other languages with the translated templates. Also, each of the new language versions is served on a separate URL.

## Background on the old issue: duplicate content caused by language variations

The configuration above allowed visitors speaking different languages to more easily interpret the
content, but for search engines it was slightly problematic: there are three URLs (English,
French, and Spanish versions) for the same main content in Javier's profile. Webmasters wanted to
avoid
[duplicate content](/search/docs/advanced/guidelines/duplicate-content)
issues (such as PageRank dilution) from these multiple versions and still ensure that we would
serve the appropriate version to the user.

## A new solution for localized templates

First of all, just to be clear, the strategy we're proposing isn't appropriate for multilingual sites that completely translate each page's content. We're trying to specifically improve the situation where the template is localized but the main content of a page remains duplicate/identical across language/country variants.

Before we get into the specific steps, our prior advice remains applicable:

-
Have one URL associated with one piece of content. We recommend against using the same URL for
multiple languages, such as serving both French and English versions on
`example.com/page.html`

based on user information (IP address,`Accept-Language`

HTTP header). -
When multiple languages are at play, it's best to include the language or country indication in
the URL, for example, example.com/en/welcome.html and example.com/fr/accueil.html (which
specify
`en`

and`fr`

) rather than`example.com/welcome.html`

and`example.com/accueil.html`

(which don't contain an explicit country/language specification). More suggestions can be found in our blog posts about[designing localized URLs](/search/blog/2010/03/working-with-multi-regional-websites)and[multilingual sites](/search/blog/2010/03/working-with-multilingual-websites).

For the new feature:

### Select the proper canonical.

The canonical designates the version of your content you'd like indexed and returned to users.
The first step towards making the right content indexable is to pick one canonical URL that best
reflects the genuine locale of the page's main content. In the example above, since Javier is a
Spanish-speaking user and he created his profile on `es.example.com`

,
`https://es.example.com/javier-lopez`

is the logical canonical. The title and snippet in
all locales will be selected from the canonical URL.

Once you have the canonical URL picked out, you can either:

-
from the language variants to the canonical. As an example, if a French speaker visits`301`

(permanent redirect)`fr.example.com/javier-lopez`

(not the canonical), have this page include a cookie to remember the user's language preference of French. Then permanently redirect from`fr.example.com/javier-lopez`

to the canonical at`es.example.com/javier-lopez`

. Because of the cookie,`es.example.com/javier-lopez`

will still render its boilerplate in French (even on the`es.example.com`

subdomain!). Similarly,`en.example.com/javier-lopez`

would set the value of this cookie to English and then`301`

redirect to`es.example.com/javier-lopez`

. Including a language selection link is also helpful should a multilingual user prefer a different experience of your site. -
Use
. On the other language variants, include a`rel="canonical"`

`link rel="canonical"`

tag pointing to your chosen canonical URL. In our example, since the canonical for Javier's profile is the Spanish version, the English and French pages (and optionally even the Spanish page itself) would include`<link rel=”canonical” href="https://es.example.com/javier-lopez" />`

. Cookies are not involved in this setup. Therefore, a French speaker will be served`es.example.com/javier-lopez`

with a Spanish template. Implement step 2 if you want the French speakers to be served the French version at`fr.example.com/javier-lopez`

in Google search results.

###
In the canonical URL, specify the various language versions via the `rel="alternate"`

link tag, using its `hreflang`

attribute.

`rel="alternate"`

URLs can be displayed in search results in accordance with a user's
language preference. The title and snippet, however, remain generated from the canonical URL (as
is customary with `rel="canonical"`

), not from the content of any
`rel="alternate"`

.

You can help Google display the correctly localized variant of your URL to our international users
by adding the following tags to `https://es.example.com/javier-lopez`

, the selected
canonical:

<link rel=”alternate” hreflang="en" href="https://en.example.com/javier-lopez" /> <link rel=”alternate” hreflang="fr" href="https://fr.example.com/javier-lopez" />

`rel="alternate"`

indicates that the URL contains an alternate version located at the
URI of the `href`

value. `hreflang`

identifies the language code of the
alternate URL and can be specified with
[ISO-639](https://www.loc.gov/standards/iso639-2/).

Please note: If your site supports many languages and you're worried about the increased file size
when declaring numerous `rel="alternate"`

URLs, please see our Help Center article
about
[configuring rel="alternate" with file size constraints](/search/docs/specialty/international/localized-versions).

Once the steps are completed, the configuration on "The Network" would look like this:

-
`https://en.example.com/javier-lopez`

: either`301`

redirects with a language cookie or contains`<link rel=”canonical” href=”https://es.example.com/javier-lopez” />`

-
`https://fr.example.com/javier-lopez`

: either`301`

redirects with a language cookie or contains`<link rel=”canonical” href=”https://es.example.com/javier-lopez” />`

-
`https://es.example.com/javier-lopez`

: is the canonical and contains`<link rel=”alternate” hreflang="en" href="https://en.example.com/javier-lopez" />`

and`<link rel=”alternate” hreflang="fr" href="https://fr.example.com/javier-lopez" />`


## Results of the above implementation

-
When your content is returned in search results, users will likely see the URL that corresponds
to their language preference, whether or not it's the canonical. (Good news!) This is because
with
`rel="canonical"`

or a`301`

redirect, we can cluster the language variations with the canonical. With`rel="alternate" hreflang="x"`

at serve-time we can deliver the URL of the most appropriate language to the user: English speakers will be served`en.example.com/javier-lopez`

as the result for the URL in Javier's profile, French speakers will see`fr.example.com/javier-lopez`

, Spanish speakers will see`es.example.com/javier-lopez`

. -
By implementing step 1, only content from the canonical version will be available for users in
search results (that is, content from the duplicate versions won't be searchable). Because the
Spanish version
`es.example.com/javier-lopez`

is the canonical, queries that include template content from this page, for example, "Javier Lopez familia"—when using any language preference—may return his profile (content from the canonical version). On the other hand, queries that include template content of the "duplicate" version, for example, "Javier Lopez family", are less likely to return his profile page. If you would like the other language versions indexed separately and searchable, avoid using`rel="canonical"`

and`rel="alternate"`

. - Indexing properties, such as linking information, from the duplicate language variants will be consolidated with the canonical.

## To recap (one more time, with feeling!)

For sites that have their template localized but the keep their pages' main content untranslated:

-
Once you have the canonical picked out you can use either
or a`rel="canonical"`

`301`

(permanent redirect) from the various localized pages to the canonical URL. -
On the canonical URL, specify the language-specific duplicated content with
different boilerplate via the
`rel="alternate"`

link tag, using its`hreflang`

attribute. This way, Google can show the correctly-localized variant of your URLs to our international users.

We realize this can be a little complicated, so if you have questions, please ask in our
[webmaster forum](https://support.google.com/webmasters/community)!
