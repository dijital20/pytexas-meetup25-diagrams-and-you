"""Example data flow diagram."""

from pytm.pytm import Boundary, Actor, Server, TM, Dataflow

if __name__ == "__main__":
    tm = TM("example")
    tm.description = "Example Threat Model"
    tm.isOrdered = True

    user_boundary = Boundary("user")
    app_boundary = Boundary("app")
    service_boundary = Boundary("service")

    user = Actor("user")
    user.inBoundary = user_boundary

    app = Server("app")
    app.inBoundary = app_boundary

    service = Server("mobile service")
    service.inBoundary = service_boundary

    identity = Server("identity service")
    identity.inBoundary = service_boundary

    Dataflow(
        user,
        app,
        "User provides username and password.",
    )
    Dataflow(
        app,
        service,
        "App calls login API with username and password.",
    )
    Dataflow(
        service,
        identity,
        "Service calls authentication check in identity service.",
    )
    Dataflow(
        identity,
        service,
        "Identity service authenticates user.",
    )
    Dataflow(
        service,
        app,
        "Service authenticates the user and returns a token.",
    )
    Dataflow(
        app,
        user,
        "User is logged in.",
    )

    tm.process()
