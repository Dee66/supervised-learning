# <span style="color:#2b4a6f">Supervised Learning Demystified: From First Principles to Production Readiness</span>

Welcome to a hands-on, architecturally-minded notebook series designed to bridge the gap between ML theory and real-world system design. Here, you’ll not only learn how supervised learning works, but also how it behaves in production—where stability, monitoring, and business impact matter as much as accuracy.

---

🚀 **Quick Start**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://bit.ly/3I4rKCk)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Dee66/supervised-learning/HEAD?filepath=notebooks%2F02_supervised_learning_systems.ipynb)

---

_Click a badge to launch the main notebook interactively—no installation needed!_

## <span style="color:#3b7c8c">Series Structure & Vision</span>

- **Modular Progression:** Each notebook builds on the last, layering new architectural and operational insights.
- **Architect’s Notes:** Embedded throughout, these insights connect ML concepts to production realities—why they matter for reliability, scaling, and business value.
- **Visual-First Approach:** Every concept is paired with interactive charts, overlays, or animations to make system behavior tangible.
- **Real Data, Real Scenarios:** Examples use realistic datasets and simulate production challenges like drift, imbalance, and label noise.
- **Failure Cases:** See how misclassification, poor scaling, or overfitting manifest—and how robust systems detect and address them.

---

## <span style="color:#4e6e58">What’s Inside?</span>

| Notebook | Key Concepts & Visuals | Production Insight |
|---|---|---|
| [**1. Foundations of Supervised Learning**](notebooks/02_supervised_learning_systems.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/02_supervised_learning_systems.ipynb)</sup> | Regression vs. Classification, Decision Boundaries | How problem framing shapes system design |
| [**2. Linear Regression: Cost & Optimization**](notebooks/03_cost_curve_and_gradient_intuition.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/03_cost_curve_and_gradient_intuition.ipynb)</sup> | Cost Landscape, Learning Curves, Parameter Evolution, Failure Modes, Interactivity | Why optimization stability matters for deployment |
| [**3. Feature Engineering and Scaling**](notebooks/04_cost_curve_and_gradient_intuition_part_2.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/04_cost_curve_and_gradient_intuition_part_2.ipynb)</sup> | Scaling Impact, Cost Surface, Learning Curves, Interactivity | How feature scaling impacts convergence and cost |
| [**4. Polynomial Regression & Regularization**](notebooks/05_polynomial_regression.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/05_polynomial_regression.ipynb)</sup> | Model Complexity, Overfitting, Regularization, Interactivity | Controlling complexity for robust, scalable ML |
| [**5. Classification in Depth: Logistic Regression**](notebooks/06_classification.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/06_classification.ipynb)</sup> | Sigmoid, Cross-Entropy, Decision Boundaries, Cost Landscape, Interactivity | Mapping model outputs to business risk |
| [**6. Pitfalls & Best Practices**](notebooks/07_best_practice.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/07_best_practice.ipynb)</sup> | Failure Modes, Best Practices, Production Reflection, Regularization Heatmap | Avoiding silent failures in real systems |
| [**7. Advanced Topics & MLOps**](notebooks/08_advanced.ipynb) <sup>[Colab](https://colab.research.google.com/github/Dee66/supervised-systems/blob/main/notebooks/08_advanced.ipynb)</sup> | Decision Boundary Failures, Precision/Recall, Threshold Tuning, MLOps Mapping | Connecting ML insights to CI/CD and monitoring |

---

*Click any notebook title to view it on GitHub, or use the Colab links to launch interactively.*

## <span style="color:#b36b00">Why This Series?</span>

The best engineers explain what and how. Architects explain why.  
This series is your portfolio superpower—not just teaching ML, but drawing a clear line from “gradient descent math” to “deployment stability,” from “loss curve” to “business risk,” and from “overfitting” to “infrastructure cost.”

---

## <span style="color:#3b7c8c">🧠 Expert-Level Refinements</span>

- **Gradient Visuals & Tangents:** Deepen optimization understanding with cost curve slopes and update directions.
- **Animated Contours:** Visualize optimization bottlenecks and the impact of feature scaling.
- **Regularization Heatmaps:** Add architectural insight into hyperparameter effects.
- **Threshold vs Precision-Recall:** Show business-aligned evaluation, not just accuracy.
- **MLOps Mapping:** Connect every insight to real-world deployment, monitoring, and retraining.

---

## <span style="color:#4e6e58">Recent Delivery</span>

- **[CodeCraft AI](https://github.com/Dee66/CodeCraft-AI):**  
  End-to-end design and deployment of a full-stack, AWS-native generative AI platform.  
  → [Implementation Checklist](https://github.com/Dee66/CodeCraft-AI/blob/main/docs/checklist.md)

---

## <span style="color:#3b7c8c">Key Technologies Used</span>

- **AWS Native:** SageMaker, Lambda, ECS (Fargate), S3, ECR, ALB, IAM, Secrets Manager, SSM, CloudWatch, VPC, KMS
- **MLOps & Automation:** CI/CD with GitHub Actions, multi-stage Docker builds, automated retraining, pre-commit hooks, code linting (Ruff), vulnerability scanning
- **AI/ML:** Hugging Face Transformers, FAISS (vector search), PEFT, RAG, PyTorch, scikit-learn
- **Infrastructure as Code (IaC):** AWS CDK (Python) for reproducible, auditable deployments
- **Security:** OIDC-based passwordless deployment, least-privilege IAM, automated secret rotation, private networking
- **Observability:** Centralized logging, CloudWatch dashboards, structured logs, proactive alerting
- **Testing:** Pytest, nbval (Jupyter), coverage, static type checking (mypy)

---

## <span style="color:#b36b00">How to Run</span>

1. **Clone the repo:**  
   `git clone https://github.com/yourusername/supervised-systems.git`

2. **Install dependencies:**  
   - With Poetry: `poetry install`
   - Or with pip: `pip install -r requirements.txt` *(if provided)*

3. **Run notebooks:**  
   - Launch Jupyter Lab or Notebook in the `notebooks/` directory.
   - Notebooks will automatically add `src/` to `sys.path` for local imports.

> **Note:**  
> This project uses a `src/` layout. If you run scripts outside notebooks, add this at the top:
> ```python
> import sys, os
> sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
> ```

---

<div style="background:solidrgb(113, 163, 224); border-left:4px solid #2b4a6f; padding:12px 18px; margin:18px 0;">
<b>Ready to go beyond the textbook?</b>  
Start with Notebook 1 and build your systems thinking, one architectural layer at a time.  
<span style="color:#4e6e58">Visuals, interactivity, and real-world context await—dive in!</span>

---

## License

This project is licensed under the [MIT License](LICENSE).

---