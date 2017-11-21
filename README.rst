=================================
collective.convertoldimgscalepath
=================================

In older Plone sites images scale were accessed as ...path_to_image/image_preview this doesn't work with p.a.imaging where scales are accessed as ...path_to_image/@@images/image/preview

This package contains a simple view which will convert the path to the new style version.

Usage
-----

- Modify view to fit your content types.
- Call @@convert_scale_paths as admin in your Plone root.


WARNING
-------

Use at your own risk, make a backup of your site before!
