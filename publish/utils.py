import html5lib
from html5lib.filters import whitespace
from html5lib_typogrify.french.filters import medor, figures


def typogrify(html):
    # Using etree is important here because it does not suffer from a bug
    # where a text featuring entitities is split into various
    # adjacent text nodes.
    # (thanks html5lib folks for the tip).
    # See <https://github.com/html5lib/html5lib-python/issues/208>
    dom = html5lib.parseFragment(html, treebuilder="etree")
    walker = html5lib.getTreeWalker("etree")

    stream = walker(dom)
    stream = whitespace.Filter(stream)
    stream = medor.Filter(stream)
    stream = figures.Filter(stream)

    s = html5lib.serializer.HTMLSerializer(quote_attr_values=True, omit_optional_tags=False)

    return s.render(stream)
