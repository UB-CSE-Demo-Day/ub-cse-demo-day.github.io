---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: none
---

<meta http-equiv="refresh" content="0;url={{
  site.by_year 
    | where: "short_title", "Fall 2023"
    | map: "url" 
    | first
  }}">
