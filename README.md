## Generalized GAN Pipeline
[![Pipeline-Run](https://github.com/swarajpande4/generalized-gan-pipeline/workflows/Pipeline-Run/badge.svg)](https://github.com/swarajpande4/generalized-gan-pipeline/actions?query=workflow%3APipeline-Run) 
[![Publish-Image](https://github.com/swarajpande4/generalized-gan-pipeline/workflows/Publish-Image/badge.svg)](https://github.com/swarajpande4/generalized-gan-pipeline/actions?query=workflow%3APublish-Image) 
[![Release](https://img.shields.io/github/v/release/swarajpande4/generalized-gan-pipeline)]() \
An ML / MLOps project implementing a streamlined system design for a train-test-deploy pipeline for various types of GANs (Generative Adversarial Networks). This project uses DVC for internal pipelining and GitHub Actions to enable CI/CD for the trained and tested models.

DAGsHub Link (for experimentation and pipelining): [Click Here!](https://dagshub.com/swarajpande4/generalized-gan-pipeline)

<br>

### To build from source
1.  Install [Git](https://git-scm.com) and [DVC](https://dvc.org). 

2.  Clone the repository. 
    ```
    git clone https://github.com/swarajpande5/generalized-gan-pipeline.git
    
    cd generalized-gan-pipeline/
    ```

3.  Set up virtual environment for python.
    ```
    pip install virtualenv
    
    virtualenv venv/

    source venv/bin/activate

    pip install -r requirements.txt
    ```

4.  Make suitable changes to `code/` directory and the `Dockerfile` in the project. If needed, changes can also be made to the pipeline itself by changing the `dvc.*` files using dvc commands. 

5.  Run the following command to execute the pipeline after making changes to the `code/` scripts.
    ```
    dvc repro
    ```

6.  Deactivate the virtual environment.
    ```
    deactivate
    ```


<br>

### Files and Directory Structure
    .
    ├── .github/workflows
        ├── pipeline-run.yaml           // Enables to run pipeline as a GitHub Action on Push
        └── push-image-on-release.yaml  // Enables to build and release a Container Image on DockerHub on Release
    ├── code
        ├── eval.py                     // Evaluation metrics script
        ├── featurization.py            // Featurization script
        ├── get_data.py                 // Fetches the datasets
        ├── model_class.py              // Model Class script
        └── train_model.py              // Trains the model instance
    ├── data
        ├── DVC data and related files   
    ├── metrics 
        ├── eval.json                   // Evaluation metrics for pipeline                       
        └── train_metric.json           
    ├── notebook (Optional)
        └── notebook.ipynb              // Jupyter Notebook 
    ├── dvc.lock
    ├── dvc.yaml
    ├── requirements.txt
    └── README.md

<br>
