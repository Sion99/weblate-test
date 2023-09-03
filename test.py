import gettext

ko = gettext.translation('lokalise', './locales', languages=['ko'], fallback=True)
en = gettext.translation('lokalise', './locales', languages=['en'], fallback=True)

_ = ko.gettext

print(_("Hello, world!"))
print(_("Good Morning"))
print(_("Good Afternoon"))
print(_("Good Night"))

_ = en.gettext

print(_("Hello, world!"))
print(_("Good Morning"))
print(_("Good Afternoon"))
print(_("Good Night"))