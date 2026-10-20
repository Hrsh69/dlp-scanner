import typer

app = typer.Typer(help="DLP scanner")


@app.callback()
def main() -> None:
    """Scan files, databases, and network captures for sensitive data."""


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo("dlp-scanner 0.1.0")


if __name__ == "__main__":
    app()