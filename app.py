from flask import Flask, request, render_template
from ultralytics import YOLO
import cv2
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# Load YOLO model
model = YOLO("best.pt")

# Labels and colors
labels = {0: "Head", 1: "Helmet", 2: "Person"}
colors = {0: (0, 0, 255), 1: (0, 255, 0), 2: (255, 0, 0)}

# Create folders if not exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]
    if file.filename == "":
        return "No selected file."

    # Save uploaded file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join("uploads", filename)
    file.save(filepath)

    # Load original image
    image = cv2.imread(filepath)
    original_path = os.path.join("static", f"orig_{filename}")
    cv2.imwrite(original_path, image)

    # YOLO Detection
    results = model(image)[0]

    # Stats dictionary
    stats = {"Head": 0, "Helmet": 0, "Person": 0}

    # Draw results
    for det in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = det
        label = labels[int(class_id)]
        color = colors[int(class_id)]
        stats[label] += 1

        # Draw bounding box
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

        # Label + confidence
        conf_text = f"{label} {score:.2f}"
        cv2.putText(image, conf_text, (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Save processed output image
    output_filename = f"det_{filename}"
    output_path = os.path.join("static", output_filename)
    cv2.imwrite(output_path, image)

    # Render result page
    return render_template(
        "result.html",
        original=f"orig_{filename}",
        output=output_filename,
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)
