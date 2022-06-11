#!./.venv/bin/python3

"""Script to auto-generate markdown files."""

import dataclasses
import os
import shutil


CONTENT_PATH = "content"
GERMAN = "de"
ENGLISH = "en"




@dataclasses.dataclass(frozen=True)
class Page(object):
    name: str
    template_name: str
    content: str = dataclasses.field(default_factory=lambda: "")
    render_german: bool = True

    def get_markdown_string(self, language: str = GERMAN) -> str:
        if language is GERMAN:
            slug = self.name
        else:
            if self.render_german:
                slug = f"{self.name}/{language}"
            # XXX: Special case for english index pge
            else:
                slug = language

        # XXX: We add language to title instead of 'lang' because
        # we want to avoid that pelican auto adds a suffix to the
        # files slug, but we still want to forward the language
        # code information to the jinja2 template.
        return fr"""title: {language}
template: {self.template_name}
Slug: {slug}
date: 11.06.2022
"""

    def render(self):
        if self.render_german:
            with open(f"{CONTENT_PATH}/{self.name}.md", "w") as f:
                f.write(self.get_markdown_string(GERMAN))

        directory_path = f"{CONTENT_PATH}/{self.name}"
        try:
            os.mkdir(directory_path)
        except FileExistsError:
            pass
        with open(f"{directory_path}/{ENGLISH}.md", "w") as f:
            f.write(self.get_markdown_string(ENGLISH))


PAGE_TUPLE = (
    Page("maps", "maps", ""),
    Page("artists", "homepage", ""),
    # XXX: This is the english index page.
    Page("/", "index", "", render_german=False),
)


if __name__ == "__main__":
    # CLeanup data from previous run
    try:
        shutil.rmtree(CONTENT_PATH)
    except FileNotFoundError:
        pass

    # Generate new data
    os.mkdir(CONTENT_PATH)

    for page in PAGE_TUPLE:
        page.render()
