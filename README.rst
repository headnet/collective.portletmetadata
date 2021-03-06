collective.portletmetadata
==========================

About
-----

collective.portletmetadata is a collection of patches that makes it possible edit
settings for each portlet assignment. We denote these settings for metadata thereby
the name of the product.

Out of the box the product provides the following features:

* Possibility for creating local portlets, i.e. portlets that will not be inherited
  even though child settings imply so.
* Possibility for adding a CSS class for a portlet assignment. These are defined
  in the controlpanel (stored in registry).
* Possibility for excluding a portlet from being indexed by Google.

Usage
-----

Whenever the product is installed a "*" will be visible in the @@manage-portlets
view for each assignment. Whenever the user selects this option, he/she can edit
the metadata as described above.

See a short guide `here <http://bo.geekworld.dk/introducing-collective-portletmetadata/>`_.

Related work
------------

Ideally, this feature should be built into plone.app.portlets as described in
`PLIP 12266 <https://dev.plone.org/ticket/12266>`_ the current milestone is set to
Plone 5, but until Plone 5 is a reality this product can be used.

Author
------

* Bo Simonsen <bo@headnet.dk>

TODO
----

* Better documentation


