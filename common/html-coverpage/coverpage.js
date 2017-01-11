/*!
 * Copyright 2017 Chris Johns <chrisj@rtems.org>
 */

/*
 * Embed the XML catalogue in this JS code to get around the Chrome on Windows
 * security "feature" where loading of a local disk file under the same path as
 * the HTML Chrome just loaded from disk is not allowed.
 */
function coverPageCatalogue() {
    xml = '@CATALOGUE';
    paintCatalogue($.parseXML(xml));
}
