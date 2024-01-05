import os


def on_pre_page(page, config, files):
    """
    Treats `_index.md` files as if they were `index.md`. This is a workaround to prohibit MkDocs from considering them
    as the parent's index, when the parent lacks one.
    """
    if '_index' in page.file.name:
        *head, parent, index, tail = page.file.url.split('/')
        page.file.name = parent
        page.file.url = page.file.url.replace('_index/', '')
        page.file.dest_uri = page.file.dest_uri.replace('_index/', '')
        page.canonical_url = page.canonical_url.replace('_index/', '')
        page.abs_url = page.abs_url.replace('_index/', '')
        # Absolute destination path is OS dependent.
        abs_dest_path = page.file.abs_dest_path.split(os.sep)
        abs_dest_path.remove('_index')
        page.file.abs_dest_path = os.sep.join(abs_dest_path)
