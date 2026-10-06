{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPKy6Dsa67hdJG+NuSH/mo3",
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
        "<a href=\"https://colab.research.google.com/github/hjk99928/MathClass/blob/main/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "LqefC5qtIcK9",
        "outputId": "3134f9e4-432d-4159-d0bf-7f4369a98954"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "관계 R: {(2, 3), (3, 2), (1, 2), (3, 4)}\n",
            "관계 행렬:(rows: A, columns: B):\n",
            "[[1 0 0]\n",
            " [0 1 0]\n",
            " [1 0 1]]\n",
            "\n",
            "합성관계 R*S: {(1, 'x'), (2, 'y'), (3, 'x')}\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "import networkx as nx\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "A={1,2,3}\n",
        "B={2,3,4}\n",
        "#A에서B로 가는 이항관계 R\n",
        "R={(1,2),(2,3),(3,2),(3,4)}\n",
        "\n",
        "print(\"관계 R:\",R)\n",
        "\n",
        "A_list=sorted(A)\n",
        "B_list=sorted(B)\n",
        "\n",
        "relation_matrix=np.zeros((len(A_list),len(B_list)),dtype=int)\n",
        "\n",
        "for i,a in enumerate(A_list):\n",
        "    for j,b in enumerate(B_list):\n",
        "        if (a,b) in R:\n",
        "            relation_matrix[i][j]=1\n",
        "\n",
        "print(\"관계 행렬:(rows: A, columns: B):\")\n",
        "print(relation_matrix)\n",
        "\n",
        "#R:A->B\n",
        "#S:B->C\n",
        "C={'x','y'}\n",
        "S={(2,'x'),(3,'y'),(4,'x')}\n",
        "\n",
        "#합성관계 R*S\n",
        "composed_relation=set()\n",
        "\n",
        "for (a,b1) in R:\n",
        "    for (b2,c) in S:\n",
        "        if b1==b2:\n",
        "            composed_relation.add((a,c))\n",
        "\n",
        "print(\"\\n합성관계 R*S:\",composed_relation)"
      ]
    }
  ]
}
