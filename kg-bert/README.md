__#__ KG-BERT: BERT for Knowledge Graph Completion

The repository is modified from [pytorch-pretrained-BERT](https://github.com/huggingface/pytorch-pretrained-BERT) and tested on Python 3.5+.


## Installing requirement packages

The requirement packages for XXX prediction.ipynb and XXX prediction (kg-bert).ipynb is differet.

Therefore, please use different environment to run them

For XXX prediction.ipynb
```bash
cd requirement_normal
pip install -r requirements.txt
```
For XXX prediction (kg-bert).ipynb
```bash
cd requirement_kg_bert
pip install -r requirements.txt
```

## Data

(1) The benchmark knowledge graph datasets are in ./data. 

(2) entity2text.txt or entity2textlong.txt in each dataset contains entity textual sequences.

(3) relation2text.txt in each dataset contains relation textual sequences.

## Reproducing results
### 1. Link Prediction and Relation Prediction on WordNet and WebChild
Download model from google drive:

**Relation Prediction**:

Go to: https://drive.google.com/drive/u/1/folders/1j_q1n2VqhiOsplO_n33ugSVtjm_wNnO0

Download pytorch_model1.zip and pytorch_model2.zip. Unzip and put them in the folder "./output_wc_result" and "./output_wc_result2".
Download kgtk_webchild_comparative.tsv and put them into a new folder in ./data/wc.
Run the notebook **Relation_Prediction_(kg-bert).ipynb**

**Link Prediction**:

Go to: https://drive.google.com/drive/u/1/folders/1K-4DBLoAdW0bjGQDhcX2jHq5fVoKRK3n

Repeat the same process, but save model in the folder, "./output_wn_result".
Download kgtk_wordnet.tsv and put them into a new folder in ./data/wn.
Run the notebook **Link_Prediction_(kg-bert).ipynb**

### 2. Triple Classification

#### WN11

```shell
python run_bert_triple_classifier.py 
--task_name kg
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/WN11 
--bert_model bert-base-uncased 
--max_seq_length 20 
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 3.0 
--output_dir ./output_WN11/  
--gradient_accumulation_steps 1 
--eval_batch_size 512
```

#### FB13

```shell
python run_bert_triple_classifier.py 
--task_name kg  
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/FB13 
--bert_model bert-base-cased
--max_seq_length 200
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 3.0 
--output_dir ./output_FB13/  
--gradient_accumulation_steps 1 
--eval_batch_size 512
```


### 3. Relation Prediction

#### FB15K

```shell
python3 run_bert_relation_prediction.py 
--task_name kg  
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/FB15K 
--bert_model bert-base-cased
--max_seq_length 25
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 20.0 
--output_dir ./output_FB15K/  
--gradient_accumulation_steps 1 
--eval_batch_size 512
```

### 4. Link Prediction

#### WN18RR

```shell
python3 run_bert_link_prediction.py
--task_name kg  
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/WN18RR
--bert_model bert-base-cased
--max_seq_length 50
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 5.0 
--output_dir ./output_WN18RR/  
--gradient_accumulation_steps 1 
--eval_batch_size 5000
```

#### UMLS

```shell
python3 run_bert_link_prediction.py
--task_name kg  
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/umls
--bert_model bert-base-uncased
--max_seq_length 15
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 5.0 
--output_dir ./output_umls/  
--gradient_accumulation_steps 1 
--eval_batch_size 135
```

#### FB15k-237

```shell
python3 run_bert_link_prediction.py
--task_name kg  
--do_train  
--do_eval 
--do_predict 
--data_dir ./data/FB15k-237
--bert_model bert-base-cased
--max_seq_length 150
--train_batch_size 32 
--learning_rate 5e-5 
--num_train_epochs 5.0 
--output_dir ./output_FB15k-237/  
--gradient_accumulation_steps 1 
--eval_batch_size 1500
```
