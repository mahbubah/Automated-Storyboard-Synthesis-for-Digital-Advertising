# Automated-Storyboard-Synthesis-for-Digital-Advertising

## Business objective  


Recent advancements in machine learning, natural language processing, and computer vision, alongside the development of Large Language Models (LLMs), have ushered in a new era of capabilities in the digital domain. These technologies enable the intricate processing and interpretation of data, facilitating the creation of detailed, dynamic content that bridges the gap between textual concepts and visual storytelling. The integration of these technologies not only simplifies the translation of complex ideas into tangible visuals but also enhances creativity and efficiency in content generation. The business objective of the challenge is to harness these capabilities to transform textual descriptions of advertisement concepts and assets into detailed storyboards. This transformation process aims to visually depict the narrative flow and user interaction within advertisements, making the conceptualization of digital campaigns both more intuitive and impactful.

## Introduction

In the realm of digital advertising, advancements in machine learning, natural language processing (NLP), and computer vision have revolutionized the creation of captivating and impactful campaigns. These technologies enable the interpretation of complex data, allowing for the seamless integration of textual concepts and visual storytelling in advertisements.

This transformative era of advertising recognizes the power of technology to streamline and enhance the ad creation process. As part of this initiative, the goal is to develop a machine learning solution that automates the conversion of textual advertisement concepts and asset descriptions into visually compelling storyboards. This solution will interpret provided concepts and assets, generate relevant visual and textual assets, and compose these assets into individual ad frames. Ultimately, it will synthesize a cohesive storyboard that encapsulates the essence of the proposed ad campaign.

## Implementation

### Image processing using OpenCV

Locating a smaller template image within a larger image. This function converts the larger image to grayscale for template matching, then uses OpenCV’s matchTemplet function to find the best match for the template within the larger image and draws a rectangle around the detected area

Analyzing the color composition of an image and extracting prominent colors. This function uses the extcolors library to extract colors from the specified image path, applying a tolerance level and a limit on the number of colors to extract.Then Converts the extracted RGB colors to HEX format and organizes them into a dataFrame and creates a pie chart representing the distribution of the extracted colors and displays the original image alongside it

Extracting text from an image using Tesseract OCR (Optical Character Recognition). This function first identifies the background color and replaces non-text colors with a specified background color, thereby enhancing the visibility of the text. Then extracts text from an image using Tesseract OCR

### Image Composition

The purpose of this task is to compose assets into advertisement frames that are not only aesthetically pleasing but also effectively convey the intended message. So the task involves determining the optimal positions for each asset within a frame, adjusting the size of each assets 
The function first loads the images using PIL (Python Imaging Library) and converts them to RGBA format (which includes an alpha channel for transparency).Then I determined the maximum width by the widest of the images provided to maintain alignment and the total height is calculated as the sum of the heights of all the images.Then the function effectively combines images one stacked image.

### Building the Storyboard

The implementation visualizes storyboard by arranging a series of combined images or frames horizontally, each accompanied by a label.The function computes the total width of the storyboard by multiplying the width of a single image by the number of images and Sets the height of the storyboard to the height of the images plus additional space (50 pixels) for the labels below them. Next Iterates over each image and its corresponding label to paste the images where I Initialized a new blank image (the storyboard) with the calculated dimensions, filling it with a white background.



## Getting Started

Clone the repository:

    git clone https://github.com/mahbubah/Automated-Storyboard-Synthesis-for-Digital-Advertising

Navigate to the project directory:

    cd Automated-Storyboard-Synthesis-for-Digital-Advertising

Install the required Python packages:

    pip install -r requirements.txt


## Project structure

    notebooks/: Contains the project main fuctionalities with visualization.
    output/: Have output image of the project.
    utils/: Contains fuctions that can be reused.
    tests/: Includes unit test for the project.


## Contributing

Pull requests are welcome. Please update as appropriate.


## License

This project is licensed under the MIT License. See the LICENSE file for details.