from fasthtml.ft import *

TITLE = "Staff and Experiments"

def all_staff(data):
    rows = []
    for record in data:
        button = Button(
            "x",
            hx_get=f"/exp/{record['staff_id']}",
            hx_trigger="click",
            hx_target="#experiments",
            hx_swap="innerHTML",
        )
        rows.append(Tr(
            Td(button),
            Td(str(record["staff_id"])),
            Td(record["personal"]),
            Td(record["family"]),
        ))

    return Html(
        Head(
            Title(TITLE),
            Link(rel="stylesheet", href="page.css"),
            Script(src="https://unpkg.com/htmx.org@1.9.4"),
        ),
        Body(
            H1(TITLE),
            Table(
                Thead(
                    Tr(
                        Th("view"),
                        Th("staff ID"),
                        Th("personal name"),
                        Th("family name"),
                    ),
                ),
                Tbody(*rows),
            ),
            Div(id="experiments"),
            Hr(),
            login_form()
        )
    )


def experiments(data, staff_id):
    rows = []
    for record in data:
        rows.append(Tr(
            Td(str(record["sample_id"])),
            Td(record["kind"]),
            Td(str(record["start"])),
            Td(str(record["end"])),
        ))
    return Div(
        H2(f"Experimenter {staff_id}"),
        Table(
            Thead(
                Tr(
                    Th("sample ID"),
                    Th("kind"),
                    Th("start"),
                    Th("end"),
                ),
            ),
            Tbody(*rows),
        )
    )


def heartbeat(data):
    return P(data["message"])


def login_form():
    """Render a simple login form."""
    return Div(
        H2("Login"),
        Form(
            Input(type="text", name="username", placeholder="Enter your username"),
            Input(type="password", name="password", placeholder="Enter your password"),
            Button("Login", type="submit"),
            method="post",
            action="/login"
        )
    )