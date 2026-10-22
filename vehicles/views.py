from pathlib import Path

import pandas as pd
from django.shortcuts import render

from .dashboard import frequency_table

BASE_DIR = Path(__file__).resolve().parent.parent


def dashboard_view(request):
    df = pd.read_csv(BASE_DIR / "vehicles_ml_dataset.csv")

    return render(request, "vehicles/index.html", {"frequency_table": frequency_table(df)})
