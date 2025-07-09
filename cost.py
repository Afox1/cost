{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c83b1bf-f31f-4e97-ae0b-b5e07c981b41",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from sklearn.neural_network import MLPRegressor\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "st.set_page_config(page_title=\"CNG ROI App\", layout=\"centered\")\n",
    "st.title(\"🔍 CNG Savings & Investment Return App\")\n",
    "\n",
    "# Inputs\n",
    "engine_size = st.number_input(\"Engine Size (L)\", min_value=0.5, max_value=10.0, step=0.1)\n",
    "distance = st.number_input(\"Distance (km)\", min_value=1.0, max_value=10000.0, step=1.0)\n",
    "install_cost = st.number_input(\"Cost of Installation (#)\", min_value=0.0, step=100.0)\n",
    "\n",
    "# Only predict when inputs are valid\n",
    "if engine_size > 0 and distance > 0:\n",
    "    # Scale the inputs using precomputed scaler\n",
    "    scaler = StandardScaler()\n",
    "    scaler.mean_ = np.array([2.038, 207.679])\n",
    "    scaler.scale_ = np.array([0.688, 111.230])\n",
    "    inputs = np.array([[engine_size, distance]])\n",
    "    inputs_scaled = scaler.transform(inputs)\n",
    "\n",
    "    # MLP Regressor (placeholder for model structure)\n",
    "    model = MLPRegressor(\n",
    "        activation='relu',\n",
    "        hidden_layer_sizes=(13, 13, 13),\n",
    "        solver=\"lbfgs\",\n",
    "        max_iter=2000,\n",
    "        random_state=42\n",
    "    )\n",
    "    model.fit(np.zeros((2, 2)), [0, 0])  # Dummy fit to activate model\n",
    "\n",
    "    # Custom estimated prediction (as placeholder)\n",
    "    predicted_savings = 35000 + (distance * 5) + (engine_size * 1000)\n",
    "    st.success(f\"Predicted Savings: ₦{predicted_savings:,.2f}\")\n",
    "\n",
    "    roi = predicted_savings - install_cost\n",
    "    if roi >= 0:\n",
    "        st.info(f\"🎉 You're now making a profit of ₦{roi:,.2f}\")\n",
    "    else:\n",
    "        st.warning(f\"⏳ You need ₦{abs(roi):,.2f} more to break even.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
