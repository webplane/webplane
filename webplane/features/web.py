from mfind import MultiFinder
from pathlib import Path
from fnmatch import fnmatch

FEATURE_RULES = {
    "after": "boot"
}

STATIC_LINES = []


def path2url(path: str):
    """ returns the url mapping for a given path """
    path = Path(path)
    parts = list(Path(path).parts)
    if path.stem == "index":
        del parts[-1]
    else:
        parts[-1] = path.stem       # consider only filename for url
    url = '/' + '/'.join(parts)
    return url


def static_handler(filename: str):
    """ skip handling for static files """
    for line in STATIC_LINES:
        if fnmatch(filename, line):
            return False


def internal_handler(filename: str):
    """ skip handling filenames with a leading _ """
    return False    # Just about all other handler checks


def template_handler(filename: str):
    url = path2url(filename)
    print("URL", url)
    #print("Handling", filename, url,"x")


def activate(content_path):
    statics_fname = Path(content_path, ".static")
    if statics_fname.exists():
        with open(statics_fname) as static_file:
            for line in static_file:
                STATIC_LINES.append(line.strip("\n"))

    file_processing_map = {
        "*" : static_handler,
        "_*" : internal_handler,
        ("*.html", "*.md") : template_handler,
    }
    mf = MultiFinder(file_processing_map)
    mf.scan(content_path, filename_only_match=True)
