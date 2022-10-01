# Reproducing the paper [Hierarchical Image Classification using Entailment Cone Embeddings](https://ankitdhall.github.io/project/learning-representations-for-images-with-hierarchical-labels/) by Dhall et. al (2020). 

### Authors: Caroline Freyer and Marios Marinos

Blog explaining the paper futher can be found [here](https://carolinefreyer.medium.com/entailment-cones-for-better-hierarchical-image-classifier-95973a18a0e1). 

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

# Predicting Taxonomy for Organisms

![alt text](https://ankitdhall.github.io/project/learning-representations-for-images-with-hierarchical-labels/featured_hu84feb2bf561f49e98504fe25e8752a1b_2231317_720x0_resize_lanczos_2.png "The ETHEC dataset hierarchy")  
*Fig. 2: The ETHEC dataset hierarchy*

One of the main applications of this work is to assist natural history collections, museums and organizations that preserve large numbers of historical and extant biodiversity specimens to digitize and organize their collections. Hobbyists create their personal collections most of which are eventually donated to public institutions. Before integration, these specimens need to be sorted taxonomically by specialists who have little time and are expensive. If this resource intensive task could be preceded by a pre-sorting procedure, for instance, where these specimens are categorized by unskilled labour based on their family, sub-family, genus, and species it would expedite and economize the process.

Thanks to the the [ETH Library Lab](https://www.librarylab.ethz.ch/) the research conducted on the thesis will be turned into classification app that can be used by hobbyists, collectors, and researchers alike to speed up and economize classification and segregation of entomological specimens. More information about the app will be made available soon!


![alt text](https://ankitdhall.github.io/project/learning-representations-for-images-with-hierarchical-labels/ec_2d_labels.png "Embedding label hierarchy with euclidean entailment cones in 2D")
*Fig. 3: Embedding label hierarchy with euclidean entailment cones in 2D*

