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
    title_english: str
    title_german: str
    name: str
    template_name: str
    content_german: str = dataclasses.field(default_factory=lambda: "")
    content_english: str = dataclasses.field(default_factory=lambda: "")
    render_german: bool = True

    def get_markdown_string(self, language: str = GERMAN) -> str:
        if language is GERMAN:
            slug = self.name
            title = self.title_german
            content = self.content_german
        else:
            content = self.content_english
            title = self.title_english
            if self.render_german:
                slug = f"{self.name}/{language}"
            # XXX: Special case for english index pge
            else:
                slug = language

        # XXX: We add language to title instead of 'lang' because
        # we want to avoid that pelican auto adds a suffix to the
        # files slug, but we still want to forward the language
        # code information to the jinja2 template.
        return fr"""title: {title}
Description: {content}
template: {self.template_name}
Slug: {slug}
date: 11.06.2022
data_slot: {language}
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
    Page("Kontaktieren Sie uns", "Contact us", "contact", "contact", ""),
    Page("Karte und Wegbeschreibung", "Map and directions", "maps", "maps", ""),
    Page(
        "Künstler:innen der ersten Ausgabe des ya¹ Tagesfestival für aktuelle Musik",
        "Acts of the first edition of the ya¹ day festival for contemporary music",
        "acts",
        "acts",
        content_german="Beim ya¹ Festival werden Virginia Nicoli, Callum Armstrong, Johannes Winkler, VOX NOSTRA, das ya¹ Ensemble und Tamon Yashima spielen.",
        content_english="Virginia Nicoli, Callum Armstrong, Johannes Winkler, VOX NOSTRA, the ya¹ Ensemble and Tamon Yashima will perform at the ya¹ festival.",
    ),
    Page(
        "Tickets kaufen für das ya¹ Tagesfestival für aktuelle Musik",
        "Buy tickets for the ya¹ day festival for contemporary music",
        "tickets",
        "tickets",
        content_german="Sie können entweder einen Festivalpass oder Einzeltickets für die jeweiligen Konzerte erwerben.",
        content_english="You can either buy a festival ticket or alternatively tickets for single concerts.",
    ),
    Page(
        "Das Festivalteam des ya¹ Tagesfestival für aktuelle Musik stellt sich vor",
        "Festival team",
        "team",
        "team",
        "",
    ),
    Page("Impressum", "Impressum", "impressum", "impressum", ""),
    Page("Datenschutz", "Datenschutz", "datenschutz", "datenschutz", ""),
    # Page("sponsors", "homepage", ""),
    # XXX: This is the english index page.
    Page(
        "ya¹ Tagesfestival für aktuelle Musik",
        "ya¹ day festival for contemporary music",
        "/",
        "index",
        content_german="Im ya¹ Tagesfestival für aktuelle Musik performen unterschiedliche Vertreter:innen räumlich und zeitlich getrennter avancierter Musiktraditionen innerhalb der in ihrer Tradition angemessenen Aufführungsbedingungen.",
        content_english="Different representatives of spatially and temporally separated advanced musical traditions perform within the performance conditions appropriate to their tradition.",
        render_german=False,
    ),
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
