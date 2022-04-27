# MRNet
This repository contains three models of MRnet. All data that was used is available via following link: [Dataset](https://drive.google.com/drive/folders/1mpSe2ONoq6XUTHMdUS9ci7V3XNKJjfYu?usp=sharing)
## Setup environment

`conda env create -f environment.yml`

`source activate mrnet`

It will create necessary conda environment with all needed packages.

Moreover, you can download Istajduh dataset by use of:
`bash download.sh`

### Neergard's model

Once you download the data, create a `data` folder and place it at the root of the project. You should have two folders inside: `vol01`, `vol02` and so on as well as a `metadata.csv` file.


#### Train
To run the script you can execute it with the following arguments. To note, some has a default values but you change with appropriate flag.

```python
    parser = argparse.ArgumentParser()
    parser.add_argument('--rundir', type=str, required=True)
    parser.add_argument('--diagnosis', type=int, required=True)
    parser.add_argument('--seed', default=42, type=int)
    parser.add_argument('--gpu', action='store_true')
    parser.add_argument('--learning_rate', default=1e-05, type=float)
    parser.add_argument('--weight_decay', default=0.01, type=float)
    parser.add_argument('--epochs', default=50, type=int)
    parser.add_argument('--max_patience', default=5, type=int)
    parser.add_argument('--factor', default=0.3, type=float)
```
`python train.py --rundir [experiment name] --diagnosis 0 --gpu`

- diagnosis is highest diagnosis allowed for negative label (0 = injury task, 1 = tear task)
- arguments saved at `[experiment-name]/args.json`
- prints training & validation metrics (loss & AUC) after each epoch
- models saved at `[experiment-name]/[val_loss]_[train_loss]_epoch[epoch_num]`

Example of use:
`python train.py --rundir vol04 --diagnosis 1 --gpu --epochs 100`
#### Evaluation
To run the script you can execute it with the following arguments. To note, some has a default values but you change with appropriate flag.
```
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True)
    parser.add_argument('--split', type=str, required=True)
    parser.add_argument('--diagnosis', type=int, required=True)
    parser.add_argument('--gpu', action='store_true')
```
`python evaluate.py --split [train/valid/test] --diagnosis 0 --model_path [experiment-name]/[val_loss]_[train_loss]_epoch[epoch_num] --gpu`

Example of use:
`python evaluate.py --split train --diagnosis 1 --model_path vol04/val0.0223_0.0173_epoch26 --gpu`

- prints loss & AUC


#### Graph of AUC and Loss
After training the model:
`python graph.py`
### YashBalgat's model
Once you download the data, create a `data` folder and place it at the root of the project. You should have two folders inside: `train` and `valid` as well as a bunch of csv files.
`Train` and `valid` folders shouls have a following subfoldes:
- sagittal
- coronal
- axial


#### Train
To run the script you can execute it with the following arguments. To note, some has a default values but you change with appropriate flag.
```python
    parser = argparse.ArgumentParser()
    parser.add_argument('--rundir', type=str, required=True)
    parser.add_argument('--task', type=str, required=True)
    parser.add_argument('--seed', default=42, type=int)
    parser.add_argument('--gpu', action='store_true')
    parser.add_argument('--learning_rate', default=1e-05, type=float)
    parser.add_argument('--weight_decay', default=0.01, type=float)
    parser.add_argument('--epochs', default=50, type=int)
    parser.add_argument('--max_patience', default=5, type=int)
    parser.add_argument('--factor', default=0.3, type=float)
    parser.add_argument('--backbone', default="alexnet", type=str)
    parser.add_argument('--abnormal_model', default=None, type=str)
```
- diagnosis is abnormal for acl and meniscus task
- arguments saved at `[experiment-name]/args.json`
- prints training & validation metrics (loss & AUC) after each epoch and elapsed time
- early stopping if AUC does not change after several epochs
- models saved at `[experiment-name]/[val_loss]_[train_loss]_epoch[epoch_num]`

#### Evaluation
To run the script you can execute it with the following arguments. To note, some has a default values but you change with appropriate flag.
```
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True)
    parser.add_argument('--split', type=str, required=True)
    parser.add_argument('--diagnosis', type=int, required=True)
    parser.add_argument('--gpu', action='store_true')
```
### AhmedBesbes's model
Once you download the data, create a `data` folder and place it at the root of the project. You should have two folders inside: `train` and `valid` as well as a bunch of csv files.
`Train` and `valid` folders shouls have a following subfoldes:
- sagittal
- coronal
- axial



Note: Before running the script, add the following (empty) folders at the root of the project:
- models
- logs


#### Train
To run the script you can execute it with the following arguments. To note, some has a default values but you change with appropriate flag.
```python
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', type=str, required=True,
                    choices=['abnormal', 'acl', 'meniscus'])
parser.add_argument('-p', '--plane', type=str, required=True,
                    choices=['sagittal', 'coronal', 'axial'])
parser.add_argument('--augment', type=int, choices=[0, 1], default=1)
parser.add_argument('--lr_scheduler', type=int, choices=[0, 1], default=1)
parser.add_argument('--epochs', type=int, default=50)
parser.add_argument('--lr', type=float, default=1e-5)
parser.add_argument('--flush_history', type=int, choices=[0, 1], default=0)
parser.add_argument('--save_model', type=int, choices=[0, 1], default=1)
parser.add_argument('--patience', type=int, choices=[0, 1], default=5)
```
- plane is sagittal,coronal and axial
- task is abnormal,acl and meniscus
- prints training & validation metrics (loss & AUC) after each epoch, time and learning rate value
- models saved at `models/model_[plane+task]_[task]_[plane]_val_auc_[val_auc_score]_train_auc_[train_auc_score]_epoch_[epoch_num].pth`
- log saved at `logs/[task]/[plane]/[YYYYMMDD]-[HHMMSS]/events.out.tfevents.[lognumber].[computer_name]`



#### Web-interface with correctly and incorrectly diagnosed cases with probabilites
This widget can be launced after training a model. Go for dash directory.
`python main.py`
Then, click on given address in a terminal to open web-widget.
#### TensorBoard to get all graphs on loss and AUC scores
After running model:
`tensorboard --logdir logs`
### Slice-by-slice Visualization 
You can run this web-widget any time.
`python display.py [plane] [file_number]`
- `file_number` for file `0000.npy` is just `0000`. After running program, tab in web browser will be opened.


Note: to run this program Stanford data should be in you path. It works only with Stanford data. Also, change project path in the file.
### Slice-by-slice image saving
You can run this web-widget any time.
`python printSlices.py [plane] [file_number] [slice_number]`
- `file_number` for file `0000.npy` is just `0000`. After running program, matplotlib plot will be shown with all slices. Also, all images will be saved in `/images`


Note: to run this program Stanford data should be in you path. It works only with Stanford data. Also, change project path in the file.

