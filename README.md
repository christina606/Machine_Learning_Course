```mermaid
graph TD
    %% Main Path
    Root((AI Training Path<br/>8 Weeks)) --> W12[Week 1-2:<br/>Foundations & Environment]
    Root --> W34[Week 3-4:<br/>Data Cleaning & Basic ML]
    Root --> W56[Week 5-6:<br/>Advanced Models & DevOps]
    Root --> W78[Week 7-8:<br/>Capstone Project & Career]

    %% Week 1-2 Details
    W12 --> W12_Common[Common: Networking, Git/GitHub, Branching]
    W12 --> W12_AI[AI Path: ML Intro, Anaconda/Jupyter, Python Basics, NumPy, Pandas]

    %% Week 3-4 Details
    W34 --> W34_Common[Common: Hosting, Domain Mgmt, Github Integration]
    W34 --> W34_AI[AI Path: EDA, Missing Values, Linear Regression, Matplotlib]

    %% Week 5-6 Details
    W56 --> W56_Common[Common: App Stores, Plugins, SEO, Trello/Jira]
    W56 --> W56_AI[AI Path: Logistic Regression, KNN, Model Evaluation, Decision Trees]

    %% Week 7-8 Details
    W78 --> W78_Common[Common: CI/CD Pipelines, Docker, Jenkins, LinkedIn & Career]
    W78 --> W78_AI[AI Path: K-Means, PCA, Feature Engineering, Capstone Project]

    %% Styling
    style Root fill:#f9f,stroke:#333,stroke-width:2px
    style W78 fill:#bbf,stroke:#333,stroke-width:2px
    style W12 fill:#dfd,stroke:#333
    style W34 fill:#dfd,stroke:#333
    style W56 fill:#dfd,stroke:#333
