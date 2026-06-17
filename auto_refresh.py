# ============================================================
# Project  : Sales Analysis Dashboard
# Script   : auto_refresh.py
# Purpose  : Automate the full data pipeline every 24 hours
# Usage    : Run this script to refresh data automatically
#            Power BI will pick up the updated Excel file
# Author   : Zoya
# Date     : 2026
# ============================================================

import subprocess
import time
import os
from datetime import datetime


def check_files_exist():
    """Check that required data files are present."""
    files = ['raw_sales_data.csv', 'clean_sales_data.xlsx']
    for file in files:
        status = "✅" if os.path.exists(file) else "❌ MISSING"
        print(f"  {status} {file}")


def run_pipeline():
    """Run the full data pipeline: generate → clean → verify."""
    print("─" * 45)
    print(f"🔄 Pipeline started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("─" * 45)

    # Step 1 — Generate fresh sales data
    print("\n📊 Step 1 : Generating new data...")
    subprocess.run(['python', 'generate_data.py'], check=True)
    print("✅ Data generated!")

    # Step 2 — Clean and engineer features
    print("\n🧹 Step 2 : Cleaning data...")
    subprocess.run(['python', 'clean_data.py'], check=True)
    print("✅ Data cleaned!")

    # Step 3 — Verify output files exist
    print("\n📁 Step 3 : Verifying output files...")
    check_files_exist()

    print("\n" + "─" * 45)
    print(f"✅ Pipeline completed : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("─" * 45)


def start_auto_refresh(hours=24):
    """
    Run the pipeline automatically every X hours.
    After each run, the Power BI file can be manually refreshed
    to show the latest data.

    Press Ctrl+C to stop.
    """
    print(f"🚀 Auto refresh started!")
    print(f"⏰ Interval : every {hours} hours")
    print("🛑 Press Ctrl+C to stop\n")

    while True:
        try:
            run_pipeline()
            seconds = hours * 3600
            print(f"\n😴 Next refresh in {hours} hours...")
            time.sleep(seconds)

        except KeyboardInterrupt:
            print("\n⛔ Auto refresh stopped by user.")
            break


def manual_refresh():
    """Run a single manual refresh of the pipeline."""
    print("🔄 Running manual refresh...\n")
    run_pipeline()
    print("\n✅ Done!")
    print("💡 Next step : Open Power BI → Home → Refresh")


# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    # Run a manual refresh by default
    # To enable auto refresh every 24 hours, comment the line below
    # and uncomment: start_auto_refresh(hours=24)
    manual_refresh()
    # start_auto_refresh(hours=24)
