import os
import sys
from PIL import Image
import cv2

folder = "frames"
tmp_frame = ".tmp_frame.jpg"
video_path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

# ascii_chars = [ "@", "%", "#", "*", "+", "=", "-", ":", ".", " " ]
ascii_chars = [ " ", ".", ":", "-", "=", "+", "*", "#", "%", "@" ]

# Create main directory where the frame should be put
if not os.path.exists(folder):
    os.makedirs(folder)

basename = os.path.basename(video_path).split('.', 1)[0]
dir = os.path.join(folder, basename)
# Create directory for the video frames
if not os.path.exists(dir):
    os.makedirs(dir)

# Get video
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0
while success:
    # Write single frame to file
    cv2.imwrite(os.path.join(dir, tmp_frame), image)
    success,image = vidcap.read()

    # Get image
    img = Image.open(os.path.join(dir, tmp_frame))
    # Resize image
    w, h = img.size
    ratio = h / w
    height = int(width * ratio)
    img = img.resize((width, height))

    # Convert to grayscale
    img = img.convert("L")

    # Convert to ASCII
    pixels = img.getdata()
    chars = "".join([ascii_chars[pix // 26] for pix in pixels])

    # Format
    pix_count = len(chars)
    chars = "\n".join(chars[i:(i + width)] for i in range(0, pix_count, width))
    
    # Save result
    with open(os.path.join(dir, basename + "_frame" + str(count).zfill(4) + ".txt"), "w") as f:
        f.write(chars)

    img.close()

    count += 1

if os.path.exists(os.path.join(dir, tmp_frame)):
    os.remove(os.path.join(dir, tmp_frame))
