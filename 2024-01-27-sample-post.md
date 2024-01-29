---
layout: post
title:  "Setting up Jekyll and GitHub Pages!"
date:   2024-01-27 23:56:18 -0600
categories: lessons
---
I had set this up a few years ago for a University of Manitoba assignment so it was fairly simple to do again. I followed a 6 year old guide by [Mike from Giraffe Academy][youtube-jekyll-tutorial] which suprisingly has held up pretty well. I remembered most of the content so understanding important concepts such like [Front Matter][front-matter] setting up the important files such as the `_config.yml` and the `Gemfile` was pretty simple. The difficult task was serving the site on [GitHub Pages][github-pages].

When I first had to do this for a class, pushing changes to the repository was enough to update the static site. Now, a [GitHub Actions][github-actions] runs before the site is updated with the changes. I have experience with making my own GitHub Action workflows before, but the one used to build and serve the site is one that I guess GitHub provides and executes automatically. I had an issue where the workflow will fail and the changes to the site would not go live. It is pretty late right now so I made the mistake of deleting the workflow before I read and understood why it failed T_T. All good, lesson for next time! I got through this issue by remaking the entire site from scratch using the CLI command `jekyll new site_name`. After remaking the site, the workflows started working again. I wish I could have read why the previous ones failed T_T oops.

Another issue I had were links working when hosting locally, but then breaking when served on GitHub Pages. Clicking around on the hosted site, I noticed the URL paths were terribly incorrect. Some quick Googling and I found this [explanation][url-and-baseurl] by [Michael Rose][michael-rose] that helped me understand the difference between the `url` and `baseurl` variables in the `_config.yml` file. Updating those fixed my issues and I got my links working pefectly!

[youtube-jekyll-tutorial]: https://www.youtube.com/playlist?list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB
[front-matter]: https://jekyllrb.com/docs/front-matter/
[github-pages]: https://pages.github.com/
[github-actions]: https://github.com/features/actions
[url-and-baseurl]: https://mademistakes.com/mastering-jekyll/site-url-baseurl/
[michael-rose]: https://mademistakes.com/about/