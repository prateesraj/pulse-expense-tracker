
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path
from datetime import datetime, date
from collections import defaultdict

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

DATA_FILE = Path(__file__).resolve().parent / "expenses.json"

BG = "#F5F6FC"
WHITE = "#FFFFFF"
INK = "#20213D"
MUTED = "#8588A5"
PURPLE = "#6857F5"
PURPLE_LIGHT = "#EFEDFF"
PINK = "#F65D91"
GREEN = "#16A886"
BLUE = "#438BFA"
ORANGE = "#F2A442"
BORDER = "#E9EAF3"
RED = "#E45468"
FONT = "Segoe UI"
CURRENCY = "₹"


# =========================================================
# DATA HELPERS
# =========================================================

def money(value):
    try:
        return f"{CURRENCY}{float(value):,.2f}"
    except (ValueError, TypeError):
        return f"{CURRENCY}0.00"


def amount_of(item):
    try:
        return float(item.get("amount", 0))
    except (ValueError, TypeError):
        return 0.0


def parse_date(value):
    if not value:
        return None

    formats = (
        "%d %B %Y",
        "%d %b %Y",
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
    )

    for fmt in formats:
        try:
            return datetime.strptime(str(value), fmt).date()
        except ValueError:
            pass

    try:
        return datetime.fromisoformat(str(value)).date()
    except ValueError:
        return None


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            messagebox.showwarning(
                "Data warning",
                "The expense file does not contain a list."
            )
            return []

        return [
            item for item in data
            if isinstance(item, dict) and "amount" in item
        ]

    except (json.JSONDecodeError, OSError) as error:
        messagebox.showerror(
            "Could not load expenses",
