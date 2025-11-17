<h1>Steel Plant Safety Detection</h1>
<p>A deep learning-based web application for detection of safety equipment and personnel in steel plant environments. This system detects heads, helmets, and persons in images using YOLOv8 object detection.</p>

<img width="1651" height="707" alt="image" src="https://github.com/user-attachments/assets/3154585f-e5cc-4790-aeb3-cc3a6abb0f56" />

<h2>Features</h2>
<ul>
  <li>Real-time Detection: Detects helmets, heads, and persons in images</li>
  <li>Web Interface: User-friendly Flask web application for image uploads</li>
  <li>Visual Results: Side-by-side comparison of original and processed images</li>
  <li>Detection Statistics: Displays count of detected objects by category</li>
  <li>Production Ready: Deployed on Render with optimized dependencies</li>
</ul>

<h2>Tech Stack</h2>

- **Backend**: Flask (Python web framework)
- **ML Model**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Frontend**: Bootstrap 5

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/ksc1728/yolo-project.git
cd yolo-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
steel-plant-internship/
├── app.py                 # Flask application
├── main.py               # Model training script
├── best.pt               # Trained YOLOv8 model
├── requirements.txt      # Python dependencies
├── Procfile             # Render deployment configuration
├── render.yaml          # Render service configuration
├── dataset/
│   ├── config.yaml      # Dataset configuration
│   ├── train/           # Training images and labels
│   ├── valid/           # Validation images and labels
│   └── test/            # Test images and labels
├── templates/
│   ├── index.html       # Upload page
│   └── result.html      # Detection results page
├── static/              # Output images
└── uploads/             # Temporary uploaded files
```

## Usage

1. Visit the home page
2. Click "Choose Image" to select an image file
3. Click "Start Detection" to process the image
4. View the detection results showing:
   - Original image
   - Processed image with bounding boxes
   - Count of detected helmets, heads, and persons
5. Upload another image or return to home page

## Model Details

- **Model**: YOLOv8 (Medium variant)
- **Classes**: 3 (Head, Helmet, Person)
- **Training**: Trained on custom steel plant safety dataset
- **Framework**: Ultralytics YOLOv8

### Color Coding
- **Red**: Head (unprotected)
- **Green**: Helmet (protected)
- **Blue**: Person


## Model Training

To retrain the model with a new dataset:

```bash
python main.py
```

This will:
1. Load a pretrained YOLOv8n model
2. Train on the dataset specified in `dataset/config.yaml`
3. Save the trained model as `best.pt`

## Author

Created during internship at Steel Plant facility.

**Note**: The `best.pt` model file is required for the application to run. Ensure it's present in the project root directory.
