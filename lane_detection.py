{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "lane_detection.py",
      "provenance": [],
      "authorship_tag": "ABX9TyP7A40FQARqTVOjOhSFUMDb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Neeraj-007/TAB-015/blob/main/lane_detection_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "1sNOK5Aj_ZZE"
      },
      "outputs": [],
      "source": [
        "\n",
        "import matplotlib.pylab as plt\n",
        "import cv2\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "\n",
        "def region_of_interest(img, vertices):\n",
        "    mask = np.zeros_like(img)\n",
        "    match_mask_color = 255\n",
        "    cv2.fillPoly(mask, vertices, match_mask_color)\n",
        "    masked_image = cv2.bitwise_and(img, mask)\n",
        "    return masked_image\n",
        "\n",
        "\n",
        "\n",
        "def drow_the_lines(img, lines):\n",
        "    img = np.copy(img)\n",
        "    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)\n",
        "\n",
        "    for line in lines:\n",
        "        for x1, y1, x2, y2 in line:\n",
        "            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)\n",
        "\n",
        "    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)\n",
        "    return img\n",
        "\n",
        "\n",
        "def process(image):\n",
        "    print(image.shape)\n",
        "    height = image.shape[0]\n",
        "    width = image.shape[1]\n",
        "   \n",
        "\n",
        "    region_of_interest_vertices = [\n",
        "    \n",
        "            (0, height/2),\n",
        "            (0,height),\n",
        "            (width/2, height),\n",
        "            (width/2,height/2)\n",
        "        ]\n",
        "\n",
        "\n",
        "\n",
        "    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)\n",
        "    canny_image = cv2.Canny(gray_image, 100 , 120)\n",
        "    cropped_image = region_of_interest(canny_image,\n",
        "                    np.array([region_of_interest_vertices], np.int32),)\n",
        "    lines = cv2.HoughLinesP(cropped_image,\n",
        "                            rho=2,\n",
        "                            theta=np.pi/180,\n",
        "                            threshold=50,\n",
        "                            lines=np.array([]),\n",
        "                            minLineLength=40,\n",
        "                            maxLineGap=100)\n",
        "    image_with_lines = drow_the_lines(image, lines)\n",
        "    return image_with_lines\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "cap = cv2.VideoCapture('rpi-video-capture.mp4')\n",
        "\n",
        "while cap.isOpened():\n",
        "    ret, frame = cap.read()\n",
        "    \n",
        "    print(frame.shape)\n",
        "    frame = process(frame)\n",
        "    cv2.imshow('frames',frame)\n",
        "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
        "        break\n",
        "\n",
        "cap.release()\n",
        "cv2.destroyAllWindows()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "ZrYjz4ERAHgn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
