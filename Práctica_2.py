{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/Vedroom/IA/blob/main/Pr%C3%A1ctica_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Prueba de funcionamiento\n"
      ],
      "metadata": {
        "id": "IclukrbKObHw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a-Q0r4KsOWPY"
      },
      "outputs": [],
      "source": [
        "def suma (a,b):\n",
        "  resultado=a * b\n",
        "  return resultado"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(suma(2,3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P0U_CzyRS8rY",
        "outputId": "53024022-4de7-41f2-b56e-749fe787a476"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Práctica 1 - Parte 1: C a F"
      ],
      "metadata": {
        "id": "dIJQFhBNA2Da"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "1dXt1wfZA-eC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "celcius = np.array([-15, -5, 0, 5, 15], dtype=float)\n",
        "fahrenheit = np.array([5, 23, 32, 41, 59], dtype=float)"
      ],
      "metadata": {
        "id": "jHOYLCXSBo6U"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#capa = tf.keras.layers.Dense(units=1, input_shape=[1])\n",
        "#modelo = tf.keras.Sequential([capa])\n",
        "oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])\n",
        "oculta2 = tf.keras.layers.Dense(units=3)\n",
        "salida = tf.keras.layers.Dense(units=1)\n",
        "modelo = tf.keras.Sequential([oculta1, oculta2, salida])"
      ],
      "metadata": {
        "id": "EB8c8fi3CsH2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.compile(\n",
        "    optimizer = tf.keras.optimizers.Adam(0.1),\n",
        "    loss='mean_squared_error'\n",
        ")"
      ],
      "metadata": {
        "id": "QLQZcWjpDYIF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Comenzando entrenamiento...\")\n",
        "historial=modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)\n",
        "print(\"Modelo entrenado!!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NRDyAfoADn9q",
        "outputId": "5449f8a8-f7c0-4e28-bfc5-3766fac59f5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Comenzando entrenamiento...\n",
            "Modelo entrenado!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.xlabel(\"# Epoca\")\n",
        "plt.ylabel(\"Magnitud de pérdida\")\n",
        "plt.plot(historial.history[\"loss\"])"
      ],
      "metadata": {
        "id": "06YxMwYRE-St",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 467
        },
        "outputId": "ec1a67ba-79ca-4af2-d687-e81eb37367e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7964467405e0>]"
            ]
          },
          "metadata": {},
          "execution_count": 26
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAGwCAYAAABIC3rIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABGFklEQVR4nO3deXxTdb7/8Xe6JF3oAlRaKm1ZVPZtWGoVUC9IWa6ich1lURBGRgUVcBQZBVHUMuAwbrgwV2BmROH6G8QRESmL4FJBlgoUqSJoUWhRCg2LtE17fn+UHIiANJD0NOb1fDzymOScb5JPDo+x78d3OzbDMAwBAAAEsRCrCwAAALAagQgAAAQ9AhEAAAh6BCIAABD0CEQAACDoEYgAAEDQIxABAICgF2Z1AYGisrJSe/fuVUxMjGw2m9XlAACAajAMQ4cPH1ZycrJCQs7eD0Qgqqa9e/cqJSXF6jIAAMB52LNnjxo1anTW8wSiaoqJiZFUdUFjY2MtrgYAAFSH0+lUSkqK+Xf8bAhE1eQeJouNjSUQAQAQYM413YVJ1QAAIOgRiAAAQNAjEAEAgKBHIAIAAEGPQAQAAIIegQgAAAQ9AhEAAAh6BCIAABD0CEQAACDoEYgAAEDQIxABAICgRyACAABBj5u7WuzQsTIdKXUpJiJccZHhVpcDAEBQsryHaO3atbruuuuUnJwsm82mxYsXe5y32WxnfMyYMcNs07hx49POT5s2zeNztmzZou7duysiIkIpKSmaPn16Tfy8c/rLsnx1+8tq/fPTb60uBQCAoGV5IDp69Kjat2+vWbNmnfH8vn37PB5z5syRzWbTwIEDPdo98cQTHu3uvfde85zT6VTv3r2VlpamjRs3asaMGZoyZYpmz57t199WHSG2qv+tNKytAwCAYGb5kFnfvn3Vt2/fs55PSkryeP3OO+/ommuuUdOmTT2Ox8TEnNbWbf78+SorK9OcOXNkt9vVunVr5ebmaubMmRo1atQZ31NaWqrS0lLztdPprO5P8kqIrSoRVRokIgAArGJ5D5E3ioqK9N5772nkyJGnnZs2bZrq16+vjh07asaMGXK5XOa5nJwc9ejRQ3a73TyWmZmp/Px8HTx48IzflZWVpbi4OPORkpLi+x+kU3uICEQAAFgloALRP/7xD8XExOimm27yOH7fffdpwYIFWr16tf74xz/q6aef1kMPPWSeLywsVGJiosd73K8LCwvP+F0TJ05USUmJ+dizZ4+Pf02VkBB6iAAAsJrlQ2bemDNnjoYMGaKIiAiP4+PHjzeft2vXTna7XX/84x+VlZUlh8NxXt/lcDjO+73eODlk5vevAgAAZxEwPUQfffSR8vPz9Yc//OGcbdPT0+VyufTtt99KqpqHVFRU5NHG/fps845qCkNmAABYL2AC0WuvvaZOnTqpffv252ybm5urkJAQNWjQQJKUkZGhtWvXqry83GyTnZ2t5s2bq27dun6ruTrcPUTkIQAArGN5IDpy5Ihyc3OVm5srSdq9e7dyc3NVUFBgtnE6nXrrrbfO2DuUk5OjZ599Vl988YV27dql+fPna9y4cRo6dKgZdgYPHiy73a6RI0cqLy9PCxcu1HPPPecx1GYV24lAVMGYGQAAlrF8DtGGDRt0zTXXmK/dIWXYsGGaN2+eJGnBggUyDEODBg067f0Oh0MLFizQlClTVFpaqiZNmmjcuHEeYScuLk7Lly/X6NGj1alTJyUkJGjy5MlnXXJfk0JPRFKGzAAAsI7NMPhLXB1Op1NxcXEqKSlRbGyszz73r8vz9cKqnRp+RWNNub61zz4XAABU/++35UNmwc7GxowAAFiOQGQxVpkBAGA9ApHFQsxJ1RYXAgBAECMQWSw0xL3snh4iAACsQiCymI0hMwAALEcgshi37gAAwHoEIosxqRoAAOsRiCxm9hDRRQQAgGUIRBZjyAwAAOsRiCzGkBkAANYjEFksJIS73QMAYDUCkcW4dQcAANYjEFnMPWRWwSQiAAAsQyCyWCiTqgEAsByByGLuVWbcugMAAOsQiCzGrTsAALAegchi7EMEAID1CEQWCznxL0APEQAA1iEQWSyEZfcAAFiOQGSxk/cys7gQAACCGIHIYvQQAQBgPQKRxdwbM5KHAACwDoHIYu5bd1SQiAAAsAyByGLc7R4AAOsRiCwWGsI+RAAAWI1AZDFu3QEAgPUIRBbj1h0AAFiPQGQxdw9RBfsQAQBgGQKRxRgyAwDAegQii3EvMwAArEcgshh3uwcAwHoEIotx6w4AAKxHILKYuTEjXUQAAFiGQGQxG0NmAABYjkBksZM7VZOIAACwCoHIYtztHgAA61keiNauXavrrrtOycnJstlsWrx4scf54cOHy2azeTz69Onj0aa4uFhDhgxRbGys4uPjNXLkSB05csSjzZYtW9S9e3dFREQoJSVF06dP9/dPqxYmVQMAYD3LA9HRo0fVvn17zZo166xt+vTpo3379pmPN9980+P8kCFDlJeXp+zsbC1ZskRr167VqFGjzPNOp1O9e/dWWlqaNm7cqBkzZmjKlCmaPXu2335Xdblv3VHBJCIAACwTZnUBffv2Vd++fX+1jcPhUFJS0hnPffnll1q2bJk+//xzde7cWZL0wgsvqF+/fnrmmWeUnJys+fPnq6ysTHPmzJHdblfr1q2Vm5urmTNnegQnK7APEQAA1rO8h6g6PvzwQzVo0EDNmzfX3XffrQMHDpjncnJyFB8fb4YhSerVq5dCQkK0bt06s02PHj1kt9vNNpmZmcrPz9fBgwfP+J2lpaVyOp0eD39wT6rm1h0AAFin1geiPn366J///KdWrlypv/zlL1qzZo369u2riooKSVJhYaEaNGjg8Z6wsDDVq1dPhYWFZpvExESPNu7X7ja/lJWVpbi4OPORkpLi658m6ZR9iAhEAABYxvIhs3O59dZbzedt27ZVu3bt1KxZM3344Yfq2bOn37534sSJGj9+vPna6XT6JRSxDxEAANar9T1Ev9S0aVMlJCRo586dkqSkpCTt37/fo43L5VJxcbE57ygpKUlFRUUebdyvzzY3yeFwKDY21uPhD+YcIhIRAACWCbhA9P333+vAgQNq2LChJCkjI0OHDh3Sxo0bzTarVq1SZWWl0tPTzTZr165VeXm52SY7O1vNmzdX3bp1a/YH/ELYiTGzCobMAACwjOWB6MiRI8rNzVVubq4kaffu3crNzVVBQYGOHDmiBx98UJ999pm+/fZbrVy5UgMGDNAll1yizMxMSVLLli3Vp08f3XnnnVq/fr0++eQTjRkzRrfeequSk5MlSYMHD5bdbtfIkSOVl5enhQsX6rnnnvMYErOKe1K1ix4iAAAsY3kg2rBhgzp27KiOHTtKksaPH6+OHTtq8uTJCg0N1ZYtW3T99dfrsssu08iRI9WpUyd99NFHcjgc5mfMnz9fLVq0UM+ePdWvXz9169bNY4+huLg4LV++XLt371anTp30wAMPaPLkyZYvuZdO6SEiEAEAYBmbwXrvanE6nYqLi1NJSYlP5xMdOFKqTk+ukCTtzupnTrIGAAAXrrp/vy3vIQp2YSEn/wnoJQIAwBoEIoudkoeYRwQAgEUIRBajhwgAAOsRiCzmXmUmsfQeAACrEIgsFnZqIKogEAEAYAUCkcVCQmxyLyxjDhEAANYgENUC7EUEAIC1CES1wMndqistrgQAgOBEIKoFQm30EAEAYCUCUS3A/cwAALAWgagWCAut+meoJBABAGAJAlEtQA8RAADWIhDVAqwyAwDAWgSiWoAeIgAArEUgqgVO9hCx7B4AACsQiGoBs4eIW3cAAGAJAlEtEMocIgAALEUgqgVCQ6r+GZhDBACANQhEtYA5h8ggEAEAYAUCUS1gDpkxhwgAAEsQiGqBMJbdAwBgKQJRLcCkagAArEUgqgXCQt09ROxDBACAFQhEtYB7lRk9RAAAWINAVAuc6CBiDhEAABYhENUCYaEn9iFilRkAAJYgENUC9hOBqLyCOUQAAFiBQFQLhJ8YMyMQAQBgDQJRLWAPq/pnKCMQAQBgCQJRLRB+YsiszEUgAgDACgSiWiCcOUQAAFiKQFQLOMLoIQIAwEoEolrgZA8Ry+4BALACgagWYFI1AADWIhDVAkyqBgDAWgSiWoB9iAAAsBaBqBZwT6omEAEAYA3LA9HatWt13XXXKTk5WTabTYsXLzbPlZeXa8KECWrbtq2io6OVnJys22+/XXv37vX4jMaNG8tms3k8pk2b5tFmy5Yt6t69uyIiIpSSkqLp06fXxM+rFobMAACwluWB6OjRo2rfvr1mzZp12rljx45p06ZNmjRpkjZt2qRFixYpPz9f119//Wltn3jiCe3bt8983HvvveY5p9Op3r17Ky0tTRs3btSMGTM0ZcoUzZ4926+/rbrMQMQqMwAALBFmdQF9+/ZV3759z3guLi5O2dnZHsdefPFFde3aVQUFBUpNTTWPx8TEKCkp6YyfM3/+fJWVlWnOnDmy2+1q3bq1cnNzNXPmTI0aNcp3P+Y8uVeZldNDBACAJSzvIfJWSUmJbDab4uPjPY5PmzZN9evXV8eOHTVjxgy5XC7zXE5Ojnr06CG73W4ey8zMVH5+vg4ePHjG7yktLZXT6fR4+MvJHiICEQAAVjjvHqJjx46poKBAZWVlHsfbtWt3wUWdzfHjxzVhwgQNGjRIsbGx5vH77rtPv/vd71SvXj19+umnmjhxovbt26eZM2dKkgoLC9WkSROPz0pMTDTP1a1b97TvysrK0uOPP+6333IqJlUDAGAtrwPRjz/+qDvuuEPvv//+Gc9XVFRccFFnUl5ert///vcyDEMvv/yyx7nx48ebz9u1aye73a4//vGPysrKksPhOK/vmzhxosfnOp1OpaSknF/x58CkagAArOX1kNnYsWN16NAhrVu3TpGRkVq2bJn+8Y9/6NJLL9V//vMff9RohqHvvvtO2dnZHr1DZ5Keni6Xy6Vvv/1WkpSUlKSioiKPNu7XZ5t35HA4FBsb6/HwF/c+RAQiAACs4XUP0apVq/TOO++oc+fOCgkJUVpamq699lrFxsYqKytL/fv392mB7jD09ddfa/Xq1apfv/4535Obm6uQkBA1aNBAkpSRkaFHHnlE5eXlCg8PlyRlZ2erefPmZxwuq2kR4aGSpFICEQAAlvC6h+jo0aNm0Khbt65+/PFHSVLbtm21adMmrws4cuSIcnNzlZubK0navXu3cnNzVVBQoPLycv3P//yPNmzYoPnz56uiokKFhYUqLCw05y7l5OTo2Wef1RdffKFdu3Zp/vz5GjdunIYOHWqGncGDB8tut2vkyJHKy8vTwoUL9dxzz3kMiVnJEV71z1Dq8s9wIwAA+HVe9xA1b95c+fn5aty4sdq3b69XX31VjRs31iuvvKKGDRt6XcCGDRt0zTXXmK/dIWXYsGGaMmWKOQzXoUMHj/etXr1aV199tRwOhxYsWKApU6aotLRUTZo00bhx4zzCTlxcnJYvX67Ro0erU6dOSkhI0OTJk2vFkntJigir6iE6Xk4PEQAAVrAZhuHVboCvv/66XC6Xhg8fro0bN6pPnz4qLi6W3W7XvHnzdMstt/irVks5nU7FxcWppKTE5/OJCkuO6/KslQoLsWnn0/18+tkAAASz6v799rqHaOjQoebzTp066bvvvtOOHTuUmpqqhISE86s2yLmX3bsqDbkqKhUWGnDbQwEAENAueKfqqKgo/e53v/NFLUHLPalaqppYTSACAKBmVSsQeTP52L0ZIqrP3UMkScfLKxTtsPyOKgAABJVq/eXdvHmzx+tNmzbJ5XKpefPmkqSvvvpKoaGh6tSpk+8rDAIhITbZQ0NUVlHJ0nsAACxQrUC0evVq8/nMmTMVExOjf/zjH+ay9oMHD+qOO+5Q9+7d/VNlEHCEVwWi4+UsvQcAoKZ5PVnlr3/9q7Kysjw2NKxbt66efPJJ/fWvf/VpccHEwdJ7AAAs43Ugcjqd5maMp/rxxx91+PBhnxQVjCLYnBEAAMt4HYhuvPFG3XHHHVq0aJG+//57ff/99/r3v/+tkSNH6qabbvJHjUHBvdKMHiIAAGqe18uZXnnlFf3pT3/S4MGDVV5eXvUhYWEaOXKkZsyY4fMCg4V7pRk9RAAA1DyvA1FUVJReeuklzZgxQ998840kqVmzZoqOjvZ5ccGEHiIAAKxz3hveREdHq127dr6sJagxhwgAAOtUKxDddNNNmjdvnmJjY885T2jRokU+KSzYuFeZldJDBABAjatWIIqLi5PNZjOfw/fcPUTH6SECAKDGVSsQzZ0794zP4TsR5j5EBCIAAGoadxGtJRzuOUQMmQEAUOOq1UPUsWNHc8jsXDZt2nRBBQUrc6dqhswAAKhx1QpEN9xwg/n8+PHjeumll9SqVStlZGRIkj777DPl5eXpnnvu8UuRwYBl9wAAWKdageixxx4zn//hD3/Qfffdp6lTp57WZs+ePb6tLoiwMSMAANbxeg7RW2+9pdtvv/2040OHDtW///1vnxQVjOghAgDAOl4HosjISH3yySenHf/kk08UERHhk6KC0ckeIgIRAAA1zeudqseOHau7775bmzZtUteuXSVJ69at05w5czRp0iSfFxgsTvYQMWQGAEBN8zoQPfzww2ratKmee+45vf7665Kkli1bau7cufr973/v8wKDhbkxI4EIAIAa51UgcrlcevrppzVixAjCj4+Zt+5gyAwAgBrn1RyisLAwTZ8+XS6Xy1/1BC3z5q70EAEAUOO8nlTds2dPrVmzxh+1BDVWmQEAYB2v5xD17dtXDz/8sLZu3apOnTopOjra4/z111/vs+KCCfsQAQBgHa8DkXs36pkzZ552zmazqaKCP+jngx4iAACs43UgqqzkD7Y/mKvM6CECAKDGXdDd7o8fP+6rOoKeucqMHiIAAGqc14GooqJCU6dO1cUXX6w6depo165dkqRJkybptdde83mBwcJxSg+RYRgWVwMAQHA5ZyBauHChCgoKzNdPPfWU5s2bp+nTp8tut5vH27Rpo//93//1T5VBwD2HyDCk8goCEQAANemcgSgiIkI9evTQF198IUn6xz/+odmzZ2vIkCEKDQ0127Vv3147duzwX6W/ce5VZhLziAAAqGnnnFQ9YMAAJSYmaujQodq6dav27t2rSy655LR2lZWVKi8v90uRwcAeGiKbraqH6Hh5hWIjwq0uCQCAoFGtOUSXX365uRljq1at9NFHH53W5v/9v/+njh07+ra6IGKz2U7uRcTEagAAalS1l93Xq1dPkjR58mQNGzZMP/zwgyorK7Vo0SLl5+frn//8p5YsWeK3QoNBRHiojpdXsjkjAAA1zOtVZgMGDNC7776rFStWKDo6WpMnT9aXX36pd999V9dee60/agwaEWFszggAgBW83phRkrp3767s7Gxf1xL03Evv6SECAKBmnffGjBs2bNC//vUv/etf/9LGjRvPu4C1a9fquuuuU3Jysmw2mxYvXuxx3jAMTZ48WQ0bNlRkZKR69eqlr7/+2qNNcXGxhgwZotjYWMXHx2vkyJE6cuSIR5stW7aoe/fuioiIUEpKiqZPn37eNfsLPUQAAFjD60D0/fffq3v37uratavuv/9+3X///erSpYu6deum77//3usCjh49qvbt22vWrFlnPD99+nQ9//zzeuWVV7Ru3TpFR0crMzPTY5fsIUOGKC8vT9nZ2VqyZInWrl2rUaNGmeedTqd69+6ttLQ0bdy4UTNmzNCUKVM0e/Zsr+v1J/P2HeX0EAEAUKMML2VmZhrp6enGjh07zGM7duwwMjIyjMzMTG8/zoMk4+233zZfV1ZWGklJScaMGTPMY4cOHTIcDofx5ptvGoZhGNu3bzckGZ9//rnZ5v333zdsNpvxww8/GIZhGC+99JJRt25do7S01GwzYcIEo3nz5met5fjx40ZJSYn52LNnjyHJKCkpuaDf+GtufvlTI23CEuO9LXv99h0AAASTkpKSav399rqHaM2aNXr55ZfVvHlz81jz5s31wgsvaO3atT4LapK0e/duFRYWqlevXuaxuLg4paenKycnR5KUk5Oj+Ph4de7c2WzTq1cvhYSEaN26dWabHj16eOysnZmZqfz8fB08ePCM352VlaW4uDjzkZKS4tPfdiYOeogAALCE14EoJSXljBswVlRUKDk52SdFuRUWFkqSEhMTPY4nJiaa5woLC9WgQQOP82FhYapXr55HmzN9xqnf8UsTJ05USUmJ+dizZ8+F/6BzcN++o9TFHCIAAGqS14FoxowZuvfee7Vhwwbz2IYNG3T//ffrmWee8WlxVnI4HIqNjfV4+P07w+ghAgDACl4vux8+fLiOHTum9PR0hYVVvd3lciksLEwjRozQiBEjzLbFxcUXVFxSUpIkqaioSA0bNjSPFxUVqUOHDmab/fv3e7zP5XKpuLjYfH9SUpKKioo82rhfu9vUBu4eIlaZAQBQs7wORM8++6wfyjizJk2aKCkpSStXrjQDkNPp1Lp163T33XdLkjIyMnTo0CFt3LhRnTp1kiStWrVKlZWVSk9PN9s88sgjKi8vV3h41T3CsrOz1bx5c9WtW7fGfs+5mLfuYB8iAABqlNeBaNiwYT4t4MiRI9q5c6f5evfu3crNzVW9evWUmpqqsWPH6sknn9Sll16qJk2aaNKkSUpOTtYNN9wgSWrZsqX69OmjO++8U6+88orKy8s1ZswY3XrrreacpsGDB+vxxx/XyJEjNWHCBG3btk3PPfec/va3v/n0t1woeogAALDGee1U7UsbNmzQNddcY74eP368pKrgNW/ePD300EM6evSoRo0apUOHDqlbt25atmyZIiIizPfMnz9fY8aMUc+ePRUSEqKBAwfq+eefN8/HxcVp+fLlGj16tDp16qSEhARNnjzZY6+i2oB9iAAAsIbNMAzD6iICgdPpVFxcnEpKSvw2wfr5lV9rZvZXGtQ1VVk3tfXLdwAAEEyq+/f7vG/dAd9z9xCV0kMEAECNIhDVIuYcIiZVAwBQo847EO3cuVMffPCBfv75Z0lVN2HFhTFXmTGpGgCAGuV1IDpw4IB69eqlyy67TP369dO+ffskSSNHjtQDDzzg8wKDCT1EAABYw+tANG7cOIWFhamgoEBRUVHm8VtuuUXLli3zaXHBxhF24tYd9BABAFCjvF52v3z5cn3wwQdq1KiRx/FLL71U3333nc8KC0bmzV3pIQIAoEZ53UN09OhRj54ht+LiYjkcDp8UFawiwtiYEQAAK3gdiLp3765//vOf5mubzabKykpNnz7dY4NFeM9cdk8PEQAANcrrIbPp06erZ8+e2rBhg8rKyvTQQw8pLy9PxcXF+uSTT/xRY9Bw0EMEAIAlvO4hatOmjb766it169ZNAwYM0NGjR3XTTTdp8+bNatasmT9qDBrcugMAAGuc173M4uLi9Mgjj/i6lqDnOLHsvtRFDxEAADWpWoFoy5Yt1f7Adu3anXcxwS7ixMaMZa5KVVYaCgmxWVwRAADBoVqBqEOHDrLZbDIMQzbbyT/S7t2pTz1WUcFwz/lyb8woVfUSRdpDf6U1AADwlWrNIdq9e7d27dql3bt369///reaNGmil156Sbm5ucrNzdVLL72kZs2a6d///re/6/1Nc9+6Q2KlGQAANalaPURpaWnm85tvvlnPP/+8+vXrZx5r166dUlJSNGnSJN1www0+LzJYhIWGyB4WojJXpY6UuhQfZbe6JAAAgoLXq8y2bt2qJk2anHa8SZMm2r59u0+KCmYJ0VUhqKD4mMWVAAAQPLwORC1btlRWVpbKysrMY2VlZcrKylLLli19WlwwqhNR1Wk3+O/rVFFpWFwNAADBwetl96+88oquu+46NWrUyFxRtmXLFtlsNr377rs+LzDYFDlLzedf7z+sFkmxFlYDAEBw8DoQde3aVbt27dL8+fO1Y8cOSVV3uh88eLCio6N9XmCwKfm53Hy+6btDBCIAAGrAeW3MGB0drVGjRvm6Fkh64NrL9NfsryRJB46UnqM1AADwBa/nEMG/7r66mTqkxEuSjnELDwAAagSBqJYJCw3RlZfUlyT9XEYgAgCgJhCIaqHIEztWE4gAAKgZBKJaKNJeNbWLITMAAGoGgagWirK7e4hcFlcCAEBwqNYqs7p163rcwPXXFBcXX1BBOBmIjjFkBgBAjahWIHr22WfN5wcOHNCTTz6pzMxMZWRkSJJycnL0wQcfaNKkSX4pMti45xARiAAAqBnVCkTDhg0znw8cOFBPPPGExowZYx6777779OKLL2rFihUaN26c76sMMlEn5hAxqRoAgJrh9RyiDz74QH369DnteJ8+fbRixQqfFBXsIt1DZuXMIQIAoCZ4HYjq16+vd95557Tj77zzjurXr++TooLdyUnV9BABAFATvL51x+OPP64//OEP+vDDD5Weni5JWrdunZYtW6a///3vPi8wGEWcmEN0vLzS4koAAAgOXgei4cOHq2XLlnr++ee1aNEiSVLLli318ccfmwEJFybSDET0EAEAUBPO6+au6enpmj9/vq9rwQkR4VUjma5KQ+UVlQoPZbsoAAD8yetAVFBQ8KvnU1NTz7sYVHEPmUlVvUQEIgAA/MvrQNS4ceNf3aSxooJhngvlCAuRzSYZhvRzeYViIsKtLgkAgN80rwPR5s2bPV6Xl5dr8+bNmjlzpp566imfFRbMbDabIsJC9XN5hUqZWA0AgN95PRbTvn17j0fnzp1155136plnntHzzz/v8wLdPVK/fIwePVqSdPXVV5927q677vL4jIKCAvXv319RUVFq0KCBHnzwQblctXuPH/c8IiZWAwDgf+c1qfpMmjdvrs8//9xXH2f6/PPPPYbhtm3bpmuvvVY333yzeezOO+/UE088Yb6Oiooyn1dUVKh///5KSkrSp59+qn379un2229XeHi4nn76aZ/X6ytV84jK9TOBCAAAv/M6EDmdTo/XhmFo3759mjJlii699FKfFeZ20UUXebyeNm2amjVrpquuuso8FhUVpaSkpDO+f/ny5dq+fbtWrFihxMREdejQQVOnTtWECRM0ZcoU2e12n9fsC5HsRQQAQI3xesgsPj5edevWNR/16tVTq1atlJOTo5dfftkfNZrKysr0+uuva8SIER4Tu+fPn6+EhAS1adNGEydO1LFjx8xzOTk5atu2rRITE81jmZmZcjqdysvLO+t3lZaWyul0ejxqkuNEIKKHCAAA//O6h2j16tUer0NCQnTRRRfpkksuUViYz0bgzmjx4sU6dOiQhg8fbh4bPHiw0tLSlJycrC1btmjChAnKz883N40sLCz0CEOSzNeFhYVn/a6srCw9/vjjvv8R1RTJHCIAAGqM1wnGZrPpiiuuOC38uFwurV27Vj169PBZcb/02muvqW/fvkpOTjaPjRo1ynzetm1bNWzYUD179tQ333yjZs2anfd3TZw4UePHjzdfO51OpaSknPfneSuC3aoBAKgxXg+ZXXPNNSouLj7teElJia655hqfFHUm3333nVasWKE//OEPv9rOffuQnTt3SpKSkpJUVFTk0cb9+mzzjiTJ4XAoNjbW41GTuH0HAAA1x+tAZBjGGTdmPHDggKKjo31S1JnMnTtXDRo0UP/+/X+1XW5uriSpYcOGkqSMjAxt3bpV+/fvN9tkZ2crNjZWrVq18lu9F8rdQ8Qd7wEA8L9qD5nddNNNkqqGzIYPHy6Hw2Geq6io0JYtW3TFFVf4vkJJlZWVmjt3roYNG+YxVPfNN9/ojTfeUL9+/VS/fn1t2bJF48aNU48ePdSuXTtJUu/evdWqVSvddtttmj59ugoLC/Xoo49q9OjRHr+htnG45xC5WGUGAIC/VTsQxcXFSarqIYqJiVFkZKR5zm636/LLL9edd97p+wolrVixQgUFBRoxYoTHcbvdrhUrVujZZ5/V0aNHlZKSooEDB+rRRx8124SGhmrJkiW6++67lZGRoejo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evjhh3X//fcrOztbklRZWakBAwaouLhYa9asUXZ2tnbt2qVbbrnFfP97772nG2+8Uf369dPmzZu1cuVKde3a1TxfXl6uqVOn6osvvtDixYv17bffavjw4RdcNwDf4m73AGoll8ul77//Xk6nU507d9aGDRsUHR2tDh066L333lNqaqrq1Knj0eNzqilTpmjq1KmKjIz0OD506FC98sorkqp6iFq2bKn333/fPH/rrbfK6XRq6dKlys7OVt++fbV7926lpKRIkrZv367WrVtr/fr16tKli6644go1bdpUr7/+erV+14YNG9SlSxcdPnxYderUOZ9LA8AP6CECUCuFhYWpcePG2rFjh7p06aJ27dqpsLBQiYmJ6tGjhxo3bnzWMOTWvHlz5ebmejyeeOIJjzYZGRmnvf7yyy8lSV9++aVSUlLMMCRJrVq1Unx8vNkmNzdXPXv2PGsNGzdu1HXXXafU1FTFxMToqquukqRzTgoHULOYXQigVmrdurW+++47lZeXq7KyUnXq1JHL5ZLL5VKdOnWUlpamvLy8X/0Mu92uSy65xK91/rIH6lRHjx5VZmamMjMzNX/+fF100UUqKChQZmamysrK/FoXAO/QQwSgVlq6dKlyc3OVlJSk119/Xbm5uWrTpo2effZZ5ebmaunSpT75ns8+++y01y1btpQktWzZUnv27NGePXvM89u3b9ehQ4fUqlUrSVK7du20cuXKM372jh07dODAAU2bNk3du3dXixYtmFAN1FL0EAGoldLS0lRYWKiioiINGDBANptNeXl5GjhwoBo2bFitz3C5XCosLPQ4ZrPZlJiYaL7+5JNPNH36dN1www3Kzs7WW2+9pffee0+S1KtXL7Vt21ZDhgzRs88+K5fLpXvuuUdXXXWVOnfuLEl67LHH1LNnTzVr1ky33nqrXC6Xli5dqgkTJig1NVV2u10vvPCC7rrrLm3btk1Tp0710RUC4Ev0EAGotT788ENzOfv69evVqFGjaochScrLy1PDhg09HmlpaR5tHnjgAW3YsEEdO3bUk08+qZkzZyozM1NSVXh65513VLduXfXo0UO9evVS06ZNtXDhQvP9V199td566y395z//UYcOHfRf//VfWr9+vSTpoosu0rx58/TWW2+pVatWmjZtmp555hkfXBkAvsYqMwBBq3Hjxho7dqzGjh1rdSkALEYPEQAACHoEIgAAEPQYMgMAAEGPHiIAABD0CEQAACDoEYgAAEDQIxABAICgRyACAABBj0AEAACCHoEIAAAEPQIRAAAIev8f0lYFZhjVsJoAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Realizar una predicción\")\n",
        "resultado = modelo.predict([100.0])\n",
        "print(\"El resultado es \" + str(resultado) + \" grados fahrenheit\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "err5Z09bGBdE",
        "outputId": "cbfc62c9-57e2-4927-8394-565ad8cfc72e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Realizar una predicción\n",
            "1/1 [==============================] - 1s 544ms/step\n",
            "El resultado es [[211.99997]] grados fahrenheit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.save('celsius_a_fahrenheit.h5')"
      ],
      "metadata": {
        "id": "BWRwVawGVSLW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e15b3e74-f7a7-4c54-d1de-2ad5616c8ef3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3079: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.\n",
            "  saving_api.save_model(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tUTJHyTbVq7q",
        "outputId": "2dd54789-0173-4775-b38c-ee639c478392"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "celsius_a_fahrenheit.h5  sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflowjs"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "7qRNh2N8V05x",
        "outputId": "2f776536-8d11-49a3-e8a8-0980885ebbb6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting tensorflowjs\n",
            "  Downloading tensorflowjs-4.13.0-py3-none-any.whl (89 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/89.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m\u001b[90m━━━\u001b[0m \u001b[32m81.9/89.2 kB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m89.2/89.2 kB\u001b[0m \u001b[31m2.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: flax>=0.7.2 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.7.5)\n",
            "Requirement already satisfied: importlib_resources>=5.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (6.1.1)\n",
            "Requirement already satisfied: jax>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20)\n",
            "Requirement already satisfied: jaxlib>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20+cuda11.cudnn86)\n",
            "Requirement already satisfied: tensorflow<3,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (2.14.0)\n",
            "Collecting tensorflow-decision-forests>=1.5.0 (from tensorflowjs)\n",
            "  Downloading tensorflow_decision_forests-1.8.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (15.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.3/15.3 MB\u001b[0m \u001b[31m73.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: six<2,>=1.16.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (1.16.0)\n",
            "Requirement already satisfied: tensorflow-hub>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.15.0)\n",
            "Requirement already satisfied: packaging~=23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (23.2)\n",
            "Requirement already satisfied: numpy>=1.22 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.23.5)\n",
            "Requirement already satisfied: msgpack in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.0.7)\n",
            "Requirement already satisfied: optax in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: orbax-checkpoint in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.4.2)\n",
            "Requirement already satisfied: tensorstore in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.45)\n",
            "Requirement already satisfied: rich>=11.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (13.7.0)\n",
            "Requirement already satisfied: typing-extensions>=4.2 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (4.5.0)\n",
            "Requirement already satisfied: PyYAML>=5.4.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (6.0.1)\n",
            "Requirement already satisfied: ml-dtypes>=0.2.0 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: opt-einsum in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (3.3.0)\n",
            "Requirement already satisfied: scipy>=1.9 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (1.11.3)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=23.5.26 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (23.5.26)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.5.4)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.9.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (16.0.6)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.20.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (67.7.2)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.3.0)\n",
            "Requirement already satisfied: wrapt<1.15,>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.14.1)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.34.0)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.59.2)\n",
            "Requirement already satisfied: tensorboard<2.15,>=2.14 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.1)\n",
            "Requirement already satisfied: tensorflow-estimator<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: keras<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (1.5.3)\n",
            "Collecting tensorflow<3,>=2.13.0 (from tensorflowjs)\n",
            "  Downloading tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.2 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m475.2/475.2 MB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: wheel in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (0.41.3)\n",
            "Collecting wurlitzer (from tensorflow-decision-forests>=1.5.0->tensorflowjs)\n",
            "  Downloading wurlitzer-3.0.3-py3-none-any.whl (7.3 kB)\n",
            "Collecting tensorboard<2.16,>=2.15 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorboard-2.15.1-py3-none-any.whl (5.5 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.5/5.5 MB\u001b[0m \u001b[31m93.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting tensorflow-estimator<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl (441 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m442.0/442.0 kB\u001b[0m \u001b[31m40.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting keras<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading keras-2.15.0-py3-none-any.whl (1.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m68.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (2.16.1)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.17.3)\n",
            "Requirement already satisfied: google-auth-oauthlib<2,>=0.5 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.0.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.5.1)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.31.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.0.1)\n",
            "Requirement already satisfied: chex>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from optax->flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: etils[epath,epy] in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.2)\n",
            "Requirement already satisfied: nest_asyncio in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.8)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2023.3.post1)\n",
            "Requirement already satisfied: dm-tree>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.1.8)\n",
            "Requirement already satisfied: toolz>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.12.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (4.9)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.3.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=11.1->flax>=0.7.2->tensorflowjs) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2023.7.22)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/dist-packages (from werkzeug>=1.0.1->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.1.3)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (2023.6.0)\n",
            "Requirement already satisfied: zipp in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (3.17.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.5.0)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.2.2)\n",
            "Installing collected packages: wurlitzer, tensorflow-estimator, keras, tensorboard, tensorflow, tensorflow-decision-forests, tensorflowjs\n",
            "  Attempting uninstall: tensorflow-estimator\n",
            "    Found existing installation: tensorflow-estimator 2.14.0\n",
            "    Uninstalling tensorflow-estimator-2.14.0:\n",
            "      Successfully uninstalled tensorflow-estimator-2.14.0\n",
            "  Attempting uninstall: keras\n",
            "    Found existing installation: keras 2.14.0\n",
            "    Uninstalling keras-2.14.0:\n",
            "      Successfully uninstalled keras-2.14.0\n",
            "  Attempting uninstall: tensorboard\n",
            "    Found existing installation: tensorboard 2.14.1\n",
            "    Uninstalling tensorboard-2.14.1:\n",
            "      Successfully uninstalled tensorboard-2.14.1\n",
            "  Attempting uninstall: tensorflow\n",
            "    Found existing installation: tensorflow 2.14.0\n",
            "    Uninstalling tensorflow-2.14.0:\n",
            "      Successfully uninstalled tensorflow-2.14.0\n",
            "Successfully installed keras-2.15.0 tensorboard-2.15.1 tensorflow-2.15.0 tensorflow-decision-forests-1.8.1 tensorflow-estimator-2.15.0 tensorflowjs-4.13.0 wurlitzer-3.0.3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "keras",
                  "tensorboard",
                  "tensorflow"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!mkdir temperatura"
      ],
      "metadata": {
        "id": "CUEro8qoWoPX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!tensorflowjs_converter --input_format keras celsius_a_fahrenheit.h5 temperatura"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RgxquOn8WxKH",
        "outputId": "a6427283-03d1-4b4c-aac3-47a658cc2782"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2023-11-22 23:27:12.631801: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "2023-11-22 23:27:12.631869: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "2023-11-22 23:27:12.633233: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "2023-11-22 23:27:13.944846: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls temperatura"
      ],
      "metadata": {
        "id": "q1OER05QXA1e",
        "outputId": "31a17515-228f-45ce-fc94-8cc7699c0d83",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "group1-shard1of1.bin  model.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Variante del código"
      ],
      "metadata": {
        "id": "yLUL_oLAvC07"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dolar = np.array([1, 2, 3, 4, 5], dtype=float)\n",
        "peso = np.array([17.34, 34.68, 52.02, 69.36, 86.7], dtype=float)\n",
        "\n",
        "#capa = tf.keras.layers.Dense(units=1, input_shape=[1])\n",
        "#modelo = tf.keras.Sequential([capa])\n",
        "oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])\n",
        "oculta2 = tf.keras.layers.Dense(units=3)\n",
        "salida = tf.keras.layers.Dense(units=1)\n",
        "modelo = tf.keras.Sequential([oculta1, oculta2, salida])\n",
        "\n",
        "modelo.compile(\n",
        "    optimizer = tf.keras.optimizers.Adam(0.1),\n",
        "    loss='mean_squared_error'\n",
        ")\n",
        "\n",
        "print(\"Comenzando entrenamiento...\")\n",
        "historial=modelo.fit(dolar, peso, epochs=1000, verbose=False)\n",
        "print(\"Modelo entrenado, ¡¡¡OMG!!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bj2L6CP6vI6j",
        "outputId": "ce7c0ef9-d2e0-4845-a2d9-944380323610"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Comenzando entrenamiento...\n",
            "Modelo entrenado, ¡¡¡OMG!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.xlabel(\"# Epoca\")\n",
        "plt.ylabel(\"Magnitud de pérdida\")\n",
        "plt.plot(historial.history[\"loss\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "W7pFGOVDxMw1",
        "outputId": "c4de7ba9-fb60-4e30-e869-d4eefa457c8f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7d1bb7f21ff0>]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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p06G0+k0WrRoYX5GTZWWlhqSTvvs2rK54Fuj2fhFxhU5ywNyfQAAwlFN/377/cjs2LFj5qOp+vXr6+DBg7rooovUvn17bdq0yd8w9qPnU1JStGrVqp+8TrNmzU57JPZD11xzjTZv3uxXfcHknWVGDxEAAMHn9yOz1q1bm9trdOzYUX/729/0zTffaMaMGea4HvjPuw4RY4gAAAg+v3uIRo0apQMHDkiSHn30UV133XWaM2eOnE5nyO0P9nPiXamaafcAAASf34HotttuM3/u3LmzvvrqK+3atUupqalKSEio1eLCyamFGQlEAAAE23kvzBgVFaVLL720NmoJazwyAwDAOjUKRNVXbP4pzzzzzDkXE87MR2b0EAEAEHQ1CkQ/nJ21adMmVVZWqnXr1pKkTz/9VBEREercuXPtVxgmqm/dYRiGbDabxRUBABA+ahSIPvjgA/PnZ555RvXq1dPs2bNVv359SdK3336rIUOGqHv37oGpMgx4F2aUTk69d0QQiAAACBa/p93/5S9/UU5OjhmGpJPrEf35z3/WX/7yl1otLpx4e4gkZpoBABBsfgcit9utgwcPnnb84MGDOnLkSK0UFY68m7tKLM4IAECw+R2IbrrpJg0ZMkTz58/X119/ra+//lpvvvmmhg4dqv79+weixrDg00PEwGoAAILK72n3M2bM0B/+8AfdeuutqqioOHkRh0NDhw7V1KlTa73AcOHweWTG1HsAAILJ70AUFRWl6dOna+rUqfriiy8kSS1btlR0dHStFxdObDabIuw2VXkMxhABABBk57wwY3R0tDp06FCbtYQ9B4EIAABL1CgQ9e/fX7NmzVJsbOxPjhOaP39+rRQWjhx2m8okVVbxyAwAgGCqUSCKi4szFwqMi4sLaEHhzBFhl1RFDxEAAEFWo0A0c+bMM/6M2sUGrwAAWMPvafcInFPbd/DIDACAYKpRD9Ell1xS4721Nm3adF4FhTPv4oz0EAEAEFw1CkT9+vUzfz5x4oSmT5+u9PR0ZWRkSJLWrl2r7du369577w1IkeGi+gavAAAgeGoUiB599FHz52HDhun+++/XpEmTTmuzb9++2q0uzHg3dGXrDgAAgsvvMUTz5s3THXfccdrx2267TW+++WatFBWuTg2qZgwRAADB5HcgioyM1Icffnja8Q8//FB169atlaLClcP+/RgieogAAAgqv1eqHj16tEaMGKFNmzbpsssukyStW7dO//znP/XII4/UeoHhxPvIjFlmAAAEl9+B6KGHHlKLFi00bdo0vfLKK5Kktm3baubMmfr9739f6wWGE9YhAgDAGn4FosrKSj311FO66667CD8BwCMzAACs4dcYIofDoSlTpqiysjJQ9YS1U4/MCEQAAAST34Oqe/bsqVWrVgWilrAXwSwzAAAs4fcYot69e+uhhx7S1q1b1blzZ0VHR/ucv/HGG2utuHDjYGFGAAAs4Xcg8q5G/cwzz5x2zmazqaqq6vyrClMOtu4AAMASfgciD1PCA8bbQ1TFPQYAIKjOa7f7EydO1FYdULUeIh6ZAQAQVH4HoqqqKk2aNEkXXHCBYmJitGfPHknSI488on/84x+1XmA4YR0iAACs8ZOB6PXXX1dBQYH5/sknn9SsWbM0ZcoUOZ1O83i7du3097//PTBVhgkGVQMAYI2fDER169ZVjx499Mknn0iSZs+erZdfflmDBg1SRESE2a5jx47atWtX4CoNA+Y6REy7BwAgqH5yUHXfvn2VmJio2267TVu3btX+/fvVqlWr09p5PB5VVFQEpMhwwUrVAABYo0ZjiC6//HJzMcb09HT95z//Oa3Nv//9b11yySW1W12YMRdmZJYZAABBVeNp9w0aNJAkTZw4UYMHD9Y333wjj8ej+fPna/fu3frXv/6lRYsWBazQcFCHrTsAALCE37PM+vbtq4ULF+r9999XdHS0Jk6cqJ07d2rhwoX69a9/7de1cnJy1LVrV9WrV0+NGzdWv379tHv3bp82J06cUHZ2tho2bKiYmBgNGDBARUVFPm0KCgrUp08fRUVFqXHjxho3btxp+62tXLlSl156qVwul1q1aqVZs2b5+9UDLsLOwowAAFjhnNYh6t69u3Jzc1VcXKzjx49rzZo16tWrl9/XWbVqlbKzs7V27Vrl5uaqoqJCvXr10rFjx8w2Y8aM0cKFCzVv3jytWrVK+/fvV//+/c3zVVVV6tOnj8rLy/XRRx9p9uzZmjVrliZOnGi22bt3r/r06aNrr71W+fn5Gj16tIYNG6Zly5ady9cPmFMLMxKIAAAIJpthGOf013fDhg3auXOnpJPjijp37nzexRw8eFCNGzfWqlWr1KNHD5WWlqpRo0aaO3eufvvb30qSdu3apbZt2yovL0+XX365lixZot/85jfav3+/EhMTJUkzZszQ+PHjdfDgQTmdTo0fP16LFy/Wtm3bzM8aOHCgSkpKtHTp0hrV5na7FRcXp9LSUsXGxp73dz2T597/VM+9/5kGdUvVkze1D8hnAAAQTmr699vvHqKvv/5a3bt312WXXaZRo0Zp1KhR6tq1q6666ip9/fXX51V0aWmppFPjlTZu3KiKigplZmaabdq0aaPU1FTl5eVJkvLy8tS+fXszDElSVlaW3G63tm/fbrapfg1vG+81zqSsrExut9vnFWj0EAEAYA2/A9GwYcNUUVGhnTt36vDhwzp8+LB27twpj8ejYcOGnXMhHo9Ho0eP1pVXXql27dpJkgoLC+V0OhUfH+/TNjExUYWFhWab6mHIe9577sfauN1ufffdd2esJycnR3FxceYrJSXlnL9bTbF1BwAA1vA7EK1atUovvfSSWrdubR5r3bq1/vrXv2r16tXnXEh2dra2bdum11577ZyvUZsmTJig0tJS87Vv376Af+aprTuYdg8AQDD5vdt9SkrKGRdgrKqqUnJy8jkVMXLkSC1atEirV69W06ZNzeNJSUkqLy9XSUmJTy9RUVGRkpKSzDbr16/3uZ53Flr1Nj+cmVZUVKTY2FhFRkaesSaXyyWXy3VO3+dcRbB1BwAAlvC7h2jq1Km67777tGHDBvPYhg0bNGrUKD399NN+XcswDI0cOVILFizQihUrlJaW5nO+c+fOqlOnjpYvX24e2717twoKCpSRkSFJysjI0NatW1VcXGy2yc3NVWxsrNLT08021a/hbeO9Rqjw9hB5zm2cOwAAOEd+zzKrX7++jh8/rsrKSjkcJzuYvD9HR0f7tD18+PCPXuvee+/V3Llz9fbbb/s8gouLizN7bkaMGKF3331Xs2bNUmxsrO677z5J0kcffSTpZM9Up06dlJycrClTpqiwsFC33367hg0bpqeeekrSyWn37dq1U3Z2tu666y6tWLFC999/vxYvXqysrKwafe9gzDKbs+4r/WnBNvVKT9TLd3QJyGcAABBOavr32+9HZs8999z51OXjpZdekiRdc801PsdnzpypO++8U5L07LPPym63a8CAASorK1NWVpamT59uto2IiNCiRYs0YsQIZWRkKDo6WoMHD9YTTzxhtklLS9PixYs1ZswYTZs2TU2bNtXf//73GoehYGGWGQAA1jjndYjCTTB6iP698Wv9Yd4nuqZ1I80acllAPgMAgHASsHWIEDjfz7qnhwgAgCAjEIUQ715mBCIAAIKLQBRCHEy7BwDAEgSiEGK3MagaAAArnHMg+vzzz7Vs2TJz6wvGZp8/ZpkBAGANvwPRoUOHlJmZqYsuukjXX3+9Dhw4IEkaOnSoHnjggVovMJxEEIgAALCE34FozJgxcjgcKigoUFRUlHn85ptv1tKlS2u1uHBDIAIAwBp+L8z43nvvadmyZT57jknShRdeqK+++qrWCgtHPDIDAMAafvcQHTt2zKdnyOvw4cNB3wz1l8ZuzjJjt3sAAILJ70DUvXt3/etf/zLf22w2eTweTZkyRddee22tFhduTm3uanEhAACEGb8fmU2ZMkU9e/bUhg0bVF5ergcffFDbt2/X4cOH9eGHHwaixrBBDxEAANbwu4eoXbt2+vTTT3XVVVepb9++OnbsmPr376/NmzerZcuWgagxbJg9ROQhAACCyu8eIkmKi4vTn/70p9quJexF0EMEAIAlahSItmzZUuMLdujQ4ZyLCXdMuwcAwBo1CkSdOnWSzWaTYRiyfb+9hHRqderqx6qqqmq5xPDBtHsAAKxRozFEe/fu1Z49e7R37169+eabSktL0/Tp05Wfn6/8/HxNnz5dLVu21Jtvvhnoen/RvHuZsbkrAADBVaMeombNmpk//+53v9Pzzz+v66+/3jzWoUMHpaSk6JFHHlG/fv1qvchw4bCfzKceAhEAAEHl9yyzrVu3Ki0t7bTjaWlp2rFjR60UFa4iIughAgDACn4HorZt2yonJ0fl5eXmsfLycuXk5Kht27a1Wly4ibAxhggAACv4Pe1+xowZuuGGG9S0aVNzRtmWLVtks9m0cOHCWi8wnJizzAwCEQAAweR3ILrsssu0Z88ezZkzR7t27ZJ0cqf7W2+9VdHR0bVeYDjxBiLDODmOyLtyNQAACKxzWpgxOjpa99xzT23XEvYiqgWgKsOQXQQiAACCwe8xRAgcR/VAxDgiAACChkAUQqr3EDHTDACA4CEQhZAIeogAALAEgSiERNgIRAAAWIFAFELsdpu8mYhABABA8NRolln9+vV9NnD9MYcPHz6vgsKdw25TRZVBIAIAIIhqFIiee+458+dDhw7pz3/+s7KyspSRkSFJysvL07Jly/TII48EpMhwcnKDV0OVHo/VpQAAEDZqFIgGDx5s/jxgwAA98cQTGjlypHns/vvv1wsvvKD3339fY8aMqf0qw4jDblOZJPIQAADB4/cYomXLlum666477fh1112n999/v1aKCmfe1anpIQIAIHj8DkQNGzbU22+/fdrxt99+Ww0bNqyVosKZd3FGD/uZAQAQNH5v3fH4449r2LBhWrlypbp16yZJWrdunZYuXar//d//rfUCw02E/WRGZWFGAACCx+9AdOedd6pt27Z6/vnnNX/+fElS27ZttWbNGjMg4dxFfN9nV1lFIAIAIFjOaXPXbt26ac6cObVdCyQ5vu8h4pEZAADB43cgKigo+NHzqamp51wMJLu3h4hHZgAABI3fgah58+Y/ukhjVVXVeRUU7sweIgIRAABB4/css82bN2vTpk3ma926dZoxY4YuuugizZs3z+8CVq9erRtuuEHJycmy2Wx66623fM7feeedstlsPq8fTvs/fPiwBg0apNjYWMXHx2vo0KE6evSoT5stW7aoe/fuqlu3rlJSUjRlyhS/aw2GCHPaPYEIAIBg8buHqGPHjqcd69Kli5KTkzV16lT179/fr+sdO3ZMHTt21F133XXW373uuus0c+ZM873L5fI5P2jQIB04cEC5ubmqqKjQkCFDdM8992ju3LmSJLfbrV69eikzM1MzZszQ1q1bdddddyk+Pl733HOPX/UGmneDV7buAAAgeM5pUPWZtG7dWh9//LHfv9e7d2/17t37R9u4XC4lJSWd8dzOnTu1dOlSffzxx+rSpYsk6a9//auuv/56Pf3000pOTtacOXNUXl6uf/7zn3I6nbr44ouVn5+vZ555JvQCkZ1ABABAsPn9yMztdvu8SktLtWvXLj388MO68MILA1GjVq5cqcaNG6t169YaMWKEDh06ZJ7Ly8tTfHy8GYYkKTMzU3a7XevWrTPb9OjRQ06n02yTlZWl3bt369tvvz3jZ5aVlZ32XYOBQAQAQPD53UMUHx9/2qBqwzCUkpKi1157rdYK87ruuuvUv39/paWl6YsvvtAf//hH9e7dW3l5eYqIiFBhYaEaN27s8zsOh0MNGjRQYWGhJKmwsFBpaWk+bRITE81z9evXP+1zc3Jy9Pjjj9f69/kpBCIAAILP70D0wQcf+Ly32+1q1KiRWrVqJYej1p7AmQYOHGj+3L59e3Xo0EEtW7bUypUr1bNnz1r/PK8JEyZo7Nix5nu3262UlJSAfZ6Xg0HVAAAEnd8Jxmaz6Yorrjgt/FRWVmr16tXq0aNHrRV3Ji1atFBCQoI+//xz9ezZU0lJSSouLj6tlsOHD5vjjpKSklRUVOTTxvv+bGOTXC7XaYO3g8FODxEAAEHn9xiia6+9VocPHz7teGlpqa699tpaKerHfP311zp06JCaNGkiScrIyFBJSYk2btxotlmxYoU8Ho+5lUhGRoZWr16tiooKs01ubq5at259xsdlVvL2EFWxUjUAAEHjdyAyDOOMCzMeOnRI0dHRfhdw9OhR5efnKz8/X5K0d+9e5efnq6CgQEePHtW4ceO0du1affnll1q+fLn69u2rVq1aKSsrS9LJfdSuu+463X333Vq/fr0+/PBDjRw5UgMHDlRycrIk6dZbb5XT6dTQoUO1fft2vf7665o2bZrPI7FQcWoMkcfiSgAACB81fmTmXSPIZrPpzjvv9HmcVFVVpS1btuiKK67wu4ANGzb49Cx5Q8rgwYP10ksvacuWLZo9e7ZKSkqUnJysXr16adKkST6fP2fOHI0cOVI9e/aU3W7XgAED9Pzzz5vn4+Li9N577yk7O1udO3dWQkKCJk6cGHJT7qXqgcjiQgAACCM1DkRxcXGSTvYQ1atXT5GRkeY5p9Opyy+/XHfffbffBVxzzTUyfuTx0LJly37yGg0aNDAXYTybDh066D//+Y/f9QWbgx4iAACCrsaByLtSdPPmzfWHP/zhnB6P4afZbcwyAwAg2PyeZfboo48Gog58zxFxMhCxuSsAAMFTo0B06aWXavny5apfv74uueSSH93tftOmTbVWXDiihwgAgOCrUSDq27evOYi5X79+gawn7DlYhwgAgKCrUSCq/piMR2aBFWE/uRICgQgAgOA55702ysvLVVxcLM8PZkOlpqaed1HhLOL7laF4ZAYAQPD4HYg+/fRTDR06VB999JHPce+CjVVVVbVWXDjy9hAxqBoAgODxOxANGTJEDodDixYtUpMmTX50gDX8Rw8RAADB53cgys/P18aNG9WmTZtA1BP2HN4eIvYyAwAgaPzeyyw9PV3//e9/A1ELdGrrDnqIAAAIHr8D0f/8z//owQcf1MqVK3Xo0CG53W6fF85PBNPuAQAIOr8fmWVmZkqSevbs6XOcQdW1g0AEAEDw+R2IPvjgg0DUge9F2AhEAAAEm9+B6Oqrrw5EHfgePUQAAASf34Foy5YtZzxus9lUt25dpaammtt8wH8OBlUDABB0fgeiTp06/ejaQ3Xq1NHNN9+sv/3tb6pbt+55FReO7GYPkecnWgIAgNri9yyzBQsW6MILL9TLL7+s/Px85efn6+WXX1br1q01d+5c/eMf/9CKFSv08MMPB6LeX7xTm7taXAgAAGHE7x6iJ598UtOmTVNWVpZ5rH379mratKkeeeQRrV+/XtHR0XrggQf09NNP12qx4SCCHiIAAILO7x6irVu3qlmzZqcdb9asmbZu3Srp5GO1AwcOnH91YcgMRAwhAgAgaPwORG3atNHkyZNVXl5uHquoqNDkyZPN7Ty++eYbJSYm1l6VYcRBDxEAAEHn9yOzF198UTfeeKOaNm2qDh06SDrZa1RVVaVFixZJkvbs2aN77723disNE95B1ZV0EQEAEDR+B6IrrrhCe/fu1Zw5c/Tpp59Kkn73u9/p1ltvVb169SRJt99+e+1WGUa8PURs7goAQPD4HYgkqV69eho+fHht1wJJdhvrEAEAEGznFIgkaceOHSooKPAZSyRJN95443kXFc4cEaxUDQBAsPkdiPbs2aObbrpJW7dulc1mk/H9ox3vYo1s7np+Iuwnx7kTiAAACB6/Z5mNGjVKaWlpKi4uVlRUlLZv367Vq1erS5cuWrlyZQBKDC8RPDIDACDo/O4hysvL04oVK5SQkCC73S673a6rrrpKOTk5uv/++7V58+ZA1Bk2vOsQeQhEAAAEjd89RFVVVeZssoSEBO3fv1/SyYUZd+/eXbvVhaEINncFACDo/O4hateunT755BOlpaWpW7dumjJlipxOp15++WW1aNEiEDWGFabdAwAQfH4HoocffljHjh2TJD3xxBP6zW9+o+7du6thw4Z6/fXXa73AcBPBwowAAASd34Go+qaurVq10q5du3T48GHVr1/fnGmGc3dqc1cCEQAAwXLO6xBV16BBg9q4DFR9c1cCEQAAwVLjQHTXXXfVqN0///nPcy4G9BABAGCFGgeiWbNmqVmzZrrkkkvMxRhR+whEAAAEX40D0YgRI/Tqq69q7969GjJkiG677TYelQWAg0AEAEDQ1XgdohdffFEHDhzQgw8+qIULFyolJUW///3vtWzZMnqMatGpzV09FlcCAED48GthRpfLpVtuuUW5ubnasWOHLr74Yt17771q3ry5jh49Gqgaw8qpzV0tLgQAgDDi90rV5i/a7ebmruezoevq1at1ww03KDk5WTabTW+99ZbPecMwNHHiRDVp0kSRkZHKzMzUZ5995tPm8OHDGjRokGJjYxUfH6+hQ4eeFtC2bNmi7t27q27dukpJSdGUKVPOueZA8u5lVkUPEQAAQeNXICorK9Orr76qX//617rooou0detWvfDCCyooKFBMTMw5FXDs2DF17NhRL7744hnPT5kyRc8//7xmzJihdevWKTo6WllZWTpx4oTZZtCgQdq+fbtyc3O1aNEirV69Wvfcc4953u12q1evXmrWrJk2btyoqVOn6rHHHtPLL798TjUHEoOqAQCwgFFDI0aMMOrXr2906NDBeO6554yDBw/W9FdrTJKxYMEC873H4zGSkpKMqVOnmsdKSkoMl8tlvPrqq4ZhGMaOHTsMScbHH39stlmyZIlhs9mMb775xjAMw5g+fbpRv359o6yszGwzfvx4o3Xr1jWurbS01JBklJaWnuvXq5Gv/nvMaDZ+kZH+yJKAfg4AAOGgpn+/azzLbMaMGUpNTVWLFi20atUqrVq16ozt5s+fXytBTZL27t2rwsJCZWZmmsfi4uLUrVs35eXlaeDAgcrLy1N8fLy6dOlitsnMzJTdbte6det00003KS8vTz169JDT6TTbZGVl6X/+53/07bffqn79+qd9dllZmcrKysz3bre71r7Xj7F/32fH5q4AAARPjQPRHXfcEfStOQoLCyVJiYmJPscTExPNc4WFhWrcuLHPeYfDoQYNGvi0SUtLO+0a3nNnCkQ5OTl6/PHHa+eL+MHxfSJic1cAAILHr4UZw8mECRM0duxY873b7VZKSkrAP5ceIgAAgu+cZ5kFQ1JSkiSpqKjI53hRUZF5LikpScXFxT7nKysrdfjwYZ82Z7pG9c/4IZfLpdjYWJ9XMHh7iAxD8hCKAAAIipAORGlpaUpKStLy5cvNY263W+vWrVNGRoYkKSMjQyUlJdq4caPZZsWKFfJ4POrWrZvZZvXq1aqoqDDb5ObmqnXr1md8XGYl7ywziQ1eAQAIFssD0dGjR5Wfn6/8/HxJJwdS5+fnq6CgQDabTaNHj9af//xnvfPOO9q6davuuOMOJScnq1+/fpKktm3b6rrrrtPdd9+t9evX68MPP9TIkSM1cOBAJScnS5JuvfVWOZ1ODR06VNu3b9frr7+uadOm+TwSCxU+gYgeIgAAgqLGY4gCZcOGDbr22mvN996QMnjwYM2aNUsPPvigjh07pnvuuUclJSW66qqrtHTpUtWtW9f8nTlz5mjkyJHq2bOn7Ha7BgwYoOeff948HxcXp/fee0/Z2dnq3LmzEhISNHHiRJ+1ikKFg0AEAEDQ2QyD5zI14Xa7FRcXp9LS0oCOJyqv9Oiih5dIkj55tJfiIusE7LMAAPilq+nfb8sfmcFX9R4iBlUDABAcBKIQY7fb5F3uian3AAAEB4EoBJ3a4JVABABAMBCIQpC5wSvDuwAACAoCUQgyA1EVgQgAgGAgEIUgeogAAAguAlEI8s40q/J4LK4EAIDwQCAKQd4eImaZAQAQHASiEGQ+MiMQAQAQFASiEMS0ewAAgotAFIIiIghEAAAEE4EoBNFDBABAcBGIQhCDqgEACC4CUQhy2E/+s7C5KwAAwUEgCkF2eogAAAgqAlEIcrBSNQAAQUUgCkF29jIDACCoCEQhyMEjMwAAgopAFIK8s8w8PDIDACAoCEQhyLsOET1EAAAEB4EoBDm+X6maafcAAAQHgSgE2ekhAgAgqAhEIcicdu/xWFwJAADhgUAUgiLMQGRxIQAAhAkCUQiKoIcIAICgIhCFoFOBiDFEAAAEA4EoBLHbPQAAwUUgCkH0EAEAEFwEohDE5q4AAAQXgSgERbC5KwAAQUUgCkER9BABABBUBKIQ5N3LjDFEAAAEB4EoBEXYT/6zEIgAAAgOAlEI8m7uSiACACA4CEQhiM1dAQAILgJRCHKwDhEAAEFFIApBdgIRAABBFfKB6LHHHpPNZvN5tWnTxjx/4sQJZWdnq2HDhoqJidGAAQNUVFTkc42CggL16dNHUVFRaty4scaNG6fKyspgf5Uaq74wo/H9CwAABE7IByJJuvjii3XgwAHztWbNGvPcmDFjtHDhQs2bN0+rVq3S/v371b9/f/N8VVWV+vTpo/Lycn300UeaPXu2Zs2apYkTJ1rxVWqk+sKM9726Wdc8vVLHykI3wAEA8HPnsLqAmnA4HEpKSjrteGlpqf7xj39o7ty5+tWvfiVJmjlzptq2bau1a9fq8ssv13vvvacdO3bo/fffV2Jiojp16qRJkyZp/Pjxeuyxx+R0OoP9dX5S9c1dF205IEla+Ml+Dbws1cqyAAD4xfpZ9BB99tlnSk5OVosWLTRo0CAVFBRIkjZu3KiKigplZmaabdu0aaPU1FTl5eVJkvLy8tS+fXslJiaabbKysuR2u7V9+/azfmZZWZncbrfPK1i8j8w81R6VfVPyXdA+HwCAcBPygahbt26aNWuWli5dqpdeekl79+5V9+7ddeTIERUWFsrpdCo+Pt7ndxITE1VYWChJKiws9AlD3vPec2eTk5OjuLg485WSklK7X+xHeKfdl1VWmccIRAAABE7IPzLr3bu3+XOHDh3UrVs3NWvWTG+88YYiIyMD9rkTJkzQ2LFjzfdutztooci7MOOxslOB6ERF1dmaAwCA8xTyPUQ/FB8fr4suukiff/65kpKSVF5erpKSEp82RUVF5pijpKSk02aded+faVySl8vlUmxsrM8rWLxjiKoPpGaiGQAAgfOzC0RHjx7VF198oSZNmqhz586qU6eOli9fbp7fvXu3CgoKlJGRIUnKyMjQ1q1bVVxcbLbJzc1VbGys0tPTg15/TXg3dz1aLRCVVXqsKgcAgF+8kH9k9oc//EE33HCDmjVrpv379+vRRx9VRESEbrnlFsXFxWno0KEaO3asGjRooNjYWN13333KyMjQ5ZdfLknq1auX0tPTdfvtt2vKlCkqLCzUww8/rOzsbLlcLou/3ZmZPUTlpwIRj8wAAAickA9EX3/9tW655RYdOnRIjRo10lVXXaW1a9eqUaNGkqRnn31WdrtdAwYMUFlZmbKysjR9+nTz9yMiIrRo0SKNGDFCGRkZio6O1uDBg/XEE09Y9ZV+0qlHZowhAgAgGGwGyyDXiNvtVlxcnEpLSwM+nujt/G806rV8OR12lX//qCy9SazeHdU9oJ8LAMAvTU3/fv/sxhCFA28PUXm1cUMnKukhAgAgUAhEIci7MGN1ZRUMqgYAIFAIRCEown76PwtjiAAACBwCUQiKOMO/CoEIAIDAIRCFoDP1ELEOEQAAgUMgCkHehRmrq/QYqqwiFAEAEAgEohAUcYZB1ZJ0gl4iAAACgkAUgrybu/4Q44gAAAgMAlEIsp/hkZlEIAIAIFAIRCHoTOsQSdIJ1iICACAgCEQh6KxjiOghAgAgIAhEIehsgaiM7TsAAAgIAlEIqnPWQdU8MgMAIBAIRCGozpmWqhaPzAAACBQCUQhynDUQ0UMEAEAgEIhCUB0GVQMAEFQEohB01kdmDKoGACAgCEQh6GwrVZfxyAwAgIAgEIUgeogAAAguAlEI+mEgqlvn5HsGVQMAEBgEohAUYbep+nZmMa46kqQyBlUDABAQBKIQVb2XqF5dhyRmmQEAECgEohBVfep9jMsbiHhkBgBAIBCIQlQdxxl6iBhUDQBAQBCIQpTDfuqf5lQPEYEIAIBAIBCFqOobvMbUPfXIzDAM/eezgyp2n7CqNAAAfnEIRCGq+qDq+lFOSSd7iBZs/ka3/2O9rn9+jY6cqLCqPAAAflEIRCGq+mrVcZEnp92fqPTo/Z1FkqT/Hi3Thi+/taQ2AAB+aQhEIcpZrYcoPurUOkT5BSXm8Q1fHQ52WQAA/CIRiELUmXqIjpZVqrDa2KFPi44GvS4AAH6JHFYXgDOLsJ0eiL7+9jufNl8cJBABAFAb6CEKUR7j1M/x3w+q9nJ+v0ZRwaHjqqhisUYAAM4XgShEVVVLRN4eIq8uzeorsk6EKj2G9h0+HuzSAAD4xSEQhajqK1XXj/INRE3rR6pFo2hJ0hcHj0mS9h0+Lk/1biUAAFBjBKIQFe2MMH+OrVtHEdX2NrsgPkotGsVIkvYcPKq/vLdb3ad8oHv+b4MMg1AEAIC/CEQhKsp5ary73W4zF2eUpAvqR6pFwskeoi3flOrFDz6XJL2/s1ibClibCAAAfxGIQlS0K8LnfYPoU4/NmjeMUsvGJ3uIFm854DMAe/6mb4JSHwAAvyRhFYhefPFFNW/eXHXr1lW3bt20fv16q0s6qyhnxA/en+oxatEoxuwh8ro4OVaStGjLAW39ulT9XvxQfZ7/jz76/L+BLxYAgJ+5sAlEr7/+usaOHatHH31UmzZtUseOHZWVlaXi4mKrSzujjJYJPu8TYk4+MnPYbWoQ7VTrpHo+oemJvu2UGOtS6XcVuuGFNcrfV6Lt+90aPHO95m/6Wuv2HNI/1uzVxq++ZZwRAAA/YDPC5K9jt27d1LVrV73wwguSJI/Ho5SUFN1333166KGHfvL33W634uLiVFpaqtjY2ECXK8Mw9Oamb9SxaZwuTKynA6XfaeLb23VFy4YacmWaJOnRt7dpdt5X6tKsvuYNz9Dzyz/Xs+9/Kklq2yRWCTFO/eez03uIWjaKVsNol9wnKhQbWUfJcXXVJD5ScZF1FO2MUP1op2JcDjkddrkcdtWJsMtus8lmk+w2myLsNtltks1mk9128md7tYUkAyHAlwcAhID4qJN/f2pTTf9+h0UgKi8vV1RUlP7973+rX79+5vHBgwerpKREb7/99mm/U1ZWprKyMvO92+1WSkpK0AJRTXg8hnYVHlFqwyjFuByqrPLo+eWfqdJj6P9d3VIxLocmLdqhf+V9qQbRTqUlROuTr0tVXslijgCA0PPUTe11a7fUWr1mTQNRWGzd8d///ldVVVVKTEz0OZ6YmKhdu3ad8XdycnL0+OOPB6O8c2a325SefOof1xFh19herX3aPHbjxXqodxu5HHbZbDZ9e6xca/ccUpVhqF7dOio5Xq7C0hM6UHpC7hMVOnqiUiXHK3S0rFLlVR5VVHlUUemRoZOLRXqMk71XHuPkzx7DkGH4LiRZE4Zq3v6XH9kBAJIUYeFAnrAIROdiwoQJGjt2rPne20P0c1S3zqmxRvWjnerdvomF1QAAEHrCIhAlJCQoIiJCRUVFPseLioqUlJR0xt9xuVxyuVzBKA8AAFgsLGaZOZ1Ode7cWcuXLzePeTweLV++XBkZGRZWBgAAQkFY9BBJ0tixYzV48GB16dJFl112mZ577jkdO3ZMQ4YMsbo0AABgsbAJRDfffLMOHjyoiRMnqrCwUJ06ddLSpUtPG2gNAADCT1hMu68NwV6HCAAAnL+a/v0OizFEAAAAP4ZABAAAwh6BCAAAhD0CEQAACHsEIgAAEPYIRAAAIOwRiAAAQNgjEAEAgLBHIAIAAGEvbLbuOF/eBb3dbrfFlQAAgJry/t3+qY05CEQ1dOTIEUlSSkqKxZUAAAB/HTlyRHFxcWc9z15mNeTxeLR//37Vq1dPNput1q7rdruVkpKiffv2sUdagHGvg4P7HBzc5+DhXgdHoO6zYRg6cuSIkpOTZbeffaQQPUQ1ZLfb1bRp04BdPzY2lv/QgoR7HRzc5+DgPgcP9zo4AnGff6xnyItB1QAAIOwRiAAAQNgjEFnM5XLp0UcflcvlsrqUXzzudXBwn4OD+xw83OvgsPo+M6gaAACEPXqIAABA2CMQAQCAsEcgAgAAYY9ABAAAwh6ByGIvvviimjdvrrp166pbt25av3691SX9rOTk5Khr166qV6+eGjdurH79+mn37t0+bU6cOKHs7Gw1bNhQMTExGjBggIqKinzaFBQUqE+fPoqKilLjxo01btw4VVZWBvOr/KxMnjxZNptNo0ePNo9xn2vHN998o9tuu00NGzZUZGSk2rdvrw0bNpjnDcPQxIkT1aRJE0VGRiozM1OfffaZzzUOHz6sQYMGKTY2VvHx8Ro6dKiOHj0a7K8SsqqqqvTII48oLS1NkZGRatmypSZNmuSz1xX3+dysXr1aN9xwg5KTk2Wz2fTWW2/5nK+t+7plyxZ1795ddevWVUpKiqZMmXL+xRuwzGuvvWY4nU7jn//8p7F9+3bj7rvvNuLj442ioiKrS/vZyMrKMmbOnGls27bNyM/PN66//nojNTXVOHr0qNlm+PDhRkpKirF8+XJjw4YNxuWXX25cccUV5vnKykqjXbt2RmZmprF582bj3XffNRISEowJEyZY8ZVC3vr1643mzZsbHTp0MEaNGmUe5z6fv8OHDxvNmjUz7rzzTmPdunXGnj17jGXLlhmff/652Wby5MlGXFyc8dZbbxmffPKJceONNxppaWnGd999Z7a57rrrjI4dOxpr1641/vOf/xitWrUybrnlFiu+Ukh68sknjYYNGxqLFi0y9u7da8ybN8+IiYkxpk2bZrbhPp+bd9991/jTn/5kzJ8/35BkLFiwwOd8bdzX0tJSIzEx0Rg0aJCxbds249VXXzUiIyONv/3tb+dVO4HIQpdddpmRnZ1tvq+qqjKSk5ONnJwcC6v6eSsuLjYkGatWrTIMwzBKSkqMOnXqGPPmzTPb7Ny505Bk5OXlGYZx8j9gu91uFBYWmm1eeuklIzY21igrKwvuFwhxR44cMS688EIjNzfXuPrqq81AxH2uHePHjzeuuuqqs573eDxGUlKSMXXqVPNYSUmJ4XK5jFdffdUwDMPYsWOHIcn4+OOPzTZLliwxbDab8c033wSu+J+RPn36GHfddZfPsf79+xuDBg0yDIP7XFt+GIhq675Onz7dqF+/vs//N8aPH2+0bt36vOrlkZlFysvLtXHjRmVmZprH7Ha7MjMzlZeXZ2FlP2+lpaWSpAYNGkiSNm7cqIqKCp/73KZNG6Wmppr3OS8vT+3bt1diYqLZJisrS263W9u3bw9i9aEvOztbffr08bmfEve5trzzzjvq0qWLfve736lx48a65JJL9L//+7/m+b1796qwsNDnPsfFxalbt24+9zk+Pl5dunQx22RmZsput2vdunXB+zIh7IorrtDy5cv16aefSpI++eQTrVmzRr1795bEfQ6U2rqveXl56tGjh5xOp9kmKytLu3fv1rfffnvO9bG5q0X++9//qqqqyuePgyQlJiZq165dFlX18+bxeDR69GhdeeWVateunSSpsLBQTqdT8fHxPm0TExNVWFhotjnTv4P3HE567bXXtGnTJn388cenneM+1449e/bopZde0tixY/XHP/5RH3/8se6//345nU4NHjzYvE9nuo/V73Pjxo19zjscDjVo0ID7/L2HHnpIbrdbbdq0UUREhKqqqvTkk09q0KBBksR9DpDauq+FhYVKS0s77Rrec/Xr1z+n+ghE+MXIzs7Wtm3btGbNGqtL+cXZt2+fRo0apdzcXNWtW9fqcn6xPB6PunTpoqeeekqSdMkll2jbtm2aMWOGBg8ebHF1vxxvvPGG5syZo7lz5+riiy9Wfn6+Ro8ereTkZO5zGOORmUUSEhIUERFx2iycoqIiJSUlWVTVz9fIkSO1aNEiffDBB2ratKl5PCkpSeXl5SopKfFpX/0+JyUlnfHfwXsOJx+JFRcX69JLL5XD4ZDD4dCqVav0/PPPy+FwKDExkftcC5o0aaL09HSfY23btlVBQYGkU/fpx/6/kZSUpOLiYp/zlZWVOnz4MPf5e+PGjdNDDz2kgQMHqn379rr99ts1ZswY5eTkSOI+B0pt3ddA/b+EQGQRp9Opzp07a/ny5eYxj8ej5cuXKyMjw8LKfl4Mw9DIkSO1YMECrVix4rRu1M6dO6tOnTo+93n37t0qKCgw73NGRoa2bt3q8x9hbm6uYmNjT/vjFK569uyprVu3Kj8/33x16dJFgwYNMn/mPp+/K6+88rRlIz799FM1a9ZMkpSWlqakpCSf++x2u7Vu3Tqf+1xSUqKNGzeabVasWCGPx6Nu3boF4VuEvuPHj8tu9/3zFxERIY/HI4n7HCi1dV8zMjK0evVqVVRUmG1yc3PVunXrc35cJolp91Z67bXXDJfLZcyaNcvYsWOHcc899xjx8fE+s3Dw40aMGGHExcUZK1euNA4cOGC+jh8/brYZPny4kZqaaqxYscLYsGGDkZGRYWRkZJjnvdPBe/XqZeTn5xtLly41GjVqxHTwn1B9lplhcJ9rw/r16w2Hw2E8+eSTxmeffWbMmTPHiIqKMl555RWzzeTJk434+Hjj7bffNrZs2WL07dv3jNOWL7nkEmPdunXGmjVrjAsvvDDsp4NXN3jwYOOCCy4wp93Pnz/fSEhIMB588EGzDff53Bw5csTYvHmzsXnzZkOS8cwzzxibN282vvrqK8Mwaue+lpSUGImJicbtt99ubNu2zXjttdeMqKgopt3/3P31r381UlNTDafTaVx22WXG2rVrrS7pZ0XSGV8zZ84023z33XfGvffea9SvX9+IiooybrrpJuPAgQM+1/nyyy+N3r17G5GRkUZCQoLxwAMPGBUVFUH+Nj8vPwxE3OfasXDhQqNdu3aGy+Uy2rRpY7z88ss+5z0ej/HII48YiYmJhsvlMnr27Gns3r3bp82hQ4eMW265xYiJiTFiY2ONIUOGGEeOHAnm1whpbrfbGDVqlJGammrUrVvXaNGihfGnP/3JZxo39/ncfPDBB2f8f/LgwYMNw6i9+/rJJ58YV111leFyuYwLLrjAmDx58nnXbjOMaktzAgAAhCHGEAEAgLBHIAIAAGGPQAQAAMIegQgAAIQ9AhEAAAh7BCIAABD2CEQAACDsEYgAAEDYIxABAICwRyACEPIOHjwop9OpY8eOqaKiQtHR0eYO8Gfz2GOPyWaznfZq06ZNkKoG8HPisLoAAPgpeXl56tixo6Kjo7Vu3To1aNBAqampP/l7F198sd5//32fYw4H/9sDcDp6iACEvI8++khXXnmlJGnNmjXmzz/F4XAoKSnJ55WQkGCeb968uSZNmqRbbrlF0dHRuuCCC/Tiiy/6XKOgoEB9+/ZVTEyMYmNj9fvf/15FRUU+bRYuXKiuXbuqbt26SkhI0E033WSe+7//+z916dJF9erVU1JSkm699VYVFxef660AECAEIgAhqaCgQPHx8YqPj9czzzyjv/3tb4qPj9cf//hHvfXWW4qPj9e999573p8zdepUdezYUZs3b9ZDDz2kUaNGKTc3V5Lk8XjUt29fHT58WKtWrVJubq727Nmjm2++2fz9xYsX66abbtL111+vzZs3a/ny5brsssvM8xUVFZo0aZI++eQTvfXWW/ryyy915513nnfdAGoXu90DCEmVlZX6+uuv5Xa71aVLF23YsEHR0dHq1KmTFi9erNTUVMXExPj0+FT32GOPadKkSYqMjPQ5ftttt2nGjBmSTvYQtW3bVkuWLDHPDxw4UG63W++++65yc3PVu3dv7d27VykpKZKkHTt26OKLL9b69evVtWtXXXHFFWrRooVeeeWVGn2vDRs2qGvXrjpy5IhiYmLO5dYACAB6iACEJIfDoebNm2vXrl3q2rWrOnTooMLCQiUmJqpHjx5q3rz5WcOQV+vWrZWfn+/zeuKJJ3zaZGRknPZ+586dkqSdO3cqJSXFDEOSlJ6ervj4eLNNfn6+evbsedYaNm7cqBtuuEGpqamqV6+err76akn6yUHhAIKL0YUAQtLFF1+sr776ShUVFfJ4PIqJiVFlZaUqKysVExOjZs2aafv27T96DafTqVatWgW0zh/2QFV37NgxZWVlKSsrS3PmzFGjRo1UUFCgrKwslZeXB7QuAP6hhwhASHr33XeVn5+vpKQkvfLKK8rPz1e7du303HPPKT8/X++++26tfM7atWtPe9+2bVtJUtu2bbVv3z7t27fPPL9jxw6VlJQoPT1dktShQwctX778jNfetWuXDh06pMmTJ6t79+5q06YNA6qBEEUPEYCQ1KxZMxUWFqqoqEh9+/aVzWbT9u3bNWDAADVp0qRG16isrFRhYaHPMZvNpsTERPP9hx9+qClTpqhfv37Kzc3VvHnztHjxYklSZmam2rdvr0GDBum5555TZWWl7r33Xl199dXq0qWLJOnRRx9Vz5491bJlSw0cOFCVlZV69913NX78eKWmpsrpdOqvf/2rhg8frm3btmnSpEm1dIcA1CZ6iACErJUrV5rT2devX6+mTZvWOAxJ0vbt29WkSROfV7NmzXzaPPDAA9qwYYMuueQS/fnPf9YzzzyjrKwsSSfD09tvv6369eurR48eyszMVIsWLfT666+bv3/NNddo3rx5euedd9SpUyf96le/0vr16yVJjRo10qxZszRv3jylp6dr8uTJevrpp2vhzgCobcwyAxC2mjdvrtGjR2v06NFWlwLAYvQQAQCAsEcgAgAAYY9HZgAAIOzRQwQAAMIegQgAAIQ9AhEAAAh7BCIAABD2CEQAACDsEYgAAEDYIxABAICwRyACAABh7/8DLRheiY/DxbsAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Realizar una predicción\")\n",
        "resultado = modelo.predict([10.0])\n",
        "print(\"Te sale en \" + str(resultado) + \" pesos mxn\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K14kEfSExp20",
        "outputId": "0ec07f5e-0f52-49d4-aff2-e6c8af393e06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Realizar una predicción\n",
            "1/1 [==============================] - 0s 35ms/step\n",
            "Te sale en [[173.4]] pesos mxn\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "-Suz7-hhUgCh"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}