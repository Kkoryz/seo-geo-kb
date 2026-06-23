---
title: "308 Permanent Redirects: How to Use Them"
source_url: https://www.withdaydream.com/library/insights/308-permanent-redirect
category: daydream
section: "Daydream — GEO library (how LLMs crawl & index)"
date: 2025-03-01
---

# 308 Permanent Redirects: How to Use Them

A 308 permanent redirect is an HTTP response status code that tells browsers and search engines that a resource has moved to a new URL — in other words, that a webpage has a new permanent address.

You’re probably familiar with [404 errors](https://en.wikipedia.org/wiki/HTTP_404). This is another type of HTTP response status code, but instead of serving up a dead-end 404 error page, a 308 code automatically and seamlessly redirects users to the new permanent URL.

This kind of redirect is most commonly used when a website owner wants to change the URL of a page without changing the action (or request) that happens when a user visits the page.

## What Is a 308 Permanent Redirect?

A 308 permanent redirect indicates that a page has permanently moved to a new URL.

The redirect will automatically redirect users to the new page without them even realizing it. All modern browsers can automatically detect a 308 permanent redirect response code because the server that’s sending it will have a special header indicating the new URL of the requested page or resource.

## When Would You Use a 308 Redirect?

301, 302, 307, 308 — how do you decide which redirect code to use? Or *when *do you decide to implement a 308 redirect instead of another redirect?

Usually, you use a 308 redirect if you want to permanently change a page’s URL without changing the request type. There are two types of requests: POST and GET.

**POST:**When a user visits a URL, a POST request submits data. It’s more secure than a GET request and is often used to send and retrieve data such as login details or payment information.**GET:**When a user hits enter on a URL, a GET request retrieves data. The server sends back the website so the browser can display it.

308 redirects don’t change the type of request, which means the information received from a user remains intact as they go to the redirected page.

In other words, if you want to retain personalized user information like cart contents, login details, or form field entries so that when a user ends up at the redirected page, they don’t have to enter that information again, you’ll implement a 308 redirect so the POST request doesn’t change. If the request changed to GET, you’d lose that information because that request simply asks the browser to display the website rather than retrieving the previously inputted data.

Here are some common scenarios where you might decide to implement a 308 redirect:

- When a webpage has permanently moved to a new location.
- When you want to redirect users to a new URL without changing the request method.
- When you want to maintain consistency with the original request’s content for search engine optimization (SEO) purposes.

If you create a new checkout page, you’d want to redirect customers from the old checkout page so the new page works in the same way. To do this, the request would need to be the same (POST) so that users successfully arrive at the new page after they’ve submitted data.

To avoid losing the products they’ve added to their cart (or any other submitted data), you can implement a 308 redirect that retains the information while redirecting them to the new checkout. Maintaining the original POST request stores the cart information and benefits the user because they don’t have to go back and fill their cart again.

But it also benefits your SEO efforts: 308 permanent redirects should pass almost all [PageRank](https://www.withdaydream.com/library/pagerank) or “link juice” from the original URL to the new URL, which maintains your rankings in search results.

Note that too many redirects can be a problem. Google’s bots struggle to process a long string of redirects. If there are more than ten “hops” (that is, more than five redirects in a chain), [Googlebot won’t land on the destination URL](https://developers.google.com/search/docs/crawling-indexing/http-network-errors).

## How Do You Implement a 308 Redirect?

A 308 redirect tells web browsers that a resource has permanently moved to a new URL and to update their indexes and caches to reflect this change.

There are a few ways you can implement an HTTP status code 308, depending on the technology you’re using. Usually, you’ll need to input a redirect directive in the access file, server block, or header function. For example, in JavaScript, you can implement a 308 redirect using the window.location object, with this code:

`window.location.replace ("http://www.example.com/new-page.html")`


## 308 Redirects Versus 301 Redirects

308 and 301 redirects both signify a permanent relocation of a resource — that is, they communicate that a URL has permanently changed. However, unlike a 308 redirect, a 301 redirect allows the browser to convert the original request method from POST to GET or vice versa.

So, if you implement a [301 redirect](https://www.withdaydream.com/library/301-redirects), a user will get redirected to the new URL, but any information or data they submitted on a previous page might be lost. The web browser can change the HTTP method from POST to GET with a 301 redirect, but it can’t with a 308 redirect.

308 redirects are more strict and require all web browsers to follow the updated URL. With 301 redirects, web browsers can update their own caches and indexes to reflect the new location. This means 308 redirects are at risk of failing if the browser being used doesn’t support the redirect, leading to a poor user experience.

**The main difference between 301 and 308 redirects: **The browser or website host can convert the HTTP request method from POST to GET with a 301 redirect but not with a 308 redirect. So a 301 redirect can lead to a loss of data.

**The main similarity between 301 and 308 redirects: **Both 301 and 308 redirects indicate a permanent change in URL. With a permanent change, search engines will update the URL for the resource.

### When would you use a 301 redirect over a 308 redirect?

301 redirects are more than adequate for webpages that aren’t data collection points. For example, if you were simply redirecting a blog post to another URL, you would use a 301 redirect instead of a 308 redirect.

However, if you want to redirect users to a new page that they will arrive at after they’ve submitted data, added products to their cart, or filled in a form, and you want to retain that information, you should use a 308 redirect.

## 308 Redirects Versus 302 Redirects

A 302 redirect indicates a temporary change to a URL. It informs the web browser that the new URL is only temporary, and that future requests should continue to take users to the original URL. Like a 301 redirect, a 302 redirect doesn’t maintain the original POST or GET request, so there’s the potential to lose user data.

**The main difference between 302 and 308 redirects: **302 redirects are temporary, while 308 redirects are permanent, so search engines won’t update URLs for 302 redirects. There’s also a difference in the request method. 308 redirects maintain the original HTTP request method while 302 redirects can convert from POST to GET.

**The main similarity between 302 and 308 redirects: **The only similarity between 302 and 308 redirects is that they both redirect users from one URL to another. As another quick note, it has long been stated that 302 redirects do not pass PageRank or communicate to Google that page authority should pass to the redirected URL. However, in 2021, [John Mueller from Google clarified](https://youtu.be/2VrjFMUU_kY?si=_qXdkJItWYqf8fdH) that 302 redirects can pass PageRank and that, over the long term, Google will tend to see longstanding 302 redirects as similar to 301 redirects.

### When would you use a 302 redirect over a 308 redirect?

302 redirects are mostly used to temporarily transfer users from one URL to another. This might be during the maintenance of an existing page or as a way to divert visitors to a temporary landing page for a product launch.

## 308 Redirects Versus 307 Redirects

A 307 redirect is a temporary redirect and advises the web browser to preserve the original request method of POST or GET. Like 302 redirects, 307 redirects tell the web browser to temporarily divert users on this occasion but to continue to use the original URL for further requests.

**The main difference between 307 and 308 redirects: **307 redirects are temporary, while 308 redirects are permanent, so search engines won’t update URLs for 307 redirects.

**The main similarity between 307 and 308 redirects: **Both 307 and 308 redirects maintain the original HTTP request method of POST.

### When would you use a 307 redirect over a 308 redirect?

307 redirects are used to temporarily redirect users to a new URL without losing the original HTTP request. This retains any data or information and transfers it to the new URL. You might use this to redirect users to a temporary thank you page or to send visitors to a temporary upsell page before they continue to the checkout.

## Final Thoughts

308 permanent redirects are commonly used to send website visitors to a new, permanent URL. They preserve the original HTTP code, which allows web owners to retain data such as login details or shopping cart information when they send users to the new URL. If you *don’t *need to retain any information (for instance, if you’re just updating a blog post’s URL), a 301 redirect is likely the easier and safer option.

But if data preservation is essential, you should implement a 308 redirect to maintain a good customer experience and a smooth transition from the old URL to the new one.
