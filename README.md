# Github-via-IPython
Make Github commit in Jupyter IPython notebook 

# Getting Started

This is simply a python script that you can copy paste in your working directory.
You can use it to commit changes in your github repo via Jupyter notebook.


## Usage


```python
#First import the script
import git_jupyter
```


```python
#Create a session by giving in your details
sess = git_jupyter.Jupyter('README.ipynb','huzaifafaruqui','Github-via-IPython','*******','******')
            #   file name  ,    owner name ,     repository name,    github username ,  github password
            # username and password will be hidden automatically
```

### Please Save your file before creation/updation 


### Create File
```python
sess.create_file('README.ipynb','Read this')
#                 file name, commit message
```


### Update File

```python
sess.update_file('README.ipynb','Updated')
#                file name, commit message
```

### Deletion 
    sess.delete.file('README.ipynb','commit msg')

## Built With

1. Requests - Requests is an elegant and simple HTTP library for Python
2. Jupyter notebook - The Jupyter Notebook is a web application that allows you to create and 
    share documents that contain live code, equations, visualizations and explanatory text.
3. Github API

## Contributing

Please feel free to send PR. This is a very simple script but I want to extend its functionalities. Also, create an issue if you find any bug.
Note - My code follows PEP8 guidelines.

## Contributing

1. Replace Basic Auth with OAuth
2. Ability to create a repo
3. Write tests

## Authors

Huzaifa Faruqui

## License
    MIT


```python
sess.update_file('README.ipynb','Updated')

```


```python

```
