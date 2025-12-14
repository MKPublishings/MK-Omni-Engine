import shutil
import time


def export_legacy(source="slizzai-5", destination="exports/SlizzAi5_Legacy.zip"):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    archive_name = destination.replace(".zip", f"_{timestamp}.zip")
    shutil.make_archive(archive_name.replace(".zip", ""), 'zip', source)
    print(f"📦 Legacy Export Complete: {archive_name}")


if __name__ == "__main__":
    export_legacy()
