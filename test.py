import gettext

ko = gettext.translation('lokalise', './locales', languages=['ko'], fallback=True)
en = gettext.translation('lokalise', './locales', languages=['en'], fallback=True)

_ = ko.gettext

print(_("Hello, world!"))

_ = en.gettext

print(_("Hello, world!"))