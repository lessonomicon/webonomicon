from fasthtml.ft import *

TITLE = "Staff and Experiments"

def all_staff(data, staff_id):
    rows = []
    logged_in_user = None
    for record in data:
        if record["staff_id"] == staff_id:
            logged_in_user = f"{record['personal']} {record['family']}"
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
            Script(src="htmx.js"),
        ),
        Body(
            H1(TITLE),
            Div(
                P(f"Welcome, {logged_in_user}"),
                logout_button(),
            ) if logged_in_user else None,
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
            login_form() if not logged_in_user else None
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


def logout_button():
    return Form(
        Button("Logout", type="submit"),
        method="post",
        action="/logout"
    )
