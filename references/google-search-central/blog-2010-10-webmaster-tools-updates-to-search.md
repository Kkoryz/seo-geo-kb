---
title: "Webmaster Tools: Updates to Search queries, Parameter handling and Messages | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/10/webmaster-tools-updates-to-search
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-10-08
---

# Webmaster Tools: Updates to Search queries, Parameter handling and Messages | Google Search Central Blog | Google for Developers

Friday, October 08, 2010

We've just released updates to several features in Webmaster Tools to provide you with more detail and more control of how your site appears in search results.

## Search queries

Time does not stand still and neither should your site. With that in mind we've added a "Change" column next to the impressions, clicks, clickthrough rate (CTR) and position columns, making it easier to identify trends for each of these important metrics. The change column is tied to the date range you specify, which should help when you're trying to pinpoint when a particular change occurred.

Each query listed in Search queries now links to a query details page which includes a graph of impressions and clicks for that specific query, providing a quick visual of its performance in the search results over time. Below the graph is a table listing of the pages returned in search results for that query, along with impressions, clicks and CTR. Each column in the table is sortable, offering a quick way to re-sort the data based on what's most interesting to you. If you'd rather use your own favorite tool to slice and dice the data you can use the "Download this table" link to export all the information from the main Search queries page or from each individual query details page.

## Better Parameter Handling:

We've moved this feature under its own tab in the Settings section of Webmaster Tools, and
introduced a new action to manage parameters. When we introduced
[Parameter Handling](/search/blog/2009/10/new-parameter-handling-tool-helps-with)
last year, we allowed you to specify URL parameters and whether they should be ignored or not.
When you choose to ignore a parameter, you are telling us that this parameter has no impact on
the displayed content. For example, consider a session id parameter, like `sid`

in the
following URLs:

https://example.com/product.php?item=swedish-fish https://example.com/product.php?item=swedish-fish&sid=1234 https://example.com/product.php?item=swedish-fish&sid=5678

Assuming that these three URLs display exactly the same product page for tasty Swedish fish candy,
Google only needs to crawl and index one of them. You can simply select action "Ignore" for
parameter `sid`

in Webmaster Tools and Google will just crawl and index one of these
URLs, avoiding duplicates.

In addition to the old functionality, you now have the ability to choose a specific value among the known values for a given URL parameter. This is important when a parameter is relevant to the content, but different values of this parameter lead to similar pages. For example, consider a sorting parameter, like "sort-by" in the following URLs:

https://example.com/shop.php?category=candy&sort-by;=asc-price&page=1 https://example.com/shop.php?category=candy&sort-by;=desc-price&page=1 https://example.com/shop.php?category=candy&sort-by;=asc-price&page=2 https://example.com/shop.php?category=candy&sort-by;=desc-price&page=2

These four URLs show products in the candy category. There are enough items in this category to
fill two pages, and the products shown can be sorted by price, in ascending or descending order.
Selecting action "Ignore" for parameter "sort-by" would be incorrect and could potentially limit
our indexing of the site. This is because, after ignoring "sort-by", we would consider the first
two URLs equivalent and may choose to index the URL with ascending sort order. We would also
consider the last two URLs equivalent and may choose to index the URL with descending sort order.
In this scenario, we would be indexing the candy category inconsistently, with some candy products
appearing in both of the pages selected for the index, while other candy products not appearing in
either of them. The right solution comes from the new action "Use specific value" now available in
Webmaster Tools. To avoid duplicates but still keep our indexing consistent, you can simply select
action "Use specific value" for parameter "sort-by" and choose one of the valid values, say
`asc-price`

. After this, our indexing would be fully consistent, as we would focus only
on the pages with products sorted by ascending price.

## Messages

Some sites receive lots of messages in the Webmaster Tools Message Center. With this update we've added the ability to "star" specific messages that you deem important. There's now a separate "Starred" view where you can see all the messages that you've starred, making tracking and finding the most important messages for your site a breeze.

We hope these updates make Webmaster Tools even more useful for your site. If you have feedback on
any of these updates, or if you have questions, post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
