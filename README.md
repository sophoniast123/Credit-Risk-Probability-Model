## **Credit Scoring Business Understanding**

### **1. Basel II Accord and Model Interpretability**

The Basel II Accord emphasizes that financial institutions must accurately measure and manage credit risk to maintain adequate capital reserves. This emphasis necessitates the use of **interpretable and well-documented models**, because:

* Regulators require transparency in how risk is assessed and quantified.
* Decisions based on credit risk models must be explainable to stakeholders, including auditors and regulators.
* Clear documentation ensures reproducibility, accountability, and easier validation of model assumptions.

Thus, in our project, even as we explore advanced techniques, we must prioritize **model interpretability** alongside predictive performance.

---

### **2. Need for Proxy Variables**

In our dataset, a direct "default" label is not available. Therefore, creating a **proxy variable** becomes necessary to indicate potential default or high-risk behavior.

**Why it’s necessary:**

* It allows the model to learn patterns associated with credit risk.
* Provides a measurable outcome for supervised learning.

**Potential business risks:**

* Proxy variables may **not fully capture true default behavior**, leading to inaccurate predictions.
* Over-reliance on proxies could result in **misclassification of good or bad borrowers**, affecting lending decisions.
* Regulatory scrutiny may increase if proxies do not align closely with real-world outcomes.

---

### **3. Trade-offs Between Simple vs. Complex Models**

In a regulated financial context, choosing the model involves balancing **interpretability** and **performance**:

| Aspect                    | Simple Model (e.g., Logistic Regression with WoE) | Complex Model (e.g., Gradient Boosting)      |
| ------------------------- | ------------------------------------------------- | -------------------------------------------- |
| **Interpretability**      | High – each coefficient is explainable            | Low – hard to explain individual predictions |
| **Performance**           | Moderate predictive power                         | High predictive power                        |
| **Regulatory Compliance** | Easier to justify and validate                    | Harder to validate and document              |
| **Implementation**        | Faster deployment                                 | More complex infrastructure required         |
| **Risk**                  | Lower model risk                                  | Potential model risk due to opacity          |

**Conclusion:** In regulated credit scoring, **simple interpretable models** are often preferred, especially when regulatory approval and explainability are required, even if it comes at the cost of some predictive performance. Complex models may be used as supplementary tools or in environments where explainability can be addressed.


