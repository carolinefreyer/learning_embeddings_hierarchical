# Reproducing the paper [Hierarchical Image Classification using Entailment Cone Embeddings](https://ankitdhall.github.io/project/learning-representations-for-images-with-hierarchical-labels/) by Dhall et. al. (2020). 

### Authors: Caroline Freyer and Marios Marinos

Blog explaining out interpretation and reproduction Dhall et. al.'s [paper](https://ankitdhall.github.io/project/learning-representations-for-images-with-hierarchical-labels/) can be found [here](https://carolinefreyer.medium.com/entailment-cones-for-better-hierarchical-image-classifier-95973a18a0e1). 

# Usage
Create a virtual environment using the `requirements.txt` file:
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r learning_embeddings/requirements_3.6.txt
pip install opencv-python
pip install gitpython
```  

Use branch `Adam1x` to run experiments with the ETHEC dataset:  
`git checkout Adam1x`  

Splits for the ETHEC dataset can be found in `splits` folder. Experiments in this repository were conducted using **v0.1** of the ETHEC dataset.  

Sample command:  
`python learning_embeddings/network/ethec_experiments.py --experiment_name exp_test --experiment_dir exp --image_dir ETHEC_dataset_v0.1/ETHEC_dataset/IMAGO_build_test_resized/ --n_epochs 1 --model resnet18 --loss multi_level --set_mode train`
