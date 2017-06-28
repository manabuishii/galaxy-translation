# galaxy-translation
Tool for Galaxy tool's xml translation

# Theoricaly & Praticaly
To translate XML tool in other languages this tool begins by creating a ".pot" file with the original ".xml" file.
A ".pot" (for ".po" template) is a text file with commented information in the beginning and numerous paired lines:
- first a misguided line who contains the original text
- second a msgstr line who is empty
After translation (automatically or manually) a ".po" file need to be created with a full ".pot".
This ".po" is converted to a binary dictionary ".mo" file with the following line:

```
msgcat file.po | msgfmt -o file.mo -
```

This is \__init\__.py (from galaxy/lib/galaxy/tools/) who use ".mo" file to translate ".xml".

__CAUTION__ ".mo" must be name like that :

```
 [...]/tool_dir/language/LC_MESSAGES/default.mo
```
Where language is language set in LANGUAGE environment variable of Galaxy (e.g. ja for Japan, fr for French, etc).

The upload.py file come from galaxy/lib/galaxy/webapps/tool_shed/controllers/ and create ".pot" when user upload ".xml" in the tool_shed (in the same directory).


# Require

```
pip install lxml
```
