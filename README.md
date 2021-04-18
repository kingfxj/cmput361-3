
# TODOs

1. **SUBMIT** the URL of this repository on eClass. 
2. List the CCID(s) of student(s) working on the project.
3. List all sources consulted while completing the assignment.

|Student name|  CCID  |
|------------|--------|
|student 1   |xinjian |
|student 2   |skavalin|


# Instructions:

# Task 1 : train the nbc model with the following command:
python3 ./nbc/nbc_train.py ./data/train.json ./full_bbc_model.tsv 

# Task 2 : test the nbc model with the following command:
python3 ./nbc/nbc_inference.py ./full_bbc_model.tsv ./data/test.json 

# Task 3 : train and test the top k features of the  nbc model with the following command:
 python3 ./nbc/feature_selection.py ./data/train.json <VALUE FOR K> ./data/train_top_10.json

# Task 4 : The Effect of different values of k on feature selection

# Task 5 : Create the KNN model with the following command:
python3 ./knn/knn_create_model.py ./data/train.json ./bbc_model.tsv

# Task 6 : Make Inferences on the Knn model from (5) with the following command:
 python3 ./knn/knn_inference.py ./bbc_doc_vectors.tsv <VALUE FOR K> ./data/test.json

# Task 7 : The Effect of different values of k on the Knn results

# Videos

Add links to videos in the `nbc` and in the `knn` folders.
* Link to xinjian's video: https://drive.google.com/file/d/1L7slZIFUthgKS-0rZl4P4NDxKZI9qxyL/view?usp=sharing
* Link to skavalin's video:https://drive.google.com/drive/folders/1Pz_7Vj8AzI9MX8_4iNun2a0sbyLXhnvi
